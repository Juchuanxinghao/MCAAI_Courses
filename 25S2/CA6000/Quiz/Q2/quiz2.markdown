# Quiz #2 (20/12/25 900am - Same venues) 
## Topics to be covered:Topic 5,8,9,10,11,12a,12b,13
### 1.Python Class.
### 2.Matplotlib.
### 3.Pandas.
### 4.Numpy
### 5.SKLearn-Feature and training
### 6.PyTorch-Features,Neural Network Modeling and Evaluation
### 7.TensorFlow-Features,Neural Network Modeling and Evaluation



---

# 🧠 Topic 5 — **NumPy（考试复习专用版）**

---

## 📌 一、考试重点速览（Exam Focus）

在 CA6000 的 MCQ 中，NumPy **通常考：**

### 🔥 高频必考（一定要会）

* ndarray 是什么（vs Python list）
* shape / ndim / dtype
* array 创建函数（zeros / ones / arange / linspace）
* 索引与切片（尤其是二维）
* 向量化运算（为什么比 for-loop 快）
* 广播（Broadcasting）**规则判断**
* `@` 和 `*` 的区别
* 常用统计函数（mean / std / sum）

### ⚠️ 容易出“陷阱题”

* `ndarray` vs `list`
* 维度不匹配是否能广播
* `reshape()` 是否改变原数组
* `copy()` vs 视图（view）
* axis=0 / axis=1 含义

---

## 📘 二、NumPy 核心概念（中英对照）

---

### 1️⃣ 什么是 NumPy？（What is NumPy）

**英文（课件核心意思）**
NumPy is a fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions.

**中文解释（考试理解版）**
NumPy 是 Python 做数值计算的核心库，提供：

* 高性能的多维数组（ndarray）
* 向量化计算（不用 for 循环）
* 科学计算常用函数

👉 **考试关键词：** `ndarray`, `vectorized`, `numerical computing`

---

### 2️⃣ ndarray（核心数据结构）

**英文**
An ndarray is a multi-dimensional array object that stores elements of the same data type.

**中文**

* ndarray 是 NumPy 的核心
* **所有元素类型必须相同**
* 比 Python list 快很多（底层是 C）

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

print(a.ndim)   # 1 维
print(b.ndim)   # 2 维
print(b.shape)  # (2, 2)
```

---

### 3️⃣ ndarray vs Python list（⚠️ 高频考点）

| 特性   | list        | ndarray    |
| ---- | ----------- | ---------- |
| 元素类型 | 可不同         | **必须相同**   |
| 运算   | 慢（for-loop） | **快（向量化）** |
| 维度   | 一维          | 多维         |
| 数值计算 | 不方便         | **非常强**    |

👉 **考试爱问：Why is NumPy faster than list?**
✔ 因为 ndarray 是连续内存 + C 实现 + 向量化

---

### 4️⃣ array 创建方式（必背）

```python
np.zeros((2,3))      # 全 0
np.ones((2,3))       # 全 1
np.arange(0, 10, 2)  # [0,2,4,6,8]
np.linspace(0, 1, 5) # 等距 5 个数
```

**考试常问：**

* `arange` vs `linspace`
* 参数顺序
* 输出 shape

---

### 5️⃣ dtype（数据类型）

**英文**
dtype defines the type of elements stored in the array.

**中文**
dtype 决定：

* 内存占用
* 精度
* 运算速度

```python
a = np.array([1,2,3], dtype=float)
print(a.dtype)
```

⚠️ **考试点：**

* ndarray 所有元素 dtype 相同
* 可以用 `astype()` 转换

---

### 6️⃣ 索引与切片（Indexing & Slicing）

```python
arr = np.array([[10,20,30],
                [40,50,60]])

arr[0, 1]   # 20
arr[:, 1]   # [20 50]
arr[1, :]   # [40 50 60]
```

👉 **axis 含义（必考）：**

* `axis=0` → **按列方向**
* `axis=1` → **按行方向**

---

### 7️⃣ 向量化（Vectorization）⭐

**英文**
Vectorization means applying operations on entire arrays without explicit loops.

**中文**

* 不用 for 循环
* 一行代码处理整个数组
* 更快、更简洁

```python
a = np.array([1,2,3])
b = a * 2     # 向量化
```

---

### 8️⃣ 广播（Broadcasting）⭐⭐⭐（最爱考）

**英文**
Broadcasting allows NumPy to perform operations on arrays of different shapes.

**广播规则（考试版）**

1. 从右往左对齐维度
2. 相等 或 其中一个是 1 → 可以
3. 否则 → ❌ 错误

```python
A = np.array([[1],[2],[3]])  # (3,1)
B = np.array([10,20,30])     # (3,)

A + B  # OK → (3,3)
```

---

### 9️⃣ reshape vs 原数组（⚠️）

```python
a = np.arange(6)
b = a.reshape(2,3)

