# 第2章完整复习资料（中英文双语）

## Chapter 2: Feature Engineering — Encoding, Scaling, and Bias Mitigation

---

## 0) 本章定位 | Why this chapter matters

**中文**
这一章讲的是“如何把原始特征变成模型真正能学、能泛化、能公平使用的特征”。核心三块：

1. 类别变量编码（Encoding）
2. 数值变量缩放与分布变换（Scaling + Power Transform）
3. 偏差与公平性（Bias, Fairness, Mitigation）

**English**
This chapter is about turning raw features into model-ready, generalizable, and fair representations through:

1. Categorical encoding
2. Numerical scaling and distribution transformation
3. Bias/fairness diagnosis and mitigation

---

## 1) Data Encoding（类别数据编码）

---

## 1.1 为什么要编码 | Why encoding is required

**中文**
大多数机器学习算法要求数值输入。类别数据（如颜色、国家、供应商）必须先转换为数值表示。编码方法的选择主要由变量类型决定：

* **Nominal（无序类别）**
* **Ordinal（有序类别）**

**English**
Most ML algorithms need numeric inputs. Categorical variables must be encoded. The key decision depends on whether the feature is:

* **Nominal** (no intrinsic order)
* **Ordinal** (ordered categories)

---

## 1.2 编码方法总览 | Encoding methods overview

课件给出的主要方法：

* Label/Ordinal Encoding
* One-Hot Encoding
* Count/Frequency Encoding
* Binary Encoding
* Target Encoding
* Hash Encoding

---

## 1.3 Label / Ordinal Encoding（有序编码）

### 定义 | Definition

 **中文** ：把有序类别映射成有序整数（例如 Small=1, Medium=2, Large=3）。
 **English** : Map ordered categories to ranked integers.

### 适用场景 | When to use

* 类别有天然顺序（size、education level、risk level）

### 优点 | Pros

* 简单、内存友好、保留顺序信息

### 缺点 | Cons

* 如果变量本来无序，会引入“假顺序”和“假线性关系”

### 课件例子 | Slide example

* `Size` 非常适合做 ordinal encoding（Small < Medium < Large）。

---

## 1.4 One-Hot Encoding（独热编码）

### 定义 | Definition

 **中文** ：每个类别生成一个0/1列。
 **English** : Create one binary indicator column per category.

### 适用场景 | When to use

* Nominal + 低基数（low cardinality）

### 优点 | Pros

* 不会人为引入顺序
* 对线性模型、逻辑回归、SVM、KNN等常见模型友好
* 可解释性强

### 缺点 | Cons

* 高基数时维度爆炸（稀疏、耗内存、耗算力）
* dummy variable trap（多重共线性风险）

### 课件例子 | Slide example

* `Color`（5类）适合 One-Hot。

---

## 1.5 Count / Frequency Encoding（频数/频率编码）

### 定义 | Definition

* Count：用类别出现次数替代类别
* Frequency：用类别占比替代类别

### 适用场景 | When to use

* Nominal + 中高基数，且想控制维度增长

### 优点 | Pros

* 不增加列数（维度友好）
* 能表达“稀有 vs 常见”信息
* 未见类别可给默认频率（如0）

### 缺点 | Cons

* 不同类别若频率相同，会“碰撞”成同值，信息损失

### 课件提醒 | Key note

* 频率编码常用于树模型（RF/XGBoost/CatBoost）。

---

## 1.6 Binary Encoding（二进制编码）

### 核心思想 | Core idea

先把类别映射成整数，再转二进制位展开成多个列。

### 适用场景 | When to use

* 高基数（比 OHE 更省维度）

### 优点 | Pros

* 减少列数、节省内存
* 相比频率编码更少“同值碰撞”
* 对树模型/神经网络常可用

### 缺点 | Cons

* 可解释性变差（bit列抽象）
* bit模式可能引入人工结构
* 对“简单线性模型”不总是最佳

### 课件例子 | Slide example

* `Supplier` 可用 binary encoding（中高基数时更合适）。

---

## 1.7 Hash Encoding（哈希编码）

### 定义 | Definition

用哈希函数把海量类别映射到固定K个桶（固定列数）。

### 适用场景 | When to use

* 超高基数（尤其 NLP / 大词表）

### 优点 | Pros

* 列数可控、内存友好、可扩展

### 缺点 | Cons

* **Hash collision（哈希碰撞）** ：不同类别映到同一桶，模型无法区分

### 课件例子 | Slide example

* Supplier 6类映到K=3时，出现多个碰撞示意。

---

## 1.8 Target Encoding（目标编码）

### 定义 | Definition

对类别 (i) 编码为该类别对应目标变量均值：
[
Enc(i)=\mathbb{E}[\text{Target} \mid \text{Category}=i]
]

**中文**

