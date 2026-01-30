# Chapter 2 (2.1–2.3) Quiz Revision Notes (EN + 中文)

> **Exam is in English**, so each key point is written in **English first**, followed by a **Chinese explanation** to help you memorize.

---

## 2.1 Correlation Analysis

### 2.1.1 Why “statistics alone is not enough”

- **EN:** Datasets can share similar statistical values but look totally different visually, so visualization is essential in analysis (classic examples: Anscombe-like cases). :contentReference[oaicite:0]{index=0}
- **中:** 只看均值/方差等统计量可能会“被骗”，不同数据集可能统计量很像但形状差很多，所以可视化是分析必需。

---

### 2.1.2 What is Exploratory Data Analysis (EDA)

- **EN:** EDA is an **iterative** process: ask questions → visualize to answer → evaluate results → ask new questions → repeat. :contentReference[oaicite:1]{index=1}
- **EN:** EDA often includes transformations like **normalize/log**, regrouping categories, and binning (e.g., histograms). :contentReference[oaicite:2]{index=2}
- **中:** EDA 是“反复迭代”的探索流程：先提出问题，再画图找答案，然后检查结果、产生新问题继续循环；常配合数据变换（归一化、log）、类别合并、分箱等。

---

### 2.1.3 What is correlation (concept)

- **EN:** Correlation examines how strongly variables are related because values are collected from the same event/situation. :contentReference[oaicite:3]{index=3}
- **EN:** Correlation asks: *Does one variable change with another? How strong is the relationship?* :contentReference[oaicite:4]{index=4}
- **中:** 相关性衡量变量是否“联动变化”以及联动强度。

---

### 2.1.4 Pearson correlation coefficient (important formula) **皮尔逊相关系数**

- **EN:** Pearson correlation coefficient **ρxy** ranges from **-1 to +1**. :contentReference[oaicite:5]{index=5}
- **EN (Formula):**
  ρx,y=cov(X,Y) /  (σx·σy)

  where **cov** is covariance and **σX, σY** are standard deviations. :contentReference[oaicite:6]{index=6}
- **EN:** Rule-of-thumb in slide: **Strong correlation** often considered **>|0.7|**. :contentReference[oaicite:7]{index=7}
- **中:** 皮尔逊相关系数范围[-1,1]：正相关/负相关；绝对值越大线性关系越强。公式一定要记住：协方差 / 标准差乘积。
- ρ 的取值范围：-1 到 +1 是什么意思？

  * **ρ = +1** ：完全正线性相关

    **EN:** as X increases, Y increases perfectly in a straight line

    **中:** X 越大，Y 也按固定比例越大（点全在一条上升直线）
  * **ρ = -1** ：完全负线性相关

    **EN:** as X increases, Y decreases perfectly in a straight line

    **中:** X 越大，Y 按固定比例越小（点全在一条下降直线）
  * **ρ = 0** ：没有“线性相关”

    **EN:** no linear relationship (could still be nonlinear)

    **中:** 不代表“完全没关系”，只是 **没有直线型关系** ，可能存在曲线关系
  * 
  * # 公式：ρx,y=cov(X,Y) /  (σx·σy)是什么意思？
  * ### cov(X,Y)（协方差）


    * **EN:** measures whether X and Y move together (same direction or opposite)
    * **中:** 衡量 X 和 Y 是否“同涨同跌”还是“一个涨一个跌”

    协方差的符号：

    * **cov > 0** ：倾向同向变化 → 正相关
    * **cov < 0** ：倾向反向变化 → 负相关
    * **cov ≈ 0** ：没有明显同向/反向趋势

    ### σX、σY（标准差）

    * **EN:** how spread out X and Y are
    * **中:** X、Y 自己的波动幅度（离散程度）

    ### 为什么要除以 σXσY？

    * **EN:** to normalize the value so correlation is always between -1 and +1
    * **中:** 这是“归一化”，把协方差变成**无单位、可比较**的指标，结果稳定落在 [-1,1]

---

### 2.1.5 Correlation ≠ Causation (high-frequency MCQ trap)

- **EN:** Do not conclude causation from correlation; correlated variables may be driven by underlying factors. :contentReference[oaicite:8]{index=8}
- **中:** “相关不等于因果”是经典陷阱题：看到相关只能说有关系，不能说X导致Y。

