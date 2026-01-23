下面是一份**完全英文题目**的 Week 1 模拟测验，题型与范围严格对齐你给的考试要求：**闭卷、客观题（单选/多选/填空）、多选有倒扣**，并覆盖 Week1 课件核心知识点（Data Science pipeline、data types、profiling/cleaning、missingness、duplicates、outliers、relationship discovery 等）。
我在每题后提供了**中文“标准答案 + 解析”**（含你闭卷时需要记的关键句）。

---

# Mock Quiz (Week 1: Data Profiling & Cleaning) — 45 points

**Instructions (English):**

* Closed book. No resources.
* Total: **27 questions**, **45 points**.
* Question types: Single-choice, Multiple-answer (with negative marking), Fill-in-the-blank.
* **Multiple-answer scoring rule (per question, 3 pts):**
  +1 for each correct option selected, **−1 for each incorrect option selected**, minimum 0, maximum 3.
  (Select **ALL** that apply.)

---

## Part A — Single-choice (18 questions × 1 point = 18 points)

### Q1 (1 pt)

Which statement best defines **data profiling**?
A. Training a machine learning model to maximize accuracy
B. Systematically examining data structure, quality, distributions, and relationships
C. Removing all missing values from a dataset
D. Deploying a model to production

**中文答案：B**
**解析：**Data profiling 是“数据体检”，重点是**结构（schema/type）+ 质量（missing/outliers/errors）+ 分布（range/pattern）+ 关系（correlation/dependency）**，为后续 cleaning/feature engineering 打基础。

---

### Q2 (1 pt)

In the Ask–Prepare–Process–Analyze–Share–Act workflow, which step focuses most on **fixing missing values and outliers**?
A. Ask
B. Prepare
C. Process
D. Share

**中文答案：C**
**解析：**Process 的核心就是把原始数据变成“可分析数据”，典型任务：**清洗、缺失处理、异常检测、格式统一**。

---

### Q3 (1 pt)

Which is an example of **structured data**?
A. A paragraph of customer reviews
B. A table with columns: Age, Income, Country
C. A raw audio recording
D. A video clip

**中文答案：B**
**解析：**结构化数据有固定 schema（列/字段），表格形式最典型；文本/音频/视频都属于非结构化或弱结构化。

---

### Q4 (1 pt)

Which data type is commonly used to represent **network/graph data**?
A. A single string per sample
B. Nodes and edges with attributes
C. Only timestamps
D. Only pixel arrays with no metadata

**中文答案：B**
**解析：**图数据=**节点（实体）+ 边（关系）**，并且节点/边都可以有属性（如类型、权重、时间等）。

---

### Q5 (1 pt)

In single-column profiling for a numeric feature, which set of statistics is MOST appropriate?
A. Unique, top, freq only
B. Mean, std, min, max, quartiles
C. TF-IDF and embeddings
D. Confusion matrix and ROC curve

**中文答案：B**
**解析：**数值列 profiling 常用：**min/max/mean/std + Q1/Q2/Q3/IQR**，用来判断范围、离散程度、偏态、异常。

---

### Q6 (1 pt)

Which function is most directly used to inspect **schema and missing counts by column** in pandas?
A. `df.head()`
B. `df.info()`
C. `df.plot()`
D. `df.sample()`

**中文答案：B**
**解析：**`df.info()`会显示列名、dtype、non-null count，非常适合快速发现**类型不对、缺失严重**的列。

---

### Q7 (1 pt)

Which statement about duplicates is MOST correct?
A. Duplicates never affect modeling
B. Duplicates can bias statistics and model training if not handled
C. Duplicates are always outliers
D. Duplicates are the same as missing values

**中文答案：B**
**解析：**重复样本会让某些模式被“重复学习”，统计分布偏移，尤其在分类不平衡时更严重。

---

### Q8 (1 pt)

Which scenario is a strong sign that missingness is **“not applicable / attribute absent”** rather than “not recorded”?
A. Missing values appear randomly across all rows
B. A numeric field is missing, but related “existence” fields indicate absence (e.g., area = 0)
C. A column has no missing values
D. Only the target variable is missing

