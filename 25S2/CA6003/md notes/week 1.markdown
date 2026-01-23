
* **Week1_Data Profiling and Cleaning_detail.pdf** 
* **Week1_recording_Data Profiling and cleaning.pdf** 

把其中**所有知识点**按**逻辑顺序**整理成一份「完整知识点提纲 + 中英双语详细讲解」。两份文件有大量重复内容（录播版更“概念化”，detail 版更多“案例化+方法细节”），已合并去重，但**不会漏掉任何概念/方法/对比/例子**。
# Week 1. Data Profiling and Cleaning

# 1. 课程定位与学习目标

## 1.1 课程结构与考核信息（Course structure & assessment）

* **CN**：6 周课程；课前看录播；周二答疑；周六上机练习（Anaconda + Python notebook）。考核：2 次 Quiz + 1 次 Assignment（给出了 Quiz 时间安排）。
* **EN**: 6-week format with a pre-recorded lecture before Tuesday consultative class; Saturday hands-on coding in Anaconda notebooks; assessments include 2 quizzes and 1 assignment. 

## 1.2 Course Learning Outcomes（录播版 ILO）

* **ILO1（CN）**：AI 全生命周期应用数据治理原则（数据收集、同意管理、文档化），关注法律伦理（GDPR/PDPA/HIPAA）与合规风险。
* **ILO2（CN）**：为机器学习准备原始数据：profiling/cleaning/validation/transforming/enrichment（缺失值处理、编码、特征工程、标准化等）。
* **ILO3（CN）**：检测并处理 bias、outliers、integrity issues，评估它们对模型的影响并做缓解。
* **ILO4（CN）**：设计健壮 EDA：解读统计与可视化，避免分析谬误。
* **ILO5（CN）**：设计伦理透明的 AI 数据流水线：可追溯、可解释、可复现。
* **EN**: Learning outcomes cover governance & compliance, data prep & transformation, bias/outlier/integrity analysis, robust EDA, and ethical/traceable pipelines. 

---

# 2. Data Science 基础框架（概念与边界）

## 2.1 Data Science 的定义（What is Data Science）

* **CN**：从复杂、多模态、异构数据中通过分析与探索提炼知识与洞察，目标是支持更好的决策；手段包括数据清洗、数据画像、统计、机器学习、可视化等。
* **EN**: Extract knowledge/insights from complex multi-modal heterogeneous data via analysis/exploration to enable better decisions; methods include cleaning, profiling, statistics, ML, visualization. 

## 2.2 Data Science vs Statistics vs AI（三者区别）

* **CN**：

  * Data Science：面向应用的洞察/模式提取与决策支持（工程化 pipeline 很重要）。
  * Statistics：建模不确定性与推断（采样、假设检验、回归等）。
  * AI：构建能学习、推理、行动的智能系统（ML/DL/NLP/CV/RL）。
* **EN**: DS focuses on actionable insights from data; Statistics focuses on inference under uncertainty; AI focuses on building intelligent systems learning and reasoning from data. 

---

# 3. Data Science thinking process（“Ask–Prepare–Process–Analyze–Share–Act”）

## 3.1 六步思维链条（Six-step thinking process）

* **Ask（CN）**：提出问题并定义问题边界。
* **Prepare（CN）**：收集与存储数据。
* **Process（CN）**：清洗与检查数据。
* **Analyze（CN）**：寻找模式、关系、趋势。
* **Share（CN）**：与受众沟通结果。
* **Act（CN）**：用结果驱动行动与改进。
* **EN**: Ask → Prepare → Process → Analyze → Share → Act.

## 3.2 Phoenix FC 故事案例：用业务语言解释每一步（Case-based mapping）

> detail 版用足球队故事把“为什么要清洗/标准化/异常检测/可视化沟通”讲得很具体。 

### 3.2.1 Ask：把“球队不稳定”拆成可量化问题

* **CN**：按球员/区域的传球成功率；下半场速度与跑动距离；射门来自哪里（xG）；犯规地点与责任人等。
* **EN**: Define measurable questions: pass completion by player/zone, second-half endurance, shot locations and xG, foul locations and responsible players.

### 3.2.2 Prepare：多源采集 + 精确记录字段

* **CN**：视频标注 + 历史比赛报告 + GPS 可穿戴；每次传球/冲刺/射门/犯规都要记录 player ID、timestamp、坐标；射门引入 xG 标注。
* **EN**: Multi-source collection; log each event with IDs, timestamps, coordinates; use xG-based tagging for shots.

### 3.2.3 Process：把 raw numbers 变成“可比较指标”并纠错

