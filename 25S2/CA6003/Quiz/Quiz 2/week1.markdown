# 第1章完整复习资料（中英文双语）

## Chapter 1: Data Profiling and Cleaning

---

## 0. 本章在课程里的定位 | Position in the Course

**中文**
这一章是后续机器学习建模的“地基章”。老师强调：模型效果差，很多时候不是算法问题，而是数据问题。Data profiling 和 data cleaning 是把“原始数据”变成“可分析、可建模数据”的关键步骤。

**English**
This chapter is foundational for all downstream ML work. Poor model performance is often caused by poor data quality, not model choice. Data profiling and cleaning convert raw data into analysis-ready and model-ready data.

---

## 1. Data Science 的定义与目标 | What Data Science Means

**中文（定义）**
课件定义：数据科学是从复杂、多样（多模态/异构）数据中提取知识与洞察，以支持更好的决策。常见方法包括数据清洗、数据画像、统计、机器学习、可视化。

**English (Definition)**
Data science extracts knowledge and insights from complex and heterogeneous data to support better decisions, using methods such as cleaning, profiling, statistics, machine learning, and visualization.

---

## 2. Data Science Thinking Process（6步流程）

课件流程： **Ask → Prepare → Process → Analyze → Share → Act** 。

### 2.1 Ask（提问/问题定义）

* **中文** ：把“业务痛点”转成“可量化问题”
  例：传球成功率、射门区域、犯规位置等。
* **English** : Translate business concerns into measurable analytical questions.

### 2.2 Prepare（准备数据）

* **中文** ：采集多源数据（视频、历史比赛、穿戴设备、裁判报告等），并保证字段可追踪（player ID、timestamp、坐标）。
* **English** : Gather and tag data from multiple sources with consistent identifiers and timestamps.

### 2.3 Process（处理/预处理）

* **中文** ：处理缺失、定义不一致、信号噪声；把原始指标转成可比较指标（如每90分钟距离、fouls per defensive action）。
* **English** : Clean and normalize raw metrics into comparable features.

### 2.4 Analyze（分析）

* 找趋势、相关关系、异常模式。

### 2.5 Share（沟通）

* 可视化与解释，让非技术角色看懂。

### 2.6 Act（行动）

* 根据结论调整训练、战术或业务策略。

---

## 3. Data Science vs Statistics vs AI（考试常见对比题）

**中文**

* **Data Science** ：更强调“从数据到洞察再到决策”
* **Statistics** ：更强调“推断、不确定性、假设检验”
* **AI** ：更强调“系统自主学习、推理和决策”

**English**

* **Data Science** : action-oriented insight extraction
* **Statistics** : inference under uncertainty
* **AI** : intelligent/autonomous behavior from learned patterns

---

## 4. Data Preparation（数据准备）是什么

**中文**
Data preparation 是把数据进行 gathering / combining / structuring / organizing，使其可用于分析和可视化。其组件包括：

1. Data profiling
2. Data cleaning
3. Feature engineering
4. Transformation。

**English**
Data preparation organizes data for analysis/visualization, with profiling, cleaning, feature engineering, and transformation as key components.

---

## 5. 数据准备前的三大假设（超高频）

### 5.1 Integrity & Completeness（完整性与真实性）

* 数据足够、真实、来源可信。
* 否则：模型学到“垃圾规律”，无法泛化。

### 5.2 Representativeness & Relevance（代表性与时效相关性）

* 样本要覆盖目标人群，不偏；模式不过时。
* 否则：模型不公平/过时。

### 5.3 Ethical & Legal Compliance（伦理与合规）

* 同意、匿名化、隐私、合法使用范围（GDPR/PDPA）。
* 否则：法律与声誉高风险。

---

## 6. 数据类型（Structured vs Unstructured）

## 6.1 Structured Data（结构化数据）

**中文**

* 固定模式、字段明确、易查询（表格/SQL）。
* 类型包括：数值、类别、时间序列、网络数据。

**English**

* Fixed schema/tabular form; easy filtering/querying.
* Includes numeric, categorical, time-series, and network data.

