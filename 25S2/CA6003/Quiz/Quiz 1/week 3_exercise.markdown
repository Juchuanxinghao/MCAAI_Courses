下面是一份 **Week 3 模拟 Exercise/Mock Quiz（全英文题目）**，严格沿用你前面的要求：**闭卷、客观题（单选/多选/填空）、多选倒扣、25–30题、总分45分**。
覆盖 Week3 两份课件的所有核心考点：

* **Imbalanced data & SMOTE（算法步骤、影响、公平性/安全性 trade-off、指标选择）**
* **Dimensionality Reduction（Feature Selection vs Extraction；PCA/SVD/t-SNE/Autoencoder 对比；PCA 优缺点与解释性风险；何时用降维）**
* **EDA Summary（House Prices）完整流程：inspection → summary → cleaning → missing semantics（None/0）→ type split → outliers → skew fix → scaling → encoding → univariate/bivariate/multivariate → derived features → pipelines → key takeaways**

---

# Week 3 Mock Exercise / Quiz — Bias Mitigation + Dimensionality Reduction + EDA (45 points)

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

In class-imbalanced classification (e.g., fraud detection), which metric is most likely to be **misleading** if used alone?
A. Recall
B. Precision
C. Accuracy
D. F1-score

**中文答案：C**
**解析：**不平衡时 Accuracy 可能很高但模型完全忽略少数类（全预测多数类也能高分）。

---

### Q2 (1 pt)

What is the key idea behind **SMOTE**?
A. Randomly delete majority samples
B. Duplicate minority samples exactly
C. Generate synthetic minority samples by interpolation between neighbors
D. Add Gaussian noise to all features for fairness

**中文答案：C**
**解析：**SMOTE 在少数类样本与其少数类近邻之间做插值生成新样本，不是简单复制。

---

### Q3 (1 pt)

SMOTE primarily aims to reduce which type of problem?
A. Multicollinearity
B. Class imbalance (representation bias toward majority class)
C. Label noise in the target
D. Feature scaling issues

**中文答案：B**
**解析：**SMOTE 主要用于类别不平衡，提升少数类代表性，缓解决策边界偏向多数类。

---

### Q4 (1 pt)

After applying SMOTE, which change is most commonly expected?
A. Minority recall increases, but precision may decrease
B. Accuracy always increases
C. Minority recall decreases
D. No change in decision boundary

**中文答案：A**
**解析：**SMOTE 常带来 Recall↑（少数类更容易被识别），但可能 Precision↓ / Accuracy↓，这属于预期 trade-off。

---

### Q5 (1 pt)

Which statement about SMOTE and fairness is most accurate?
A. SMOTE guarantees equal error rates across all groups
B. SMOTE can reduce decision boundary bias toward the majority class
C. SMOTE always eliminates historical bias
D. SMOTE replaces the need for evaluation metrics

**中文答案：B**
**解析：**SMOTE通过提升少数类代表性，常使边界更不偏向多数类；但它不“保证”所有公平指标都满足。

---

### Q6 (1 pt)

What is **dimensionality reduction** mainly used for?
A. Increasing feature count to improve accuracy
B. Reducing features while preserving useful information
C. Converting numeric features into text
D. Preventing data leakage by default

**中文答案：B**
**解析：**降维目标是减少维度但尽量保留信息：加速训练、减少噪声冗余、帮助可视化。

---

### Q7 (1 pt)

Which option correctly distinguishes feature selection and feature extraction?
A. Selection creates new features; extraction drops features
B. Selection keeps a subset of original features; extraction transforms into new low-dimensional features
C. Both always require labels
D. Both are only for images

**中文答案：B**
**解析：**Selection=选子集；Extraction=变换到新空间（PCA/SVD/t-SNE/Autoencoder）。

---

### Q8 (1 pt)

Which method is a **linear**, unsupervised feature extraction technique aimed at maximizing explained variance?
A. PCA
B. t-SNE
C. DBSCAN
D. SMOTE-ENN

