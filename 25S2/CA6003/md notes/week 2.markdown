

# Week 2.Feature engineering encoding, scaling and bias mitigation methods

按**逻辑顺序**把 Week2 文件里的**全部知识点**（中英双语）整理成「完整知识点提纲 + 详细讲解」。把 **detail版**（更完整、含例子/表格/公式/对比/正则化与 SMOTE 变体）和 **recording版**（更精炼、重点提示）合并去重，但每个点都会覆盖到。
引用来源：Week2 detail  + Week2 recording 

---

# 1. Feature Engineering 总览（特征工程概览）

## 1.1 什么是特征工程（What is Feature Engineering）

* **CN**：特征工程是把原始数据通过编码、缩放、变换、派生等操作，变成更适合模型学习的输入。
* **EN**: Feature engineering transforms raw data (encoding, scaling, transformation, derived features) into model-friendly inputs.

## 1.2 课程覆盖的三块内容（Three blocks in Week2）

1. **Data encoding（类别编码）**
2. **Feature scaling（数值缩放）**
3. **Bias & Bias mitigation（偏差与缓解）**

---

# 2. Data Encoding（类别特征编码）

## 2.1 编码的定义与必要性（Definition & why needed）

* **CN**：编码就是把类别数据转成整数/数值表示，让模型能吃进去并提升预测。大多数 ML 算法需要数值输入。
* **EN**: Encoding converts categorical variables to numeric formats so models can process them and improve predictions.

## 2.2 类别数据两种类型（Two types of categorical variables）

* **Nominal（名义型）**：无内在顺序（no intrinsic order）
* **Ordinal（有序型）**：有自然顺序（has meaningful order）
* **关键结论（CN/EN）**：编码方法的选择高度依赖 nominal vs ordinal。

## 2.3 编码方法清单（Types of encoding）

* Label / Ordinal Encoding（用于 ordinal）
* One-Hot Encoding（用于 nominal）
* Count / Frequency Encoding（用于 nominal）
* Binary Encoding（用于 nominal）
* Target Encoding（用于 nominal，尤其高基数）
* Hash Encoding（用于 nominal，尤其超高基数/NLP）

---

## 2.4 Label / Ordinal Encoding（标签/有序编码）

### 2.4.1 核心思想（Idea）

* **CN**：按“等级/顺序”把类别映射到整数（rank-based mapping）。
* **EN**: Map each ordered category to an integer respecting rank.

### 2.4.2 什么时候用（When to use）

* **CN**：只有在类别确实有“自然顺序”时用，否则会制造虚假的大小关系。
* **EN**: Use only when a true natural order exists; otherwise creates a false order/linear relationship.

### 2.4.3 优缺点（Pros & Cons）

* **Pros（EN/CN）**：简单、节省内存、保留顺序信息。
* **Cons（EN/CN）**：若本来无序，模型会误以为有序且线性关系存在。

### 2.4.4 课件例子（Example）

* **Size: Small < Medium < Large** 是典型可 ordinal 的列（保留层级含义），树模型/boosting 往往能很好用。 

---

## 2.5 One-Hot Encoding (OHE)（独热编码）

### 2.5.1 核心思想（Idea）

* **CN**：每个类别开一列 0/1，表示“是否属于该类别”。
* **EN**: Create one binary column per category; each row has a 1 in its category column.

### 2.5.2 优点（Pros）

* 不会引入虚假顺序（prevents artificial order）
* 对 **线性/逻辑回归、SVM、KNN** 等距离/线性模型友好
* 可解释性强（透明，易解释）
* 对 nominal 给出更“表达性/非偏置”的表示

### 2.5.3 缺点（Cons）

* **维度灾难（curse of dimensionality）**：高基数会爆列，计算与内存开销大
* **多重共线性（dummy variable trap）**：某一列可被其他列线性预测（完美共线）

### 2.5.4 课件例子（Example）

* **Color** 是 nominal 且类别数少（5 类），最适合 OHE；并特别指出对线性/逻辑回归很合适。 

---

## 2.6 Count / Frequency Encoding（计数/频率编码）

### 2.6.1 核心思想（Idea）

