# Week 3.Bias Mitigation and Dimensionality Reduction + EDA summary

把 **Week 3 的两个文件**（**Bias Mitigation and Dimensionality Reduction** + **EDA summary**）里的知识点 **按逻辑顺序**整理成一份**完整提纲**，并在每个知识点下做**中英文讲解**确保覆盖两份 PDF 的全部核心内容与例子。

---

## 1. Bias Mitigation：类别不平衡与 SMOTE（合成少数类过采样）

### 1.1 为什么“类别不平衡”会造成偏差（Data Bias）

**中文讲解**
很多真实任务里，**少数类才是我们最关心的**：如欺诈检测、疾病诊断、贷款违约、罕见事件预测。问题是少数类样本太少，模型为了提高总体准确率，会更“讨好”多数类：

* 损失函数被多数类主导
* 少数类错分被当成“便宜错误”（cheap errors）
* 模型学到对多数类的结构性偏向
  这在课件中被强调为 **“数据偏差（Data Bias）而非算法偏差（Algorithm Bias）”**。

**English**
In imbalanced datasets, models optimize overall accuracy, majority class dominates the loss, minority errors are treated as cheap, creating **structural bias toward the majority**—this is **data bias** rather than algorithm bias.

---

### 1.2 不平衡数据的典型挑战：为什么 Accuracy 会“骗人”

**中文讲解**
课件点出 3 个关键挑战：

1. **Biased Models**：算法优先学多数类，少数类效果差
2. **Misleading Metrics**：例如 95:5 的数据，即使模型全预测多数类也能有 95% Accuracy（毫无意义）
3. **Difficulty in Learning Patterns**：少数类样本少，模式更难学到
   因此评估应更关注：**Precision / Recall / F1 / ROC-AUC**。

**English**
Accuracy can be deceptive in imbalanced datasets; use **Precision, Recall, F1, ROC-AUC** instead.

---

### 1.3 SMOTE 的核心思想：不是复制，而是“插值生成”

**中文讲解（按课件步骤原序）**
SMOTE（Synthetic Minority Over-sampling Technique）的做法：

1. 选一个少数类样本 (x_i)
2. 在少数类内部找它的 (k) 个最近邻
3. 随机选一个邻居 (x_j)
4. 生成新样本：在Xi和Xj的连线上，取一个中间点当新样本

   X*new* = X*i*+ r*(X*j* - X*i*),      r取值范围是(0,1)

   **·x**j−**x**i：从 xi指向 **x**j 的 方向向量
   ·乘上 r∈(0,1)：走一段比例（比如走 30%、70%）
   ·加回 xi：从 xix_i**x**i 出发走过去

   这样生成的新点“像少数类、但不是重复点”，能减少简单过采样导致的过拟合（duplicate points → overfitting）。

**English**
SMOTE creates synthetic minority samples by interpolating between a minority sample and its k-nearest minority neighbors (not duplicating).

---

### 1.4 SMOTE 在“公平性/安全性”上的作用：纠正哪些偏差

**中文讲解**
课件把 SMOTE 带来的改变总结为 4 类（非常适合出选择题/配对题）：

* **Representation Bias（代表性偏差）**：少数类曝光不足 → 更均衡的曝光
* **Decision Boundary Bias（边界偏差）**：决策边界偏向多数类 → 边界更公平
* **Error Asymmetry（错误不对称）**：少数类 FN 很高 → Recall 提升
* **Algorithmic Blindness（算法“失明”）**：少数类被忽略 → 模型开始学到少数类

**English**
SMOTE reduces representation bias, boundary skew, minority FN (improves recall), and algorithmic blindness.

---

### 1.5 用混淆矩阵与分类报告读懂“代价权衡”（Trade-off）

**中文讲解**
课件给了 SMOTE 前后的混淆矩阵、Accuracy 以及分类报告（precision/recall/f1/support）。
核心结论一句话（课件原意）：

> **SMOTE 通过提高少数类 recall 来提升公平性与安全性，但会牺牲 accuracy 与 precision；在不平衡问题中，这种权衡是“预期且必要”的。**

再结合银行风控语境：**漏判一个“风险人”（FN）代价远高于误报一个“安全人”（FP）**，所以宁愿牺牲一些总体准确率，也要减少 FN。

**English**
SMOTE increases minority recall (fairness/safety) at the cost of accuracy and precision—an expected trade-off in imbalanced problems; FN may be far costlier than FP in risk settings.