### 6.1.1 Time Series（时间序列）

* 时间戳 + 顺序依赖（chronological dependency）。

### 6.1.2 Network Data（网络/图数据）

* Node + Edge + 属性；常可表格化存储，但语义是图关系。
* 例：社交网络、物流网络、MRT、金融交易网络。

## 6.2 Unstructured Data（非结构化数据）

文本、图像、语音、视频；无固定 schema，语义强、维度高，通常需要 NLP/CV/DL。

### 6.2.1 Text 难点

* 高维词汇空间
* 语境依赖（同词不同义）
* 歧义/反讽
* 顺序重要
* 常用处理：tokenization、lemmatization、stopword removal。

### 6.2.2 Image 难点

* 像素维度极高
* 空间相关性
* 语义鸿沟
* CNN 通过局部卷积学习空间模式。

---

## 7. Data Profiling（数据画像）完整内容

## 7.1 定义

 **中文** ：系统性检查数据结构、内容和关系，先理解数据再清洗。
 **English** : Systematic examination of structure, content, and relationships before cleaning/modeling.

## 7.2 三类 Discovery（必考）

### A) Structure Discovery（结构发现）

* 看 schema、字段类型、格式合法性。
* 目标：找 type mismatch / format error。

### B) Content Discovery（内容发现）

* 看缺失、分布、极值、异常。
* 指标：missing %, mean, std, outliers。

### C) Relationship Discovery（关系发现）

* 看字段间依赖和相关。
* 常见方法：correlation、chi-square、covariance、association rules。

## 7.3 单列与多列 profiling

* **Single-column** ：基数、空值、distinct、模式、分位数/直方图。
* **Cross-column** ：相关、聚类、跨列异常关系。

## 7.4 课件中的 pandas 典型函数（你要会解释“为什么用”）

* `.min()`：查不合理下界（如年龄负数）
* `.max()`：查异常上界
* `.describe()`：数值统计概览
* `describe(include='object')`：看类别列唯一值/众数/频次，发现标准化问题（如 `SG` vs `Singapore`）。
* `.corr()`：数值列线性相关（方向+强度），不是因果。

---

## 8. Data Cleaning（数据清洗）完整内容

## 8.1 定义

清洗是发现并纠正错误/不一致/不准确，使数据准确、一致、可用于分析与ML，通常在 profiling 之后进行。

## 8.2 常见问题类型（逐条记）

1. Missing / incomplete values
2. Duplicated rows
3. Outliers / invalid values
4. Inconsistent formats / units
5. Typographical / case errors
6. Encoded or garbled data
7. Truncated data
8. Unnecessary metadata

---

## 9. Missing Values（缺失值）完整体系

## 9.1 缺失机制（概念题高频）

### MCAR（Missing Completely at Random）

* 缺失与任何变量都无关。
* 相对“安全”使用简单插补。

### MAR（Missing at Random）

* 缺失与“已观测特征”有关。
* 应利用相关列插补。

### MNAR（Missing Not at Random）

* 缺失与缺失值本身有关。
* 不宜简单均值填补；可单独建模或加缺失标记。

## 9.2 缺失值处理方法（按场景记忆）

* **Deletion** ：缺失少（如<5%）时可删；简单但损失信息。
* **Constant imputation** ：填 `"Unknown"` 等，快但可能引偏差。
* **Mean/Median/Mode** ：基线方法，易实现但忽略关系，降低方差。
* **Forward/Backward fill** ：时间序列连续性好，但会掩盖突变。
* **KNN imputation** ：利用近邻关系更准，但计算重。
* **Multiple imputation (MICE)** ：更稳健，复杂度高。
* **Binning / Clustering based** ：有时用于数值或群组结构数据。

## 9.3 Golden Rule（数据泄漏必考）

**绝对不要**在 split 前用全量数据算均值/中位数等。
正确步骤：

1. 先 split train/test
2. 只在 train 上 fit imputer
3. 用同一个 imputer transform train/test。

---

## 10. Outlier Detection（离群值）完整内容

