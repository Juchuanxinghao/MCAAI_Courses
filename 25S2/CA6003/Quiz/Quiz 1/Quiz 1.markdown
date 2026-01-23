


# 1. Week 1 — Data Profiling and Cleaning（数据画像与清洗）

## 1.1 课程结构与考核信息

* **课程时间与形式（CN）**：6 周；课前看录播；周二答疑；周六上机练习；使用 Anaconda + Python notebook。
* **Assessments（EN）**: 2 quizzes + 1 assignment; hands-on coding required. 

## 1.2 Data science thinking process（用 Phoenix FC 故事串起全流程）

> 这一段的目的：让你记住“每一步为什么存在”，而不是只记工具。

### 1.2.1 Ask（提出可被数据回答的问题）

* **CN**：把“球队不稳定”拆成可量化问题：传球成功率（按区域/球员）、下半场跑动/速度、射门位置/xG、犯规的地点与责任人等。
* **EN**: Convert vague problems into measurable questions (pass completion by zone/player, second-half sprinting, shot location/xG, foul patterns). 

### 1.2.2 Prepare（数据获取与标注）

* **CN**：多源数据：视频标注、比赛/裁判/队医报告、GPS 可穿戴定位；所有事件要带 player id、时间戳、坐标；并引入 xG 标注体系。
* **EN**: Multi-source logging with IDs/timestamps/coordinates; xG tagging improves shot quality measurement. 

### 1.2.3 Process（把原始数据“打磨成指标”）

* **CN**：原始数据必然脏：GPS 掉线、人工标注错误、定义不一致；需要把 raw numbers 变成可比较的指标（如每 90 分钟距离、每防守动作犯规、射门热力图、平均 xG/shot），并处理异常与标准化。
* **EN**: Raw data is messy; convert into normalized metrics + fix outliers + standardize definitions.  

### 1.2.4 Analyze（找规律/找证据）

* **CN**：发现长传成功率在后场→前场很低且导致反击；射门多但平均 xG/shot 低（射门质量差）；70 分钟后高强度冲刺下降显著。
* **EN**: Identify low-success long passes, low xG/shot, and sprint drop-off after ~70 minutes. 

### 1.2.5 Share（用可视化“桥接直觉与证据”）

* **CN**：用热力图/趋势图把教练直觉变成可验证证据（控球丢失热区、冲刺距离趋势、射门位置聚类等）。
* **EN**: Visuals bridge intuition and evidence (heatmaps/trends). 

### 1.2.6 Act（落地改进）

* **CN**：根据证据调整训练与策略：耐力训练、数据驱动换人、后场长传训练、进攻更聚焦高 xG 区域、过渡防守站位减少犯规。
* **EN**: Turn insights into targeted interventions (training, substitution strategy, shot selection, transition defense). 

## 1.3 Data science pipeline（标准流程框架）

* **CN**：定义问题 → 获取数据（新采集或既有数据）→ 理解与准备数据（结构/质量/分布/关系）→ 清洗/变换/特征工程 → 训练评估 → 部署维护。
* **EN**: Pipeline stresses data structure, quality, distribution, and relationships before modeling. 

## 1.4 The rise of data（数据规模增长的背景）

* **CN**：用“Data never sleeps”例子说明数据规模与流速巨大，驱动数据科学需求。
* **EN**: Massive growth in daily digital content motivates data science. 

## 1.5 Data collection 的关键假设与风险（非常适合出判断题）

* **关键假设（CN）**：数据完整真实、能代表目标群体、合法合规可用。
* **Critical risks（EN）**：数据太少/伪造会学到“胡话”；不具代表性会不公平且过时；不合规会项目终止与法律风险。 

## 1.6 Data preparation（数据准备）的定义与组成

* **CN**：把数据“收集、组合、结构化与组织”到可用于分析/可视化/建模；组成包括 profiling、cleaning、feature engineering、transformation。
* **EN**: Data preparation organizes data for analytics; includes profiling/cleaning/feature engineering/transformation. 

## 1.7 数据类型：Structured vs Unstructured（以及常见子类型）

### 1.7.1 Structured data（结构化）

