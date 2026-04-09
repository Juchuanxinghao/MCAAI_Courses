# CA6115 Final Quiz Bilingual Review Notes

# CA6115 期末测验中英文双语复习资料

> **Quiz info｜测验信息**
> **Date:** 2026-04-11 10:45 AM
> **Format:** 30 MCQs, 30% of total score
> **Scope:** **All topics are tested｜全部主题都会考**
> Based on the lecture PDFs `L1` to `L6` in `25S3/CA6115/lecture notes`.

---

## 1. Exam Snapshot｜考试速览

### Likely question styles｜常见题型

- **Definition recall｜概念定义题**: e.g. FEAT, CAPM, RAG, DBSCAN
- **Comparison questions｜对比题**: e.g. Logistic Regression vs Decision Tree, RAG vs MCP
- **Formula understanding｜公式理解题**: Accuracy, Precision, Recall, Sharpe Ratio, CAPM
- **Use-case matching｜应用场景题**: Which ML method fits which finance problem?
- **Interpretation questions｜含义判断题**: e.g. What does `beta > 1` mean? What does `RSI > 80` mean?

### Last-minute strategy｜临考策略

1. **Memorize the key comparisons｜先背关键对比表**
2. **Know the formulas and what they mean｜记住公式及其含义**
3. **Focus on finance applications, not just AI terms｜重点看金融应用场景**
4. **Pay attention to trade-offs｜特别注意各种取舍关系**
   - false positives vs false negatives
   - overfitting vs underfitting
   - explainability vs complexity
   - privacy/governance vs innovation

---

## 2. High-Yield One-Page Summary｜高频一页速记

- **AI/ML in finance is not only about models, but also domain knowledge.****金融中的 AI/ML 不只是模型，更依赖金融场景知识。**
- **Data quality, governance, and explainability are core themes across the whole course.****数据质量、治理和可解释性是全课程主线。**
- **Supervised learning uses labels; unsupervised learning finds patterns; reinforcement learning learns from rewards.****监督学习有标签；无监督学习找结构；强化学习通过奖励学习。**
- **In finance, generalization matters more than in-sample accuracy.****在金融场景中，泛化能力比样本内高准确率更重要。**
- **CAPM says market risk matters; factor models extend CAPM with more drivers.****CAPM 强调市场风险；因子模型在此基础上加入更多驱动因素。**
- **NLP and LLMs turn text into usable signals for sentiment, KYC, compliance, and research.****NLP 和 LLM 能把文本转成可用信号，用于情绪分析、KYC、合规和研究。**
- **K-means and DBSCAN are key unsupervised methods in compliance/fraud detection.****K-means 和 DBSCAN 是合规/欺诈检测中的重要无监督方法。**
- **Agentic AI is goal-directed, tool-using, and action-oriented; GenAI is more focused on generation.**
  **Agentic AI 以目标与执行为中心；GenAI 更偏向生成内容。**

---

## 3. Lecture-by-Lecture Revision｜按讲义逐章复习

---

## L1. Introduction to AI in Finance｜金融中的 AI 导论

### Core knowledge points｜核心知识点

#### 1) Where AI/ML is used in finance｜AI/ML 在金融中的应用

- Financial operations｜金融运营
- Credit loans｜信贷审批
- Customer prospecting/segmentation｜客户开发与分层
- Trading and risk management｜交易与风险管理
- Regulatory compliance, AML/KYC｜监管合规、反洗钱、KYC
- Chatbots and customer service｜聊天机器人与客户服务

#### 2) Types of data in finance｜金融数据类型

- **Structured data｜结构化数据**Numeric prices, market cap, financial ratios, statements数值型数据，如价格、市值、财务比率、财报
- **Ordinal data｜有序数据**Credit ratings, analyst recommendations如信用评级、分析师评级
- **Nominal data｜名义数据**Industry sectors, SIC/NAICS/GICS categories如行业分类
- **Unstructured data｜非结构化数据**Text, images, audio文本、图像、音频
- **Alternative data｜另类数据**
  Satellite imagery, transaction data, web traffic, geolocation
  卫星图像、交易数据、网页流量、地理位置数据

#### 3) Data transformation｜数据变换

- Smoothing｜平滑
- Aggregation｜聚合
- Generalization｜概括/泛化
- Normalization｜归一化
- Feature construction｜特征构造

**Min-max normalization｜最小-最大归一化**
Maps data into a fixed range, often `[0,1]`.
把数据映射到固定区间，常见为 `[0,1]`。

**Z-score standardization｜Z 分数标准化**
\[
z = \frac{x-\mu}{\sigma}
\]
Used to center data around the mean and scale by standard deviation.
按均值和标准差标准化数据。

#### 4) Data encoding｜数据编码

- Models need numeric inputs｜模型需要数值输入
- **One-hot encoding** avoids fake ordering among categories
  **独热编码**避免类别之间出现“假顺序”

#### 5) AI governance in finance｜金融中的 AI 治理

**MAS FEAT Principles｜新加坡 MAS 的 FEAT 原则**

- **F – Fairness｜公平性**: avoid bias, treat similar customers consistently
- **E – Ethics｜伦理性**: use AI responsibly and appropriately
- **A – Accountability｜问责性**: institutions remain responsible for AI outcomes
- **T – Transparency｜透明性**: AI decisions should be explainable and documented

#### 6) Data governance｜数据治理

- Data quality｜数据质量
- Security & privacy｜安全与隐私
- Standardization｜标准化
- Accountability｜责任归属
- Value creation｜价值创造

**Data life cycle｜数据生命周期**
Plan → Design → Create/Obtain → Storage/Maintenance → Use → Enhance
规划 → 设计 → 创建/获取 → 存储/维护 → 使用 → 完善

### Exam focus｜考点提示

- Know the difference between **structured / unstructured / alternative data**区分结构化、非结构化和另类数据
- Understand **FEAT** and **data governance**理解 FEAT 和数据治理
- Know why **one-hot encoding** is used
  知道为什么要用独热编码

---

## L2. ML in Finance Operations｜金融运营中的机器学习

### Core knowledge points｜核心知识点

#### 1) Types of ML｜机器学习类型

- **Supervised learning｜监督学习**: learn from labeled data
- **Unsupervised learning｜无监督学习**: learn hidden patterns
- **Reinforcement learning｜强化学习**: learn through rewards and environment

#### 2) Supervised learning workflow｜监督学习流程

1. Prepare labeled data｜准备带标签数据
2. Split into training/test sets｜划分训练集和测试集
3. Train the classifier｜训练分类器
4. Evaluate with proper metrics｜用正确指标评估

#### 3) Data partition methods｜数据划分方式

