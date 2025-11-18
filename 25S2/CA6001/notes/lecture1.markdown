
---

# 🧠 CA6001 Chapter 1 – Supervised vs Unsupervised Learning

*Nanyang Technological University – Dr. Zhang Jiehuang*

---

## 🎯 **Learning Outcomes / 学习目标**

* 了解并解释人工智能 (AI) 与数据科学 (Data Science) 的基本原理
* 掌握监督学习 (Supervised Learning) 与非监督学习 (Unsupervised Learning) 的区别与应用场景
* 学会线性回归 (Linear Regression) 与逻辑回归 (Logistic Regression) 的数学模型
* 理解聚类 (Clustering) 的原理与客户分群 (Customer Segmentation) 的应用
* 理解模型评估指标（Precision, Recall, F1-score, AUC）

---

## 🧩 **1. What is AI and Data Science / 什么是人工智能与数据科学**

**English:**
Data Science is an interdisciplinary field that uses data to generate insights and value.
It overlaps with AI, Machine Learning (ML), and Deep Learning (DL).
It applies to domains like healthcare, finance, and marketing.

**中文：**
数据科学是一个跨学科领域，通过数据来创造洞察与价值。
它与人工智能、机器学习、深度学习紧密相关。
在医疗、金融、市场等行业都有广泛应用。

```python
# Example: Simple data science operation
import pandas as pd

data = {"Age": [25, 30, 45], "Income": [4000, 6000, 10000]}
df = pd.DataFrame(data)
print(df.describe())  # Generate basic insights from data
```

---

## 🧭 **2. Why Supervised & Unsupervised Learning Matter / 为什么监督与非监督学习重要**

* 它们构成了 AI/ML 的基础，所有高级算法都基于这两类学习方式。
* 可广泛用于不同产业（金融、医疗、市场营销等）。
* 帮助企业和科研决策者制定基于数据的决策。

---

## 🧮 **3. Supervised Learning / 监督学习**

### 🧠 Definition / 定义

**English:**
Supervised Learning uses labeled data `(X, Y)` where `Y` is known.
The goal is to learn the mapping function `f(X) = Y`.

**中文：**
监督学习使用带标签的数据 `(X, Y)`，目标是学习输入与输出之间的映射关系。

### 🏠 Example: Linear Regression / 线性回归

**Concept:**

* Input (X): house size
* Output (Y): house price
* Goal: Find the best-fit line minimizing error.

**Formula:**
[
f_{w,b}(x) = w x + b
]
Minimize:
[
J(w,b) = \frac{1}{m} \sum_{i=1}^m (f_{w,b}(x^{(i)}) - y^{(i)})^2
]

```python
# Linear Regression Example
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[1000], [1500], [2000], [2500], [3000]])  # sqft
y = np.array([150, 200, 250, 280, 310])  # price in $K

model = LinearRegression()
model.fit(X, y)

plt.scatter(X, y, color="blue", label="Data points")
plt.plot(X, model.predict(X), color="red", label="Best fit line")
plt.xlabel("House Size (sqft)")
plt.ylabel("Price ($K)")
plt.legend()
plt.show()
```

---

### 📈 Logistic Regression / 逻辑回归

**Purpose:**
Used for **classification problems**, mapping outputs between 0 and 1 using the **sigmoid function**:

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

```python
# Logistic Regression Example: Spam Detection
from sklearn.linear_model import LogisticRegression

X = [[50], [100], [200], [250], [300]]   # number of words in email
y = [0, 0, 1, 1, 1]                      # 1 = spam, 0 = not spam

clf = LogisticRegression()
clf.fit(X, y)
print(clf.predict([[150]]))  # Predict if an email with 150 words is spam
```

---

### 💸 Application: Financial Fraud Detection / 金融欺诈检测

**Key Idea:**
Use labeled historical transactions (`fraud` / `not fraud`) to train models to detect suspicious activities.
In practice, labels may be rare, so **synthetic labels** and **domain knowledge** are essential.

```python
# Simulated fraud detection example
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.DataFrame({
    "amount": [20, 500, 10000, 50, 12000],
    "is_foreign": [0, 0, 1, 0, 1],
    "label": [0, 0, 1, 0, 1]
})

model = RandomForestClassifier()
model.fit(data[["amount", "is_foreign"]], data["label"])
print(model.predict([[7000, 1]]))  # Predict if new transaction is fraud
```

---

## 🔍 **4. Unsupervised Learning / 非监督学习**

### Definition / 定义

**English:**
Unsupervised Learning works with unlabeled data, discovering hidden patterns and structures.

**中文：**
非监督学习在没有标签的数据中寻找潜在的结构与规律。

### Example: Clustering / 聚类

```python
# K-Means Example: Customer Segmentation
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[18, 1500], [25, 2500], [40, 4000], [50, 5000], [60, 5500]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.xlabel("Age")
plt.ylabel("Monthly Spending ($)")
plt.title("Customer Segmentation by KMeans")
plt.show()
```

**Applications / 应用领域：**

* 客户分群（Customer Segmentation）
* 推荐系统（Recommender Systems）
* 市场篮分析（Market Basket Analysis）

---

## ⚖️ **5. Comparison: Supervised vs Unsupervised / 对比总结**

| Feature    | Supervised Learning                       | Unsupervised Learning                 |
| ---------- | ----------------------------------------- | ------------------------------------- |
| Labels     | Uses labeled data                         | Uses unlabeled data                   |
| Goal       | Predict outcomes                          | Find hidden patterns                  |
| Output     | Continuous or categorical                 | Clusters or associations              |
| Algorithms | Linear/Logistic Regression, Decision Tree | K-Means, PCA, Hierarchical Clustering |

---

## ⚙️ **6. Evaluation Metrics / 模型评估指标**

### Train-Test Split & Cross Validation

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X, y, cv=5)
print("Cross-validation accuracy:", scores.mean())
```

### Precision, Recall, F1-score & Confusion Matrix

```python
from sklearn.metrics import classification_report, confusion_matrix
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### AUC (Area Under Curve)

```python
from sklearn.metrics import roc_auc_score
import numpy as np

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
print("AUC =", roc_auc_score(y_true, y_scores))
```

---

## 📊 **7. Overfitting vs Underfitting / 过拟合与欠拟合**

| Type             | Description                                           | Example                                     |
| ---------------- | ----------------------------------------------------- | ------------------------------------------- |
| **Overfitting**  | Model learns noise and performs poorly on unseen data | Too complex model (e.g., too many features) |
| **Underfitting** | Model too simple, fails to capture pattern            | Linear model for nonlinear data             |

```python
# Visual intuition (conceptual, not executable)
# Overfitting: Perfect fit on train data but poor test performance
# Underfitting: Straight line ignoring complex pattern
```

---

## 🧾 **Summary / 总结**

* 监督学习：输入有标签，适用于预测与分类。
* 非监督学习：输入无标签，适用于聚类与模式发现。
* 常见算法：

  * 监督：Linear Regression, Logistic Regression, Decision Tree
  * 非监督：K-Means, PCA, Association Rules
* 模型评估指标：Accuracy, Precision, Recall, F1, AUC
* 注意过拟合与欠拟合的平衡。

---