**中文答案：B**
**解析：**课件/练习强调：缺失可能是语义缺失。比如 GarageYrBlt 缺失且 GarageArea=0、GarageCars=0 → 很可能是**没有车库**，不是填错。

---

### Q9 (1 pt)

Which missingness mechanism means missingness is related to unobserved values themselves?
A. MCAR
B. MAR
C. MNAR
D. IID

**中文答案：C**
**解析：**MNAR（Missing Not At Random）= 缺失与未观测值本身相关，最难处理；MCAR/MAR 相对更可处理。

---

### Q10 (1 pt)

Which imputation method is most appropriate for **time series** when values are missing and continuity is important?
A. One-hot encoding
B. Forward fill (ffill) / backward fill (bfill)
C. Drop all rows
D. Hash encoding

**中文答案：B**
**解析：**时间序列常用 ffill/bfill 保持连续性；但要小心“掩盖突变”。

---

### Q11 (1 pt)

Which outlier detection method relies on the **mean and standard deviation**?
A. IQR rule
B. Z-score
C. DBSCAN
D. LOF

**中文答案：B**
**解析：**Z-score 计算 ((x-\mu)/\sigma)，典型阈值 (|z|>3)。

---

### Q12 (1 pt)

Why can Z-score fail to detect extreme outliers in heavily skewed data?
A. It ignores the mean entirely
B. Outliers inflate mean and std, reducing z-values for extremes
C. It uses quartiles instead of mean
D. It only works for categorical variables

**中文答案：B**
**解析：**极端值会拉大均值和标准差，导致“极端值的 z 反而没那么大”，这也是 IQR 更鲁棒的原因。

---

### Q13 (1 pt)

Which method is generally more robust for skewed distributions?
A. Z-score
B. IQR
C. Accuracy
D. One-hot encoding

**中文答案：B**
**解析：**IQR 基于分位数（Q1/Q3），不容易被极端值拉歪，适合偏态。

---

### Q14 (1 pt)

Which statement about `.corr()` in pandas is MOST correct?
A. It computes causation between variables
B. It measures linear association (typically Pearson) between numeric variables
C. It works only for text columns
D. It outputs a confusion matrix

**中文答案：B**
**解析：**相关系数描述线性关系强弱，**相关≠因果**；默认常用 Pearson。

---

### Q15 (1 pt)

Which is an example of a data quality issue caused by **inconsistent category formatting**?
A. “SG” vs “Singapore” in the same Country column
B. A column has many outliers
C. A column is normally distributed
D. A model has high accuracy

**中文答案：A**
**解析：**同义不同写会造成类别被拆分，影响统计、编码和模型学习，需要标准化。

---

### Q16 (1 pt)

Which technique is most appropriate to detect outliers based on **local density**?
A. LOF.
B. Z-score
C. IQR
D. Mean imputation

**中文答案：A**
**解析：**LOF（Local Outlier Factor）基于局部密度对比，密度显著低于邻居则可能离群。

---

### Q17 (1 pt)

Which algorithm can label points as **noise** based on density clustering?
A. DBSCAN
B. StandardScaler
C. OneHotEncoder
D. MinMaxScaler

**中文答案：A**
**解析：**DBSCAN 做密度聚类，无法归入任何簇的点会被标记为 noise（可视为离群）。

---

### Q18 (1 pt)

What is the best reason to perform profiling BEFORE cleaning?
A. Cleaning always increases dataset size
B. Profiling reveals where issues are and guides the right cleaning strategy
C. Profiling requires a trained model
D. Profiling is only for visualization

**中文答案：B**
**解析：**先 profiling 才知道问题在哪、严重程度、分布与语义，否则清洗会“瞎处理”。

---

## Part B — Multiple-answer (6 questions × 3 points = 18 points)

**Select ALL that apply. Negative marking applies.**

### Q19 (3 pts)

Which of the following are core goals of **data profiling**?
A. Detect missing values and invalid entries
B. Understand distributions (range, patterns, trends)
C. Identify relationships/dependencies between variables
D. Choose the final neural network architecture

