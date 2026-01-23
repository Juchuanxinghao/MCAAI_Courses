下面是一份 **Week 2 模拟 Exercise/Mock Quiz（全英文题目）**，题型与评分规则完全沿用你 Week1 的要求：**闭卷、客观题（单选/多选/填空）、多选倒扣、25–30 题、总分 45 分**。并且覆盖 Week2 课件全部核心知识点范围：**Encoding（OHE/Frequency/Binary/Hash/Target + 选型）、Scaling（4 scalers + 适用场景 + interpretability + distance-based）、Power Transform（skewness + Box-Cox vs Yeo-Johnson + 何时使用）、Advanced FE（derived/NLP/PCA）、Bias & Mitigation（4 类 bias、公平性与泛化影响、Reweighing/Oversampling/SMOTE/ADASYN/SMOTE-ENN + trade-off + proxy bias）**。

---

# Week 2 Mock Exercise / Quiz — Feature Engineering + Bias Mitigation (45 points)

**Instructions (English):**

* Closed book, no resources.
* Total: **27 questions**, **45 points**.
* Types: Single-choice, Multiple-answer (negative marking), Fill-in-the-blank.
* **Multiple-answer scoring rule (per question, 3 pts):**
  +1 for each correct option selected, **−1 for each incorrect option selected**, min 0, max 3.
  (Select **ALL** that apply.)

---

## Part A — Single-choice (18 questions × 1 point = 18 points)

### Q1 (1 pt)

What is the primary goal of **feature engineering**?
A. To guarantee causal relationships
B. To transform raw data into model-friendly features that improve learning
C. To remove all categorical variables
D. To always increase the number of features

**中文答案：B**
**解析：**特征工程的核心是把原始数据通过**编码、缩放、变换、派生**变得更适合模型学习与泛化，并不等于“越多特征越好”。

---

### Q2 (1 pt)

Which encoding is most appropriate for an **ordinal** feature (e.g., Small < Medium < Large)?
A. One-hot encoding
B. Ordinal/Label encoding
C. Hash encoding
D. Target encoding

**中文答案：B**
**解析：**有自然顺序的类别应使用 **Ordinal/Label** 来保留顺序信息；OHE 会丢失顺序。

---

### Q3 (1 pt)

Which encoding is typically best for a **low-cardinality nominal** feature (e.g., Color with 4 categories)?
A. One-hot encoding
B. Target encoding
C. Binary encoding
D. PCA

**中文答案：A**
**解析：**低基数无序类别最适合 OHE：不引入虚假顺序且可解释性强。

---

### Q4 (1 pt)

A major drawback of **one-hot encoding** for high-cardinality features is:
A. It creates artificial ordering
B. It leads to dimensionality explosion and sparse matrices
C. It cannot handle nominal variables
D. It always causes leakage

**中文答案：B**
**解析：**高基数用 OHE 会产生大量列，带来维度爆炸与稀疏矩阵开销。

---

### Q5 (1 pt)

Which statement best describes **frequency (count) encoding**?
A. Replace categories with random integers
B. Replace categories with their occurrence count or frequency
C. Create a binary column for each category
D. Use the target variable mean directly without risk

**中文答案：B**
**解析：**Frequency/Count 用出现次数或频率替换类别，优点是不增维，但可能出现 **collision（不同类别同频率）**。

---

### Q6 (1 pt)

Which encoding most directly introduces **hash collisions** by design?
A. Target encoding
B. Hash encoding
C. Ordinal encoding
D. One-hot encoding

**中文答案：B**
**解析：**Hash encoding 将类别映射到固定桶数，天然存在 collision 风险。

---

### Q7 (1 pt)

Which encoding usually produces about **log2(K)** columns for K categories?
A. Binary encoding
B. One-hot encoding
C. Frequency encoding
D. Label encoding

**中文答案：A**
**解析：**Binary encoding 将类别编号转为二进制位展开，列数约为 log2(K)。

---

### Q8 (1 pt)

What is the key idea of **target encoding**?
A. Replace each category with the global mean of the target
B. Replace each category with the mean of the target conditioned on that category
C. Replace each category with its one-hot vector
D. Replace each category with its hash bucket index only