* **CN**：字段固定、表格化，易查询过滤；常见：数值/类别（factor）、时间序列、网络数据。
* **EN**: Organized, tabular, fast querying; includes numeric/categorical, time series, network. 

### 1.7.2 Unstructured data（非结构化）

* **CN**：无预定义 schema，高度依赖语境；常见：文本、图像、语音、视频；需要 NLP/CV/DL 抽取结构。
* **EN**: Lacks schema, contextual; requires DL/NLP/CV to derive structure. 

## 1.8 Data profiling（数据画像/剖析）：要检查什么

* **结构（Structure discovery）**：数据集大小、字段与类型（数值/类别/其他）。 
* **质量（Quality）**：缺失、离群、错误、噪声。 
* **分布（Distribution）**：范围、模式、趋势。 
* **关系（Relationship）**：变量相关性与依赖结构。 

## 1.9 Data cleaning（数据清洗）：定义与常见问题类型清单

* **CN**：清洗是在建模前纠正/处理数据质量问题，提升有效性与可用性。
* **常见脏数据类型（CN/EN）**：缺失值、重复、噪声/无关特征、格式/单位不一致、截断数据、无用元数据等。 

## 1.10 Missing values（缺失值）：检测与处理方法全集

### 1.10.1 检测与统计

* `df.isnull().sum()` / `df.info()` 用于定位缺失列与缺失比例。 

### 1.10.2 处理策略（按课件清单逐项覆盖）

* **删除（Drop）**：缺失少且删除不影响信息时删除行/列。 
* **均值/中位数/众数填补（Mean/Median/Mode）**：数值/类别常用基线方法。 
* **前向/后向填补（FFill/BFill）**：时间序列常用。 
* **预测式插补（Predictive/KNN imputation）**：用模型预测缺失（如 `KNNImputer`）。 
* **领域规则填补（Domain-based）**：按业务逻辑补（如基线情绪=neutral）。 
* **分箱插补（Binning imputation）**：先分箱再用箱内统计补。 

## 1.11 Outlier detection（离群点检测）：基础两法 + 进阶三法 + 方法选择指南

### 1.11.1 Z-score（适合近似正态）

* **公式（EN）**: (x_{new}=(x-\mu)/\sigma)，常用阈值 (|Z|>3)。
* **优缺点（CN）**：简单快；但对偏态/非正态不稳，且极端值会抬高均值与标准差导致漏检。  

### 1.11.2 IQR（更鲁棒，适合偏态/非参数）

* **定义（EN）**: (Q1,Q3,IQR=Q3-Q1)，超出区间视为离群。
* **优缺点（CN）**：对极端值不敏感，适合偏态；但不擅长高维复杂模式。 

### 1.11.3 LOF / DBSCAN / One-Class SVM（进阶方法：你要会“适用场景”）

* **LOF（CN）**：比较局部密度；密度显著低于邻居 → 离群。
* **DBSCAN（CN）**：密度聚类；不属于任何簇的点标记为 Noise（离群）。
* **OCSVM（CN）**：学习高维边界，把落在边界外的点视为离群/新颖。 

### 1.11.4 方法选择指南（课件总结版）

* **Normal** → Z-score
* **Skewed / Non-normal** → IQR 或 Isolation Forest
* **局部密度/簇结构明显** → LOF / DBSCAN
* **高维复杂数据** → Isolation Forest / One-Class SVM 

---

# 2. Week 2 — Feature Engineering（Encoding / Scaling / Transformation）+ Bias Mitigation（偏差缓解）

## 2.1 类别特征编码（Categorical Encoding）总览：方法与适用条件

* **CN**：编码把类别变量转成数值；选择取决于：是否有序（ordinal/nominal）、基数（cardinality）、是否容易引入维度爆炸或泄漏。
* **EN**: Choose encoding by order, cardinality, and leakage risk.
  课件给出方法与推荐逻辑汇总：Ordinal/Label、One-Hot、Frequency、Binary、Hash、Target。 

## 2.2 Target Encoding（目标编码）定义与“为什么强”

* **定义（EN）**：(Enc(i)=Mean(Target \mid Category=i))，二分类时是正类比例，连续目标时是均值。 
* **CN**：它把“类别→目标”的统计关系直接注入特征，所以通常很强，但也最容易过拟合/泄漏（尤其类别样本很少时）。