---

## 2. Dimensionality Reduction：降维（减少特征维度，但尽量保留信息）

### 2.1 降维的定义与为什么要降维

**中文讲解**
降维：在尽量保留有用信息的前提下，减少输入特征数量。它的好处（课件列得很“考试友好”）：

* 更易可视化（Easier to visualize）
* 提升模型表现、减少过拟合（Less prone to overfitting）
* 训练更快（Faster to train）
* 更少噪声/冗余（Less noisy, removes redundancy）
* 处理多重共线性（Multicollinearity）

**English**
Dimensionality reduction reduces the number of input features while preserving useful information; helps visualization, speed, noise reduction, overfitting, and multicollinearity.

---

### 2.2 两大路线：Feature Selection vs Feature Extraction（必考区分）

**中文讲解**

* **Feature Selection（特征选择）**：从原特征里选一部分保留，特征语义不变

  * Filter：相关性阈值、卡方
  * Embedded：Lasso、树模型重要性
* **Feature Extraction（特征提取）**：把原特征“变换”为更少的新特征（通常是组合/表示）

  * PCA、SVD、t-SNE、Autoencoder

**English**
Selection keeps a subset of original features; Extraction transforms into fewer new variables (PCA/SVD/t-SNE/Autoencoder).

---

### 2.3 常见降维方法对比（PCA / SVD / t-SNE / Autoencoder）

下面按课件表格的“考点结构”讲：类别、理论目标、适用场景、局限。

#### 2.3.1 PCA（线性、无监督）

**中文讲解**

* **目标/理论**：找能解释最大方差的方向（主成分）
* **优势**：压缩、降噪、简单快速；常用于特征提取与 2D/3D 可视化
* **局限**：线性假设；成分可解释性差（原特征的组合）；对尺度敏感（需 scaling）

**English**
PCA finds directions capturing maximum variance; good for compression/noise reduction; but linear, less interpretable, and sensitive to feature scaling.

#### 2.3.2 SVD（线性、无监督，矩阵分解）

**中文讲解**

* 把数据矩阵分解成三个矩阵，取最大奇异值对应的低维表示
* 是 PCA 的数学基础之一，常用于推荐系统、图像压缩、潜因子建模
* 局限与 PCA 类似：偏线性、解释性弱

**English**
SVD factorizes the data matrix; foundation for PCA; used in recommender systems/image compression; similar linear/interpretability limitations.

#### 2.3.3 t-SNE（非线性、无监督，偏可视化）

**中文讲解**

* **核心**：尽量保留“局部结构”（邻近点距离关系），做高维到低维的概率分布匹配
* **优势**：探索性可视化很强，复杂非线性簇分离效果好，常用于 EDA
* **局限**：计算慢；不适合生产；对超参数敏感

**English**
t-SNE preserves local structure for visualization/EDA, but is slow and hyperparameter-sensitive; not ideal for production.

#### 2.3.4 Autoencoder（非线性、神经网络）

**中文讲解**

* Encoder-Decoder 学习瓶颈层（低维表示），再重建输入
* 优势：能学复杂非线性关系，可做去噪/生成式建模
* 局限：需要更多数据与调参；计算贵；输出难解释

**English**
Autoencoders learn a compressed bottleneck representation via encoder-decoder; powerful but data-hungry, expensive, and hard to interpret.

---

### 2.4 PCA 的“优缺点表”与考试常问点

课件对 PCA 做了总结性强调：PCA 能提升性能、加速训练、增强可视化；当模型拟合慢可考虑用 PCA。
同时给出优缺点对照表（强烈建议背成“配对题”）：

* 优点：降维、加速、抗过拟合、压缩
* 缺点：信息可能丢；PCA 本身也有计算成本；可能去掉“低方差但很关键”的特征；压缩是有损；不适合对可解释性/监管语义要求强的领域（医疗、金融指标等）

---

### 2.5 降维的“风险警告”：可解释性与合规语境

**中文讲解（课件原意非常关键）**
降维很强大但并非无害：

* 降维前：income/age/blood pressure 语义清楚
* 降维后：变成各种线性混合（例如 0.3×income + 0.5×age − …）
* 你无法再解释“因为收入高所以拒贷”
  当决策影响人（健康、金融、法律）且需要解释时，这很危险。

**English**
After reduction, features become mixtures, harming interpretability—dangerous when explanations are required (health/finance/law).

