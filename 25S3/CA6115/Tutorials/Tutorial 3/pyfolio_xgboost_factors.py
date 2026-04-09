import yfinance as yf
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from xgboost.core import XGBoostError
import pyfolio as pf
from tqdm import tqdm

# ----------------------------
# 1. Parameters
# ----------------------------
tickers = ["AAPL","MSFT","GOOG","AMZN","TSLA"]  # example; expand to S&P500
start_date = "2023-01-01"
end_date = "2025-12-01"

lookback = 60           # days for feature calculation
prediction_horizon = 20 # days ahead return
train_window = 252      # rolling training window (1 year)
top_decile = 2          # long top 2
bottom_decile = 2       # short bottom 2
transaction_cost = 0.001 # 0.1% per trade

# ----------------------------
# 2. Download price data
# ----------------------------
prices = yf.download(tickers, start=start_date, end=end_date)['Close']
returns = prices.pct_change().fillna(0)

# Download benchmark
benchmark = yf.download("SPY", start=start_date, end=end_date)['Close'].pct_change()
benchmark = benchmark.reindex(returns.index).fillna(0)

# ----------------------------
# 3. Compute features
# ----------------------------
momentum = prices.pct_change(lookback).shift(1)
volatility = prices.pct_change().rolling(lookback).std().shift(1)
features = pd.concat([momentum.add_suffix('_mom'), volatility.add_suffix('_vol')], axis=1).dropna()

# Target: forward returns
future_returns = prices.pct_change(prediction_horizon).shift(-prediction_horizon)
future_returns = future_returns.loc[features.index]

# ----------------------------
# 4. Rolling ML factor prediction
# ----------------------------
predicted_signal = pd.DataFrame(index=features.index, columns=tickers, dtype=float)
dates = features.index[train_window:]

for date in tqdm(dates, desc="ML factor backtest"):
    train_start = date - pd.Timedelta(days=train_window)
    X_train = features.loc[train_start:date].dropna()
    y_train = future_returns.loc[X_train.index]

    for ticker in tickers:
        try:
            cols = [ticker+'_mom', ticker+'_vol']
            model = XGBRegressor(n_estimators=50, max_depth=3, learning_rate=0.1)
            model.fit(X_train[cols], y_train[ticker].dropna())
            X_test = features.loc[date, cols].values.reshape(1, -1)
            predicted_signal.loc[date, ticker] = model.predict(X_test)[0]
        except XGBoostError:
            print("No prediction for 20 days ahead:" + str(date))
            print("Ticker is: " + ticker)
            break
# ----------------------------
# 5. Monthly rebalancing
# resample('M').last() : time-based grouping operation in pandas that:
# Groups your time-indexed data by calendar month ('M')
# Takes the last observation in each monthly group
# note below, you are only taking the last predicted signal value for re-balancing
# ----------------------------
predicted_signal = predicted_signal.resample('M').last()
weights = pd.DataFrame(0, index=predicted_signal.index, columns=predicted_signal.columns)

signal_rank = predicted_signal.rank(axis=1, ascending=False)
weights[signal_rank <= top_decile] = 0.5  # for the bullish stock, you allocate long 50% 
weights[signal_rank >= len(tickers)-bottom_decile+1] = -0.5 # for the bearish stock, you allocate short 50% 

# Align weights to daily returns with forward fill
weights = weights.reindex(returns.index).ffill()

# ----------------------------
# 6. Apply transaction costs
# ----------------------------
weight_change = weights.diff().abs().sum(axis=1)
daily_returns = (weights * returns).sum(axis=1)
daily_returns = daily_returns - weight_change * transaction_cost

# ----------------------------
# 7. PyFolio analysis
# ----------------------------
# remove the initial 60 days lookback period
daily_returns = daily_returns.replace([np.inf, -np.inf], np.nan).dropna()
pf.create_full_tear_sheet(daily_returns.squeeze(), benchmark_rets=benchmark.squeeze())