# reshape 通常返回视图（共享内存）
```

👉 **考试陷阱：**

* reshape 不一定创建新数组
* 修改 b 可能影响 a

---

### 🔟 常用统计函数（必记）

```python
np.sum(a)
np.mean(a)
np.std(a)
np.min(a)
np.max(a)
```

---

## 📝 三、选择题（MCQ 练习）

### **Q1. Which of the following best describes a NumPy ndarray?**

A. A list that can store elements of different types
B. A multi-dimensional array storing elements of the same type
C. A dictionary-like data structure
D. A file-based data structure

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

* A ❌（这是 Python list）
* B ✅（ndarray 定义）
* C ❌
* D ❌

</details>

---

### **Q2. Why is NumPy generally faster than Python lists?**

A. It uses Python loops
B. It stores data in non-contiguous memory
C. It uses vectorized operations implemented in C
D. It allows mixed data types

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

* C 是核心原因（考试高频）

</details>

---

### **Q3. What is the shape of the result?**

```python
A = np.array([[1],[2],[3]])
B = np.array([10,20,30])
A + B
```

A. (3,)
B. (3,1)
C. (1,3)
D. (3,3)

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：D**

* 广播后：(3,1) + (3,) → (3,3)

</details>

---

### **Q4. Which function creates evenly spaced numbers between two values?**

A. `arange()`
B. `zeros()`
C. `linspace()`
D. `reshape()`

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. What does `axis=0` mean in NumPy operations?**

A. Operate across rows
B. Operate across columns
C. Operate element-wise
D. Flatten the array

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

## ✅ NumPy 本章小结（考试版）

你现在应该能 **100% 回答以下问题**：

✔ ndarray 是什么
✔ list vs ndarray
✔ 广播能不能发生
✔ axis=0 / axis=1
✔ reshape 是否复制
✔ 为什么 NumPy 快



好，我们**回到 Topic 8 —— Matplotlib**，这次我给你的是 **「考试完整强化版」**，不是简单用法说明，而是：

> 🎯 **完全对齐 CA6000 第二次考试的 MCQ 出题方式**
> 📌 **哪些函数考、怎么考、选项怎么设陷阱**
> ❌ **最容易选错的点我会直接点出来**

你可以把这一章当作 **“看完就能做选择题”的版本**。

---

# 🧠 Topic 8 — **Matplotlib（考试复习专用版）**

---

## 📌 一、考试重点速览（Exam Focus）

在 CA6000 中，Matplotlib **几乎 100% 是选择题**，而且考点非常固定。

### 🔥 高频必考

* Matplotlib 的用途（是什么 / 干什么）
* `pyplot` 的角色
* 常见图类型：`line / scatter / bar / histogram`
* `plt.plot()` vs `plt.scatter()`
* 标题、坐标轴、图例函数
* `plt.show()`
* 多图绘制（`subplot`）

### ⚠️ 高频陷阱

* `plt.plot()` 默认是 **折线图**
* `scatter` 和 `plot` 的区别
* `hist()` 画的是 **分布**
* `subplot(2,1,1)` 参数含义
* 没 `plt.show()` 会发生什么

---

## 📘 二、Matplotlib 核心概念（中英对照）

---

## 1️⃣ 什么是 Matplotlib？

### 📌 英文（课件原意）

Matplotlib is a Python library used for data visualization.

### 📌 中文（考试理解版）

Matplotlib 是 Python 中 **最基础、最常用的数据可视化库**，主要用于：

* 把数据画成图
* 帮助理解数据分布、趋势、关系

👉 **考试关键词**：
`data visualization`, `plot`, `graph`

---

## 2️⃣ pyplot 模块（必考）

```python
import matplotlib.pyplot as plt
```

### 📌 英文

pyplot provides a MATLAB-like interface for plotting.

### 📌 中文

* `pyplot` 是 Matplotlib 中**最常用的接口**
* 提供一堆“画图函数”

👉 **考试常问：**

> Which module is commonly used for plotting in Matplotlib?

✅ **答案：pyplot**

---

## 3️⃣ 折线图（Line Plot）⭐⭐⭐

```python
plt.plot(x, y)
plt.show()
```

### 📌 关键点（考试版）

* `plt.plot()` → **默认是折线图**
* 用于展示 **趋势（trend）**

👉 **非常容易考：**

> What type of plot is created by plt.plot()?

✅ **Line plot**

---

## 4️⃣ 散点图（Scatter Plot）⭐⭐

```python
plt.scatter(x, y)
plt.show()
```

### 📌 用途

* 查看两个变量之间的关系
* 常用于数据分析前的探索

👉 **plot vs scatter（必考对比）**

| 函数      | 图类型 |
| ------- | --- |
| plot    | 折线  |
| scatter | 散点  |

---

## 5️⃣ 柱状图（Bar Chart）

```python
plt.bar(x, height)
```

### 📌 中文理解

* 比较不同类别的数值
* x 通常是分类

---

## 6️⃣ 直方图（Histogram）⭐⭐⭐（非常爱考）

```python
plt.hist(data)
```

### 📌 重点理解

* **展示数据分布**
* x 轴是区间（bins）
* y 轴是频数

👉 **考试常问：**

> Which plot is used to show data distribution?

✅ **Histogram**

---

## 7️⃣ 图形基本元素（必考函数）

---

### ✔ 标题

```python
plt.title("My Plot")
```

---

### ✔ 坐标轴标签

```python
plt.xlabel("X axis")
plt.ylabel("Y axis")
```

---

### ✔ 图例（Legend）

```python
plt.legend()
```

（前提是 plot 时有 `label=`）

---

## 8️⃣ plt.show()（⚠️ 超级容易忽略）

```python
plt.show()
```

### 📌 考试理解

* 用于 **显示图形**
* 在某些环境（脚本）中不写就不显示

👉 **MCQ 常见问法：**

> What does plt.show() do?

✅ Displays the figure

---

## 9️⃣ 多图绘制：subplot（⭐⭐）

```python
plt.subplot(2, 1, 1)
plt.plot(x1, y1)

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
```

### 📌 参数解释（必考）

```text
subplot(rows, cols, index)
```

* 2 行
* 1 列
* 当前是第 1 / 2 个子图

---

## 🔟 面向对象接口（了解即可）

```python
fig, ax = plt.subplots()
ax.plot(x, y)
```

📌 **考试一般只考 pyplot，不深究 OOP 接口**

---

# 📝 三、选择题（MCQ 强化）

---

### **Q1. What is Matplotlib mainly used for?**

A. Machine learning
B. Data visualization
C. Web development
D. Database management

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q2. Which module is commonly imported as `plt`?**

A. matplotlib
B. pyplot
C. seaborn
D. pandas

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q3. What type of plot is created by `plt.plot()` by default?**

A. Scatter plot
B. Bar chart
C. Line plot
D. Histogram

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q4. Which function is used to create a histogram?**

A. `plt.bar()`
B. `plt.scatter()`
C. `plt.hist()`
D. `plt.plot()`

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. What does `plt.show()` do?**

A. Saves the plot
B. Clears the plot
C. Displays the plot
D. Adds a legend

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q6. In `plt.subplot(2,1,2)`, what does `2` mean?**

A. Number of columns
B. Number of rows
C. Index of subplot
D. Number of figures

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

## ✅ Topic 8 最终考试清单（背这个就够）

你现在应该可以**稳定答对 Matplotlib 的题目**，如果你能：

✔ 说出 Matplotlib 的用途
✔ 区分 plot / scatter / hist / bar
✔ 记住 pyplot
✔ 理解 subplot 参数
✔ 知道 show() 的作用

---





---

# 🧠 Topic 9 — **Pandas（考试复习专用版）**

---

## 📌 一、考试重点速览（Exam Focus）

在 MCQ 中，Pandas **通常考：**

### 🔥 高频必考

* Series vs DataFrame（**必考对比题**）
* DataFrame 的基本属性（`shape`, `columns`, `index`）
* 数据读取函数（`read_csv()`）
* 列选择 vs 行选择
* `loc` vs `iloc`（**最容易出选择题**）
* 缺失值处理（`isna`, `dropna`, `fillna`）
* 基本统计函数（`mean`, `sum`, `describe`）

### ⚠️ 高频陷阱

* `df['col']` vs `df[['col']]`
* `loc` 用 **标签**，`iloc` 用 **位置**
* `axis=0` / `axis=1`
* `drop()` 默认是行不是列
* `inplace=True` 是否返回新对象

---

## 📘 二、Pandas 核心概念（中英对照）

---

## 1️⃣ 什么是 Pandas？

### 📌 英文（课件核心意思）

Pandas is a Python library used for data manipulation and analysis, providing data structures such as Series and DataFrame.

### 📌 中文解释（考试理解版）

Pandas 是 Python 中用于：

* **结构化数据处理**
* **表格数据分析**
* **数据清洗与统计**

👉 核心思想：

> **像操作 Excel 表格一样操作数据**

---

## 2️⃣ Pandas 的两大核心数据结构（必考）

---

### ✅ Series（一维数据）

**英文**
A Series is a one-dimensional labeled array.

**中文**

* 类似一列数据
* 有 index（索引）
* 每个值有标签

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```

