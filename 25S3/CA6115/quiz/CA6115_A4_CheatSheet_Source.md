## [[Exam-First Reminders]]
- [[Core theme]]: finance context + AI/ML methods matter equally. Generalization > in-sample fit. [[Data quality]], governance, explainability, and practical cost-benefit thinking run through all lectures.
- [[Most tested contrasts]]: FEAT; structured vs unstructured vs alternative data; precision vs recall; overfitting vs underfitting; CAPM vs factor pricing; Sharpe vs Sortino vs Max DD; K-means vs DBSCAN; RAG vs MCP; Agentic AI vs GenAI.

## [[L1. Introduction to AI in Finance]]
- [[Uses]] financial operations, credit loans, customer prospecting/segmentation, trading, risk management, robo-advisory, chatbots, compliance, AML/KYC, news monitoring.
- [[Why finance differs]] systemic risk, human behavior not natural law, self-learning/adaptive markets, unpredictability, real-world economic impact.
- [[Course theme]] not only AI methods but finance context/domain knowledge; successful use needs both.
- [[Data families]] structured numeric (prices, statements, ratios, macro data); ordinal (credit ratings, analyst recommendations); nominal (industry class, ESG); unstructured (text/images/audio); alternative data (satellite, social, transaction, geolocation, weather).
- [[Numeric examples]] stock price, volume, bid-ask spread, market cap, revenue, earnings, cash flow, GDP, inflation, unemployment, PMI, rates.
- [[Ordinal warning]] AAA to BB has order but not equal distance; encoding choice affects model performance.
- [[Data sources]] Bloomberg/Refinitiv, exchanges, SEC/SGX/ACRA filings, FED/IMF/World Bank, AlphaVantage/Kaggle/web-scraped data, PREQIN/PitchBook/BVAL.
- [[Transformations]] smoothing, aggregation, generalization, normalization, standardization, feature construction. Aggregation can turn daily data into weekly/monthly/yearly series.
- [[Normalization]] min-max maps to a range (often 0 to 1). Z-score: z=(x-μ)/σ.
- [[Integration issues]] redundancy, data quality, conflict resolution; transformation may cause information loss or subjective distortion.
- [[Encoding]] models need numeric inputs. One-hot encoding prevents fake ordering among categories.
- [[Unstructured examples]] news, earnings calls, SEC filings, social media, satellite imagery, chart images, product photos, OCR scans, podcasts, trader audio.
- [[Alternative data value]] retail traffic, oil storage/tanker usage, app downloads, card spending, foot traffic, crop yield, commodity demand/supply clues.
- [[Governance]] data quality, privacy/security, standardization, accountability, value creation. Data life cycle: Plan -> Design -> Create/Obtain -> Store/Maintain -> Use -> Enhance.
- [[MAS FEAT]] Fairness, Ethics, Accountability, Transparency.
- [[Example MCQs]]
- {{Q}} Which FEAT principle means institutions remain responsible for AI outcomes? {{Ans}} Accountability.
- {{Q}} Which encoding prevents fake ordering among categories? {{Ans}} One-hot encoding.

## [[L2. ML in Finance Operations]]
- [[ML types]] supervised = labeled data; unsupervised = hidden patterns; reinforcement learning = reward-based agent learning.
- [[Training intuition]] many models reduce error by gradient descent / parameter adjustment.
- [[Workflow]] collect labeled data -> split train/test (optionally validation) -> train -> test -> evaluate with metrics.
- [[Data partition]] resubstitution (use only if data is scarce), hold-out (often 80/20), cross-validation, bootstrap.
- [[Common classifiers]] logistic regression, naive Bayes, decision trees, neural networks/DL, SVM.
- [[Logistic regression]] interpretable baseline; good for binary outcomes; outputs probabilities; threshold often 0.5. Odds = p/(1-p).
- [[Naive Bayes]] simple benchmark using Bayes rule; strong independence assumption.
- [[Decision tree]] transparent rules, decision nodes/branches/leaves; handles numeric + categorical data; weaknesses = unstable, can become complex, prone to overfit.
- [[Deep learning]] strong on complex data but high compute, black-box, may overfit.
- [[Confusion matrix]] TP, TN, FP, FN.
- [[Accuracy]] = (TP+TN)/(TP+TN+FP+FN).
- [[Precision]] = TP/(TP+FP): among predicted positives, how many are truly positive.
- [[Recall / Sensitivity / TPR]] = TP/(TP+FN): among actual positives, how many were caught.
- [[ROC/AUC]] ROC plots TPR vs FPR across thresholds; AUC summarizes discrimination, best = 1.
- [[No free lunch]] no single algorithm is always best. Lower threshold -> fewer FN but more FP; higher threshold -> fewer FP but more FN. Choose based on economic cost of errors.
- [[Fit problems]] overfitting = learns noise/details and generalizes badly; underfitting = too simple.
- [[Finance data issues]] scarce, expensive, noisy, non-stationary; do not trust training accuracy alone.
- [[Use cases]] loan approval, fraud detection, customer prospecting, sentiment analysis, trading algorithms.
- [[Example MCQs]]
- {{Q}} Bank is conservative in default detection. More important metric? {{Ans}} Recall / sensitivity.
- {{Q}} Marketing does not want to pester uninterested customers. Better metric? {{Ans}} Precision.
- {{Q}} 99% train accuracy but ~52% test accuracy means? {{Ans}} Overfitting.