**中文答案：B**
**解析：**Target encoding 用 **E[target | category]** 编码，强但易泄漏/过拟合。

---

### Q9 (1 pt)

Which practice best prevents **target leakage** when using target encoding on the training set?
A. Fit target encoding on the full dataset before splitting
B. Use K-fold out-of-fold target encoding
C. Use one-hot encoding instead
D. Always add more noise without validation

**中文答案：B**
**解析：**OOF target encoding：每个样本的编码只能由“其他折”统计得到，避免把自身 y 泄漏进特征。

---

### Q10 (1 pt)

Which scaler is most robust to outliers?
A. MinMaxScaler
B. StandardScaler
C. RobustScaler
D. PCA

**中文答案：C**
**解析：**RobustScaler 用 median 与 IQR，抗 outlier 能力最强。

---

### Q11 (1 pt)

Which scaler **preserves sparsity** (keeps zeros as zeros), making it suitable for sparse text features?
A. MaxAbsScaler
B. StandardScaler
C. MinMaxScaler
D. RobustScaler

**中文答案：A**
**解析：**MaxAbsScaler 适合稀疏数据，0 仍为 0（preserves sparsity）。

---

### Q12 (1 pt)

Why is scaling critical for **distance-based** algorithms like KNN or SVM (RBF)?
A. They require categorical inputs
B. Large-scale features dominate distances without scaling
C. Scaling increases the number of samples
D. Scaling guarantees fairness

**中文答案：B**
**解析：**距离模型依赖距离度量，不缩放会让大尺度特征主导距离，导致偏差与性能下降。

---

### Q13 (1 pt)

In a linear model, scaling helps interpretability because:
A. It makes the model nonlinear
B. Coefficients become comparable across features on similar scales
C. It removes multicollinearity completely
D. It turns ordinal variables into nominal

**中文答案：B**
**解析：**缩放后特征尺度统一，系数大小才更可比较（“影响力”更可解释）。

---

### Q14 (1 pt)

Which statement about **MinMax scaling** is most accurate?
A. It is robust to outliers
B. It maps data to a bounded range (e.g., [0, 1])
C. It preserves sparsity perfectly
D. It uses median and IQR

**中文答案：B**
**解析：**MinMax 将数据压到固定区间，但对 outlier 极敏感（极端值会挤压其他样本）。

---

### Q15 (1 pt)

What is **skewness**?
A. The number of missing values
B. A measure of distribution asymmetry
C. The correlation between two variables
D. The variance of the target variable

**中文答案：B**
**解析：**Skewness 衡量分布相对均值的偏斜程度。

---

### Q16 (1 pt)

Which transformation is commonly used to reduce **right (positive) skew**?
A. Squaring
B. Log transform
C. One-hot encoding
D. StandardScaler only

**中文答案：B**
**解析：**右偏常用 log / sqrt / root 来压缩右长尾。

---

### Q17 (1 pt)

Which statement is correct about **Box-Cox vs Yeo-Johnson**?
A. Box-Cox can handle negative values
B. Yeo-Johnson can handle zero/negative values
C. Both require strictly positive inputs
D. Neither can reduce skewness

**中文答案：B**
**解析：**Box-Cox 仅正数；Yeo-Johnson 可处理正/零/负。

---

### Q18 (1 pt)

Which bias type is best described as “dataset underrepresents certain groups”?
A. Measurement bias
B. Sampling bias
C. Label bias
D. Historical bias

**中文答案：B**
**解析：**Sampling bias：采样/收集过程中某些群体样本不足，导致系统性偏差。

---

## Part B — Multiple-answer (6 questions × 3 points = 18 points)

**Select ALL that apply. Negative marking applies.**

### Q19 (3 pts)

Which encodings are typically appropriate for **high-cardinality nominal** features?
A. One-hot encoding
B. Frequency/Count encoding
C. Binary encoding
D. Hash encoding
E. Target encoding (with regularization)

**中文答案：B, C, D, E**
**解析：**高基数不适合 OHE（维度爆炸）。可选 Frequency（不增维但 collision）、Binary（降维）、Hash（固定维度但 collision）、Target（强但需正则化防泄漏）。

---

### Q20 (3 pts)