---

### ✅ DataFrame（二维数据 ⭐⭐⭐）

**英文**
A DataFrame is a two-dimensional labeled data structure with columns.

**中文**

* 类似 Excel 表格
* 行 + 列
* 最常用的数据结构

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Score': [85, 90]
})
print(df)
```

---

### 🔥 Series vs DataFrame（选择题最爱）

| 特性 | Series | DataFrame |
| -- | ------ | --------- |
| 维度 | 1D     | 2D        |
| 类似 | 一列     | 表格        |
| 列名 | ❌      | ✔         |
| 多列 | ❌      | ✔         |

---

## 3️⃣ DataFrame 的常用属性（必记）

```python
df.shape     # (行数, 列数)
df.columns   # 列名
df.index     # 行索引
df.dtypes    # 每列数据类型
```

---

## 4️⃣ 读取数据（Data Input）⭐

### 📌 CSV 是考试重点

```python
df = pd.read_csv("data.csv")
```

👉 常考参数（理解即可）：

* `sep=','`
* `header=0`
* `index_col=0`

---

## 5️⃣ 查看数据（Exploration）

```python
df.head()    # 前 5 行
df.tail()    # 后 5 行
df.info()    # 结构信息
df.describe()  # 统计信息
```

👉 **选择题会问：哪个函数用于查看统计摘要？**
✔ `describe()`

---

## 6️⃣ 列选择（非常重要）

```python
df['Score']        # 返回 Series
df[['Score']]      # 返回 DataFrame
```

⚠️ **考试陷阱**：
这两者**类型不同**

---

## 7️⃣ 行选择 & loc / iloc（⭐⭐⭐必考）

---

### ✅ loc（基于标签 label）

```python
df.loc[0]            # 行标签是 0
df.loc[:, 'Score']   # 所有行 + Score 列
```

---

### ✅ iloc（基于位置 index）

```python
df.iloc[0]           # 第一行
df.iloc[:, 1]        # 第二列
```

---

### 🔥 loc vs iloc 对比（必考）

| 方法   | 基于 | 使用      |
| ---- | -- | ------- |
| loc  | 标签 | 行名 / 列名 |
| iloc | 位置 | 整数索引    |

---

## 8️⃣ 条件筛选（Filtering）

```python
df[df['Score'] > 80]
```

👉 **选择题常问**：
如何筛选满足条件的行？

---

## 9️⃣ 缺失值处理（Missing Values）⭐⭐

```python
df.isna()        # 检测缺失值
df.dropna()      # 删除缺失值
df.fillna(0)     # 填充缺失值
```

⚠️ `dropna()` 默认：

* `axis=0`（行）
* 删除包含 NaN 的行

---

## 🔟 删除数据（drop）

```python
df.drop('Score', axis=1)   # 删除列
df.drop(0, axis=0)         # 删除行
```

👉 **axis 再次是高频考点**

---

## 1️⃣1️⃣ 基本统计函数

```python
df['Score'].mean()
df['Score'].sum()
df['Score'].max()
df['Score'].min()
```

---

## 📝 三、选择题（MCQ 练习）

---

### **Q1. What is the main difference between a Series and a DataFrame?**

A. Series is two-dimensional, DataFrame is one-dimensional
B. Series has columns, DataFrame does not
C. Series is one-dimensional, DataFrame is two-dimensional
D. They are the same

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

* Series → 1D
* DataFrame → 2D

</details>

---

### **Q2. Which method is used to read a CSV file in Pandas?**

A. `read_excel()`
B. `read_csv()`
C. `load_csv()`
D. `open_csv()`

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q3. What is returned by `df['Score']`?**

A. DataFrame
B. Series
C. List
D. NumPy array

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q4. Which statement about `loc` and `iloc` is correct?**

A. Both use integer index
B. loc uses position, iloc uses label
C. loc uses label, iloc uses position
D. They are identical

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. What does `axis=1` refer to in Pandas operations?**

A. Operate on rows
B. Operate on columns
C. Operate on elements
D. No effect

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

## ✅ Topic 9 总结（考试视角）

你现在应该能 **稳定答对以下类型的题：**

✔ Series vs DataFrame
✔ loc / iloc 区分
✔ 列选择返回类型
✔ 缺失值处理
✔ axis 含义
✔ describe() 的用途


很好，我们继续 **Topic 10 — Python Class（OOP）**。
这一章在 CA6000 第二次考试里属于 **“概念理解型 + 高频判断型 MCQ”**，**不写代码也能考你**，而且**非常容易“看着都对，但只能选一个”**。

下面是**完全对齐你 Topic 10（Python Class）PPT 的考试复习版**。

---

# 🧠 Topic 10 — **Python Class（OOP，考试复习专用版）**

---

## 📌 一、考试重点速览（Exam Focus）

在 MCQ 中，Python Class **通常考：**

### 🔥 高频必考

* 什么是 Class / Object
* `__init__` 的作用
* `self` 是什么
* 实例属性 vs 类属性
* 方法（method） vs 函数（function）
* 继承（Inheritance）
* 方法重写（Override）
* `super()`

### ⚠️ 高频陷阱

* `self` 不是关键字
* 类属性 vs 实例属性混淆
* 构造方法是否必须存在
* 子类是否自动拥有父类方法
* 没写 `__init__` 会不会报错（不会）

---

## 📘 二、Python Class 核心概念（中英对照）

---

## 1️⃣ 什么是 Class？

### 📌 英文（课件核心）

A class is a blueprint for creating objects.

### 📌 中文（考试理解版）

* Class（类）是**对象的模板**
* 定义了对象：

  * 有哪些 **属性**
  * 能做哪些 **行为（方法）**

```python
class Person:
    pass