## 10.1 Z-score

* 参数法；适合近似正态。
* 常用阈值 `|z| > 3`。
* 弱点：对偏态和极端值不稳健。

## 10.2 IQR

* 非参数法；适合偏态。
* 公式：
  * `IQR = Q3 - Q1`
  * Lower fence = `Q1 - 1.5*IQR`
  * Upper fence = `Q3 + 1.5*IQR`。
* 优点：对极值更稳健（中间50%）。

## 10.3 Isolation Forest

* 思想：通过随机切分“快速孤立”异常点。
* 判据：路径越短，越可能异常。
* 优点：高维、非线性、大数据友好；不要求分布假设。
* 缺点：可解释性较差、需调 contamination 等超参数。

## 10.4 其他方法（了解）

* **LOF** ：比较局部密度，低密度点更像异常。
* **DBSCAN** ：噪声点即异常点。
* **OCSVM** ：学习“正常边界”，边界外为异常。

## 10.5 方法选择（匹配题常考）

* 正态数据 → Z-score
* 偏态数据 → IQR
* 高维非线性 → Isolation Forest。

---

## 11. Benefits（为什么一定要做 profiling + cleaning）

* 更早发现错误
* 提升数据质量
* 更快更准的分析与决策。

---

## 12. 考试高频易错点（你必须死记）

1. `.corr()` 是相关，不是因果。
2. IQR 不是正态专用；它恰恰对偏态稳健。
3. 多选题有负分：不确定的选项宁可不选。
4. 填补缺失时最易错是 data leakage（顺序错）。
5. `describe(include='object')` 是发现类别不一致的关键入口（SG/Singapore）。

---

# Chapter 1 练习题（按你考试格式）

（含答案与双语解析）

## A. MCQ 单选

**Q1.** Which discovery type checks schema/type mismatch?
A. Content discovery
B. Relationship discovery
C. Structure discovery
D. Feature selection
**Answer: C**

* 中：schema/type/format 属于结构发现。
* EN: Schema/type/format validation is structure discovery.

---

**Q2.** For strongly skewed numeric data, a robust outlier method is:
A. Z-score
B. IQR
C. One-hot encoding
D. Pearson correlation
**Answer: B**

* 中：IQR 对偏态更稳健。
* EN: IQR is non-parametric and robust on skewed distributions.

---

**Q3.** The biggest risk of imputing before train-test split is:
A. Underfitting
B. Data leakage
C. Over-regularization
D. Class imbalance
**Answer: B**

* 中：测试信息泄露到训练过程。
* EN: Test-set information leaks into training.

---

## B. Fill in the blanks 填空

**Q4.** IQR outlier fences are `Q1 - ____*IQR` and `Q3 + ____*IQR`.
**Answer:** 1.5, 1.5

**Q5.** In Isolation Forest, a point with ______ path length is more likely an outlier.
**Answer:** shorter

**Q6.** Missingness related to observed features is called ______.
**Answer:** MAR

---

## C. Multiple answers 多选（有负分）

**Q7.** Which statements about missing data handling are correct?
A. Deletion is always best
B. Forward fill is often used in time series
C. KNN imputation may be computationally expensive
D. MNAR is always safe for mean imputation
**Answer:** B, C

* 中：A和D错。删除不总是最好；MNAR不宜简单均值。
* EN: Deletion is conditional; MNAR usually needs more careful treatment.

---

**Q8.** Which belong to data cleaning issues?
A. Duplicated rows
B. Inconsistent units/formats
C. Typographical/case errors
D. Hyperparameter tuning
**Answer:** A, B, C

* 中：D 属于建模阶段，不是清洗问题。
* EN: Hyperparameter tuning is modeling, not data cleaning.

---

## D. Matching 配对题

Match method to best scenario:

1. Z-score
2. IQR
3. Isolation Forest
4. Forward Fill

a. high-dimensional nonlinear anomaly patterns
b. approximately normal distribution
c. time-series continuity
d. skewed distribution with extreme values

**Answer:** 1-b, 2-d, 3-a, 4-c