- **Resubstitution｜重代入法**: training data also used as test data; only if data is scarce
- **Hold-out｜留出法**: common `80/20` split
- **Cross-validation｜交叉验证**: more robust average performance
- **Bootstrap｜自助采样法**: repeated random sampling

#### 4) Classification models｜分类模型

- **Logistic Regression｜逻辑回归**Interpretable, baseline model, good for binary classification可解释性强，常用基线模型
- **Naïve Bayes｜朴素贝叶斯**Simple probabilistic benchmark简单快速，常作基准模型
- **Decision Tree｜决策树**Transparent rules, easy to explain规则清晰、易解释
- **Neural Networks / Deep Learning｜神经网络/深度学习**
  Powerful but black-box and may overfit
  能力强但黑箱且容易过拟合

#### 5) Evaluation metrics｜评估指标

**Confusion matrix｜混淆矩阵** includes:

- TP: True Positive｜真正例
- TN: True Negative｜真负例
- FP: False Positive｜假正例
- FN: False Negative｜假负例

**Accuracy｜准确率**
\[
\text{Accuracy} = \frac{TP+TN}{TP+TN+FP+FN}
\]

**Precision｜精确率**
\[
\text{Precision} = \frac{TP}{TP+FP}
\]
Meaning: among predicted positives, how many are truly positive?
表示模型判为正类的样本中，有多少是真的正类。

**Recall / Sensitivity / TPR｜召回率 / 灵敏度**
\[
\text{Recall} = \frac{TP}{TP+FN}
\]
Meaning: among actual positives, how many were detected?
表示真实正类中，有多少被模型识别出来。

**ROC / AUC｜ROC 曲线与 AUC**

- ROC plots TPR against FPR at different thresholds
- AUC measures overall discrimination ability
  AUC 越接近 1 越好

#### 6) No free lunch & threshold trade-off｜没有免费午餐与阈值取舍

- No single algorithm is best for all tasks没有任何一个算法在所有问题上都最好
- Lower threshold → fewer FN but more FP阈值降低 → 更少漏判、更多误报
- Higher threshold → fewer FP but more FN
  阈值提高 → 更少误报、更多漏判

#### 7) Overfitting vs underfitting｜过拟合与欠拟合

- **Overfitting｜过拟合**: learns noise in training data, poor generalization
- **Underfitting｜欠拟合**: model too simple to capture patterns

### Finance examples｜金融场景例子

- Loan approval｜贷款审批
- Fraud detection｜欺诈检测
- Customer prospecting｜客户营销筛选
- Sentiment analysis｜情绪分析
- Trading algorithms｜交易算法

### Exam focus｜考点提示

- Precision vs Recall in different business settings不同业务场景下选择精确率还是召回率
- Which model is most explainable? → **Decision Tree**
- Why does high training accuracy not guarantee success? → **Overfitting**

---

## L3. ML in Investment Management｜投资管理中的机器学习

### Core knowledge points｜核心知识点

#### 1) Risk and return｜风险与收益

- Investors are usually **risk-averse｜风险厌恶**
- Higher risk usually requires higher expected return风险越高，要求的回报通常也越高
- **Risk premium｜风险溢价** = return on risky asset − risk-free return

#### 2) Expected return and risk｜期望收益与风险

- **Expected return｜期望收益**: probability-weighted average return
- **Standard deviation｜标准差**: measures stand-alone risk / total risk
  标准差越大，波动和风险越大

#### 3) CAPM｜资本资产定价模型

\[
r_i = r_{RF} + (r_M - r_{RF})\beta_i
\]
Where:

- `r_RF` = risk-free rate｜无风险利率
- `r_M - r_RF` = market risk premium｜市场风险溢价
- `β_i` = stock beta｜股票对市场波动的敏感度

**Interpretation of beta｜Beta 的含义**

- `β = 1`: same risk as market｜与市场风险相同
- `β > 1`: more risky than market｜比市场更风险
- `β < 1`: less risky than market｜比市场更稳健

#### 4) Factor pricing theory｜因子定价理论

CAPM uses one factor (market), but real returns may depend on multiple factors.
CAPM 只有单一市场因子，而现实中收益常受多个因子影响。

Common factors｜常见因子:

- Market｜市场
- Size｜规模
- Value｜价值
- Momentum｜动量
- Profitability｜盈利能力
- Investment｜投资风格

#### 5) Why factors work｜因子为何有效

- **Risk-based view｜风险补偿视角**
- **Behavioral view｜行为金融视角**
- **Structural view｜市场摩擦/结构视角**

#### 6) Performance metrics｜业绩评价指标

**Sharpe Ratio｜夏普比率**
\[
\text{Sharpe} = \frac{R_p - R_f}{\sigma_p}
\]
Measures excess return per unit of total risk.
衡量每承担一单位风险所得到的超额收益。

**Sortino Ratio｜索提诺比率**
\[
\text{Sortino} = \frac{R_p - R_f}{\sigma_d}
\]
Only penalizes downside volatility.
只惩罚下行波动，更符合“怕亏损”的投资者偏好。

**Maximum Drawdown｜最大回撤**
\[
\text{Max DD} = \frac{\text{Trough} - \text{Peak}}{\text{Peak}}
\]
Largest peak-to-trough loss.
从峰值到谷值的最大跌幅。

#### 7) Backtesting｜回测

Backtesting simulates how a strategy would have performed historically.
回测是用历史数据模拟策略过去的表现。

**Common pitfalls｜常见陷阱**

- Relying on one metric only｜只看单一指标
- Short sample period｜样本期过短
- Ignoring non-normality｜忽略偏度和峰度
- Survivorship bias｜幸存者偏差
- Data snooping｜数据窥探/过度调参

#### 8) AI/ML methods in investment｜投资中的 AI/ML 方法

- **Multinomial / Ordered Logistic Regression｜多项/有序逻辑回归**Useful for predicting market regimes such as bear / rangebound / bull用于预测熊市/震荡/牛市等有序状态
- **Bagging｜装袋法**: reduces variance
- **Boosting｜提升法**: sequential learning, reduces bias, captures nonlinearity
- **AdaBoost｜自适应提升**
- **Gradient Boosting｜梯度提升**

### Exam focus｜考点提示

- Memorize the **CAPM formula** and meaning of **beta**
- Distinguish **Sharpe vs Sortino vs Max Drawdown**
- Know why backtests can look great but fail out-of-sample
  理解为什么回测好看，但实盘/样本外表现差

---

## L4. ML in Algorithmic Trading and NLP in Finance｜算法交易与金融 NLP

### Core knowledge points｜核心知识点

#### 1) NLP in finance｜NLP 在金融中的应用

Text data comes from:

- News｜新闻
- Earnings call transcripts｜财报电话会议纪要
- Emails and contracts｜邮件与合同
- Social media｜社交媒体
- Legal and regulatory documents｜法律和监管文件