* **CN**：原始数据会脏（GPS 掉线、标注错误、定义不一致）；把总跑动→每 90 分钟平均距离；犯规→每防守动作犯规；射门→热力图与平均 xG/shot；识别不可能值（例如半场 20km）并过滤；交叉验证（传球数据与视频对照）；统一字段定义（foul vs dispossession）。
* **EN**: Raw data is messy; normalize into meaningful metrics, detect impossible values, cross-check with video, standardize definitions.

### 3.2.4 Analyze：发现模式（低成功长传、低质量射门、疲劳窗口、转移犯规）

* **CN**：后场长传到前场成功率低且导致反击；射门多但平均 xG/shot 低（角度差/禁区外）；70 分钟后高强度冲刺下降；犯规聚集在丢球后的转换阶段。
* **EN**: Identify low-success long passes leading to counters; low xG/shot despite many attempts; sprint drop-off after ~70 mins; fouls clustered in transition moments.

### 3.2.5 Share & Act：用热力图/趋势图沟通，并制定训练/策略调整

* **CN**：用证据桥接直觉：丢球热区、冲刺距离趋势、射门热力图；行动包括耐力训练、数据驱动换人、长传训练、优先高 xG 区域进攻、转换防守站位训练。
* **EN**: Communicate with heatmaps/trends; act via endurance drills, data-driven substitutions, long-ball practice, high-xG shot selection, transition defense drills.

---

# 4. Data Science pipeline（标准项目流程与关键检查点）

## 4.1 Pipeline 主流程（end-to-end）

* **CN**：定义任务类型 → 获取数据（新采集或复用现有）→ 理解与准备（结构/质量/分布/关系）→ 清洗（缺失/异常/错误修正）→ 变换（归一化/编码）→ 特征工程 → 训练/评估 → 部署/维护。
* **EN**: Define task → get data → understand/prepare (structure/quality/distribution/relationships) → clean → transform → feature engineering → train/evaluate → deploy/monitor.

## 4.2 数据收集的三大假设与风险（Assumptions & critical risks）

* **Integrity & completeness（完整真实）**：数据量足够、来自可信源且未损坏；否则模型学到“胡话”无法泛化。
* **Representativeness & relevance（代表性与相关性）**：覆盖目标人群多样性、且不过时；否则模型不公平、结果过期。
* **Ethical & legal compliance（合法合规）**：用户同意、匿名化、隐私保护；否则项目终止与罚款/诉讼。 

---

# 5. Data preparation（数据准备）与数据类型

## 5.1 数据准备的定义与组成（Definition & components）

* **CN**：收集、组合、结构化并组织数据，使其可用于分析与可视化；组成包含 profiling、cleaning、feature engineering、transformation。
* **EN**: Gather/combine/structure/organize data for analytics; includes profiling, cleaning, feature engineering, and transformation.

## 5.2 两大数据类型：Structured vs Unstructured

### 5.2.1 Structured data（结构化数据）

* **CN**：固定 schema、表格化、易查询过滤；包括数值/类别混合数据、时间序列、网络（图）数据。
* **EN**: Tabular with fixed schema; easy to query; includes numeric/categorical, time series, and network/graph data.

#### a) Categorical/Mixed（混合数据）

* **CN**：字段清晰、可直接统计建模（如交易记录、人口统计、传感器读数）。
* **EN**: Clear fields, easy mining and analysis.

#### b) Time series（时间序列）

* **CN**：带时间戳、固定间隔、存在时间依赖；每个时间点可有多个特征（温度、湿度等）。
* **EN**: Timestamped, regular intervals, chronological dependency; multi-feature per time step.

#### c) Network data（网络/图数据）

* **CN**：节点（实体）+ 边（关系），节点/边都有属性；常以表形式或图数据库管理；例子：社交网络、物流供应链、网络安全、地铁网络、学术引用网络。
* **EN**: Nodes + edges with structured attributes; stored in tabular or graph DBs; examples include social/logistics/cyber/MRT/citations.

### 5.2.2 Unstructured data（非结构化数据）

* **CN**：无预定义 schema，高度依赖语境；需要 NLP/CV/DL 抽取结构。包括文本、图像、视频、语音。
* **EN**: Lacks schema; contextual; requires advanced AI/ML to derive structure.

#### a) Text（文本）挑战

* Curse of vocabulary（词汇维度灾难）；Context dependency（同词不同义）；Ambiguity/sarcasm（歧义/讽刺）；Sequence matters（顺序重要）。
* **清洗举例（CN）**：lemmatization、stop word removal、tokenization。
* **EN**: High dimensionality, context dependence, ambiguity, and sequence sensitivity; cleaning includes lemmatization, stop-word removal, tokenization.

#### b) Image（图像）挑战