## 2.3 编码方法的选型表（课件给的“Reasoning”）

* **有自然顺序** → Ordinal/Label
* **无序且低基数** → One-Hot
* **高基数且可能碰撞** → Frequency（有 collision 风险）
* **中等基数、想降维** → Binary
* **更大词表、可接受 hash collision** → Hash
* **与目标强相关** → Target Encoding 

## 2.4 Target encoding 的正则化（防过拟合/小样本不稳定）

* **CN**：课件强调对小样本类别要“向全局均值收缩”，category_encoders 使用 sigmoid 权重：样本量 (n_i) 小就几乎不信该类别均值，(n_i) 大才逐渐信。 

## 2.5 Feature scaling（特征缩放）是什么、为什么需要

* **定义（CN）**：改变数值特征的幅度/范围，但尽量保持分布形状；用于不同特征量纲差异很大时避免“大数值特征压制小特征”。 
* **Mechanism（EN）**：线性变换（减均值/除标准差/用 min-max 等）。 
* **Why（EN）**：

  * 距离模型（KNN/SVM/K-means）需要各特征“公平参与距离计算”；
  * 梯度优化更易收敛。  

### 2.5.1 缩放与线性模型可解释性（考试很爱考这段逻辑）

* **CN**：线性模型 (y=\sum w_ix_i + b)。特征尺度不同会导致系数尺度不同，不能直接比较哪个特征更重要；缩放后系数才可直接比较“影响力”。 

## 2.6 四大 scaler：Standard / MinMax / Robust / MaxAbs（定义+适用场景+对离群点/稀疏性的影响）

课件对比表的要点如下（你需要能“对号入座”）：

* **StandardScaler（标准化）**：适合近似高斯；对 outlier 敏感；会平移到 0 附近（零不再保持零）。 
* **MinMaxScaler（归一化）**：压到固定范围（常 [0,1]）；对 outlier 极其敏感。 
* **RobustScaler**：用 median 与 IQR，抗 outlier 强。 
* **MaxAbsScaler**：适合稀疏数据（NLP/文本）；**保持 0 仍为 0**。 

（课件还给了 property tax 数据的选择直觉与范围表现）

## 2.7 Power transformation（幂变换）与 Skewness（偏度）

### 2.7.1 为什么需要幂变换

* **CN**：很多算法（尤其参数模型）更喜欢近似正态；现实数据偏态/重尾/异方差会让线性/逻辑回归等表现变差。
* **EN**: Power transforms map data closer to Gaussian; helps with skew, heavy tails, heteroscedasticity. 

### 2.7.2 Skewness 三类与修复方法

* **右偏（Positive/Right skew）**：右长尾；用 log/开方/取根修复（如收入、房价、里程）。
* **左偏（Negative/Left skew）**：左长尾；用平方/立方等幂修复（如退休年龄、考试分数）。
* **对称（Zero skew）**：近似钟形。 

### 2.7.3 Box-Cox vs Yeo-Johnson

* **Box-Cox（EN）**：仅适用于正数；
* **Yeo-Johnson（EN）**：可处理正数/0/负数。 

### 2.7.4 什么时候用、哪些模型收益最大

* **Use when（EN）**：强偏态、非恒定方差、重尾、线性模型因非正态而表现差。
* **Benefiting models（EN）**：Linear/Logistic Regression、KNN 等距离模型。 

## 2.8 Advanced feature engineering（进阶特征工程）

* **派生特征（Derived features）**：如 DOB→Age、Price/Area→Price per SqFt。
* **NLP 特征**：TF-IDF（词重要性），Word2Vec（稠密语义向量）。
* **降维（Dimensionality Reduction）**：PCA 保留方差信息降低复杂度。 

---

## 2.9 Bias / Fairness（偏差与公平）：偏差类型与后果

### 2.9.1 偏差类型（课件逐条）

* Historical bias：历史不平等被数据继承（招聘偏向男性）。
* Sampling bias：群体采样不足（人脸识别对深色皮肤差）。
* Label bias：标签本身不公（贷款违约标签受偏见审批影响）。
* Measurement bias：测量方式对不同群体不一致（医疗设备对某人群更准）。 