#### 2) How text becomes numbers｜文本如何变成数字

- **Bag of Words (BoW)｜词袋模型**: counts words, simple but loses order
- **Tokenization｜分词/标记化**: breaks text into tokens/subwords
- **Word Embedding｜词向量/词嵌入**: represents words as vectors based on context
- **LLMs｜大语言模型**: large pretrained transformer-based models

#### 3) Finance use cases of NLP/LLMs｜NLP/LLM 的金融应用

- Sentiment analysis｜市场与客户情绪分析
- KYC / AML entity matching｜KYC/AML 实体识别与匹配
- Topic classification｜主题分类
- Intelligent tagging｜智能标签
- Research summarization｜研究摘要生成
- Personal banking assistants / chatbots｜客服与理财助手

#### 4) Technical analysis｜技术分析

Technical analysis studies historical prices and chart patterns to predict market direction.
技术分析通过历史价格和图形形态判断未来走势。

#### 5) Dow Theory｜道氏理论

Key ideas:

1. The market discounts everything｜市场价格反映一切
2. The primary trend matters｜主要趋势最重要
3. Trends have phases｜趋势分阶段
   - **Accumulation｜吸筹阶段**
   - **Public participation｜公众参与阶段**
   - **Distribution｜派发阶段**

#### 6) Key technical indicators｜常见技术指标

**Moving Average (MA)｜移动平均线**

- Smooths price fluctuations
- Helps identify trends and support/resistance
  平滑价格波动，用于识别趋势和支撑/阻力

**MACD｜指数平滑异同移动平均线**

- `MACD line = 12-EMA − 26-EMA`
- `Signal line = 9-EMA of MACD`
- Crossover signals possible buy/sell points
  交叉常被视为买卖信号

**RSI｜相对强弱指标**
\[
RSI = 100 - \frac{100}{1 + \frac{n_{up}}{n_{down}}}
\]

- `< 30` often oversold｜低于 30 常视为超卖
- `> 80` often overbought｜高于 80 常视为超买

**Bollinger Bands｜布林带**

- Middle line + upper/lower bands (±2 standard deviations)
- Tightening may imply a strong move is coming
  带宽收窄可能预示大波动即将到来

#### 7) Strengths and weaknesses of technical analysis｜技术分析优缺点

**Pros｜优点**

- Easy to use｜容易上手
- Good for short-term trading｜适合短线交易
- Captures behavioral signals｜可反映贪婪与恐惧

**Cons｜缺点**

- Subjective｜主观性强
- Not strongly theory-based｜理论基础较弱
- Cannot predict unexpected fundamental events｜无法预测突发基本面事件

### Exam focus｜考点提示

- BoW loses **word order**
- RSI / MACD / Bollinger Bands are favorite MCQ topics
- Dow Theory phases are easy to test
  道氏理论三阶段很容易出选择题

---

## L5. ML in Regulatory Compliance｜监管合规中的机器学习

### Core knowledge points｜核心知识点

#### 1) Financial compliance｜金融合规

Two major aspects:

- **Regulatory compliance｜监管合规**
- **Financial crime compliance｜金融犯罪合规**

#### 2) AML / CFT｜反洗钱与反恐融资

**Money laundering has 3 stages｜洗钱三阶段**

1. **Placement｜投放**: illegal funds enter the financial system
2. **Layering｜分层/掩饰**: multiple transactions obscure the source
3. **Integration｜整合**: funds re-enter the economy as “legitimate” money

#### 3) FATF and obligations｜FATF 与核心义务

- KYC (Know Your Customer)｜了解你的客户
- CDD (Customer Due Diligence)｜客户尽职调查
- SAR (Suspicious Activity Reporting)｜可疑交易报告
- Record keeping｜记录保存
- Risk-based approach｜风险为本的方法

#### 4) Red flags｜可疑活动警示信号

- Unusual volumes/frequencies｜异常交易金额或频率
- Rapid fund movement｜资金迅速转移
- Transactions just below thresholds｜刻意低于申报门槛
- High-risk jurisdictions｜高风险地区交易
- Shell companies / nominees｜壳公司、代持人

#### 5) Why AI/ML helps compliance｜为什么 AI/ML 适合合规

- Huge data volume｜数据量巨大
- Need anomaly detection｜需要找异常
- Need to reduce false positives｜需要减少误报积压

#### 6) K-means clustering｜K-means 聚类

- Need to pre-specify `k`需要先设定聚类数 `k`
- Groups similar data points together把相似对象归为同一类
- Uses distance measures such as:
  - Euclidean distance｜欧氏距离
  - Manhattan distance｜曼哈顿距离
  - Minkowski distance｜闵可夫斯基距离

#### 7) DBSCAN｜基于密度的聚类

- Finds clusters based on density根据密度识别簇
- Can detect **arbitrary-shaped clusters** and **noise/outliers**能发现任意形状簇，并识别噪声点/异常点
- Key hyperparameters:
  - `eps` = radius｜半径
  - `minPts` = minimum points｜最少邻域点数

#### 8) Anomaly detection｜异常检测

Used for:

- Fraud detection｜欺诈检测
- Suspicious trades｜可疑交易识别
- AML monitoring｜反洗钱监控

#### 9) Graphical ML / networks｜图网络与图机器学习

A graph consists of **nodes** and **links**.
图由**节点**和**连接边**组成。

**3 C's of graphs｜图的 3 个 C**

- **Centrality｜中心性**
- **Clusterness｜聚集性**
- **Connectedness｜连接性**

Finance applications｜金融应用:

- Correlation networks in portfolios｜投资组合相关性网络
- KYC entity linkage｜KYC 实体关系识别
- Risk contagion / financial stability｜风险传染与金融稳定

### Exam focus｜考点提示

- AML three stages are very testable
- Know **K-means vs DBSCAN**
- DBSCAN is better when data has irregular clusters and noise
  数据形状不规则且有噪声时，DBSCAN 更合适

---

## L6. Agentic AI in Finance｜金融中的 Agentic AI

### Core knowledge points｜核心知识点

#### 1) What is Agentic AI?｜什么是 Agentic AI

Agentic AI refers to autonomous systems that can **perceive, reason, act, and adapt** toward goals.
Agentic AI 指能够围绕目标进行**感知、推理、执行和适应**的自主系统。

#### 2) Agentic AI vs GenAI｜Agentic AI 与生成式 AI 的区别

- **GenAI｜生成式 AI**: generates summaries, reports, text, images
- **Agentic AI｜智能体式 AI**: focuses on completing tasks and workflows autonomously
  更强调完成任务、调用工具、分解目标、执行流程

#### 3) How agentic AI works｜Agentic AI 工作流程