```

---

## 2️⃣ 什么是 Object？

### 📌 英文

An object is an instance of a class.

### 📌 中文

* Object（对象）是类创建出来的**具体实例**

```python
p = Person()
```

👉 **考试常问：**

> Object is an instance of a class ✅

---

## 3️⃣ `__init__`（构造方法）⭐⭐⭐

### 📌 英文

The `__init__` method is called automatically when an object is created.

### 📌 中文

* `__init__` 在**创建对象时自动执行**
* 用于初始化对象属性

```python
class Person:
    def __init__(self, name):
        self.name = name
```

⚠️ **考试陷阱：**

* `__init__` **不是必须的**
* 不写也可以创建对象

---

## 4️⃣ `self` 是什么？（超级高频）

### 📌 英文

`self` refers to the current object instance.

### 📌 中文

* `self` 表示“当前对象本身”
* 用来访问对象的属性和方法

```python
class Person:
    def say_hi(self):
        print("Hi")
```

⚠️ **必考判断题：**

| 说法             | 对错      |
| -------------- | ------- |
| self 是关键字      | ❌       |
| self 表示当前对象    | ✔       |
| self 必须作为第一个参数 | ✔（实例方法） |

---

## 5️⃣ 实例属性 vs 类属性（⭐⭐⭐）

---

### ✅ 实例属性（Instance Attribute）

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

* 每个对象**各自一份**

---

### ✅ 类属性（Class Attribute）

```python
class Dog:
    species = "Canine"
```

* 所有对象**共享**

---

### 🔥 高频对比题

| 项目   | 实例属性       | 类属性       |
| ---- | ---------- | --------- |
| 定义位置 | `__init__` | 类内部       |
| 是否共享 | ❌          | ✔         |
| 访问方式 | self.xxx   | Class.xxx |

---

## 6️⃣ 方法（Method） vs 函数（Function）

### 📌 中文

* **方法**：定义在类中，作用于对象
* **函数**：独立存在

```python
def func():        # 函数
    pass

class A:
    def method(self):   # 方法
        pass
```

👉 **考试常问：**

> A method is a function defined inside a class ✅

---

## 7️⃣ 继承（Inheritance）⭐⭐⭐

### 📌 英文

Inheritance allows a class to inherit attributes and methods from another class.

### 📌 中文

* 子类自动拥有父类的方法和属性

```python
class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    pass
```

👉 **考试判断题：**

> A subclass inherits methods from its parent class ✅

---

## 8️⃣ 方法重写（Override）

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

📌 **理解**

* 子类重新定义父类方法
* 覆盖原实现

---

## 9️⃣ super()（理解型考点）

```python
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
```

### 📌 中文

* `super()` 调用父类方法
* 常用于扩展而不是完全替换

---

## 🔟 没写 `__init__` 会怎样？（陷阱题）

```python
class A:
    pass

a = A()   # ✔ 不报错
```

📌 **结论（考试版）**

* `__init__` **不是强制的**
* Python 会提供默认构造方法

---

## 📝 三、选择题（MCQ）

---

### **Q1. What is a class in Python?**

A. A variable
B. A function
C. A blueprint for creating objects
D. A module

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q2. What is an object?**

A. A class definition
B. An instance of a class
C. A Python file
D. A module

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q3. What is the purpose of `__init__`?**

A. Delete an object
B. Initialize object attributes
C. Print object info
D. Import modules

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q4. Which statement about `self` is TRUE?**

A. It is a keyword
B. It refers to the class
C. It refers to the current object
D. It is optional in methods

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. Which attribute is shared by all objects of a class?**

A. Local attribute
B. Instance attribute
C. Class attribute
D. Temporary attribute

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q6. What happens if a class does not define `__init__`?**

A. Error occurs
B. Object cannot be created
C. Python provides a default constructor
D. Class cannot be inherited

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q7. What does inheritance allow?**

A. A class to use multiple modules
B. A class to inherit methods from another class
C. A function to call another function
D. A variable to change type

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

## ✅ Topic 10 考试速记表（你要会的）

✔ Class vs Object
✔ `__init__` 作用
✔ `self` 的意义
✔ 类属性 vs 实例属性
✔ 继承 & 重写
✔ super() 的作用

---

非常好 👍
**Topic 11（Scikit-learn）是第二次考试里“分值高 + 套路非常固定”的一章**，只要把概念顺清，选择题基本是送分。

下面我会**严格对齐你 Topic 11（SKLearn）PDF 的内容范围**，并完全按照**考试复习模式**来讲。

---

# 🧠 Topic 11 — **Scikit-learn（Feature & Training）考试复习专用版**

---

## 📌 一、考试重点速览（Exam Focus）

在 CA6000 第二次考试中，SKLearn **几乎全是概念型 MCQ**，常考：

### 🔥 高频必考

* 什么是 Scikit-learn
* 机器学习 workflow（流程）
* Feature（特征） vs Label（标签）
* `fit()` / `transform()` / `fit_transform()`
* `train_test_split()`
* 常见模型：

  * Linear Regression
  * Logistic Regression
  * KNN
* `predict()`
* 模型评估（accuracy）

### ⚠️ 高频陷阱

* `fit()` ≠ `predict()`
* 训练数据 vs 测试数据
* Feature scaling 的目的
* 分类 vs 回归模型混淆
* Logistic Regression **是分类，不是回归**

---

## 📘 二、Scikit-learn 核心概念（中英对照）

---

## 1️⃣ 什么是 Scikit-learn？

### 📌 英文（课件核心）

Scikit-learn is a Python library for machine learning, providing simple and efficient tools for data analysis and modeling.

### 📌 中文（考试理解版）

Scikit-learn 是 Python 中**最常用的机器学习库**，特点是：

* 统一 API（fit / predict）
* 支持分类、回归、聚类
* 非常适合教学与工程实践

👉 **考试关键词**：
`machine learning`, `model`, `training`, `prediction`

---

## 2️⃣ 机器学习基本流程（⭐⭐⭐ 必考）

### 📌 标准 ML Workflow

```text
Data → Feature → Model → Training → Prediction → Evaluation
```

### 📌 中文解释

1. 准备数据
2. 分离 **Feature (X)** 和 **Label (y)**
3. 选择模型
4. 训练模型（fit）
5. 预测（predict）
6. 评估效果

👉 **选择题极爱问：步骤顺序**

---

## 3️⃣ Feature vs Label（必考对比）

| 项目 | Feature (X) | Label (y) |
| -- | ----------- | --------- |
| 含义 | 输入特征        | 输出结果      |
| 作用 | 模型输入        | 模型学习目标    |
| 示例 | 面积、年龄       | 房价        |

```python
X = df[['size', 'age']]
y = df['price']
```

---

## 4️⃣ 训练集 & 测试集（⭐⭐⭐）

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)
```