* **CN**：用“类别出现次数/频率”替换类别：Count 或 Frequency。
* **EN**: Replace each category with its occurrence count or frequency.

### 2.6.2 优点（Pros）

* 不增加维度（dimensionality stays 1 column）
* 编码里包含“常见/稀有”信息（rare vs frequent）
* 对新类别处理简单：可赋默认频率（如 0）
* 稀有类别自然得到小值，有助于减少过拟合风险

### 2.6.3 缺点（Cons）

* **Collision（碰撞）**：不同类别若频率相同会变成同一个值 → 信息损失

### 2.6.4 课件例子（Example）

* 对 Color 可算出 Silver=3、Black=3、Blue=1… 或频率 0.3、0.3、0.1… 

---

## 2.7 OHE vs Frequency（名义型编码选择对比）

课件给出一个对照表（你要能“按条件选”）：

* **Cardinality（基数）**：OHE 适合低基数（<5），Frequency 适合高基数（>10）
* **维度**：OHE 增维，Frequency 不增维
* **风险**：OHE 稀疏/维度爆炸，Frequency 有 collision 风险
* **模型匹配**：OHE 更适合线性/距离/NN；Frequency 更适合树模型（RF/XGBoost/CatBoost）

---

## 2.8 Binary Encoding（二进制编码）

### 2.8.1 核心思想（Idea）

* **CN**：先把类别映射成序号，再把序号用二进制展开成若干列（列数约为 log2(K)）。
* **EN**: Convert categories to ordinal integers then represent them in binary across multiple columns.

### 2.8.2 什么时候用（When to use）

* **CN**：基数较高、OHE 会爆列时，用 Binary 来显著降维节省内存并加速训练。
* **EN**: Use when cardinality is high and OHE would create too many columns.

### 2.8.3 优点（Pros）

* 降维省内存、训练更快
* 不像 Label 那样直接假设线性顺序（但仍引入固定数字关系，需要模型自己学）
* 相比 Frequency，能保留每个类别的唯一性（减少 collision）

### 2.8.4 缺点（Cons）

* 可解释性差（抽象的 bit 列）
* 仍可能引入“人工关系”（bit 组合之间的固定关系）
* 课件提醒：不太适合“简单线性模型”

### 2.8.5 课件例子（Example）

* Supplier 5/6 类：OHE=5/6 列；Binary=3 列更省；适合树模型与能学非线性的 NN。 

---

## 2.9 Hash Encoding（哈希编码 / Hashing trick）

### 2.9.1 核心思想（Idea）

* **CN**：把类别通过 hash 映射到固定 K 个“桶/列”，K 预先设定；适合超高基数（尤其 NLP 词表）。
* **EN**: Map categories via a hash function into a fixed number of columns (bins), ideal for very high-cardinality features (esp. NLP).

### 2.9.2 优点（Pros）

* 维度可控、内存高效（fixed dimension, memory efficient）

### 2.9.3 缺点（Cons）

* **Hash collision**：不同类别可能落到同一个桶，模型无法区分，引入噪声。

### 2.9.4 课件例子（Example）

* 选 K=3，6 个 Supplier 通过 mod 3 落桶，产生 3 组 collision（Samsung/Xiaomi、Dell/Sony、Lenovo/HP）。 

---

## 2.10 Target Encoding（目标编码 / 均值编码）

### 2.10.1 核心定义（Definition）

* **EN**: Enc(i) = Mean(Target | Category = i).

  * Binary target → proportion of positive class
  * Continuous target (e.g., price) → mean target value
* **CN**：用该类别对应的目标均值/正类比例替换类别。

### 2.10.2 为什么强（Why it’s powerful）

* **CN**：它直接把“类别与目标的关系”编码进来，往往对树模型（LightGBM/CatBoost/XGBoost）非常有效。
* **EN**: Injects category–target relationship; often very powerful in tree models.

### 2.10.3 两大风险（Two key risks）

* **Overfitting / Data leakage（泄漏与过拟合）**：小样本类别出现 1–2 次时，均值几乎等于目标本身，等于把答案塞进特征。
* **Sensitivity to noise（对噪声敏感）**：n=1 与 n=1000 被同等信任会导致高方差不稳定。