## [[L3. ML in Investment Management]]
- [[Risk attitude]] investors are usually risk-averse: higher risk requires higher expected return / risk premium, but not always the lowest-risk choice.
- [[Return]] = (Ending Value - Invested Amount)/Invested Amount; if dividends exist, include dividend + price change.
- [[Risk]] measured by standard deviation; distinguish stand-alone risk vs portfolio risk.
- [[Probability distributions]] expected return + standard deviation show central tendency and uncertainty.
- [[Graphs/networks]] 3 Cs = centrality, clusterness, connectedness; useful in portfolio/correlation thinking.
- [[CAPM]] r_i = r_RF + (r_M - r_RF)β_i.
- [[Market risk premium]] extra return for taking average market risk; often around 4% to 8% yearly.
- [[Beta]] β=1 same as market; β>1 riskier than market; β<1 less risky. Market index acts as the system-wide risk proxy.
- [[Factor pricing]] E[R_i] = R_f + β1F1 + β2F2 + ... + βkFk.
- [[Factor examples]] market, size, value, momentum, profitability, investment; practical factors include P/E, P/B, EV/EBITDA, EV/Sales, ROE.
- [[AI/ML factors]] can “cook” more factors from alternative data such as sentiment or image/satellite factors and learn non-linear relations.
- [[Why factors work]] risk-based view, behavioral view, structural/frictions view.
- [[Factor challenges]] timing is hard, crowding reduces returns, implementation costs matter.
- [[Performance metrics]] Sharpe = (R_p-R_f)/σ_p; Sortino = (R_p-R_f)/σ_d (downside only); Max Drawdown = (Trough-Peak)/Peak; also total return/CAGR, information ratio, skewness, kurtosis.
- [[Backtesting]] simulate a strategy on historical data to judge profitability, drawdowns, and robustness.
- [[Backtesting traps]] one metric only, short periods, ignoring skewness/kurtosis, survivorship bias, data snooping.
- [[ML methods]] multinomial/ordered logistic regression for market regimes (bear/rangebound/bull), bagging, AdaBoost, gradient boosting.
- [[Ensembles]] bagging lowers variance; boosting learns sequentially to reduce bias / capture nonlinearity. Profitability and stability matter more than sophistication.
- [[Example MCQs]]
- {{Q}} If β > 1, what does it mean? {{Ans}} The stock is more sensitive/riskier than the market.
- {{Q}} Sharpe vs Sortino: which penalizes only downside risk? {{Ans}} Sortino.
- {{Q}} Great backtest but weak future results often indicate? {{Ans}} Overfitting / data snooping / non-stationarity.

<!--PAGEBREAK-->