### 📌 中文理解

* 训练集：**用来学习**
* 测试集：**用来评估**
* 防止过拟合（overfitting）

👉 **考试常问：**

> Why do we split data into training and testing sets?

✅ To evaluate model performance on unseen data

---

## 5️⃣ fit / predict（超级高频）

---

### ✅ fit()

```python
model.fit(X_train, y_train)
```

📌 **作用**
→ 让模型从数据中**学习参数**

---

### ✅ predict()

```python
y_pred = model.predict(X_test)
```

📌 **作用**
→ 用训练好的模型做预测

---

### 🔥 必考对比

| 方法      | 作用   |
| ------- | ---- |
| fit     | 训练模型 |
| predict | 预测结果 |

---

## 6️⃣ transform / fit_transform（理解题）

常见于 **特征缩放（StandardScaler）**。

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

| 方法            | 含义          |
| ------------- | ----------- |
| fit           | 学习参数（均值、方差） |
| transform     | 应用变换        |
| fit_transform | 两步合一        |

---

## 7️⃣ 常见模型（考试重点）

---

### 7️⃣1️⃣ Linear Regression（回归）

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

📌 用途：

* 预测 **连续值**
* 如：房价、温度

---

### ⚠️ Logistic Regression（陷阱！）

```python
from sklearn.linear_model import LogisticRegression
```

📌 **虽然叫 Regression，但它是：**

> ✅ **分类模型**

👉 **考试非常爱问：**

> Logistic Regression is used for:

✅ **Classification**

---

### 7️⃣2️⃣ KNN（K-Nearest Neighbors）

```python
from sklearn.neighbors import KNeighborsClassifier
```

📌 核心思想：

* 看最近的 K 个邻居
* 多数投票决定类别

---

## 8️⃣ 模型评估（Evaluation）⭐⭐

---

### 准确率 Accuracy（最常考）

```python
from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)
```

📌 中文解释

* 正确预测 / 总预测数
* 常用于分类问题

---

## 9️⃣ 完整最小示例（理解流程即可）

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))
```

---

## 📝 三、选择题（MCQ 强化）

---

### **Q1. What is Scikit-learn mainly used for?**

A. Web development
B. Machine learning
C. Game development
D. Database management

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q2. What does `fit()` do in Scikit-learn?**

A. Makes predictions
B. Evaluates the model
C. Trains the model
D. Visualizes data

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q3. Which data is used to evaluate model performance?**

A. Training data
B. Feature data
C. Test data
D. Label data

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q4. What is the purpose of `train_test_split()`?**

A. To clean data
B. To train model
C. To split data into training and testing sets
D. To normalize data

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. Logistic Regression is mainly used for:**

A. Regression problems
B. Clustering
C. Classification
D. Dimensionality reduction

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

（这是**必考陷阱题**）

</details>

---

### **Q6. What does `predict()` return?**

A. Model parameters
B. Training data
C. Predicted labels
D. Accuracy score

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q7. Which metric is commonly used for classification evaluation?**

A. MSE
B. Accuracy
C. Variance
D. Mean

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

## ✅ Topic 11 考前速记（你要背的）

✔ ML 基本流程
✔ Feature vs Label
✔ fit / predict
✔ train vs test
✔ Logistic Regression 是分类
✔ Accuracy 用于评估

---

非常好，现在进入**第二次考试里最“技术感强、但考法其实很固定”的章节之一** 👍
**Topic 12a — PyTorch（Overview / Features）**

> 放心：**考试不会考你写复杂 PyTorch 代码**
> 👉 **考的是概念、流程、名词对应关系（MCQ 超友好）**

下面是**完全对齐 Topic 12a PDF 的考试复习版**。

---

# 🧠 Topic 12a — **PyTorch（Overview & Features）考试复习专用版**

---

## 📌 一、考试重点速览（Exam Focus）

在 CA6000 第二次考试中，**Topic 12a 通常考：**

### 🔥 高频必考

* 什么是 PyTorch
* Tensor 是什么（vs NumPy array）
* PyTorch 的核心组件
* 动态计算图（Dynamic Graph）
* GPU / CPU 的概念
* `torch.Tensor`
* Autograd（自动求导）的概念

### ⚠️ 高频陷阱

* Tensor ≠ NumPy array（但可互转）
* PyTorch 默认是 **动态图**
* backward() 是做什么的
* `.requires_grad`
* PyTorch vs TensorFlow（静态 / 动态）

---

## 📘 二、PyTorch 核心概念（中英对照）

---

## 1️⃣ 什么是 PyTorch？

### 📌 英文（课件核心）

PyTorch is an open-source machine learning library used for deep learning applications.

### 📌 中文（考试理解版）

PyTorch 是一个用于 **深度学习（Deep Learning）** 的 Python 库，特点是：

* 灵活
* 易调试
* 支持 GPU
* 广泛用于研究和工业

👉 **考试关键词**：
`deep learning`, `tensor`, `autograd`, `GPU`

---

## 2️⃣ PyTorch 的核心组件（必考）

| 组件       | 作用     |
| -------- | ------ |
| Tensor   | 数据结构   |
| Autograd | 自动求导   |
| nn       | 神经网络模块 |
| optim    | 优化器    |
| CUDA     | GPU 支持 |

👉 **选择题常问：**

> Which component handles automatic differentiation?

✅ **Autograd**

---

## 3️⃣ Tensor（最核心概念）⭐⭐⭐

### 📌 英文

A Tensor is a multi-dimensional array similar to NumPy array.

### 📌 中文

* Tensor 是 PyTorch 的基本数据结构
* 类似 NumPy 的 ndarray
* **但可以在 GPU 上计算**
* 支持自动求导

```python
import torch