- **Perception｜感知**: gather data from APIs, files, feeds, sensors
- **Reasoning｜推理**: analyze options using LLMs / ML
- **Action｜执行**: generate outputs, call tools, trigger workflows
- **Goal-oriented behavior｜目标导向**: break large goals into smaller tasks

#### 4) Main technologies｜关键技术

- LLMs and ML models｜大模型与机器学习模型
- APIs and tools｜API 与工具接口
- Planning algorithms｜规划算法
- Memory systems｜记忆系统
- Orchestration frameworks｜编排框架

#### 5) Ollama｜本地部署 LLM 运行环境

Advantages in finance｜在金融中优势明显:

- Data privacy｜数据隐私更好
- Cost control｜成本可控
- Offline usage｜支持离线
- Reproducibility｜模型版本可复现
- Easier compliance｜更容易满足监管要求

#### 6) RAG｜检索增强生成

RAG combines LLMs with external knowledge bases/documents.
RAG 把大模型和外部知识库/文档结合起来。

Typical use cases｜典型应用:

- Q&A over PDFs｜基于 PDF 问答
- Summaries of internal docs｜内部文档摘要
- Grounded explanation｜基于事实的解释

#### 7) MCP｜模型上下文协议

MCP is a standardized way to connect LLMs to tools, databases, APIs, and services.
MCP 是让大模型连接外部工具、数据库、API 的标准协议。

#### 8) RAG vs MCP｜RAG 与 MCP 对比

- **RAG** = bring knowledge to the model**把知识带给模型**
- **MCP** = bring the model to live systems/data/tools
  **把模型带到实时系统/数据/工具前**

#### 9) Enterprise considerations｜企业落地注意点

- Scalability｜可扩展性
- Security｜安全性
- Legacy system integration｜与旧系统集成
- Robustness｜稳健性
- Customization｜定制化
- Human-in-the-loop｜人类监督

#### 10) Finance use cases｜金融应用场景

- FX hedging agents｜外汇对冲智能体
- Stock trading agents｜股票交易智能体
- Risk analysis agents｜风险分析智能体
- Compliance/reporting agents｜合规与报告智能体

### Exam focus｜考点提示

- Agentic AI is **goal-directed and action-oriented**
- RAG vs MCP is a high-probability comparison question
- Human judgment, ethics, and supervision remain essential
  人类判断、伦理与监督依然关键

---

## 4. Must-Memorize Comparison Tables｜必背对比表

### 4.1 Supervised learning models｜监督学习模型对比

| Method              | Key idea                        | Strength                 | Weakness                             | Typical finance use                     |
| ------------------- | ------------------------------- | ------------------------ | ------------------------------------ | --------------------------------------- |
| Logistic Regression | Linear probabilistic classifier | Interpretable            | May miss nonlinear patterns          | Loan approval, default prediction       |
| Naïve Bayes        | Probabilistic baseline          | Simple, fast             | Strong independence assumption       | Benchmark text or classification tasks  |
| Decision Tree       | Rule-based splits               | Explainable              | Unstable, prone to overfitting       | Credit decisions, explainable screening |
| Deep Learning       | Many layers and parameters      | Powerful on complex data | Black-box, computationally expensive | Complex prediction / signals            |

### 4.2 Precision vs Recall｜精确率 vs 召回率

| Metric    | Meaning                                         | Best when                                                 |
| --------- | ----------------------------------------------- | --------------------------------------------------------- |
| Precision | Predicted positives that are truly positive     | You want fewer false alarms / less customer annoyance     |
| Recall    | Actual positives that are successfully detected | Missing positives is costly, e.g. default/fraud detection |

### 4.3 K-means vs DBSCAN｜K-means vs DBSCAN

| Method  | Need k?                    | Handles noise? | Cluster shape             | Best use                               |
| ------- | -------------------------- | -------------- | ------------------------- | -------------------------------------- |
| K-means | Yes                        | Poorly         | Usually spherical/regular | Customer grouping, simple segmentation |
| DBSCAN  | No fixed k in the same way | Yes            | Arbitrary/irregular       | Fraud detection, anomaly spotting      |

### 4.4 RAG vs MCP｜RAG vs MCP

| Aspect    | RAG                         | MCP                                       |
| --------- | --------------------------- | ----------------------------------------- |
| Core idea | Ground model with documents | Connect model to tools/systems            |
| Data type | PDFs, reports, memos        | APIs, databases, live systems             |
| Output    | Narrative answers           | Actions, structured results, computations |
| Best for  | Document Q&A, summaries     | Real-time workflow execution              |

---

## 5. Formula Sheet｜公式速记表

| Topic         | Formula                         | Meaning                                      |
| ------------- | ------------------------------- | -------------------------------------------- |
| Accuracy      | `(TP+TN)/(TP+TN+FP+FN)`       | Overall correctness                          |
| Precision     | `TP/(TP+FP)`                  | Predicted positive that is actually positive |
| Recall        | `TP/(TP+FN)`                  | Actual positive that is correctly found      |
| CAPM          | `r_i = r_RF + (r_M-r_RF)β_i` | Required return depends on market risk       |
| Sharpe Ratio  | `(R_p-R_f)/σ_p`              | Excess return per unit of total risk         |
| Sortino Ratio | `(R_p-R_f)/σ_d`              | Excess return per unit of downside risk      |
| Max Drawdown  | `(Trough-Peak)/Peak`          | Worst historical loss from a peak            |
| MACD          | `12-EMA - 26-EMA`             | Trend/momentum signal                        |
| RSI           | `100 - 100/(1 + n_up/n_down)` | Overbought / oversold indicator              |

---

## 6. Common Trap Questions｜常见易错点

1. **High accuracy does not always mean a good model.****准确率高不一定代表模型好。** Class imbalance can make accuracy misleading.
2. **Decision Tree is usually more explainable than Deep Learning.****决策树通常比深度学习更可解释。**
3. **BoW is simple, but it loses word order.****词袋模型简单，但会丢失词序信息。**
4. **DBSCAN is often better than K-means for irregular clusters and noise.****面对不规则簇和噪声时，DBSCAN 往往优于 K-means。**
5. **RAG and MCP are not the same thing.**
   **RAG 和 MCP 不是一回事。** One is a retrieval pattern, the other is a connection protocol.

---

## 7. Practice MCQs with Answers｜模拟选择题 + 答案解析

### Q1

Which of the following is an example of **ordinal data** in finance?
以下哪项属于金融中的**有序数据**？

A. Satellite images
B. GICS sector labels
C. Credit ratings such as AAA, AA, BBB
D. Earnings call audio

**Answer｜答案：C**
**Explanation｜解析：** Credit ratings have a natural ranking order, so they are ordinal.
信用评级有天然顺序，因此属于有序数据。

---