**中文答案：A**
**解析：**PCA 通过主成分最大化方差解释，是线性无监督降维。

---

### Q9 (1 pt)

Which dimensionality reduction method is mainly used for **visualization** and preserving local neighborhoods, but is often slow and hyperparameter-sensitive?
A. PCA
B. t-SNE
C. StandardScaler
D. One-hot encoding

**中文答案：B**
**解析：**t-SNE 非线性强、可视化很强，但慢且对参数敏感，不适合生产建模特征。

---

### Q10 (1 pt)

Which statement about PCA interpretability is most correct?
A. PCA components are always directly interpretable as original features
B. PCA can reduce interpretability because components are mixtures of original features
C. PCA preserves semantics of each original feature
D. PCA is required for fairness

**中文答案：B**
**解析：**PCA 生成的主成分是原特征的线性组合，往往难以解释（特别在金融/医疗等强解释场景）。

---

### Q11 (1 pt)

In House Prices EDA, many NaN values (e.g., garage-related) often mean:
A. Random sensor failure
B. “The attribute does not exist” (e.g., no garage), not “unknown”
C. The data is always corrupted
D. The target is missing

**中文答案：B**
**解析：**很多 NaN 是“没有该结构”（如没有车库/泳池/围栏），应使用 None/0 进行语义填充。

---

### Q12 (1 pt)

Which action best matches the **Data Inspection** step in EDA?
A. Training XGBoost with grid search
B. Checking `df.shape`, `df.info()`, basic missingness
C. Applying PCA immediately
D. Oversampling the minority class

**中文答案：B**
**解析：**Inspection 是“看清数据”：大小、类型、缺失、字段意义，不是直接建模。

---

### Q13 (1 pt)

Which plot is most appropriate for detecting outliers in a single numeric feature?
A. Confusion matrix
B. Box plot
C. ROC curve
D. Word cloud

**中文答案：B**
**解析：**箱线图（IQR）直观展示离群点与分布范围。

---

### Q14 (1 pt)

If a numeric feature shows strong **right skew**, which transformation is commonly used?
A. Log transform
B. Squaring
C. One-hot encoding
D. Label encoding

**中文答案：A**
**解析：**右偏常用 log/根号压缩右长尾，改善线性关系和方差稳定性。

---

### Q15 (1 pt)

Why is scaling important before clustering with K-means?
A. K-means uses target labels
B. K-means is distance-based and feature scales can dominate the distance
C. K-means automatically scales features
D. Scaling increases interpretability for categorical features

**中文答案：B**
**解析：**K-means 基于欧氏距离，缩放保证各特征公平贡献距离。

---

### Q16 (1 pt)

Which EDA category asks: “How do multiple variables jointly relate and whether redundancy exists?”
A. Univariate
B. Bivariate
C. Multivariate
D. Labeling

**中文答案：C**
**解析：**Multivariate 关注多变量共同作用、冗余、相关矩阵、降维/聚类线索。

---

### Q17 (1 pt)

Which derived feature best represents the **age of a house at the time of sale**?
A. `HouseAge = YrSold - YrBuilt`
B. `HouseAge = YrBuilt - YrSold`
C. `HouseAge = SalePrice / GrLivArea`
D. `HouseAge = OverallQual + OverallCond`

**中文答案：A**
**解析：**HouseAge=卖出年份-建造年份（常见 House Prices 特征工程）。

---

### Q18 (1 pt)

A key reason to use **pipelines** in EDA-to-model workflow is:
A. Pipelines guarantee higher accuracy
B. Pipelines ensure consistent, repeatable preprocessing without leakage
C. Pipelines remove the need for EDA
D. Pipelines only work for categorical data

**中文答案：B**
**解析：**Pipeline 把“插补→变换→缩放→编码”等步骤固定化，避免 train/test 泄漏，保证可复现。

---

## Part B — Multiple-answer (6 questions × 3 points = 18 points)

**Select ALL that apply. Negative marking applies.**