x = torch.tensor([1.0, 2.0, 3.0])
```

---

## 4️⃣ Tensor vs NumPy array（高频对比题）

| 特性     | Tensor | NumPy |
| ------ | ------ | ----- |
| GPU 支持 | ✔      | ❌     |
| 自动求导   | ✔      | ❌     |
| 深度学习   | ✔      | ❌     |
| 科学计算   | ✔      | ✔     |

👉 **考试常问：**

> Which feature does PyTorch Tensor have but NumPy array does not?

✅ GPU + Autograd

---

## 5️⃣ Tensor 的创建方式（理解即可）

```python
torch.zeros(2,3)
torch.ones(2,3)
torch.rand(2,3)
torch.randn(2,3)
```

---

## 6️⃣ requires_grad（自动求导关键）

```python
x = torch.tensor([2.0], requires_grad=True)
```

### 📌 中文理解

* 表示这个 Tensor 是否参与梯度计算
* **训练参数必须设为 True**

👉 **考试问法：**

> What does requires_grad=True indicate?

✅ Track gradients for backpropagation

---

## 7️⃣ Autograd & backward()（⭐⭐⭐）

```python
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2
y.backward()

print(x.grad)  # dy/dx = 4
```

### 📌 中文解释

* Autograd 自动构建计算图
* `backward()` 计算梯度
* 梯度存储在 `.grad`

---

## 8️⃣ 动态计算图（Dynamic Computation Graph）⭐⭐

### 📌 英文

PyTorch uses a dynamic computation graph.

### 📌 中文（考试重点）

* **边运行边构建**
* 每次 forward 都可以不同
* 更易调试

👉 **考试爱问对比题：**

> PyTorch uses dynamic computation graphs.

✅ True

---

## 9️⃣ CPU vs GPU（CUDA）

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = x.to(device)
```

### 📌 中文

* GPU 适合大规模矩阵运算
* PyTorch 可在 CPU / GPU 间切换

---

## 🔟 PyTorch vs TensorFlow（概念对比）

| 项目   | PyTorch | TensorFlow |
| ---- | ------- | ---------- |
| 计算图  | 动态      | 静态（传统）     |
| 易调试  | ✔       | ❌          |
| 学习曲线 | 平缓      | 较陡         |

👉 **考试更偏概念，不考细节 API**

---

## 📝 三、选择题（MCQ 强化）

---

### **Q1. What is PyTorch mainly used for?**

A. Web development
B. Data visualization
C. Deep learning
D. Database management

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q2. What is a PyTorch Tensor?**

A. A Python list
B. A NumPy array
C. A multi-dimensional array with GPU support
D. A database object

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q3. Which PyTorch component supports automatic differentiation?**

A. Tensor
B. nn
C. optim
D. autograd

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：D**

</details>

---

### **Q4. What does `requires_grad=True` mean?**

A. Tensor is stored on GPU
B. Tensor is immutable
C. Tensor will track gradients
D. Tensor is read-only

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. What does `backward()` do?**

A. Updates parameters
B. Computes gradients
C. Makes predictions
D. Plots data

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q6. Which statement about PyTorch computation graph is correct?**

A. It is static
B. It is dynamic
C. It is fixed before execution
D. It cannot change

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

## ✅ Topic 12a 考前速记（你要背的）

✔ PyTorch 用途
✔ Tensor 是什么
✔ Tensor vs NumPy
✔ Autograd 作用
✔ backward()
✔ 动态计算图

---

太好了，我们进入 **Topic 12b — PyTorch（Model Training & Evaluation）** 👍
这是**第二次考试里 PyTorch 的“收官章”**，也是**最容易拿分的一章之一**，因为：

> ❗ **考试不考你写复杂网络**
> ❗ **只考：训练流程、名词对应、顺序判断**

我会 **完全贴合 Topic 12b PDF**，并用**考试视角**来讲。

---

# 🧠 Topic 12b — **PyTorch（Model Training & Evaluation）考试复习专用版**

---

## 📌 一、考试重点速览（Exam Focus）

在 CA6000 第二次考试中，**Topic 12b 通常考：**

### 🔥 高频必考

* 神经网络训练的 **完整流程**
* `nn.Module`
* `forward()` 的作用
* Loss Function（损失函数）
* Optimizer（优化器）
* `loss.backward()`
* `optimizer.step()`
* Training vs Evaluation
* `model.train()` vs `model.eval()`

### ⚠️ 高频陷阱

* forward ≠ backward
* loss ≠ optimizer
* `backward()` 不会更新参数
* evaluation 阶段 **不需要反向传播**
* `zero_grad()` 的作用

---

## 📘 二、神经网络训练核心概念（中英对照）

---