### 2.9.2 公平性后果

* Unequal error rates（不同群体误差率差异）
* 自动化决策歧视（招聘/贷款/保险/执法）
* 信任与伦理问题 + 合规风险 

### 2.9.3 对泛化能力的影响（generalization）

* 对主导群体过拟合 → 其他群体表现差
* 学到“捷径特征” → 域外失败（wolf vs dog 用雪背景）
* Domain shift（只在晴天训练的自动驾驶雨天失败）
* 算法假设过简（线性假设不适配非线性现实） 

### 2.9.4 如何降低偏差、提升公平与泛化

* 提升数据多样性；平衡采样/重加权；公平标注；公平算法；跨群体指标（FPR/FNR、demographic parity）；审计工具；高风险决策 human-in-the-loop。 

## 2.10 Bias mitigation techniques（偏差缓解技术：课件聚焦预处理）

* **预处理（pre-processing）**：在训练前改数据。 
* **Reweighing / Resampling**：对弱势群体不利结果样本加更高权重。 
* **Oversampling**：复制/合成少数类直至分布更平衡，用于推动 demographic/statistical parity。 
* **SMOTE**：两相近少数类点连线插值生成新样本；比简单复制更不易过拟合，但边界附近可能生成噪声点。 
* **ADASYN / SMOTE-ENN**：

  * ADASYN：对“难学的边界点”生成更多样本；但对噪声敏感。
  * SMOTE-ENN：先 SMOTE 再用 ENN 清理噪声/重叠点，边界更干净但实现更复杂、会删原始数据点。 
* **重要提醒（CN）**：重加权/重采样并不改变特征本身，若存在 proxy bias（非敏感特征与敏感属性强相关），仍可能保留偏差；且对少数群体过拟合风险存在。 

---

# 3. Week 3 — Bias Mitigation and Dimensionality Reduction（偏差缓解与降维）

> Week3 的核心是：**不平衡数据（尤其少数群体/少数类）如何影响模型公平与性能，以及用 SMOTE 等方法缓解；并引出“维度灾难”与降维必要性。**

## 3.1 EDA 与统计视角（录播总结：从单变量到多变量）

* **单变量（Univariate）**：均值/中位数/众数，方差/std/IQR，形状（skewness/kurtosis），极值（min/max），可视化（hist/KDE/boxplot/bar）。 
* **双变量（Bivariate）**：两变量关系、强度、线性/非线性；相关（Pearson/Spearman）等；可视化（scatter/box/line）。 
* **多变量（Multivariate）**：变量联合交互、冗余检测、可否降维；方法：多元回归、相关矩阵、聚类；为降维做准备。 

## 3.2 SMOTE（作为偏差缓解/不平衡学习工具）的关键定义与逻辑

* **CN**：SMOTE 用“相近少数类样本插值”合成新样本，提高少数类/弱势群体的表示，让模型更好学习决策边界；优缺点与变体（ADASYN、SMOTE-ENN）在 Week2 已完整列出。 

## 3.3 Dimensionality Reduction（降维）为什么需要：维度灾难的直觉

* **CN**：维度越高，同样密度覆盖空间所需样本呈指数增长（“10 个位置→100→1000”的直观图）；高维下距离度量变得不可靠，训练更慢、更易过拟合，噪声特征会掩盖信号。
* **EN**: Curse of dimensionality: volume grows exponentially, distances become less informative, learning becomes harder.

## 3.4 降维的两大路线：Feature Selection vs Feature Extraction

* **Feature selection（特征选择）**：从原特征中挑子集（保留可解释性更强）。
* **Feature extraction（特征提取）**：把原特征映射到新空间（如 PCA），通常更压缩但解释性下降。

## 3.5 PCA（主成分分析）的定位（与 Week2 的“降维”呼应）

* **CN**：PCA 用线性变换把数据投影到方差最大的方向（主成分），用更少维度保留尽可能多的信息；常与 StandardScaler 搭配（因为 PCA 对尺度敏感）。
* **EN**: PCA finds directions of maximum variance; scaling is crucial.

---