## [[L4. Algorithmic Trading and NLP in Finance]]
- [[NLP]] computationally converts text into usable signals to answer what/who/where/relationship questions from unstructured data.
- [[Text sources]] business news, reports, contracts, emails, legal docs, transcripts, analyst reports, customer feedback, social media, Fed minutes, web pages.
- [[BoW]] count-based term representation; fast and simple but loses word order/context.
- [[Tokenization]] breaks text into tokens/subwords/root forms; helps models and LLMs process language efficiently.
- [[Word embeddings]] words become vectors; semantic closeness depends on context.
- [[LLMs]] large transformer-based models pre-trained on massive data; training flow: data collection -> transformer model -> optimization -> fine-tuning with human feedback.
- [[Finance NLP uses]] sentiment analysis, earnings call analysis, topic classification, intelligent tagging, research summarization, KYC/AML entity matching, personal banking assistants.
- [[Intelligent tagging]] answers who/what/where/relationship questions; useful in asset management, compliance, and tracking news affecting portfolios or competitors.
- [[KYC/AML text challenge]] entity names may appear in many spellings/regions; name matching is not trivial.
- [[Topic classification]] supervised learning maps text/news into IPO, bond issuance, compliance, rates, markets, etc.
- [[TA vs fundamentals]] both can be used; AI/ML can augment either rather than relying only on human intuition.
- [[Technical analysis]] studies historical prices/patterns to estimate direction/timing; usually more useful for shorter-term trading.
- [[Dow Theory]] the market discounts everything; primary trend matters; phases = accumulation -> public participation -> distribution.
- [[MA]] smooths prices; used for trend, support/resistance, and filtering noise.
- [[MACD]] MACD line = 12-EMA - 26-EMA; signal line = 9-EMA of MACD. Crossovers/divergence can hint at buy/sell or reversal.
- [[RSI]] = 100 - 100/(1 + n_up/n_down). In slides: <30 often oversold; >80 often overbought.
- [[Bollinger Bands]] SMA with upper/lower bands around plus/minus 2 standard deviations. Tightening can precede a sharp move; above upper band = overbought sign; below lower band = oversold sign.
- [[TA pros/cons]] easy to apply and behavior-aware, but subjective, weakly theory-based, and poor at surprise fundamental events.
- [[Example MCQs]]
- {{Q}} Biggest weakness of BoW? {{Ans}} It loses word order and deep context.
- {{Q}} RSI > 80 suggests? {{Ans}} Overbought. RSI < 30? Oversold.
- {{Q}} MACD crossing above the signal line often suggests? {{Ans}} Possible bullish / buy signal.

## [[L5. ML in Regulatory Compliance]]
- [[Compliance types]] regulatory compliance + financial crime compliance.
- [[AML/CFT process]] Placement -> Layering -> Integration.
- [[Why AML matters]] undermines financial integrity, distorts trade/investment, funds crime/terrorism, causes reputational/regulatory damage, needs global cooperation.
- [[FATF]] founded 1989; FATF 40 Recommendations cover risk assessment, KYC, suspicious transaction reporting, beneficial ownership, sanctions, cooperation.
- [[Core obligations]] KYC, Customer Due Diligence (CDD), Suspicious Activity Reporting (SAR), record keeping, risk-based approach.
- [[Red flags]] unusual volume/frequency, just-below-threshold transactions, rapid movement between accounts, complex structures, reluctance to provide info, shell companies, high-risk jurisdictions, sanctions links, trade finance misuse, crypto mixing/layering.
- [[AI/ML help]] sifts huge datasets, improves transaction monitoring, reduces false positives, traces crypto/blockchain links, continuously monitors risk/news.
- [[Unsupervised learning]] reduces complexity/noise through grouping. Main methods here: K-means, DBSCAN, graphical ML.
- [[K-means]] choose k -> initialize centers -> assign points to nearest center -> update means -> repeat until stable. Works best for compact groups when k is known.
- [[Distance measures]] Euclidean, Manhattan, Minkowski. Standardize numeric data first; nominal data can use simple matching or binary expansion.
- [[Anomaly detection]] = outlier detection; used in fraud, AML, suspicious trades, market anomalies, stress testing.
- [[DBSCAN]] density-based using eps (radius) + minPts. Strengths = finds arbitrary shapes, handles noise, good for fraud/outlier detection.
- [[Rules vs ML]] rules-based compliance is static; ML is more adaptive and can use high-dimensional features.
- [[False positives]] too many alerts create huge backlogs; tuning is a trade-off between strictness and laxness.
- [[Graph ML]] nodes + links represent relationships. 3 Cs = centrality, clusterness, connectedness. Uses include KYC links, portfolio correlations, contagion/stability analysis.
- [[Example MCQs]]
- {{Q}} Correct order of money-laundering stages? {{Ans}} Placement -> Layering -> Integration.
- {{Q}} Best method for irregular suspicious clusters + outliers? {{Ans}} DBSCAN.
- {{Q}} What must K-means know upfront? {{Ans}} Number of clusters k.

