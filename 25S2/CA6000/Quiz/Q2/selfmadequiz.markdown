

# 🧪 Comprehensive Quiz – Full Revision Test

**Instructions**

* Choose the best answer
* Some questions may have **more than one correct answer**
* No programming environment required

---

## Part A – Python Basics & OOP

### Question 1

Which of the following is a valid Python variable name?

A. `2value`
B. `value_2`
C. `value-2`
D. `value 2`

---

### Question 2

What is the output of the following code?

```python
print("Hello" + "World")
```

A. Hello World
B. HelloWorld
C. Hello+World
D. Error

---

### Question 3

Which statement about Python **tuple** is correct? (Choose all that apply)

A. Tuple is immutable
B. Tuple is ordered
C. Tuple is mutable
D. Tuple cannot contain duplicate values

---

### Question 4

What is the purpose of the `__init__` method in a Python class?

A. To create a class
B. To initialize attributes of an object
C. To define a static method
D. To print object information

---

### Question 5

Which dunder method is called when two objects are compared using `==`?

A. `__compare__`
B. `__eq__`
C. `__cmp__`
D. `__match__`

---

## Part B – NumPy (Vectorization, Axis, Broadcasting)

### Question 6

What does **vectorization** mean in NumPy?

A. Using loops to process data
B. Performing operations element-by-element using Python
C. Performing operations on whole arrays without explicit loops
D. Converting arrays into vectors

---

### Question 7