### 2.10.4 课件例子（Example）

* Category=Premium/Budget/Standard 用 Price 求均值得到 1060/373.33/425；并说明“用原始 Price 作为 target 做 mean target encoding”。 

---

## 2.11 Target Encoding 的正则化（Regularization techniques）

课件给了 3 个方法（你要能解释“怎么防泄漏”）：

### 2.11.1 Smoothing（平滑/贝叶斯均值）

* **CN**：把类别均值与全局均值混合，小样本类别更靠近全局均值（收缩），减少过拟合。
* **EN**: Blend category mean with global mean; rare categories are shrunk towards the global mean. 

**公式解释（课件版）**：

* Weight 基于类别计数（support）
* prior（平滑参数）像“伪计数”，prior 越大越信 global mean 

**数值例子**：全局均价 727，prior=3：
Premium(n=5) 从 1060 拉到 935.12；Standard(n=2) 从 425 拉到 606.2；Budget(n=3) 拉到 550.17。并解释“n 大→拉得少；n 小→拉得多”。 

### 2.11.2 K-Fold Out-of-Fold Encoding（K 折 OOF 编码，gold standard）

* **CN**：对训练集中每个样本，它的编码只用“其他折”的目标均值算，保证“该样本的 y 不会用于编码它自己”，从根本上避免泄漏。
* **EN**: Compute encoding for each observation using means from other folds only (no self-target contribution), preventing leakage. 

### 2.11.3 Adding random noise（加噪声）

* **CN**：给编码值加小高斯噪声，打破“完美对应”，迫使模型学总体趋势，提高泛化。
* **EN**: Add small Gaussian noise to break perfect relationships and improve generalization. 

### 2.11.4 category_encoders 的权重机制（Sigmoid weight）

* **CN**：库里常用 sigmoid 权重：当类别样本数 n_i 超过阈值时几乎完全信类别均值；当 n_i 太小则几乎不信（更靠近全局均值）。 

---

## 2.12 编码方法选择总结表（Encoding selection summary）

课件用同一示例表格给出了“哪一列适合哪种编码 + 理由”，你需要掌握“选择逻辑”（而不是死背列名）：

* Size → Ordinal（自然顺序）
* Color → One-hot（无序、低基数）
* Frequency/Count → nominal 且希望不增维时可用
* Supplier → Binary/Hash（中高基数、降维；Hash 可控维度但有 collision）
* Category → Target（与 Price 强相关）

---

# 3. Data / Feature Scaling（特征缩放）

## 3.1 Scaling 是什么（Definition）

* **CN**：改变特征的幅度与范围，但尽量保持分布形状（shape）。
* **EN**: Change magnitude/range while preserving distribution shape.

## 3.2 什么时候必须缩放（When scaling is needed）

* 不同数值特征的范围差异很大时：大尺度特征会压制小尺度特征。
* 目标：把特征带到可比的范围。

## 3.3 为什么缩放能提升可解释性（Interpretability in linear models）

线性模型：( y = w_1x_1 + \dots + w_nx_n + b )。

* **CN**：若 x1 范围 0–100000、x2 范围 0–1，则 w1 必须很小、w2 很大；此时不能比较 w1 与 w2 判断重要性。
* **EN**: Without scaling, coefficients live on different scales; after scaling, coefficient magnitude becomes comparable, improving interpretability. 

## 3.4 为什么缩放对距离模型关键（Distance-based algorithms）

* **CN**：KNN/SVM/K-means 基于距离；未缩放时大尺度特征主导距离，导致分类/聚类偏。缩放后各特征平等参与，准确率可显著提升（课件图对比）。
* **EN**: Scaling prevents large-magnitude features from dominating distances; improves accuracy (illustrated in plots). 

---

## 3.5 四种 scaler（定义 + 公式 + 适用 + 离群影响 + 稀疏性）

### 3.5.1 StandardScaler / Standardization（标准化）