---

### 2.6 最终总结：为什么用降维、但要谨慎

课件的收束要点：让模型更快、减少过拟合、去冗余、抓大结构；但代价是解释性下降、可能丢重要信号、并非通用，需要结合上下文。

---

## 3. EDA Summary：探索性数据分析的完整流程（以 House Prices 为例）

### 3.1 学习目标与数据集背景（考试常用“概念定义题”）

**中文讲解**
EDA 的目标：理解 EDA 的作用，识别数据质量与分布问题，应用清洗/编码/变换/缩放，并对比 EDA 前后模型表现。数据集是 Kaggle House Prices：1460 条样本、80+ 特征，混合数值/有序/无序，目标 SalePrice。

**English**
EDA aims to diagnose quality/distribution issues, apply preprocessing, and evaluate model performance before vs after EDA; dataset: House Prices (1460 rows, 80+ features), target SalePrice.

---

### 3.2 EDA 的步骤总览（从“看清数据”到“可建模数据”）

课件按顺序给出步骤，我在这里把每一步“为什么做 + 怎么做 + 常考点”展开。

#### 3.2.1 Data Inspection / Exploration（先不变换）

**中文讲解**

* `df.shape`：数据规模（行列）
* `df.info()`：类型、缺失、非空数
* 目的：尽早发现潜在问题（缺失、类型不对、字符串混入数值等）
* 注意：此时**不要做任何变换**（避免一上来就“处理过头”）

#### 3.2.2 Statistical Summary（均值/中位数/范围 → 暗示 skew / scaling / outlier）

**中文讲解**

* Mean/Median 差距大 → **偏态（skew）**
* Range 很宽 → **尺度差异（scaling issues）**
* 极值/范围异常 → **离群点（outlier）** 线索

---

### 3.3 Data Cleaning：让数据“语义正确 + 模型可用”

**中文讲解**：纠正无效值、解决命名不一致、保证语义正确、让数据可被模型消费。

---

### 3.4 把“模糊 NaN”变成“有意义的类别/数值”（非常容易考案例题）

**中文讲解（House Prices 经典坑点）**
很多 NaN 不是 unknown，而是 **“没有这个结构”**。例如车库相关特征：GarageType / GarageFinish / GarageQual / GarageCond / GarageCars / GarageArea：

* 如果 NaN 表示“没有车库”

  * 类别型填 `"None"`
  * 数值型填 `0`
    这样避免把“缺失”误当成“坏数据”，并保留领域语义。

**English**
Many NaNs mean “absence of structure” (e.g., no garage). Fill categorical with “None”, numerical with 0 to preserve domain meaning.

---

### 3.5 Missing Value Analysis：缺失不等于错误，策略要分类型

**中文讲解**
要点：

* 不同特征要用不同策略
* 缺失本身可能携带信息（missingness carries information）
* LotFrontage / MasVnrArea / Electrical / KitchenQual 等缺失通常需要“合理插补”，并结合 MCAR/MAR/MNAR 的判断

**“缺失合理”的典型列与处理**（课件给的表）：

* Alley：大部分房子没有巷道 → 填 “None”
* PoolQC：没泳池 → “None”
* Fence：没围栏 → “None”
* MiscFeature：罕见设施（棚屋、电梯）→ “None”
* FireplaceQu：没壁炉 → “None”

---

### 3.6 Separating Feature Types：数值 / 类别（nominal vs ordinal）要分开走不同 pipeline

**中文讲解**

* 数值特征：连续/离散
* 类别特征：名义（nominal）/有序（ordinal）
* 不分开会导致错误变换（比如把 nominal 当成有序数值做缩放/相关性）

---

### 3.7 Outliers：识别后“保留/截断/移除”，并且每一步都要可视化验证

**中文讲解**

* 先识别极端值
* 决策：keep、cap、remove
* 每一步都画图验证（避免误删“真实豪宅”这类合理极端点）

**课件给的直观例子（GrLivArea 极端值对树模型的伤害）**：
少数超大面积房子会让决策树产生“很宽且不自然”的划分区间，导致中等价位区域不稳定、碎片化。

---

### 3.8 Skewness（偏态）修正：为什么、以及常用方法

**中文讲解**
修正偏态的目的：稳定方差、改善线性关系、降低极端值影响。常用方法：Log / Square / Yeo-Johnson / Box-Cox。