* 超高维像素；空间相关性；semantic gap（像素→语义）；invariance（同物不同形）。
* **EN**: CNNs learn local patterns (edges/shapes) to address pixel-level high dimensionality; need invariance via varied data + pooling.

#### c) Video（视频）挑战

* 维度爆炸（w×h×c×time×batch）；时序相关；多模态融合（音频+视觉）；事件定位与时序分割。
* **EN**: Use 3D-CNNs for spatio-temporal cubes; RNN/LSTM or other memory mechanisms for temporal linking; multimodal fusion for audio+visual.

#### d) Voice/Audio（语音）挑战

* 波形的序列与时间依赖；特征提取（spectrogram、MFCC）；说话人/情绪差异；噪声干扰与降噪预处理。
* **EN**: Temporal models (RNN/TCN), feature extraction (MFCC), invariance to speaker/emotion, and aggressive noise reduction.

---

# 6. Data Profiling（数据画像/剖析）完整知识点

## 6.1 Profiling 的定义、目标与价值

* **CN**：像给数据做“体检”：检查并总结结构、内容分布、变量关系；用于发现缺失/无效/重复、理解分布模式、为清洗与变换做准备，并确保分析前的数据完整性。
* **EN**: A “health check” to examine/summarize structure, content, and interrelationships; detects quality issues, learns distributions, and prepares cleaning/transformation.

## 6.2 Profiling 三大类 Discovery（结构/内容/关系）

### 6.2.1 Structure discovery（结构发现）

* **Goal（EN）**: verify schema, data types, formats.
* **CN**：验证字段、数据类型、格式、pattern（正则/格式校验），输出 schema summary、type mismatch。

### 6.2.2 Content discovery（内容发现）

* **Goal（EN）**: assess data quality and value distributions.
* **CN**：描述统计、频数统计、缺失与异常检测；输出 missing%、mean/std、outliers。

### 6.2.3 Relationship discovery（关系发现）

* **Goal（EN）**: identify dependencies/correlations among attributes.
* **CN**：相关系数、卡方检验、协方差、关联规则；输出 correlation matrix、key integrity（键一致性/关联正确）。

## 6.3 Profiling 的两种粒度：Single-column vs Cross-/Multi-column

* **Single-column profiling（CN）**：看单列的基数（rows/min/max/null/distinct）、pattern 与类型、分布（直方图、四分位）。
* **Cross-/Multi-column profiling（CN）**：看列间关系：correlation、clusters、outliers、summaries。
* **EN**: Single-column focuses on cardinalities/patterns/distributions; cross-column focuses on relationships (correlations/clusters/outliers). 

## 6.4 “为什么 profiling 重要”示例（Customer info）

这份例子把每列 profiling 输出如何指向真实问题讲得很明确：

* ID：5 个唯一值 → 无重复
* Name：4 个唯一值且 John Doe 出现两次 → 可能重复记录
* Age：范围 -5 到 29 且有缺失 → 负年龄无效 + 缺失
* Email：出现非法格式（mike_tan）→ 数据质量问题
* Country：SG vs Singapore → 标准化问题（同义不同写）
* **Key benefits（EN/CN）**：提升质量与可靠性；支持更好决策；避免报表/分析错误；为清洗与变换做准备。

## 6.5 Content discovery 常用函数（你要会“目的→语法→洞察”）

* `.min()`：找低端异常/下界（如 Age 最小值 -5 暗示无效）。
* `.max()`：找高端极值（如 Revenue 最大 900）。
* `.describe()`（numeric）：统计摘要（均值、四分位、离散程度），用于看分布与异常对均值的扭曲。
* `.describe(include='object')`（categorical）：unique/top/freq，发现标准化问题（SG vs Singapore）。
* **EN**: min/max/describe (numeric & categorical) support anomaly detection and distribution understanding.

## 6.6 Relationship discovery 常用函数：`.corr()`

* **CN**：计算数值列两两线性相关（Pearson’s r），给出强度与方向；示例解释“年龄越大浏览越少”的强负相关。
* **EN**: `.corr()` measures covariance/linear association; strong negative r suggests inverse relationship.

---

# 7. Data Cleaning（数据清洗）完整知识点

## 7.1 Cleaning 的定义

* **CN**：数据清洗/擦洗是识别并纠正错误、不一致与不准确，使数据准确、一致、可用于分析/ML；通常在 profiling 之后进行。
* **EN**: Detect and correct errors/inconsistencies/inaccuracies to make data accurate, consistent, and analysis/ML-ready.

## 7.2 常见清洗问题清单（必须能逐条识别）

* Missing/incomplete values
* Duplicated rows
* Outliers/invalid values
* Inconsistent formats/units
* Typographical/case errors（Happy/happy/Hapy）
* Encoded/garbled data（乱码编码）
* Truncated data（字段被截断）
* Unnecessary metadata（Last Edited By 等）