**中文答案：A, B, C**
**解析：**profiling=结构/质量/分布/关系；选 D 属于建模阶段，不是 profiling 的核心目标。

---

### Q20 (3 pts)

Which of the following are typical **data cleaning** tasks?
A. Handling missing values
B. Removing duplicates
C. Standardizing inconsistent formats/units/categories
D. Training a gradient boosting model

**中文答案：A, B, C**
**解析：**清洗=纠正错误/不一致/不准确；训练模型不是 cleaning。

---

### Q21 (3 pts)

Which statements about **structured vs unstructured data** are correct?
A. Structured data has predefined schema (columns/fields)
B. Unstructured text often requires NLP to extract structure
C. Images and videos are always low-dimensional
D. Network data can be represented by nodes and edges with attributes

**中文答案：A, B, D**
**解析：**C 错：图像/视频通常是高维（像素×通道×时间）。

---

### Q22 (3 pts)

Which statements about missing values are correct?
A. Missing values may mean “not recorded” or “not applicable (attribute absent)”
B. MCAR means missingness depends on unobserved values
C. Forward fill is commonly used for time series missing values
D. Domain knowledge can help decide a proper imputation strategy

**中文答案：A, C, D**
**解析：**B 错：MCAR 是完全随机缺失；“依赖未观测值”是 MNAR。

---

### Q23 (3 pts)

Which statements about outlier methods are correct?
A. Z-score is best suited for approximately normal distributions
B. IQR is robust for skewed distributions
C. DBSCAN can mark points as noise/outliers
D. Z-score never fails on skewed data

**中文答案：A, B, C**
**解析：**D 错：Z-score 在偏态/极端值场景可能失真或漏检。

---

### Q24 (3 pts)

Which statements about correlation are correct?
A. High correlation implies causation
B. Correlation helps quickly screen features related to a numeric target
C. Correlation mainly measures linear relationships (e.g., Pearson)
D. A heatmap can visualize correlation strength and direction

**中文答案：B, C, D**
**解析：**A 错：相关≠因果；其余都是 Week1 常考点。

---

## Part C — Fill in the blanks (3 questions × 3 points = 9 points)

### Q25 (3 pts)

Fill in the formula for Z-score:
( z = __________________ )

**中文答案：** ( z = (x-u)/{sigma} )
**解析：**Z-score 表示一个点距离均值多少个标准差（standard deviations）。

---

### Q26 (3 pts)

Complete the IQR outlier fences (use the common 1.5×IQR rule):
Lower fence = ( __________________ )
Upper fence = ( __________________ )

**中文答案：**
Lower fence = (Q1 - 1.5* IQR)
Upper fence = (Q3 + 1.5*IQR)
**解析：**IQR = Q3 − Q1；基于分位数更鲁棒，适合偏态数据。

---

### Q27 (3 pts)

In the Ask–Prepare–Process–Analyze–Share–Act workflow, the step that focuses on communicating results to stakeholders is:

---

**中文答案：Share**
**解析：**Share = 用图表/报告/口头陈述把洞察传达给受众，使其可用于决策。

---

# Chinese Answer Key (简表)

* 单选：1B 2C 3B 4B 5B 6B 7B 8B 9C 10B 11B 12B 13B 14B 15A 16A 17A 18B
* 多选：19 ABC；20 ABC；21 ABD；22 ACD；23 ABC；24 BCD
* 填空：25 ((x-\mu)/\sigma)；26 (Q1-1.5IQR,,Q3+1.5IQR)；27 Share

---

如果你希望我把这份模拟题做得更像你真实 quiz（25–30题、总分45、题目难度更贴近“老师出题风格”），我可以在下一条直接给你一个**升级版**：

* 加入更多“情境题”（像 Phoenix FC/Customer info 的 mini-case）
* 多选题设计成更容易“踩坑”（比如把 MCAR/MAR/MNAR 混进选项）
* 每题解析补充“闭卷记忆口诀”（中英对照）

z-score的计算公式和方法是什么

###### ChatGPT 说：

z-score的计算公式和方法是什么

###### ChatGPT 说：