## [[L6. Agentic AI in Finance]]
- [[Agentic AI]] autonomous, goal-directed systems that perceive, reason, act, and adapt to achieve outcomes.
- [[Benefits]] automate repetitive work, reduce manual effort, improve responsiveness, fit enterprise workflows.
- [[Vs GenAI]] GenAI mainly generates content/summaries; Agentic AI is more task-based, tool-using, and action-oriented (though it may use GenAI inside the workflow).
- [[How it works]] perception (APIs/data feeds/text/images) -> reasoning/decision making (LLMs/RL/ML) -> action execution -> goal-driven adjustment.
- [[Technologies]] LLMs, neural nets, RL, APIs/tools, planning algorithms, short-term + long-term memory systems.
- [[Need own data?]] generic LLMs are not enough; use local hosting, RAG, or MCP.
- [[Ollama]] local runtime for open-source LLMs. Benefits: privacy, cost control, low latency, reproducibility, offline use, easier compliance.
- [[RAG]] grounds answers in external/internal documents via vector DB + parsing. Types: pure document RAG; hybrid document + web RAG.
- [[MCP]] standard way for LLMs to connect to tools, APIs, databases, and services.
- [[RAG vs MCP]] RAG brings knowledge/docs to the model; MCP brings the model to live systems/tools. RAG is for grounded Q&A/summaries; MCP is for dynamic querying, analytics, execution, orchestration.
- [[Enterprise concerns]] scalability, security/confidentiality, legacy integration, robustness, customization, structured JSON output, conversational memory, search.
- [[Framework roles]] Ollama = local model runner; LlamaIndex = RAG framework; LangChain = general LLM app framework; LangGraph = multi-agent orchestration.
- [[Building blocks]] knowledge bases, RAG/MCP for context, LLM for reasoning, actionable APIs for execution, orchestration/workflow management, supervision and regulation.
- [[Finance agent examples]] FX hedging agents (portfolio, market data, risk, compliance, reporting) and stock-trading agents (market data, technical analysis, risk management, execution).
- [[Design questions]] objective? current process? what needs perception/action/supervision? what memory? what knowledge base? what LLM? what actions? where is human-in-the-loop?
- [[Example MCQs]]
- {{Q}} Summarize a PDF prospectus section: RAG or MCP? {{Ans}} RAG.
- {{Q}} Query live spending categories from a database: RAG or MCP? {{Ans}} MCP.
- {{Q}} Agentic AI vs GenAI in one line? {{Ans}} action/orchestration toward goals vs mainly generation/summarization.

## [[Quick Compare + MCQ Traps]]
- [[Supervised]] = labels; [[Unsupervised]] = patterns; [[Reinforcement]] = reward-based learning.
- [[Metrics]] default/fraud detection usually values recall/sensitivity more; marketing/prospecting often values precision more.
- [[Risk]] β>1 = stock more sensitive/riskier than market. Sharpe compares return per total risk; Sortino only penalizes downside risk.
- [[Text]] BoW loses order/context; embeddings preserve contextual similarity.
- [[Clustering]] K-means needs k and is weaker with irregular/noisy clusters; DBSCAN is better for irregular clusters + noise/outliers.
- [[Asset pricing]] CAPM is single-factor (market). Factor models are multi-factor.
- [[Generalization]] overfitting can make training accuracy look excellent but real performance collapse.
- [[LLM integration]] RAG = docs/knowledge grounding; MCP = live tools/systems connectivity.
- [[Governance]] Agentic AI still needs privacy controls, safety, and human judgment.
- [[Quick thresholds]] market risk premium often 4% to 8%; common stock betas 0.5 to 1.5; RSI <30 oversold, >80 overbought; Sharpe 1+ good, 2+ excellent, 3+ exceptional.

## [[Ultra-Compact Formula Box]]
- [[Min-max]] x' = (x - min)/(max - min) scaled to a new range.
- [[z-score]] z = (x - μ)/σ.
- [[Accuracy]] = (TP+TN)/(TP+TN+FP+FN).
- [[Precision]] = TP/(TP+FP).
- [[Recall]] = TP/(TP+FN).
- [[CAPM]] r_i = r_RF + (r_M-r_RF)β_i.
- [[Factor model]] E[R_i] = R_f + ΣβF.
- [[Sharpe]] = (R_p-R_f)/σ_p.
- [[Sortino]] = (R_p-R_f)/σ_d.
- [[Max DD]] = (Trough-Peak)/Peak.
- [[MACD]] = 12-EMA - 26-EMA; Signal = 9-EMA(MACD).
- [[RSI]] = 100 - 100/(1 + n_up/n_down).