**English**
Fixing skew stabilizes variance, improves linearity, reduces impact of extremes; methods include Log, Square, Yeo-Johnson, Box-Cox.

---

### 3.9 Scaling：它不改变数据本身，而是改变“模型看到数据的方式”

**中文讲解（课件原话的逻辑）**

* scaling 改变优化地形（optimization landscape），未缩放时大尺度特征主导学习
* 提升系数可解释性
* 距离模型（KNN/K-Means/SVM/层次聚类）依赖尺度
* 梯度模型收敛更快
* 但：scaling **不提升特征相关性/不直接提升数据质量**（别迷信）

---

### 3.10 Categorical Encoding：为什么必须编码、以及关键注意点

**中文讲解**
不编码，类别还是文本，模型/统计无法：

* 与 target 做相关性
* 数值化做分组统计
* 做多变量关系建模
  编码让“类别影响”可度量。常见还要：
* 用众数做插补（most frequent / mode）
* 处理未见类别（unseen categories）

**有序编码的典型例子（Po → Fa → TA → Gd → Ex）**：价格随等级单调上升，把视觉规律变成可计算关系。

---

### 3.11 Univariate vs Bivariate vs Multivariate：每一类回答什么问题、用什么统计与图

这是 EDA summary 的“结构化考点核心表”，很容易出“配对题/选择题”。

#### 3.11.1 Univariate（单变量）

问：分布怎样？是否偏态？是否有离群点？
统计：均值/中位数/方差/std/IQR/偏度等；类别看频数与平衡
图：直方图、KDE、箱线图、条形图

#### 3.11.2 Bivariate（双变量）

问：两个变量是否相关？强度？线性/非线性？影响？
配对：数值-数值、类别-数值、类别-类别
统计：Pearson/Spearman 相关、协方差
图：散点图、箱线图等

#### 3.11.3 Multivariate（多变量）

问：变量如何共同作用？哪些一起最重要？是否冗余？能否降维？
方法：多元回归、相关矩阵、聚类；图：相关热力图、pair plot
作用：解释联合效应、去冗余、为建模/降维做准备

---

### 3.12 Feature Engineering 在 EDA 里的价值：把“更可解释的信号”做出来

课件给了 3 个很典型的“时间类衍生特征”（House Prices 经典）：

* `HouseAge = YrSold - YrBuilt`：卖出时房龄（相对尺度更有意义）
* `YearsSinceRemodel = YrSold - YrRemodAdd`：翻新距今时间（解释“老房为什么也能卖高价”）
* `EffectiveAge = min(HouseAge, YearsSinceRemodel)`：捕捉“买家感知年龄”，把多条时间线压缩成一个信号（降噪）

---

### 3.13 为什么要用 Pipelines：EDA 负责探索，Pipeline 负责“正确性与一致性”

**中文讲解**
Pipeline 是一组按顺序、可重复的处理步骤，保证把原始数据变成可分析数据时不引入错误或泄漏。
课件给出典型 pipeline：

* 数值：Impute → Transform → Scale（例：中位数插补 → Log → StandardScaler）
* 类别：Impute → Encode（例：众数插补 → One-Hot）
* 混合：按列处理（Column-wise pipelines）
* 聚类：Scale → Cluster（先统一尺度再分群）

---

### 3.14 Key Takeaways（结课式总结，常变成判断题/填空题）

**中文讲解**

* EDA 不是可选项，而是基础
* 它建立数据质量与有效性、分布假设、合适变换与可行建模选择
* “你无法对不了解的数据建模”
* 数据表示（representation）往往比算法更重要
* 模型失败很多时候不是模型错，而是表示错（Models don’t fail — representations do）

---

## 4. 你做题时最容易被考的“高频点清单”（按 Week3 文件归纳）

1. **SMOTE 的步骤**（选点、kNN、插值公式、不是复制）
2. **为什么 Accuracy 误导**，以及该用哪些指标
3. **SMOTE 的 trade-off：Recall↑ vs Accuracy/Precision↓**
4. **Feature Selection vs Feature Extraction 区分+例子**
5. **PCA 的优缺点 & 对 scaling 敏感 & 可解释性风险**
6. **EDA 流程顺序**：inspection → summary → cleaning → missing handling → type split → outlier → skew fix → scaling → encoding → multivariate/pipelines
7. **“NaN 可能表示没有结构”**（Garage 的 None/0）

---