## 1️⃣ 什么是模型（Model）？

### 📌 英文（课件核心）

A model in PyTorch is typically defined as a class that inherits from `nn.Module`.

### 📌 中文（考试理解版）

* PyTorch 中的模型本质是一个 **类**
* 必须继承 `nn.Module`
* 包含：

  * 网络结构
  * forward 传播逻辑

```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        return x
```

👉 **考试常问：**

> What should a PyTorch model inherit from?

✅ `nn.Module`

---

## 2️⃣ forward()（前向传播）⭐⭐⭐

### 📌 英文

The `forward()` method defines how input data flows through the network.

### 📌 中文

* forward 定义 **数据如何通过网络**
* 自动被 PyTorch 调用
* 你不手动调用 `forward()`，而是 `model(x)`

👉 **高频 MCQ：**

> forward() is used for forward propagation ✅

---

## 3️⃣ Loss Function（损失函数）⭐⭐⭐

### 📌 英文

A loss function measures the difference between predicted output and true labels.

### 📌 中文

* 衡量模型预测的“错多少”
* 越小越好

```python
loss_fn = nn.MSELoss()
loss = loss_fn(y_pred, y_true)
```

👉 **考试常问：**

> What is the purpose of a loss function?

✅ Measure prediction error

---

## 4️⃣ Optimizer（优化器）⭐⭐⭐

### 📌 英文

An optimizer updates model parameters based on gradients.

### 📌 中文

* 用梯度来 **更新模型参数**
* 常见：SGD、Adam

```python
import torch.optim as optim

optimizer = optim.SGD(model.parameters(), lr=0.01)
```

👉 **必考概念：**

> Optimizer updates weights, not backward()

---

## 5️⃣ backward()（反向传播）⭐⭐⭐

```python
loss.backward()
```

### 📌 中文理解

* 计算梯度
* 梯度存储在 `.grad`
* **不更新参数**

👉 **超级高频陷阱题：**

> backward() updates model parameters ❌

---

## 6️⃣ optimizer.step()（参数更新）

```python
optimizer.step()
```

📌 **作用**

* 根据梯度更新参数
* 真正改变模型权重

---

## 7️⃣ zero_grad()（容易被忽略但必考）

```python
optimizer.zero_grad()
```

### 📌 中文

* 清空旧梯度
* 防止梯度累积

👉 **考试问法：**

> Why do we need zero_grad()?

✅ To clear previous gradients

---

## 8️⃣ 完整训练流程（⭐⭐⭐ 必背顺序）

```text
1. model.train()
2. optimizer.zero_grad()
3. y_pred = model(x)
4. loss = loss_fn(y_pred, y)
5. loss.backward()
6. optimizer.step()
```

👉 **顺序题必考**

---

## 9️⃣ Training vs Evaluation（训练 vs 测试）

---

### ✅ Training Mode

```python
model.train()
```

* 启用 dropout / batchnorm
* 需要反向传播

---

### ✅ Evaluation Mode

```python
model.eval()
```

* 关闭 dropout
* **不计算梯度**
* 用于测试

👉 **考试判断题：**

> model.eval() is used during evaluation phase ✅

---

## 🔟 torch.no_grad()（评估阶段）

```python
with torch.no_grad():
    y_pred = model(x)
```

📌 **作用**

* 禁止梯度计算
* 提升推理速度
* 减少内存占用

---

## 📝 三、选择题（MCQ 强化）

---

### **Q1. What class should a PyTorch model inherit from?**

A. torch.Tensor
B. nn.Model
C. nn.Module
D. torch.Model

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q2. What is the role of `forward()` in a PyTorch model?**

A. Compute gradients
B. Update weights
C. Define forward propagation
D. Evaluate accuracy

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q3. What does `loss.backward()` do?**

A. Updates model parameters
B. Computes gradients
C. Clears gradients
D. Makes predictions

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q4. Which function actually updates model weights?**

A. backward()
B. zero_grad()
C. forward()
D. optimizer.step()

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：D**

</details>

---

### **Q5. Why is `optimizer.zero_grad()` necessary?**

A. To update parameters
B. To clear old gradients
C. To stop training
D. To evaluate model

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：B**

</details>

---

### **Q6. Which mode should be used during model evaluation?**

A. model.train()
B. model.fit()
C. model.eval()
D. model.test()

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q7. What is the purpose of `torch.no_grad()`?**

A. Enable training
B. Compute gradients
C. Disable gradient computation
D. Update weights

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

## ✅ Topic 12b 考前速记（必背）

✔ nn.Module
✔ forward()
✔ loss function
✔ backward() ≠ update
✔ optimizer.step()
✔ zero_grad()
✔ train() vs eval()

---

## 🎯 PyTorch 总结（12a + 12b）

如果你能回答：

* PyTorch 是干嘛的
* Tensor vs NumPy
* 动态计算图
* 完整训练流程
* backward / optimizer.step 区别

👉 **PyTorch 这一整块基本稳了**。

---

很好，我们进入**第二次考试的最后一章** 🎯
**Topic 13 — TensorFlow（Features, Neural Network Modeling & Evaluation）**

这一章的**考试风格非常明确**：

> ⚠️ **不考复杂代码**
> ✅ **考：概念、流程、与 PyTorch 的对比、名词理解（MCQ）**

我会 **完全按课件 PDF 的知识范围来总结**，并用**考试友好的方式**呈现。

---

# 🧠 Topic 13 — **TensorFlow（Features, NN Modeling & Evaluation）考试复习专用版**

---

## 📌 一、考试重点速览（Exam Focus）

### 🔥 高频必考

* TensorFlow 是什么
* TensorFlow vs PyTorch（对比）
* TensorFlow 的核心组件
* Keras 是什么
* Sequential Model
* Compile / Fit / Evaluate
* Loss Function & Optimizer
* Training vs Evaluation

### ⚠️ 高频陷阱

* TensorFlow 默认是 **静态计算图**
* `compile()` ≠ `fit()`
* Keras 是 TensorFlow 的一部分
* `fit()` 才是训练
* `evaluate()` 只评估，不训练

---

## 📘 二、TensorFlow 核心概念（中英对照）

---