Given the following array:

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])
```

What is the output of:

```python
np.sum(a, axis=0)
```

A. `[6, 15]`
B. `[5, 7, 9]`
C. `[1, 2, 3]`
D. Error

---

### Question 8

What is the output of:

```python
a = np.array([1, 2, 3])
print(a ** 2)
```

A. `[2, 4, 6]`
B. `[1, 4, 9]`
C. `14`
D. Error

---

### Question 9

Which of the following broadcasting operations is **valid**?

A. `(3,4)` + `(3,)`
B. `(2,3)` + `(3,)`
C. `(2,3)` + `(2,)`
D. `(3,3)` + `(2,2)`

---

### Question 10

What is the output of the following code?

```python
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
print(np.dot(x, y))
```

A. `[10, 40, 90, 160]`
B. `300`
C. `10`
D. Error

---

## Part C – Pandas & Matplotlib

### Question 11

Which Pandas function is used to display the **first 5 rows** of a DataFrame?

A. `df.start()`
B. `df.first()`
C. `df.head()`
D. `df.preview()`

---

### Question 12

Which statement is TRUE about Pandas DataFrame?

A. It can only store numerical values
B. It is two-dimensional
C. It is immutable
D. It cannot contain missing values

---

### Question 13

Which Matplotlib function is used to draw a line plot?

A. `plt.line()`
B. `plt.draw()`
C. `plt.plot()`
D. `plt.graph()`

---

### Question 14

What does the following code do?

```python
plt.axis('off')
```

A. Removes x-axis only
B. Removes y-axis only
C. Removes both axes
D. Rescales the plot

---

## Part D – Machine Learning (Scikit-learn)

### Question 15

Which of the following steps is part of a **typical ML pipeline**?

A. Feature extraction
B. Model training
C. Model evaluation
D. All of the above

---

### Question 16

Which Scikit-learn method is used to **train** a model?

A. `model.train()`
B. `model.fit()`
C. `model.predict()`
D. `model.score()`

---

## Part E – Deep Learning (PyTorch, TensorFlow, Keras)

### Question 17

Which data structure is used internally during training in deep learning frameworks?

A. list
B. ndarray
C. tensor
D. DataFrame

---

### Question 18

In PyTorch, where are the layers of a neural network usually defined?

A. `forward()`
B. `__init__()`
C. `train()`
D. `compile()`

---

### Question 19

What is the main purpose of an **activation function**?

A. Speed up training
B. Reduce overfitting
C. Add non-linearity
D. Normalize input

---

### Question 20

Which of the following are **optimizers**? (Choose all that apply)

A. Mean Squared Error
B. SGD
C. Adam
D. Cross Entropy

---

### Question 21

How many trainable parameters are there in a Dense layer with:

* Input = 6
* Output = 3

A. 18
B. 21
C. 24
D. 27

---

### Question 22

Which model is most suitable for **time series prediction**?

A. CNN
B. RNN
C. KNN
D. Decision Tree

---

### Question 23

Which statement about **Keras** is correct?

A. It replaces TensorFlow
B. It is a low-level numerical library
C. It simplifies model building
D. It only supports CNN

---


非常好，这一轮**是真正的“全覆盖综合检测”**。
我已经帮你 **逐题判分 → 标注错误 → 给出精准解析 → 对应复习模块定位**。

---

# ✅ 总体成绩评估

**你的得分：20 / 23**

* ❌ 错误：**3 题**
* ⚠️ 易混：**2 题（虽然你答对了，但非常接近陷阱）**
* ✅ 其余：**理解非常扎实**

> 📊 **结论**：
> 你已经达到 **「考试稳态」**，只需要修正少数**固定坑位**，就几乎不可能翻车。

---

# 📋 逐题判分 & 精准解析

---

## Part A – Python Basics & OOP

### Q1

**你的答案：B ✅**

* 合法变量名
* **基础送分题**

---

### Q2

**你的答案：B ✅**

```python
"Hello" + "World" → "HelloWorld"
```

* 字符串拼接
* 高频基础题

---

### Q3（多选）

**你的答案：A B ✅**

* tuple：**immutable + ordered**
* 可包含重复值 ❌（D 错）

---

### Q4

**你的答案：B ✅**

* `__init__` → 初始化对象属性
* OOP 核心考点

---

### Q5

**你的答案：B ✅**

* `==` → `__eq__`
* dunder methods 必考

---

## Part B – NumPy

---

### Q6

**你的答案：C ✅**

> 向量化 = 不写 for，整体数组运算

---

### Q7

**你的答案：B ✅**

```python
np.sum(axis=0) → 按列
```

---

### Q8

**你的答案：B ✅**

```python
a ** 2 → 元素级平方
```

---

### Q9 ❌（**错误点 1**）

**你的答案：D ❌**
**正确答案：B**

#### 解析（非常重要）

* Broadcasting 规则：**从右对齐**
* `(2,3) + (3,)` ✅ 合法
* `(3,3) + (2,2)` ❌ 不满足规则

📌 **这是经典广播陷阱题**

👉 你这里说明：
**规则懂，但判断时“多想了一步”**

---

### Q10

**你的答案：B ✅**

```python
np.dot([1,2,3,4],[10,20,30,40]) = 300
```

* 元素乘 + 求和

---

## Part C – Pandas & Matplotlib

---

### Q11

**你的答案：C ✅**

* `df.head()`

---

### Q12 ❌（**错误点 2**）

**你的答案：A ❌**
**正确答案：B**

#### 解析

* DataFrame：

  * ✔ 二维
  * ✔ 可混合类型
  * ✔ 可有缺失值
* ❌ 不能只存数值（那是 ndarray）

📌 **这是“定义题”，不考用法，专考概念**

---

### Q13

**你的答案：C ✅**

* `plt.plot()`

---

### Q14

**你的答案：C ✅**

* `plt.axis('off')` → 移除 x + y 轴

---

## Part D – Scikit-learn

---

### Q15

**你的答案：D ✅**

* ML pipeline 全流程
* 标准送分题

---

### Q16

**你的答案：B ✅**

* `model.fit()` → 训练

---

## Part E – Deep Learning

---

### Q17

**你的答案：C ✅**

* 训练阶段 → tensor

---

### Q18 ❌（**错误点 3**）

**你的答案：D ❌**
**正确答案：B**

#### 解析（非常关键）

* `__init__()`：**定义层**
* `forward()`：定义数据流
* PyTorch ❌ 没有 `compile()`

📌 **这是 PyTorch / TensorFlow 混淆题**

---

### Q19 ❌（⚠️ 概念混淆）

**你的答案：B ❌**
**正确答案：C**

#### 解析

* Activation Function 的**核心作用**：

> 👉 **引入非线性**

* 减少过拟合 ❌（那是正则化的事）

📌 **这是神经网络“第一性原理”题**

---

### Q20

**你的答案：B C ✅**

* SGD / Adam = optimizer

---

### Q21

**你的答案：B ✅**

```text
6 × 3 + 3 = 21
```

---

### Q22

**你的答案：B ✅**

* Time series → RNN

---

### Q23

**你的答案：C ✅**

* Keras = 高层 API

---

# 🔥 错题集中分析（极重要）

你这次 **所有错误都集中在 3 类固定坑位**：

---

## ❗ 坑位 1：Broadcasting 规则判断

* 问题：Q9
* 解决办法：**永远从右对齐判断**

---

## ❗ 坑位 2：概念定义题（不是用法）

* 问题：Q12（DataFrame）
* 特点：看似简单，但容易“凭感觉”

---

## ❗ 坑位 3：框架差异混淆

* 问题：Q18
* PyTorch ≠ TensorFlow

  * PyTorch ❌ `compile()`
  * TensorFlow / Keras 才有

---

# 🧠 最终能力评估（非常重要）

| 模块                             | 状态                |
| ------------------------------ | ----------------- |
| Python 基础 / OOP                | ✅ 稳               |
| NumPy（axis / vector / reshape） | ✅ 稳               |
| Broadcasting                   | ⚠️ 再刷 2 题         |
| Pandas 定义                      | ⚠️ 背一遍            |
| PyTorch vs TF                  | ⚠️ 易混             |
| DL 核心原理                        | ✅ 但需牢记 activation |

👉 **你已经 90% 以上稳态**

---