* **公式（EN）**: (x`=(x-m)/(sigma))
* **CN**：假设近似正态；中心 0、方差 1；无固定边界；对 outlier 敏感（mean/std 会被拉）。

> 注意：recording 里写“less affected by outliers”，但 detail 的对比表明确写 **Sensitive**（因为均值/方差会被 outlier 拉动）。考试更稳的说法是：**比 MinMax 稍好，但仍会被 outlier 扭曲**。

### 3.5.2 MinMaxScaler / Normalization（归一化）

* **公式（EN）**: (x`=(x-min)/(max-min))
* **CN**：映射到固定范围（常 [0,1] 或 [-1,1]）；适合需要 bounded input 的模型（某些神经网络、像素数据）；对 outlier 极度敏感（一个极端值会把其他值都“挤扁”）。

### 3.5.3 RobustScaler（鲁棒缩放）

* **公式（EN）**: (x=(x-median)/IQR),   where IQR=Q3-Q1
* **CN**：用中位数与 IQR（25%~75%）缩放；强抗 outlier；适合“有极端值但不想删”的数据。

### 3.5.4 MaxAbsScaler（最大绝对值缩放）

* **公式（EN）**: x`=x/max(|x|)
* **EN/CN**：按最大绝对值缩放到 [-1,1]；特别适合稀疏数据（文本/NLP），**保持 0 仍为 0（zero preservation / preserves sparsity）**；但对极端最大值敏感。

### 3.5.5 课件对比表你必须会（Exam-friendly table）

课件按 “Best suited / Mechanism / Impact on outliers / Preserves sparsity” 对比四种 scaler。

### 3.5.6 图示理解（Standard vs MinMax vs Robust vs MaxAbs）

detail 版用散点图展示四种缩放的几何效果：Standard 以均值中心化；MinMax 压到盒子；Robust 以 median/IQR；MaxAbs 不中心化且保 0。 

### 3.5.7 property tax 数据的选择建议（Use case summary）

detail 版以 property tax 举例总结：

* StandardScaler：线性模型/SVM/PCA 默认选择但对 outlier 敏感
* MinMax：NN/图像，但 outlier 会“挤压”
* Robust：极端 outlier 多、但不想删
* MaxAbs：稀疏文本，保 0 

---

# 4. Power Transformation（幂变换）与 Skewness（偏度）

## 4.1 为什么需要幂变换（Why needed）

* **CN**：很多算法假设特征接近高斯；现实数据常偏态/重尾/方差不恒定。幂变换把数据映射到更接近正态，降低长尾极端值影响，并缓解异方差（heteroscedasticity）。
* **EN**: Power transforms map distributions closer to Gaussian, reduce tail/outlier influence, and stabilize variance (heteroscedasticity).

## 4.2 Skewness 定义与三种形态（Definition & types）

* **EN**: Skewness measures distribution asymmetry around the mean.
* **CN**：偏度描述分布是否“向某一侧倾斜”。

三种类型 + 修复方法（课件表）：

* **Right/Positive skew（右偏）**：右长尾；用 log/开方/取根修复；例：收入、房价、里程。
* **Left/Negative skew（左偏）**：左长尾；用平方/立方等幂修复；例：退休年龄、考试分数（大多数及格）。
* **Zero skew（对称）**：钟形；例：身高、标准化产品重量。

## 4.3 Box-Cox vs Yeo-Johnson（两种 Power transform）

* **Box-Cox（EN）**：拟合 λ，把特征变得更接近正态；**仅适用于正数**。
* **Yeo-Johnson（EN）**：可处理正/零/负。

## 4.4 何时使用 + 哪些模型收益最大（When to use & who benefits）

* **Use when（EN）**：强偏态、非恒定方差、重尾、线性模型因非正态而表现差。 
* **Models that benefit（EN）**：Linear Regression、Logistic Regression、KNN、其他距离模型。 

---

# 5. Advanced Feature Engineering（进阶特征工程）

## 5.1 Derived Features（派生特征）

* **CN**：从已有列构造更有意义的特征，如 DOB→Age，Price/Area→Price per SqFt。
* **EN**: Create new informative features from existing ones (Age from DOB; Price per SqFt).

## 5.2 Text Feature Extraction（文本特征）

* **TF-IDF（EN/CN）**：衡量词在文档 vs 语料中的重要性（越“文档特有”权重越高）。
* **Word2Vec（EN/CN）**：学习稠密向量，捕捉语义关系。

## 5.3 Dimensionality Reduction（降维）

* **PCA（EN/CN）**：在保留主要方差的前提下降低复杂度。

---

# 6. Bias（偏差）对公平与泛化的影响

## 6.1 Bias 对 Fairness 的影响（Bias → fairness）

四类偏差（你要会定义 + 例子）：

* **Historical bias**：历史不平等被数据继承（过去招聘偏向男性）。
* **Sampling bias**：某些群体样本不足（人脸识别对深色皮肤差）。
* **Label bias**：标签本身不公/受人类判断偏差影响（贷款违约标签来自偏见审批系统）。
* **Measurement bias**：不同群体测量方式不同（医疗设备对不同人群准确度不同）。

## 6.2 公平性后果（Consequences on fairness）

* 不同群体错误率不一样（Unequal error rates）
* 自动化决策歧视（招聘/贷款/保险/执法）
* 信任与伦理问题
* 法律合规风险（GDPR、公平性指南等）

## 6.3 Bias 对模型泛化的影响（Bias → generalization）

* **Overfitting to dominant groups**：过度适配主导群体，其他群体表现差（成人医疗模型对儿童失效）。
* **Poor feature learning / shortcuts**：学到捷径（wolf vs dog 用雪背景）。
* **Domain shift**：训练环境单一（自动驾驶只在晴天训练，雨夜失败）。
* **Algorithmic bias**：算法假设过于简化（用线性模型拟合非线性现实）。

## 6.4 降低偏差、提升公平与泛化（How to reduce bias）

* 提升数据多样性
* 平衡采样与重加权
* 公平标注
* 公平算法（fairness-aware algorithms）
* 跨群体评估指标：FPR/FNR、demographic parity
* 定期审计与检测工具
* 高风险决策 human-in-the-loop

---

# 7. Bias Mitigation Techniques（偏差缓解技术：预处理为主）

## 7.1 预处理（Pre-processing: intervene on data）

* **CN**：在喂给模型前先改训练数据，减少/消除偏差。
* **EN**: Modify training data before model training to reduce bias.

## 7.2 Reweighing / Re-sampling（重加权/重采样）

* **CN**：对“弱势群体 + 不利结果”的样本赋更高权重，对过度代表的样本赋更低权重，用于实现 statistical/demographic parity。
* **EN**: Upweight underrepresented/unprivileged unfavorable-outcome samples; downweight overrepresented ones to achieve parity.

**优缺点（Pros & Cons）**

* Pros：模型无关、实现概念简单
* Cons：不改变特征，因此 proxy bias 仍可能存在；可能导致对少数群体过拟合 

## 7.3 Oversampling（过采样）

* **CN**：识别少数群体/少数结果；复制或合成样本直到更平衡；用于推动统计/人口平等，让模型不只为多数群体优化。
* **EN**: Duplicate/synthesize minority samples to balance class/group representation and reduce majority bias.

## 7.4 SMOTE（合成少数类过采样）

* **CN**：在两个相近的少数类点之间做插值生成新点，帮助模型更好学习少数类边界，避免简单复制导致过拟合。
* **EN**: Create synthetic points by interpolation between nearest minority neighbors; better boundary learning than naive duplication. 

**Pros & Cons**

* Pros：算法无关；减少“忽略少数类”；比复制更能泛化
* Cons：若少数类本就在边界附近，可能生成噪声/加重重叠，偏离真实分布 

## 7.5 SMOTE 变体（ADASYN / SMOTE-ENN）

* **ADASYN**：对“难学的少数类点”（被多数类包围）生成更多样本，推动边界更贴近多数类；但对噪声敏感，可能增加重叠。 
* **SMOTE-ENN**：先 SMOTE 再用 ENN 删除噪声/重叠点（含两类），边界更干净但更复杂，且会删除原始点。 

---

# 8. Conclusion（结论与关键 takeaway）

* **CN**：特征工程既是科学也是艺术，需要领域知识与实验。更好的特征常常比更复杂的模型更有效。按“算法类型 + 数据分布”选择编码/缩放/变换。
* **EN**: Feature engineering is both art and science; better features yield better models; choose encoding/scaling based on algorithm and data distribution.

---