## 1️⃣ 什么是 TensorFlow？

### 📌 英文（课件核心）

TensorFlow is an open-source deep learning framework developed by Google.

### 📌 中文（考试理解版）

TensorFlow 是由 **Google 开发的深度学习框架**，主要特点：

* 高性能
* 工业级部署能力强
* 支持分布式训练
* 使用 **Keras** 作为高层 API

👉 **考试关键词**：
`deep learning`, `static graph`, `Keras`, `compile`, `fit`

---

## 2️⃣ TensorFlow 的核心组件

| 组件            | 作用     |
| ------------- | ------ |
| Tensor        | 数据结构   |
| Keras         | 高层 API |
| Model         | 神经网络   |
| Optimizer     | 参数更新   |
| Loss Function | 误差计算   |

---

## 3️⃣ Tensor（TensorFlow Tensor）

### 📌 英文

A Tensor is a multi-dimensional array used in TensorFlow.

### 📌 中文

* Tensor 是 TensorFlow 的基本数据结构
* 类似 NumPy array
* 但可运行在 CPU / GPU / TPU 上

```python
import tensorflow as tf

x = tf.constant([1, 2, 3])
```

👉 **考试对比点**：
TensorFlow Tensor vs PyTorch Tensor → 都支持 GPU

---

## 4️⃣ Keras（⭐⭐⭐ 必考）

### 📌 英文

Keras is a high-level API for building and training neural networks.

### 📌 中文

* Keras 是 TensorFlow 的**官方高层接口**
* 极大简化模型构建
* **考试 100% 会考**

👉 **判断题常见：**

> Keras is part of TensorFlow ✅

---

## 5️⃣ Sequential Model（顺序模型）⭐⭐⭐

### 📌 英文

Sequential model is a linear stack of layers.

### 📌 中文

* 一层接一层
* 最常见的模型结构
* 适合初学者

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(10, activation='relu'),
    Dense(1)
])
```

👉 **考试常问：**

> Sequential model is used to stack layers linearly ✅

---

## 6️⃣ compile()（模型配置）⭐⭐⭐

```python
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['accuracy']
)
```

### 📌 中文解释

`compile()` 用于指定：

* 优化器（optimizer）
* 损失函数（loss）
* 评估指标（metrics）

👉 **高频 MCQ：**

> What does compile() do?

✅ Configure training process

---

## 7️⃣ fit()（训练模型）⭐⭐⭐

```python
model.fit(X_train, y_train, epochs=10)
```

📌 **作用**

* 执行训练
* 自动完成 forward + backward

👉 **考试重点：**

> fit() trains the model ✅

---

## 8️⃣ evaluate()（模型评估）

```python
model.evaluate(X_test, y_test)
```

📌 **作用**

* 测试模型性能
* **不更新参数**

---

## 9️⃣ Training vs Evaluation（训练 vs 测试）

| 阶段         | 方法         | 是否更新参数 |
| ---------- | ---------- | ------ |
| Training   | fit()      | ✔      |
| Evaluation | evaluate() | ❌      |

---

## 🔟 TensorFlow 训练完整流程（⭐⭐⭐ 必背）

```text
1. Build model
2. Compile model
3. Train model (fit)
4. Evaluate model
```

👉 **顺序题高频**

---

## 1️⃣1️⃣ Loss Function（损失函数）

### 常见损失函数（考试只考名字）

| 任务 | Loss          |
| -- | ------------- |
| 回归 | MSE           |
| 分类 | Cross Entropy |

---

## 1️⃣2️⃣ Optimizer（优化器）

常见优化器：

* SGD
* Adam
* RMSprop

👉 **考试问法：**

> Optimizer updates model parameters ✅

---

## 1️⃣3️⃣ TensorFlow vs PyTorch（⭐⭐⭐ 必考对比）

| 项目   | TensorFlow | PyTorch |
| ---- | ---------- | ------- |
| 计算图  | 静态         | 动态      |
| 易调试  | ❌          | ✔       |
| 工业部署 | ✔✔✔        | ✔       |
| 学习曲线 | 较陡         | 平缓      |

👉 **考试爱考判断题**

---

## 📝 三、选择题（MCQ 强化）

---

### **Q1. TensorFlow is mainly used for?**

A. Web development
B. Game development
C. Deep learning
D. Database systems

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q2. Which API is commonly used to build models in TensorFlow?**

A. NumPy
B. PyTorch
C. Keras
D. Pandas

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q3. What does `compile()` do in TensorFlow?**

A. Train the model
B. Evaluate the model
C. Configure training process
D. Save the model

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q4. Which function is used to train a TensorFlow model?**

A. compile()
B. train()
C. fit()
D. run()

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q5. Which statement is TRUE?**

A. TensorFlow uses dynamic graphs by default
B. PyTorch uses static graphs
C. TensorFlow uses static graphs
D. Neither uses graphs

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：C**

</details>

---

### **Q6. What does `evaluate()` do?**

A. Trains the model
B. Updates weights
C. Computes gradients
D. Evaluates performance

<details>
<summary>答案 & 解析</summary>

✅ **正确答案：D**

</details>

---

## ✅ Topic 13 考前速记（你只需记住这些）

✔ TensorFlow 是什么
✔ Keras 是什么
✔ Sequential Model
✔ compile / fit / evaluate
✔ TensorFlow vs PyTorch

---

## 🎉 第二次考试知识点已全部覆盖！

你现在已经系统复习了：

| Topic | 内容               |
| ----- | ---------------- |
| 5     | NumPy            |
| 8     | Matplotlib       |
| 9     | Pandas           |
| 10    | Python Class     |
| 11    | Scikit-learn     |
| 12a   | PyTorch Overview |
| 12b   | PyTorch Training |
| 13    | TensorFlow       |

---

## 🔥 接下来我可以继续帮你做的（强烈推荐）

1️⃣ **整合一份《二次考试终极速记表（1–2 页）》**
2️⃣ **帮你出一整套【模拟 MCQ 试卷】+ 答案解析**
3️⃣ **把 PyTorch vs TensorFlow vs SKLearn 做成对比表（必拿分）**

👉 你只要告诉我：
**你想先要哪一个？**