### Q2

Which FEAT principle means the institution remains responsible for AI outcomes?
FEAT 原则中，哪一项强调机构要对 AI 结果负责？

A. Fairness
B. Ethics
C. Accountability
D. Transparency

**Answer｜答案：C**
**Explanation｜解析：** Accountability means firms cannot “blame the algorithm.”
问责性表示机构不能把责任推给算法。

---

### Q3

Why is **one-hot encoding** often used?
为什么常使用**独热编码**？

A. To reduce data to one variable
B. To prevent false ordinal relationships among categories
C. To increase image resolution
D. To calculate market beta

**Answer｜答案：B**
**Explanation｜解析：** One-hot encoding avoids implying that categories have ranked distance when they do not.
独热编码避免模型误以为类别之间存在大小顺序关系。

---

### Q4

Supervised learning mainly learns from:
监督学习主要从什么中学习？

A. Unlabeled patterns
B. Rewards only
C. Labeled data
D. Random guesses

**Answer｜答案：C**
**Explanation｜解析：** Supervised learning uses known labels to map inputs to outputs.
监督学习利用已知标签学习输入与输出之间的关系。

---

### Q5

In a loan default model, if missing a real defaulter is very costly, which metric is especially important?
在违约识别中，如果漏掉真正违约者代价很高，哪个指标更重要？

A. Precision
B. Recall
C. Market beta
D. Max drawdown

**Answer｜答案：B**
**Explanation｜解析：** High recall reduces false negatives, which is critical if defaulters must not be missed.
召回率高意味着更少漏判，适合违约/欺诈等高风险场景。

---

### Q6

Which model is usually the most transparent and explainable?
哪种模型通常最透明、最容易解释？

A. Deep neural network
B. Decision tree
C. Transformer LLM
D. Reinforcement learning agent

**Answer｜答案：B**
**Explanation｜解析：** Decision trees show explicit rules and branches.
决策树通过清晰的分支规则进行判断，更容易解释。

---

### Q7

A model performs extremely well on training data but poorly on test data. This is most likely:
模型在训练集表现极好，但在测试集表现很差，这最可能是：

A. Diversification
B. Overfitting
C. Normalization
D. Transparency

**Answer｜答案：B**
**Explanation｜解析：** The model has learned noise in the training data rather than generalizable patterns.
这是典型过拟合：学到了噪声，而不是可泛化规律。

---

### Q8

In CAPM, a stock with `β > 1` is:
在 CAPM 中，`β > 1` 的股票表示：

A. Less risky than the market
B. As risky as the market
C. More risky than the market
D. Risk-free

**Answer｜答案：C**
**Explanation｜解析：** A beta above 1 means the stock is more sensitive to market movements than the average market portfolio.
Beta 大于 1 说明其对市场波动更敏感，风险通常高于市场平均水平。

---

### Q9

Which ratio measures **excess return per unit of total risk**?
哪个比率衡量“每单位总风险对应的超额收益”？

A. Sortino Ratio
B. Sharpe Ratio
C. Recall Ratio
D. ROC Ratio

**Answer｜答案：B**
**Explanation｜解析：** Sharpe Ratio is the classic risk-adjusted performance metric.
夏普比率是最经典的风险调整后收益指标。

---

### Q10

Which metric focuses only on **downside volatility**?
哪个指标只关注**下行波动**？

A. Sharpe Ratio
B. Accuracy
C. Sortino Ratio
D. Beta

**Answer｜答案：C**
**Explanation｜解析：** Sortino penalizes bad volatility only.
索提诺比率只惩罚“坏波动”，即下跌风险。

---

### Q11

Which of the following is a common backtesting pitfall?
以下哪项是常见的回测陷阱？

A. Using multiple metrics
B. Checking skewness and kurtosis
C. Data snooping
D. Long enough evaluation period

**Answer｜答案：C**
**Explanation｜解析：** Data snooping means over-optimizing to the past, which may not work in the future.
数据窥探是针对历史反复调参，可能导致未来失效。

---

### Q12

Bag of Words has which major limitation?
词袋模型的主要缺点是什么？

A. It cannot count words
B. It loses word order and context
C. It only works on images
D. It requires no preprocessing

**Answer｜答案：B**
**Explanation｜解析：** BoW is simple and efficient, but it ignores sequence and deeper context.
词袋模型虽然简单高效，但会丢失词序和上下文。

---

### Q13

Which technical indicator is commonly used to identify **overbought or oversold** conditions?
哪个技术指标常用于识别**超买/超卖**？

A. CAPM
B. RSI
C. K-means
D. FATF

**Answer｜答案：B**
**Explanation｜解析：** RSI is a momentum oscillator widely used for overbought/oversold conditions.
RSI 是常见动量指标，用于判断超买和超卖。

---

### Q14

According to Dow Theory, after accumulation and public participation comes:
根据道氏理论，吸筹阶段和公众参与阶段之后是：

A. Distribution
B. Normalization
C. Placement
D. Tokenization

**Answer｜答案：A**
**Explanation｜解析：** The classic phases are accumulation → public participation → distribution.
道氏理论常见三阶段为：吸筹 → 公众参与 → 派发。

---

### Q15

MACD mainly helps identify:
MACD 主要用于识别：

A. Customer identity
B. Trend direction and momentum
C. Anti-money laundering obligations
D. Data privacy law

**Answer｜答案：B**
**Explanation｜解析：** MACD is a trend-following momentum indicator.
MACD 是一种判断趋势方向和动量的技术指标。

---

### Q16

Which sequence correctly describes the **three stages of money laundering**?
下面哪一项正确描述了**洗钱的三个阶段**？

A. Integration → Placement → Layering
B. Placement → Layering → Integration
C. Layering → Integration → Placement
D. Detection → Reporting → Closure

**Answer｜答案：B**
**Explanation｜解析：** Illegal money first enters the system, then gets obscured, then reappears as seemingly legitimate wealth.
先进入系统，再被层层掩饰，最后以“合法财富”形式重新出现。

---

### Q17

Which unsupervised method is especially good at finding **arbitrary-shaped clusters and noise**?
哪种无监督方法特别适合发现**任意形状的簇和噪声点**？

A. Logistic Regression
B. Decision Tree
C. K-means
D. DBSCAN

**Answer｜答案：D**
**Explanation｜解析：** DBSCAN is density-based and can naturally flag outliers/noise.
DBSCAN 基于密度，特别适合识别异常点和不规则聚类。

---

### Q18

K-means differs from DBSCAN because K-means:
K-means 与 DBSCAN 的一个关键区别是：

A. Uses no distance measure
B. Must pre-specify the number of clusters
C. Only works for text data
D. Is a supervised learning method