Which statements about **target encoding risks and fixes** are correct?
A. Target encoding can leak target information and overfit small categories
B. Smoothing shrinks category means toward the global mean, especially for rare categories
C. K-fold out-of-fold encoding reduces leakage
D. Adding small random noise can help generalization
E. Target encoding is always safer than one-hot encoding

**中文答案：A, B, C, D**
**解析：**E 错：target encoding风险更高；其余均为课件重点：泄漏/过拟合 + smoothing/OOF/noise 解决。

---

### Q21 (3 pts)

Which statements about scaling are correct?
A. Scaling is crucial for KNN/K-means/SVM with distance kernels
B. Scaling can improve gradient-based optimization convergence
C. Scaling makes correlation become causation
D. RobustScaler is less affected by outliers than MinMaxScaler
E. MaxAbsScaler preserves sparsity (zeros stay zero)

**中文答案：A, B, D, E**
**解析：**C 错：缩放不改变因果；其余为 Week2 高频点。

---

### Q22 (3 pts)

Which statements about **power transformations** are correct?
A. They can reduce skewness and make data more Gaussian-like
B. They can help when variance is non-constant (heteroscedasticity)
C. They are only useful for categorical variables
D. Box-Cox requires strictly positive inputs
E. Yeo-Johnson can handle negative values

**中文答案：A, B, D, E**
**解析：**幂变换用于数值特征；C 错。

---

### Q23 (3 pts)

Which are common **bias types** discussed in Week 2?
A. Historical bias
B. Sampling bias
C. Label bias
D. Measurement bias
E. Hash collision bias

**中文答案：A, B, C, D**
**解析：**前四个是课件定义的核心 bias 类型；E 属于编码碰撞问题，不是 fairness bias 分类。

---

### Q24 (3 pts)

Which statements about **pre-processing bias mitigation** are correct?
A. Reweighing changes sample importance weights to reduce representation imbalance
B. Oversampling duplicates/synthesizes minority samples to balance distribution
C. SMOTE generates synthetic samples via interpolation between minority neighbors
D. ADASYN generates more samples in “hard-to-learn” regions near the decision boundary
E. SMOTE-ENN combines SMOTE with cleaning noisy/overlapping points

**中文答案：A, B, C, D, E**
**解析：**全对。注意：这些方法多用来解决不平衡/代表性问题，但仍可能存在 proxy bias 风险。

---

## Part C — Fill in the blanks (3 questions × 3 points = 9 points)

### Q25 (3 pts)

Fill in the StandardScaler formula:
( x' = __________________ )

**中文答案：** ( x' = \dfrac{x-\mu}{\sigma} )
**解析：**标准化=减均值除标准差，使均值约 0、标准差约 1。

---

### Q26 (3 pts)

Fill in the MinMaxScaler formula (range scaling):
( x' = __________________ )

**中文答案：** ( x' = \dfrac{x-\min(x)}{\max(x)-\min(x)} )
**解析：**映射到 [0,1]（或再线性变换到其他区间）；对极端值敏感。

---

### Q27 (3 pts)

Complete the target encoding definition:
For category (c), the target encoding is:
( Enc(c) = __________________ )

**中文答案：** ( Enc(c) = \mathbb{E}[y \mid x=c] )（即该类别对应的目标均值/正类比例）
**解析：**把“类别与目标的统计关系”直接注入特征，强但需正则化与防泄漏。

---

# Chinese Answer Key (简表)

* 单选：1B 2B 3A 4B 5B 6B 7A 8B 9B 10C 11A 12B 13B 14B 15B 16B 17B 18B
* 多选：19 BCDE；20 ABCD；21 ABDE；22 ABDE；23 ABCD；24 ABCDE
* 填空：25 ((x-\mu)/\sigma)；26 ((x-\min)/(\max-\min))；27 (E[y|x=c])

---

如果你想让它更贴近老师练习题的“操作型问法”，我也可以再给你一个 **Week2 Practical Exercise 版本**（仍是客观题风格）：

* 给一个小表（类别列 + 目标列 + 数值列），让你判断用哪种 encoding/scaler/transform，并识别泄漏点；
* 以及公平性场景（银行贷款/招聘）让你选择用 reweighing/SMOTE/SMOTE-ENN 的理由与 trade-off。