* 二分类目标：编码值≈该类别正类比例
* 连续目标：编码值≈该类别目标均值（如平均价格）

**English**

* Binary target: encoded value is positive-class rate
* Continuous target: encoded value is category-wise target mean

### 优点 | Pros

* 对高基数类别很强
* 与目标关系强时效果显著（常用于树模型）

### 缺点 | Cons（考试高频）

* **过拟合风险** （小样本类别均值不稳定）
* **数据泄漏风险** （目标信息“泄漏”到特征）

### 课件 mitigation（必须会）

1. **Smoothing（平滑）**
2. **K-fold Out-of-Fold encoding（黄金标准）**
3. **Add random noise（少量噪声）**

---

## 1.9 Smoothing Target Encoding（平滑目标编码）

### 公式 | Formula

# [

\text{SmoothedMean}_i

\frac{n_i \mu_i + m\mu_{global}}{n_i + m}
]

* (n_i): 类别样本数
* (\mu_i): 类别目标均值
* (\mu_{global}): 全局目标均值
* (m): prior / smoothing strength

### 直觉 | Intuition

* 类别样本越少，越“拉向全局均值”
* 类别样本越多，越接近本类别原始均值

### 课件示例结论

* 高样本类别（Premium）拉动较小
* 低样本类别（Standard）拉动更大，更稳定、抗过拟合。

---

## 1.10 Nominal 编码选择对比（考点表）

| 场景                  | 推荐                               |
| --------------------- | ---------------------------------- |
| 低基数 nominal        | One-Hot                            |
| 高基数 nominal        | Frequency / Binary / Hash / Target |
| 与目标关系强          | Target Encoding                    |
| 极高词表（NLP）       | Hash Encoding                      |
| 强调可解释性 + 低基数 | One-Hot                            |

（课件也给出 OHE vs Frequency 的适配模型对比：线性/距离模型 vs 树模型）

---

## 2) Feature Scaling（特征缩放）

---

## 2.1 为什么要做缩放 | Why scaling is needed

**中文**
缩放改变数值尺度，但不改变分布形状的“相对结构”。当不同特征量纲差异很大时，不缩放会导致大数值特征主导模型。
尤其影响：

* 距离类算法（KNN, SVM, KMeans）
* 梯度优化收敛速度
* 线性模型系数可比性（interpretability）

**English**
Scaling aligns feature magnitudes so that no single large-scale feature dominates distance or optimization. It improves fairness of contribution and convergence.

---

## 2.2 四种常见缩放器 | 4 common scalers

---

### 2.2.1 StandardScaler（标准化）

[
x'=\frac{x-\mu}{\sigma}
]

* 均值0、方差1，**无固定上下界**
* 假设更接近高斯分布
* 对离群值敏感（均值和标准差会被拉动）

---

### 2.2.2 MinMaxScaler（归一化）

[
x'=\frac{x-\min(x)}{\max(x)-\min(x)}
]

* 映射到固定区间（通常 [0,1]）
* 对输入范围有要求的模型常用（部分神经网络）
* 对离群值非常敏感（一个极端值会压扁其余样本）

---

### 2.2.3 RobustScaler（稳健缩放）

[
x'=\frac{x-\text{median}}{\text{IQR}}
]

* 中位数+IQR，抗离群值
* 适合“脏数据/重尾数据/明显异常值”

---

### 2.2.4 MaxAbsScaler

[
x'=\frac{x}{\max(|x|)}
]

* 最大绝对值缩放到1
* **保留0（zero-preserving）** ，适合稀疏数据（文本特征）
* 仍对离群值敏感

---

## 2.3 Scaler 选型口诀 | Scaler selection cheatsheet

* 近高斯 + 一般场景：**StandardScaler**
* 有固定边界需求：[0,1]：**MinMaxScaler**
* 异常值多：**RobustScaler**
* 稀疏矩阵/NLP：**MaxAbsScaler**

---

## 3) Power Transformation（幂变换）

---

## 3.1 为什么需要 | Why needed

**中文**
很多参数模型对“正态性/方差稳定”更友好。现实数据常偏态、重尾、异方差，影响模型拟合。幂变换的目标是把分布拉向更对称、近似高斯。

**English**
Power transforms reduce skewness/heavy tails and stabilize variance, often improving performance in parametric models.

---

## 3.2 偏度（Skewness）

* 正偏（右长尾）：常用 log / root 类变换
* 负偏（左长尾）：可考虑幂次变换（平方/立方等，按数据方向）
* 零偏：近对称钟形分布

---

## 3.3 Box-Cox vs Yeo-Johnson

* **Box-Cox** ：仅适用于正值
* **Yeo-Johnson** ：可处理正/零/负值（更通用）

---

## 3.4 什么时候用幂变换 | Use cases