**Answer｜答案：B**
**Explanation｜解析：** K-means typically requires choosing `k` in advance.
K-means 通常需要事先指定聚类数量 `k`。

---

### Q19

In graph analytics, **centrality** is mainly about:
在图分析中，**中心性**主要关注：

A. How to normalize numeric data
B. Which nodes are most influential/important
C. Whether returns are normally distributed
D. The number of tokens in a sentence

**Answer｜答案：B**
**Explanation｜解析：** Centrality asks which nodes are important or influential in the network.
中心性衡量网络中哪些节点最关键、最有影响力。

---

### Q20

Which statement best distinguishes **Agentic AI** from **GenAI**?
哪句话最能区分 **Agentic AI** 和 **GenAI**？

A. Agentic AI only works offline
B. GenAI cannot use language
C. Agentic AI is more goal-driven and action-oriented in workflows
D. GenAI is always more explainable

**Answer｜答案：C**
**Explanation｜解析：** Agentic AI emphasizes planning, tool use, and autonomous task completion.
Agentic AI 更强调目标分解、工具调用和自主完成任务。

---

### Q21

What is the main purpose of **RAG**?
**RAG** 的主要目的是什么？

A. To replace all databases
B. To ground model responses in external documents/knowledge
C. To cluster suspicious trades
D. To compute CAPM beta

**Answer｜答案：B**
**Explanation｜解析：** RAG retrieves relevant knowledge and feeds it into generation.
RAG 会先检索相关知识，再辅助模型生成更可靠答案。

---

### Q22

What is the main purpose of **MCP**?
**MCP** 的主要目的是什么？

A. To provide a standard connection between LLMs and tools/services
B. To calculate Sharpe Ratio
C. To detect chart patterns manually
D. To replace tokenization

**Answer｜答案：A**
**Explanation｜解析：** MCP is a standard protocol for connecting LLMs to external systems.
MCP 是连接大模型与外部系统/工具的标准协议。

---

### Q23

Why is **Ollama** attractive in finance settings?
为什么 **Ollama** 在金融场景中很有吸引力？

A. It removes the need for any governance
B. It allows fully local model hosting with better privacy and compliance comfort
C. It only works for images
D. It guarantees perfect accuracy

**Answer｜答案：B**
**Explanation｜解析：** Local hosting improves privacy, cost control, offline use, and regulatory comfort.
本地部署更有利于隐私保护、成本控制、离线运行与合规要求。

---

### Q24

Which is **not** a common enterprise consideration for agentic AI?
以下哪项**不是**企业落地 agentic AI 的常见考虑因素？

A. Scalability
B. Security
C. Integration with legacy systems
D. Ignoring human supervision

**Answer｜答案：D**
**Explanation｜解析：** Human oversight remains very important in enterprise and finance settings.
在企业和金融场景中，人类监督依然非常重要，不能忽略。

---

## 8. Final 15-Minute Review Checklist｜考前 15 分钟冲刺清单

Before the quiz, make sure you can answer these quickly:考试前请确认你能快速回答以下问题：

- What are the **FEAT** principles?
- What is the difference between **precision** and **recall**?
- What is **overfitting**?
- What does `beta > 1` mean in **CAPM**?
- What is the difference between **Sharpe** and **Sortino**?
- What is the weakness of **Bag of Words**?
- What do **RSI > 80** and **RSI < 30** suggest?
- What are the 3 stages of **money laundering**?
- How do **K-means** and **DBSCAN** differ?
- What is the difference between **RAG** and **MCP**?
- Why is **human-in-the-loop** still important?

---

## 9. One-Sentence Course Takeaway｜一句话总结全课

**AI in finance works best when good data, sound governance, domain knowledge, and the right model are combined.**
**金融中的 AI 真正有效，依赖于高质量数据、良好治理、金融领域知识和合适模型的结合。**

---

## 10. Full-Coverage Addendum｜全量补充知识点（逐页强化版）

> This section expands the first revision set into a more complete lecture-by-lecture checklist.
> 本节用于把前面的浓缩版扩展成更接近逐页覆盖的强化版。

### L1 extra points not to miss｜L1 补充细节

#### What makes AI/ML in finance different?｜为什么金融里的 AI/ML 更特殊

- Finance deals with **systemic risk** and affects livelihoods at scale.金融关系到系统性风险，影响范围大。
- Financial behavior depends on **human behavior**, not fixed natural laws.金融受人类行为影响，不像自然科学那样稳定。
- Financial environments are **self-learning, adaptive, and unpredictable**.
  金融环境会自我调整，具有不确定性。

#### Sources of financial data｜金融数据来源

- Market data providers: `Bloomberg`, `Refinitiv`
- Exchanges and trading venues: `NYSE`, `SGX`, `TradeWeb`
- Public filings: `SEC EDGAR`, `SGXNet`, `ACRA`
- Regulatory/macroeconomic sources: `FED`, `World Bank`, `IMF`
- Open-source / web data: `AlphaVantage`, `Kaggle`, scraped web data, `Alpaca`
- Specialized sources: `PREQIN`, `PitchBook`, `BVAL`

#### More structured-data examples｜更多结构化数据例子

- Price, volume, bid-ask spread, market cap, OHLC data价格、成交量、买卖价差、市值、开高低收
- Income statement, balance sheet, cash flow data利润表、资产负债表、现金流量表
- Ratios such as `P/E`, `ROE`, debt-to-equity, profit margin常见财务比率如市盈率、ROE、负债权益比、利润率
- Macro data such as GDP, inflation, unemployment, PMI, interest rates
  宏观数据如 GDP、通胀、失业率、PMI、利率

#### Data transformation and integration issues｜数据变换与整合问题

- Aggregation can turn daily data into weekly/monthly/yearly data聚合可以把日频数据变成周/月/年频数据
- Integration challenges include:
  - data redundancy｜数据冗余
  - poor data quality｜数据质量差
  - conflict resolution across sources｜多来源冲突
- Transformation may cause:
  - information loss｜信息丢失
  - subjective choices｜主观性过强
  - over-processing without benefit｜过度处理未必有帮助

#### Unstructured and alternative data examples｜非结构化与另类数据例子

- **Text**: news, earnings calls, SEC filings, social media
- **Images**: satellite images, chart patterns, product images, OCR scans
- **Audio**: earnings-call tone, podcasts, trader communications
- **Alternative data**: credit card spending, app usage, web traffic, geolocation, weather data

#### Data governance and legal issues｜数据治理与法律风险

- Missing values, outliers, and noisy data are common
- Feature engineering quality matters greatly
- Privacy, GDPR/PDPA, and non-public information concerns must be considered
  需要关注隐私法规和内幕信息风险

---

### L2 extra points not to miss｜L2 补充细节

#### Training intuition｜训练过程直觉