---

### 2.1.6 Univariate / Bivariate / Multivariate analysis (what to use)

- **EN:** Univariate analysis analyzes **one variable at a time**; purpose: understand central tendency (mean/median/mode), dispersion (range/variance/quartiles), and outliers. :contentReference[oaicite:9]{index=9}
- **中:** 单变量分析：不谈变量之间关系，主要看“中心位置”“离散程度”“离群点”。
- **EN:** Multivariate analysis studies **3 or more variables**; a common visualization is a **scatterplot matrix**, and Seaborn **pairplot()** provides it. :contentReference[oaicite:10]{index=10}
- **EN:** In **pairplot()**, `kind='reg'` can show regression lines. :contentReference[oaicite:11]{index=11}
- **EN:** `hue=` adds a categorical variable by color in pairplot. :contentReference[oaicite:12]{index=12}
- **中:** 多变量分析常用 pairplot（散点矩阵）；`kind='reg'`画回归线；`hue`用颜色引入类别变量。

---

### 2.1.7 Heatmap + corr() for correlation values (code idea)

- **EN:** Use Pandas `corr()` and Seaborn `heatmap()` to compute/display Pearson correlations; `vmin=-1, vmax=1` and a diverging colormap improve interpretability. :contentReference[oaicite:13]{index=13}
- **EN:** You can focus on correlation vs one target variable and sort using `sort_values()`. :contentReference[oaicite:14]{index=14}
- **中:** 热力图=相关系数矩阵可视化；`corr()`算系数；对某个目标变量（如Price）排序能更快找最相关特征。

---

### 2.1.8 Confirmatory analysis**验证性分析** (hypothesis testing假设检验) essentials

- **EN:** **One-tailed test** has more statistical power than two-tailed at the same significance level (if direction is correctly predicted). :contentReference[oaicite:15]{index=15}
- **EN:** Example hypotheses:
  - **H0:** μReading = μWriting (no difference)
  - **Ha:** μReading ≠ μWriting (two-tailed) OR μReading > μWriting (one-tailed, “larger”) :contentReference[oaicite:16]{index=16}
- **EN:** Common threshold: reject H0 when **p < 0.05** (less than 5% chance due to randomness). :contentReference[oaicite:17]{index=17}
- **中:** 验证性分析=假设检验；单尾/双尾要看你是否“提前预测方向”；p值<0.05通常认为显著，拒绝原假设。只有在看数据之前就有充分理由认为方向一定是“>”或“<”，才用单尾。否则就应该用双尾。

---

## 2.2 Visualisation for AI

### 2.2.1 Count plots (imbalance checking)

- **EN:** Count plots visualize the **quantity of each category**; for better analysis, **sort categories** and **annotate counts** on bars. :contentReference[oaicite:18]{index=18}
- **EN (Code idea):** using `value_counts().index` for order + `ax.bar_label()` for labels. :contentReference[oaicite:19]{index=19}
- **中:** countplot 常用来快速检查类别是否不平衡；排序+标注数值更利于比较。

---

### 2.2.2 Scatter plots (2D relationships + categorical coloring)

- **EN:** Scatter plot shows relationship between two numeric features; limitation: only **two variables at a time**. :contentReference[oaicite:20]{index=20}
- **EN:** `hue=` in Seaborn scatterplot uses color for **categorical** labels to compare relationships by class. :contentReference[oaicite:21]{index=21}
- **EN:** The slide notes iris-setosa can look distinct in feature relationships, useful for classification intuition. :contentReference[oaicite:22]{index=22}
- **EN:** Use **alpha transparency** to reduce occlusion and reveal hidden clusters. :contentReference[oaicite:23]{index=23}
- **中:** 散点图用于两变量关系；`hue`用颜色区分类别（必须是类别型）；alpha透明度解决点遮挡，能发现隐藏簇。

---

### 2.2.3 Parallel Coordinates Plot (PCP) (multivariate relationships)

**Concept**

- **EN:** PCP visualizes relationships between **multiple variables**; each vertical axis is a numeric feature; each data point is a polyline across axes; colormap maps the target category. :contentReference[oaicite:24]{index=24}
- **中:** PCP=多维数据可视化：每个轴一个特征，一条线代表一个样本，颜色表示类别/目标。