* 强偏态（尤其右偏）
* 非恒定方差（heteroscedasticity）
* 重尾分布
* 线性模型表现差且怀疑非正态导致时
* KNN/距离模型也常受益（距离结构更均衡）

---

## 4) Advanced Feature Engineering（扩展特征工程）

* 派生特征：DOB→Age，Price/Area→PricePerSqFt
* 文本特征：TF-IDF，Word2Vec
* 降维：PCA（保留主要方差信息同时降复杂度）

---

## 5) Bias, Fairness, and Generalization（偏差、公平与泛化）

---

## 5.1 偏差类型 | Types of bias

1. **Historical bias** ：历史不平等被数据继承
2. **Sampling bias** ：某些群体样本不足
3. **Label bias** ：标签本身带偏见
4. **Measurement bias** ：不同群体测量误差不同

---

## 5.2 对公平性的影响 | Fairness impact

* 不同群体错误率不均（FPR/FNR 差异）
* 自动化决策歧视（招聘、贷款、保险等）
* 信任下降、伦理风险、合规风险（如 GDPR）

---

## 5.3 对泛化的影响 | Generalization impact

* 对主导群体过拟合
* 学到“捷径特征”（spurious correlations）
* 域迁移失败（train环境单一，test环境变化即崩）
* 算法假设过于简化导致外推差

---

## 5.4 缓解方法 | Mitigation methods

### 总体策略

* 提升数据多样性
* 平衡采样/重加权
* 公平标注流程
* 公平感知算法
* 分组评估（FPR/FNR/DP）
* 审计与人工复核（high-risk decisions）

### 预处理技术（课件重点）

1. **Reweighing/Re-sampling** ：给受保护/弱势群体更高权重
2. **Oversampling** ：补齐少数群体样本
3. **SMOTE** ：少数类插值合成（比纯复制更不易过拟合）
4. **ADASYN** ：更关注“难学”边界样本
5. **SMOTE-ENN** ：先合成再清噪，边界更清晰

---

## 6) Chapter 2 高频易错点（考试必看）

1. **Nominal 用 Label Encoding** （通常错，除非真有序）
2. **Target Encoding 不做 OOF / Smoothing** （高风险泄漏+过拟合）
3. **MinMax 对离群值不敏感** （错，它很敏感）
4. **StandardScaler 有固定范围 [0,1]** （错，无固定范围）
5. **MaxAbs 会改变0** （错，0保持0）
6. **Hash encoding 无信息损失** （错，有 collision）
7. **公平=总体准确率高** （错，公平要看分组指标）

---

# Chapter 2 Quiz（混合题型，含答案与解析）

---

## A) Single Choice（单选）

**Q1.** Which encoding is most appropriate for an ordinal feature like `Size: Small < Medium < Large`?
A. One-Hot
B. Label/Ordinal Encoding
C. Hash Encoding
D. Target Encoding
**Answer: B**

* 中：有序变量应保留顺序。
* EN: Ordinal relationships should be preserved.

---

**Q2.** Which scaler is most robust to outliers?
A. MinMaxScaler
B. StandardScaler
C. RobustScaler
D. MaxAbsScaler
**Answer: C**

---

**Q3.** Which statement about Hash Encoding is correct?
A. It avoids collisions completely
B. It always improves interpretability
C. It maps categories into fixed-size feature space
D. It is only for ordinal variables
**Answer: C**

---

## B) Fill in the Blanks（填空）

**Q4.** Target encoding for category (i):
[
Enc(i)=\text{Mean}(____ \mid Category=i)
]
**Answer:** Target

**Q5.** RobustScaler uses ______ and ______ to reduce outlier influence.
**Answer:** median, IQR

**Q6.** Box-Cox can only be applied to ______ values.
**Answer:** positive

---

## C) Multiple Answers（多选）

**Q7.** Which are valid risks of One-Hot Encoding on high-cardinality features?
A. Dimensionality explosion
B. Sparse matrix issues
C. Guaranteed collision
D. Higher memory and computation cost
**Answer:** A, B, D

* 中：碰撞是 hash/frequency 更常见风险，不是 OHE 本质。
* EN: OHE risks high dimensionality/sparsity, not hash-like collision.

---

**Q8.** Which are common mitigation techniques for target encoding overfitting/leakage?
A. Smoothing
B. K-Fold Out-of-Fold encoding
C. Add small random noise
D. Fit on full train+test target together
**Answer:** A, B, C

---

## D) Matching（匹配）

Match each method with best scenario:

1. One-Hot
2. Frequency
3. Binary
4. Target
5. Hash

a. very high-cardinality vocabulary, fixed output dimension
b. low-cardinality nominal feature with high interpretability
c. medium/high cardinality, fewer columns than OHE
d. high-cardinality nominal with relation to target
e. keep one numeric column, possible collision for equal frequencies

**Answer:** 1-b, 2-e, 3-c, 4-d, 5-a

---