- Many classifiers reduce training error through **gradient descent**.
  很多分类模型通过梯度下降来降低训练误差。

#### Classification data issues｜分类任务常见数据问题

- Test data should represent real operational data测试集应尽量代表真实业务环境
- Financial data is often **scarce, expensive, noisy, and non-stationary**金融数据常常稀缺、昂贵、含噪且非平稳
- A classic mistake is using training data as test data (`resubstitution accuracy`)
  常见错误是把训练集当测试集

#### Decision tree details｜决策树细节

- Components: **decision nodes, leaf nodes, branches**组成包括判断节点、叶子节点、分支
- Strengths:
  - easy to understand｜容易解释
  - no strong prior assumptions｜先验假设少
  - handles numeric and categorical data｜能处理数值和类别数据
- Weaknesses:
  - unstable to small data changes｜对数据变动敏感
  - can become complex｜树可能变复杂
  - only one output attribute at a time｜一次通常对应一个输出目标

#### Naïve Bayes details｜朴素贝叶斯细节

- It is a **probability-based benchmark model**.
- It applies **Bayes' rule** and is often used as a simple baseline.
- The strong simplifying assumption is that predictors are conditionally independent.
  其核心简化假设是特征条件独立。

#### Logistic regression details｜逻辑回归细节

- Works well for **binary outcomes**
- Outputs probabilities and can be converted into classes using a **cutoff**, e.g. `0.5`
- Uses **odds**: `p / (1-p)`
- It is more interpretable than many black-box methods
  比许多黑箱模型更容易解释

#### Deep learning notes｜深度学习补充

- Perceptron is the basic building block of neural networks
- Deep learning is accurate on complex data but has high computational cost
- It may suffer from the **black-box problem** and overfitting
  有黑箱问题，也更容易过拟合

#### Case-based metric choice｜案例型指标选择

- **Loan approval / default detection**: usually more emphasis on **Recall/Sensitivity** because missing true defaulters is costly
- **Customer prospecting / marketing**: often more emphasis on **Precision** to avoid bothering uninterested customers
  营销触达中常更重视精确率，避免骚扰无意向客户

#### Overfitting case insight｜过拟合案例启示

A strategy can show `99%` training accuracy and still fail out-of-sample due to:

- too many parameters vs weak signal
- data snooping
- regime shifts / non-stationarity
- lack of proper cross-validation

---

### L3 extra points not to miss｜L3 补充细节

#### Risk aversion and return intuition｜风险厌恶与收益直觉

- Most investors are **risk-averse**, but that does **not** mean they always choose the lowest-risk asset.
  大多数投资者是风险厌恶者，但并不意味着总选最低风险资产。

#### Calculating return｜收益率计算

- Basic return:
  \[
  \text{Return} = \frac{\text{Ending Value} - \text{Invested Amount}}{\text{Invested Amount}}
  \]
- If dividends are included, total return includes price gain **plus** dividend income
  若有股息，收益应包括资本利得和股息收入

#### Stand-alone risk vs portfolio risk｜单个资产风险与组合风险

- **Stand-alone risk** = total risk of one asset
- **Portfolio risk** depends on interactions/correlations among assets
  投资组合风险还受到资产间相关性的影响

#### Market risk premium and beta｜市场风险溢价与 Beta

- Typical market risk premium estimates often range around `4%–8%` per year
- Beta captures sensitivity to market-wide events
- Market portfolio is used because it reflects common market shocks
  市场组合常被用作衡量系统性风险的代理

#### Common factor examples｜常见因子例子

- `P/E` – valuation / growth expectations
- `P/B` – useful for banks and asset-heavy firms
- `EV/EBITDA` – cross-industry enterprise valuation
- `EV/Sales` – useful for unprofitable firms
- `ROE` – return on shareholder capital

#### Challenges in factor investing｜因子投资难点

- **Factor timing** is extremely difficult
- **Factor crowding** can reduce future returns
- **Implementation costs** such as transaction costs and market impact matter a lot
  实施成本会侵蚀真实收益

#### Why simpler models may be preferred｜为什么有时更偏好简单模型

- In practice, the best model is not the fanciest one but the one that is **profitable, stable, and understandable**
  实务上更重视盈利性、稳健性和可理解性，而不是“最复杂”

---

### L4 extra points not to miss｜L4 补充细节

#### NLP basics｜NLP 基础

- NLP is the computational conversion and analysis of text to extract meaning such as **what, where, who, relationships**
  NLP 的目标是把文本转成可计算信息并提取含义与关系。

#### More text sources in finance｜金融文本更多来源

- analyst reports｜分析师报告
- contracts and legal documents｜合同与法律文件
- customer feedback and call transcripts｜客户反馈与通话文本
- memos and manuals｜备忘录与手册

#### Bag-of-Words vs embeddings｜词袋模型与词嵌入

- **BoW** is efficient and easy, but loses order and context
- **Embeddings** place words in vector space so contextually similar words are “closer”
  词嵌入能更好表达语义关系

#### How LLMs are trained｜LLM 的基本训练流程

1. Data collection｜数据收集
2. Transformer model configuration｜Transformer 架构配置
3. Training to optimize weights｜训练并优化参数
4. Fine-tuning with human feedback｜结合人工反馈进行微调

#### Topic classification & intelligent tagging｜主题分类与智能标签

- Topic classification assigns documents/news into topics such as IPO, bond issuance, compliance, or market news
- Intelligent tagging helps answer questions like **who / what / where / relationship** in articles
  智能标签能从大量非结构化信息中提取实体与关系

#### KYC/AML text challenge｜KYC/AML 中的文本挑战

- Name matching is non-trivial because the same entity can appear under multiple spellings or regional entries
  名称匹配并不简单，同一实体可能有多种写法或地区录入方式

#### Technical analysis practical notes｜技术分析实务提示

- TA is more suited to **shorter trading horizons**, not usually long-term investing alone
- It is behavior-based and cannot predict unexpected fundamental events
- **Not trading is also a decision**
  有时“不交易”本身也是一个决策

---

### L5 extra points not to miss｜L5 补充细节

#### Why AML/CFT matters globally｜AML/CFT 为什么重要

- Economic impact: undermines integrity and distorts trade/investment
- Social impact: funds crime and terrorism
- Regulatory impact: severe penalties, sanctions, reputational damage, loss of license
- Global cooperation is essential because suspicious flows are often cross-border
  因为很多资金流跨境，国际合作非常关键

#### FATF points to remember｜FATF 要点

- FATF was established in `1989`
- FATF 40 Recommendations cover KYC, reporting, transparency, cooperation, and sanctions
  FATF 40 项建议是全球反洗钱/反恐融资的重要框架

#### Clustering intuition｜聚类直觉