## 7.3 Missing values（缺失值）——类型、策略、选择指南

### 7.3.1 缺失机制（Missingness mechanisms）

* **MCAR（完全随机缺失）**：与其他变量无关（随机漏填年龄）→ 可相对安全用 mean/median。
* **MAR（条件随机缺失）**：与其他观测变量有关（收入缺失与教育相关）→ 用相关列做更合理的插补。
* **MNAR（非随机缺失）**：与自身值相关（低收入更不报收入）→ 不宜简单插补，应单独建模或加缺失标志。 

### 7.3.2 缺失处理方法全集（methods + impact）

* **Deletion（删除）**：缺失 <5% 或影响小；优点简单，缺点可能丢信息。
* **Constant value（常数填补）**：类别用 “Unknown”；快但可能引入偏差。
* **Mean/Median/Mode（均值/中位数/众数）**：baseline；会降低方差、忽略变量关系。
* **Forward/Backward fill（前向/后向填补）**：时间序列；可能掩盖突变。
* **KNN imputation**：利用相似样本关系；更准但大数据慢。
* **Multiple imputation / MICE**：更严谨（考虑不确定性），但复杂。
* **Binning-based / Clustering-based**：分箱/聚类再按组填补；更“子群体敏感”，但需要调参且有信息损失风险。

### 7.3.3 选择原则（how to choose）

* 看每列缺失比例；看缺失是否成组/有模式；按数据类型与重要性选方法；若缺失本身带信息可加 missing-flag。 

### 7.3.4 Golden rule：防止数据泄漏（Data leakage）

* **CN**：不要在 train/test split 之前用全数据计算均值/中位数来填补；要先 split，再只在训练集 fit imputer，再 transform train/test。
* **EN**: Never compute imputation stats on the full dataset before splitting; fit on train only, transform both.

## 7.4 Outlier detection（离群点检测）——三大主线 + 对比表 + 选型指南

### 7.4.1 Z-score（参数法，适合正态/对称）

* **定义（EN）**：看点距均值多少个标准差；(|Z|>3) 常用。
* **优点（CN）**：简单、快、对高斯/对称数据有效。
* **缺点（CN）**：偏态/非正态不可靠；对极端值非常敏感。

### 7.4.2 IQR（非参数法，适合偏态）

* **定义（EN）**：用 Q1/Q3 和 IQR，构造 fences；超出视为离群。
* **优点（CN）**：鲁棒（不受极端值影响），箱线图可视化友好。
* **缺点（CN）**：高维数据不理想，抓不住复杂非线性结构。

### 7.4.3 课件“反例”讲清楚：Z-score 可能漏检高端离群

* **CN**：示例数据中高值（140/145/150）没被 Z-score 判为离群，因为极端高值抬高了均值和标准差；IQR 因用中间 50% 更鲁棒，不受极端值影响。
* **EN**: Z-score can miss high outliers when extreme values inflate mean/std; IQR remains robust using the middle 50%.

### 7.4.4 Isolation Forest（ML-based，适合高维与非线性）

* **核心思想（CN）**：不是去“拟合正常”，而是通过随机切分把点隔离；离群点更容易被少量切分隔离（更短 path length）。
* **适用（EN）**：large datasets, high-dimensional data, complex nonlinear patterns; no distribution assumption; fast & scalable.
* **限制（CN）**：可解释性较弱；需要设置 contamination 等超参。

### 7.4.5 其他离群方法（你要会“关键词+机制”）

* **LOF**：基于局部密度，密度明显低于邻居 → LOF≫1 视为离群。
* **DBSCAN**：密度聚类；不属于任何簇的点标为 Noise（离群）。
* **One-Class SVM (OCSVM)**：学习高维边界/“包住大多数点”的区域，边界外即离群（Novelty detection）。

### 7.4.6 方法对比表（Z / IQR / Isolation Forest）

* **Z-score**：parametric；best for normal；弱点：skewed data。
* **IQR**：non-parametric；best for skewed；弱点：高维弱。
* **Isolation Forest**：ML-based；best for high-dim nonlinear；弱点：需调参。

### 7.4.7 选型指南（按数据特征选方法）

* Normal distribution → Z-score
* Skewed / non-normal → IQR 或 Isolation Forest
* Varying density / local clusters → LOF 或 DBSCAN
* High-dimensional complex → Isolation Forest 或 One-Class SVM

---

# 8. Profiling + Cleaning 的综合收益（Benefits）

* **CN**：更早发现错误；产出高质量数据；提升分析与决策效率与质量；避免报表/模型的代价性错误。
* **EN**: Catch errors early, produce high-quality data, enable faster/more reliable analysis and decisions. 

---