### Q19 (3 pts)

Which statements about imbalanced datasets are correct?
A. A model can achieve high accuracy by predicting only the majority class
B. Precision/Recall/F1 are often more informative than accuracy
C. Minority patterns are harder to learn due to limited samples
D. Class imbalance never affects fairness

**中文答案：A, B, C**
**解析：**D 错：不平衡会造成系统性偏差与不公平。

---

### Q20 (3 pts)

Which are correct steps/ideas in SMOTE?
A. Pick a minority sample
B. Find k nearest neighbors among minority samples
C. Interpolate to generate synthetic points between neighbors
D. Always delete majority samples

**中文答案：A, B, C**
**解析：**SMOTE 不要求删多数类；删除属于 undersampling 体系。

---

### Q21 (3 pts)

Which are common expected effects after applying SMOTE?
A. Reduced representation bias toward majority class
B. A less skewed decision boundary
C. Minority recall often increases
D. Accuracy is guaranteed to increase

**中文答案：A, B, C**
**解析：**D 错：准确率不保证上升，可能下降。

---

### Q22 (3 pts)

Which methods are feature extraction (not selection)?
A. PCA
B. SVD
C. t-SNE
D. Lasso (L1)
E. Autoencoder

**中文答案：A, B, C, E**
**解析：**Lasso 属于 embedded feature selection（通过稀疏系数选择特征）。

---

### Q23 (3 pts)

Which statements about PCA are correct?
A. PCA is sensitive to feature scale, so scaling is often needed
B. PCA always improves interpretability
C. PCA can reduce noise and redundancy
D. PCA may discard low-variance but important predictive signals

**中文答案：A, C, D**
**解析：**B 错：PCA 常降低可解释性；D 是课件强调的风险点。

---

### Q24 (3 pts)

Which EDA actions are appropriate and correctly matched?
A. Univariate → distribution shape, skewness, outliers
B. Bivariate → correlation or relationship between two variables
C. Multivariate → correlation matrix, redundancy, joint effects
D. “NaN always means unknown” → fill everything with mean

**中文答案：A, B, C**
**解析：**D 错：House Prices 中大量 NaN 是“没有该结构”，应 None/0 语义填充。

---

## Part C — Fill in the blanks (3 questions × 3 points = 9 points)

### Q25 (3 pts)

Fill in the SMOTE synthetic sample formula:
Given minority sample (x_i), neighbor (x_j), and random (r \in (0,1)),
( x_{new} = __________________ )

**中文答案：** ( x_{new} = x_i + r\cdot(x_j - x_i) )
**解析：**沿着两点连线插值生成新样本。

---

### Q26 (3 pts)

Fill in one key dimensionality reduction benefit:
Dimensionality reduction can make models less prone to __________________ and faster to train.

**中文答案：** overfitting（过拟合）
**解析：**降维减少冗余与噪声，有助于泛化并提升训练效率。

---

### Q27 (3 pts)

Complete the derived feature definition:
HouseAge (=) __________________

**中文答案：** `YrSold - YrBuilt`
**解析：**卖出时房龄，是 House Prices EDA/FE 高频特征。

---

# Chinese Answer Key (简表)

* 单选：1C 2C 3B 4A 5B 6B 7B 8A 9B 10B 11B 12B 13B 14A 15B 16C 17A 18B
* 多选：19 ABC；20 ABC；21 ABC；22 ABCE；23 ACD；24 ABC
* 填空：25 (x_i+r(x_j-x_i))；26 overfitting；27 YrSold − YrBuilt

---

如果你想让 Week3 这份更像老师可能出的“操作型题目”，我可以再给你一份 **Practical-style Exercise**（仍是客观题）：

* 给一个小混淆矩阵，让你判断 SMOTE 前后哪个模型更适合“风险控制”（FN 比 FP 贵）；
* 给一个 PCA explained variance 表，让你填“选多少个主成分”；
* 给 House Prices 的缺失列清单，让你选择 None/0/median 的正确填法。