- Unsupervised learning often aims to **reduce complexity** and **reduce noise** by grouping similar points
  无监督学习通常通过“分组”来提炼结构、降噪降复杂度

#### Distance and preprocessing｜距离与预处理

- Numeric data often needs **standardization first** so features have comparable weight
- Common distances:
  - Euclidean｜欧氏距离
  - Manhattan｜曼哈顿距离
  - Minkowski｜闵可夫斯基距离
- For nominal variables, simple matching or binary-variable expansion may be used
  对名义变量可采用简单匹配或转成多个二元变量

#### Why ML beats static rules in many compliance tasks｜为什么 ML 常优于静态规则

- Static rules are rigid｜规则过于僵化
- ML can handle many dimensions simultaneously｜ML 能同时处理高维特征
- ML adapts better to evolving patterns｜更适应变化中的模式

#### False positives tension｜误报问题是监管重点

- Too many suspicious alerts create large operational backlogs
- Compliance design is often a tug-of-war between being **too lax** and generating **too many false positives**
  误报过多会积压案件，太宽松又会带来合规风险

#### Graphical ML reminder｜图网络复习提醒

- Graphs are highly relevant in finance because relationships matter
- Correlation matrices can be represented as networks
- Diversification aims to reduce risk through lower/negative correlations
  分散化的核心就是利用较低或负相关来降低整体波动

---

### L6 extra points not to miss｜L6 补充细节

#### Benefits of agentic AI｜Agentic AI 的直接好处

- Automates repetitive work
- Reduces manual effort
- Can react more quickly to changing environments
  能更快响应环境变化

#### When company-specific data matters｜当企业自有数据很重要时

- General LLMs are trained on broad public knowledge
- If the task depends on internal documents or restricted enterprise data, you need `RAG`, `MCP`, or local deployment
  如果任务依赖企业内部资料，就需要 RAG、MCP 或本地部署

#### RAG solution types｜RAG 的两类方案

- **Pure document RAG**: only internal docs
- **Hybrid RAG**: internal docs first, then possibly web if confidence is low
  混合式 RAG 会在需要时再接入互联网信息

#### Framework roles｜常见框架分工

- `Ollama`: local model runner
- `LlamaIndex`: RAG / indexing framework
- `LangChain`: general LLM app framework
- `LangGraph`: multi-agent workflow orchestration
  `LangGraph` 更偏多智能体流程编排

#### Enterprise-ready design features｜企业级设计特征

- RAG with enterprise knowledge base
- Structured output such as JSON
- Conversational/context memory
- Search capability
- Strong security and confidentiality controls

#### Workflow patterns worth memorizing｜值得背的工作流模式

- delegation / hand-off｜委派与交接
- tool use / function calling｜工具调用
- sequential chain｜顺序链式执行
- judge-and-critic feedback loop｜评审-反馈闭环
- parallelization for speed｜并行化提速
- guardrails for safety and governance｜安全与治理护栏

#### Finance agent examples｜金融智能体例子

- FX hedging agents: portfolio, market data, risk, compliance, reporting
- Trading agents: market data, technical analysis, risk management, execution
  智能体可以分别承担感知、分析、监督与执行角色

---

## 11. 30-MCQ Sprint Add-On｜补足到 30 题的冲刺题

### Q25

Which of the following is **most likely** an alternative data source in finance?
以下哪项**最可能**属于金融中的另类数据？

A. Balance sheet totals
B. GDP growth report
C. Satellite images of retail parking lots
D. Standard stock OHLC prices

**Answer｜答案：C**
**Explanation｜解析：** Satellite imagery is a classic example of alternative data used to infer demand, traffic, or inventory conditions.
卫星图像是典型另类数据，可用于推断客流、需求或库存状态。

---

### Q26

In logistic regression, a probability estimate is commonly converted into a class label using:
在逻辑回归中，概率通常通过什么转成类别标签？

A. A clustering radius
B. A cutoff threshold such as `0.5`
C. A Sharpe ratio filter
D. A correlation matrix

**Answer｜答案：B**
**Explanation｜解析：** Logistic regression outputs probabilities, and a threshold (often 0.5) is used for final classification.
逻辑回归先输出概率，再通过阈值（常见 0.5）转成分类结果。

---

### Q27

Which of the following is a major challenge in factor investing?
以下哪项是因子投资的主要挑战？

A. Factor timing is easy and reliable
B. Implementation costs do not matter
C. Crowding may reduce returns
D. CAPM already captures all factors perfectly

**Answer｜答案：C**
**Explanation｜解析：** Factor crowding is a well-known issue: if too much capital chases the same factor, returns may shrink.
因子拥挤是常见问题，太多资金追逐同一因子会压缩未来收益。

---

### Q28

Why are word embeddings generally more informative than a simple Bag of Words representation?
为什么词嵌入通常比简单词袋模型信息更多？

A. They remove all preprocessing needs
B. They represent contextual semantic similarity
C. They only work for compliance tasks
D. They ignore relationships between words

**Answer｜答案：B**
**Explanation｜解析：** Embeddings place words in a vector space where contextual and semantic similarity can be captured.
词嵌入能够在向量空间中表达上下文和语义相似性。

---

### Q29

Which of the following is a classic AML red flag?
以下哪项是典型的反洗钱红旗信号？

A. Stable long-term salary deposits consistent with profile
B. Rapid movement of funds among multiple accounts with no clear purpose
C. Low portfolio volatility
D. High Sharpe ratio

**Answer｜答案：B**
**Explanation｜解析：** Rapid transfers and complex movements without a clear rationale are classic suspicious patterns.
资金在多个账户间快速流转且缺乏合理解释，是典型可疑行为。

---

### Q30

Which framework is most closely associated with **multi-agent workflow orchestration** in the lecture notes?
讲义中哪一框架最贴近**多智能体流程编排**？

A. Ollama
B. LlamaIndex
C. LangChain
D. LangGraph

**Answer｜答案：D**
**Explanation｜解析：** The slides position `LangGraph` as the framework whose primary strength is multi-agent orchestration.
讲义中 `LangGraph` 的主要强项就是多智能体工作流编排。

---

## 12. Final Reminder｜最后提醒

This file is now designed to be a **near-full revision version**: first a condensed high-yield summary, then a more detailed slide-coverage addendum, and finally a 30-question MCQ bank.
这份文件现在已经扩展为**接近全量覆盖版**：前面是浓缩重点，后面是逐章补充，最后附 30 题选择题冲刺。

**Best revision method tonight｜今晚最佳复习顺序：**

1. Read sections `2`, `4`, and `5` first
2. Then review `L2`, `L3`, `L5`, `L6` carefully
3. Finally do all `30 MCQs` once without looking at the answers

**建议顺序：先背重点表，再看逐章补充，最后刷 30 道题。**