**Interactive features**

- **EN:** Axes can be **swapped by dragging**. :contentReference[oaicite:25]{index=25}
- **EN:** **Brushing**: click-hold and slide on an axis to select/highlight a subset. :contentReference[oaicite:26]{index=26}
- **中:** 交互是考点：拖动换轴；刷选(brushing)能高亮某范围样本。

**Interpreting patterns (MCQ-style)**

- **EN:** Understanding simple patterns helps interpret complex PCP; examples include strong/weak negative correlation, strong positive correlation, separated clusters, circular patterns, and outliers. :contentReference[oaicite:27]{index=27}
- **中:** 线条“交叉程度/倾斜方向/是否成束”等可提示相关性、分群、离群点等。

---

### 2.2.4 Visualising model performance

#### Confusion Matrix (CM)

- **EN:** CM compares predicted vs actual labels; diagonal cells are correct classifications; off-diagonal are misclassifications; can be shown as a heatmap with a colormap. :contentReference[oaicite:28]{index=28}
- **中:** 混淆矩阵=分类结果对照表；对角线正确，非对角错误；用热力图更直观。

#### ROC curve + AUC

- **EN:** ROC plots **TPR vs FPR** across thresholds for binary classifier; **AUC** summarizes discrimination ability. :contentReference[oaicite:29]{index=29}
- **EN:** AUC ranges **0–1**, where **0.5** is random guessing and **1.0** is perfect. :contentReference[oaicite:30]{index=30}
- **中:** ROC看阈值变化下TPR/FPR；AUC越大越好；0.5≈随机。

#### Precision–Recall (P–R) curve

- **EN:** P–R curve plots **Precision (y)** vs **Recall (x)** across thresholds; good for **imbalanced datasets**, where ROC can be overly optimistic. :contentReference[oaicite:31]{index=31}
- **EN:** It can show the point where the first false positive occurs (precision drops from 1.0). :contentReference[oaicite:32]{index=32}
- **中:** 不平衡数据（如欺诈检测）更偏向用PR曲线；它直观看“找全(Recall)”和“找准(Precision)”的权衡。

#### Learning curve (underfitting vs overfitting)

- **EN:** Learning curve shows performance vs training data/epochs; diagnostic for underfitting/overfitting. :contentReference[oaicite:33]{index=33}
- **EN:** Underfitting: training and validation plateau at low scores; adding data won’t help much (flattening). :contentReference[oaicite:34]{index=34}
- **EN:** Overfitting: large/increasing gap between training and validation. :contentReference[oaicite:35]{index=35}
- **中:** 学习曲线是“诊断图”：都低=欠拟合；训练高验证低且差距扩大=过拟合。

---

## 2.3 Time Series Analysis

### 2.3.1 What is a time series & why it matters

- **EN:** A time series is a sequence of data points in time order; can be sampled from milliseconds to years. :contentReference[oaicite:36]{index=36}
- **EN:** Time series analysis helps understand and forecast future trends (important in finance/science). :contentReference[oaicite:37]{index=37}
- **中:** 时间序列=按时间排序的观测值；分析目的常是发现趋势/周期并为预测做准备。

---

### 2.3.2 Handling time series datasets (Pandas)

- **EN:** `parse_dates` normalizes date formats when reading CSV; common format is **YYYY-MM-DD**. :contentReference[oaicite:38]{index=38}
- **EN:** Typical single-parameter time series has two columns: timestamp + measured value. :contentReference[oaicite:39]{index=39}
- **EN:** Create helper columns like `Year` and `Month` for grouping and hue-based plots. :contentReference[oaicite:40]{index=40}
- **中:** 读入时间列要标准化；经常要从日期拆出Year/Month方便画季节性图和箱线图。

---

### 2.3.3 Components of a time series

- **EN:** Time series can include **Seasonal (St)**, **Trend (Tt)**, **Cyclical (Ct)**, and **Residual/Noise (Rt)** components. :contentReference[oaicite:41]{index=41}
- **EN:** Cyclical component is often merged into a trend-cycle component. :contentReference[oaicite:42]{index=42}
- **中:** 四大成分：季节性、趋势、周期（中期非严格周期）、残差噪声；周期很多时候并入趋势项一起看。

---

### 2.3.4 Additive vs Multiplicative decomposition (must memorize)

- **EN (Equations):**
  - Additive: \(x_t = S_t + T_t + R_t\) :contentReference[oaicite:43]{index=43}
  - Multiplicative: \(x_t = S_t \, T_t \, R_t\) :contentReference[oaicite:44]{index=44}
- **EN (When to use):**
  - Additive: seasonality magnitude **does not depend** on the series level. :contentReference[oaicite:45]{index=45}
  - Multiplicative: seasonality magnitude **varies with** the series level. :contentReference[oaicite:46]{index=46}
- **中:** 加法模型：季节波动幅度固定；乘法模型：序列越大季节波动也越大（幅度随水平变化）。

---

### 2.3.5 Visualising seasonality and trend

**Seasonality**

- **EN:** Seasonal patterns can be compared using **seasonal line plots** with different colors (e.g., hue by Year). :contentReference[oaicite:47]{index=47}
- **EN:** Seasonal variation within a season can be shown using **month-wise box plots**; median lines show peak/trough; box height shows variation. :contentReference[oaicite:48]{index=48}
- **中:** 季节性：按年份上色的季节折线图；月度箱线图看每个月分布差异，median提示峰谷。

**Trend**

- **EN:** Trend over years can be visualized using **year-wise box plots**; tracing medians shows trend changes. :contentReference[oaicite:49]{index=49}
- **中:** 趋势：按年份分组做箱线图，连看中位线变化就是趋势。

---

### 2.3.6 Decomposing time series (workflow + statsmodels)

- **EN:** One approach is isolating trend using **moving average/local averaging** over a window. :contentReference[oaicite:50]{index=50}
- **EN:** After isolating trend and choosing model type, seasonal and residual can be extracted (e.g., multiplicative: \(S_t \times R_t = x_t / T_t\); additive: \(S_t + R_t = x_t - T_t\)). :contentReference[oaicite:51]{index=51}
- **EN:** `statsmodels.tsa.seasonal.seasonal_decompose()` can decompose series into components using additive or multiplicative model. :contentReference[oaicite:52]{index=52}
- **中:** 分解流程：先移动平均提取趋势，再根据模型类型提取季节项与残差；statsmodels 的 seasonal_decompose 是常见工具（会考函数名/用途）。

---

# Practice MCQs (Selection-based Quiz Style)

## A. Correlation Analysis (2.1) — 8 Questions

**Q1.** Which statement best describes EDA?

A. A one-time process done after modeling

B. An iterative process of asking questions, visualizing, and refining questions

C. A process that avoids data transformations

D. A process only for time series

**Answer: B**

- **EN:** EDA is iterative: ask → visualize → evaluate → ask new questions.
- **中:** EDA 是不断循环的探索流程，不是一锤子买卖。

**Q2.** Pearson correlation coefficient ρ ranges from:

A. 0 to 1

B. -∞ to +∞

C. -1 to +1

D. -0.5 to +0.5

**Answer: C**

- **中:** [-1,1] 必背。

**Q3.** The correct formula for Pearson correlation is:
A. cov(X,Y) / (σX + σY)
B. cov(X,Y) / (σX σY)
C. (σX σY) / cov(X,Y)
D. cov(X,Y) / (σX² + σY²)
**Answer: B**

**Q4.** “Correlation implies causation.” This statement is

A. True

B. False

C. True only for |ρ|>0.7

D. True if p<0.05

**Answer: B**

- **中:** 相关≠因果，常考陷阱。

**Q5.** Which visualization is explicitly stated as common for multivariate data?
A. Pie chart
B. Scatterplot matrix / pairplot
C. Word cloud
D. Gantt chart
**Answer: B**

**Q6.** In Seaborn `pairplot()`, adding regression lines is done by:
A. `kind='reg'`
B. `style='reg'`
C. `line='reg'`
D. `reg=True`
**Answer: A**

**Q7.** Which p-value rule is mentioned for rejecting H0?
A. p < 0.10
B. p < 0.01 only
C. p < 0.05
D. p > 0.05
**Answer: C**

**Q8.** One-tailed tests are often more likely to be significant than two-tailed tests because they:
A. Always use larger sample sizes
B. Have more statistical power at the same significance level
C. Ignore the null hypothesis
D. Always increase variance
**Answer: B**

---

## B. Visualisation for AI (2.2) — 8 Questions

**Q9.** Why sort categories and annotate counts in a count plot?
A. It makes the plot 3D
B. It improves visual comparison and readability
C. It removes outliers
D. It converts data to continuous
**Answer: B**

**Q10.** In Seaborn scatterplot, `hue=` should be assigned to:
A. A continuous numeric variable only
B. A categorical variable
C. The x-axis variable
D. The y-axis variable
**Answer: B**

# **Q11.** The alpha parameter in scatter plots helps mainly with:

A. Increasing correlation strength

# B. Occlusion from overlapping points

C. Changing axis units
D. Adding regression coefficients
**Answer: B**

# Q12.A PCP represents each data point as:

A. A single dot
B. A bar

# C. A line connecting values across multiple axes

D. A pie slice
**Answer: C**

# Q13.In an interactive PCP (Plotly Express), “brushing” means:

A. Smoothing the curve with moving average

# B. Selecting a subset by dragging on an axis

C. Rotating the plot in 3D
D. Sorting categories by frequency
**Answer: B**

# Q14.In a confusion matrix, off-diagonal values indicate:

A. Correct classifications

# B. Misclassifications

C. The AUC score
D. Feature importance
**Answer: B**

# **Q15.** ROC curve plots:

A. Precision vs Recall

# B. TPR vs FPR across thresholds

C. Loss vs Epochs only
D. Mean vs Variance
**Answer: B**

# **Q16.** Precision–Recall curves are especially useful when:

A. Dataset is perfectly balanced

# B. Dataset is imbalanced (e.g., fraud detection)

C. Only one class exists
D. Only time series data is used
**Answer: B**

---

## C. Time Series Analysis (2.3) — 8 Questions

**Q17.** A time series is:
A. A random set of points with no order
B. A sequence of data points in successive time order
C. A categorical dataset only
D. A scatter plot output
**Answer: B**


# **Q18.** A common single-parameter time series dataset typically contains:

A. Two timestamp columns

# B. Timestamp + measured value

C. Only measured values
D. Only categories
**Answer: B**

# **Q19.** Additive decomposition is preferred when:

A. Seasonal magnitude depends on the series level

## B. Seasonal magnitude does not depend on the series level

C. There is no trend
D. There is no residual
**Answer: B**


# **Q20.** Multiplicative decomposition is preferred when:

## A. Seasonal magnitude varies with the series level

B. Seasonal magnitude is constant
C. Trend is always zero
D. Cycles are strictly periodic
**Answer: A**

# **Q21.** Month-wise box plots are used mainly to:

## A. Visualize within-season variations (seasonality)

B. Compute ROC AUC
C. Show class imbalance
D. Replace scatter plots
**Answer: A**

# **Q22.** Trend can be observed by:

A. Randomizing the time index

## B. Year-wise box plots and tracing median changes

C. Pie charts
D. Confusion matrices
**Answer: B**

# **Q23.** The method described for isolating trend before decomposition is:

A. Brushing

## B. Moving average / local averaging

C. Countplot sorting
D. Pairplot hue
**Answer: B**

# **Q24.** `seasonal_decompose()` is used to:

A. Compute Pearson correlation

#  B. Decompose time series into components using additive/multiplicative model

C. Plot confusion matrix
D. Generate PCP brushing
**Answer: B**

---

## Quick English Keywords (High-frequency)

- **EDA** (Exploratory Data Analysis): iterative exploration
- **Correlation / Pearson ρ**: linear relationship strength, -1..+1
- **Causation**: not guaranteed by correlation
- **Confusion Matrix**: diagonal correct, off-diagonal errors
- **ROC / AUC**: TPR vs FPR, AUC 0.5 random, 1 perfect
- **Precision–Recall**: best for imbalanced datasets
- **Learning curve**: underfitting vs overfitting patterns
- **Time series decomposition**: additive vs multiplicative 

---
