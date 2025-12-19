
---

# 📘 Quiz Simulation Test (Python & Machine Learning)

---

## Question 1

**Which of the following is the correct way to add matplotlib library to your application?**

* A. `import matplotlib as plt`
* B. `import matplotlib.pyplot as plt`
* C. `import matplotlib.plt`
* D. `from matplotlib import pyplot as plt`

### ✅ Correct Answer

**B,D**

### 📖 Explanation



### 🎯 Exam Focus

* Matplotlib basic import
* Library usage convention
* **Memory-based question**

---

## Question 2

**How do you save a Pandas DataFrame to a CSV file?**

* A. `df.write_csv("file.csv")`
* B. `df.save_csv("file.csv")`
* C. `df.export_csv("file.csv")`
* D. `df.to_csv("file.csv")`

### ✅ Correct Answer

**D**

### 📖 Explanation

Pandas uses the `to_xxx()` naming convention for exporting data, such as `to_csv()`, `to_excel()`.

### 🎯 Exam Focus

* Pandas I/O functions
* API naming rules

---

## Question 3

**What is the output of the following code?**

```python
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = arr.reshape(2, 3)
print(new_arr)
```

### ✅ Correct Answer

```text
[[1 2 3]
 [4 5 6]]
```

### 📖 Explanation

The array has 6 elements and is reshaped into 2 rows and 3 columns using row-major order.

### 🎯 Exam Focus

* NumPy `reshape()`
* Array dimensions
* **Understanding-based question**

---

## Question 4

**Which of the following application can use RNN for prediction?**

* A. Image recognition
* B. Time Series prediction
* C. Text summarization
* D. Object detection

### ✅ Correct Answer

**B**
*(If multiple answers allowed: B and C)*

### 📖 Explanation

RNNs are designed for sequential data, making them ideal for time series and text-based tasks.

### 🎯 Exam Focus

* RNN application scenarios
* Conceptual understanding

---

## Question 5

**Which of the following data structure is used during the ML training?**

* A. ndarray
* B. tensor
* C. dataframe
* D. list

### ✅ Correct Answer

**B**

### 📖 Explanation

Deep learning frameworks such as TensorFlow and PyTorch use **tensors** as the core data structure during training.

### 🎯 Exam Focus

* ML vs DL data structures
* Framework fundamentals

---

## Question 6

**The ( ______ ) method in PyTorch defines how the data flows through the model.**

### ✅ Correct Answer

**`forward`**

### 📖 Explanation

The `forward()` method defines the forward propagation logic of a PyTorch model.

### 🎯 Exam Focus

* PyTorch model structure
* Core API knowledge

---

## Question 7

**Which of the following functions can be used to optimize the parameters in TensorFlow?**

* A. Mean Square Error
* B. SGD
* C. Adam
* D. Mean Absolute Error

### ✅ Correct Answer

**B and C**
*(If single choice: C – Adam)*

### 📖 Explanation

SGD and Adam are optimizers, while MSE and MAE are loss functions.

### 🎯 Exam Focus

* Optimizer vs Loss function
* Deep learning fundamentals

---

## Question 8

**What is the main purpose of Keras?**

* A. To replace TensorFlow as a backend engine
* B. To simplify the building and training of model for TensorFlow
* C. To create low-level ML algorithms
* D. All of the above

### ✅ Correct Answer

**B**

### 📖 Explanation

Keras is a high-level API built on TensorFlow to simplify model construction and training.

### 🎯 Exam Focus

* Keras framework positioning
* High-level vs low-level APIs

---

## Question 9

**What is the purpose of an activation function in neural networks?**

* A. To optimize model performance
* B. To reduce model complexity
* C. To add non-linearity to the model
* D. To increase training speed

### ✅ Correct Answer

**C**

### 📖 Explanation

Activation functions introduce non-linearity, enabling neural networks to learn complex patterns.

### 🎯 Exam Focus

* Neural network theory
* Core conceptual question

---

## Question 10

**Which of the following is most suitable to be used with CNN?**

* A. Speech recognition
* B. Financial forecasting
* C. Image recognition
* D. Natural Language Processing

### ✅ Correct Answer

**C**

### 📖 Explanation

CNNs excel at spatial data processing, making them ideal for image recognition tasks.

### 🎯 Exam Focus

* CNN application scenarios
* Model selection

---

## Question 11

**How many trainable parameters are there in a Dense network?**

* Input = 10 nodes

* Output = 5 nodes

* A. 10

* B. 15

* C. 50

* D. 55

### ✅ Correct Answer

**D**

### 📖 Explanation

* Weights = 10 × 5 = 50
* Biases = 5
* Total = 55 parameters

### 🎯 Exam Focus

* Dense layer parameter calculation
* **High-frequency calculation question**

---

## Question 12

**What is the purpose of the `__init__` method in a Python class?**

* A. To access the attributes of an instance
* B. To create a new instance of a class
* C. To initialize the attributes for a new instance
* D. To define a new method

### ✅ Correct Answer

**C**

### 🎯 Exam Focus

* Python OOP
* Constructor behavior

---

## Question 13

**A ( ______ ) in Python is a blueprint for creating objects.**

### ✅ Correct Answer

**Class**

### 🎯 Exam Focus

* Object-Oriented Programming basics
* Definition recall

---

## Question 14

**What does the dunder method `__str__` perform?**

### ✅ Correct Answer

Defines the **string representation of an object**, used when calling `print()`.

### 🎯 Exam Focus

* Python magic (dunder) methods
* Object representation

---

## Question 15

**What does `super()` refer to in the following code?**

```python
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```

### ✅ Correct Answer

Refers to the **parent class (`Rectangle`)**.

### 📖 Explanation

`super()` is used to call methods from the parent class, typically the constructor.

### 🎯 Exam Focus

* Inheritance
* Parent class initialization

---

## 📌 Overall Exam Focus Summary

| Topic                  | Frequency |
| ---------------------- | --------- |
| NumPy reshape / arrays | ⭐⭐⭐⭐      |
| Pandas I/O             | ⭐⭐⭐       |
| CNN / RNN concepts     | ⭐⭐⭐⭐      |
| Tensor / Optimizer     | ⭐⭐⭐⭐⭐     |
| Dense parameters       | ⭐⭐⭐⭐⭐     |
| Python OOP             | ⭐⭐⭐⭐      |

---



---

## ✅ 问题 1

**Which of the following is the correct way to add matplotlib library to your application?**

**正确答案：**
👉 **B,D. `import matplotlib.pyplot as plt` `from matplotlib import pyplot as plt`**

### 解析

* `matplotlib.pyplot` 是 Matplotlib 中用于**绘图的子模块**
* 约定俗成使用 `plt` 作为别名

❌ A：`import matplotlib as plt`

* `matplotlib` 是整个包，不是绘图接口

❌ C：`import matplotlib.plt`

* 不存在这个模块

❌ D：`from matplotlib import pyplot as plt`

* **其实是正确的，但考试一般只认标准写法 B**

### 🎯 考点分析

* **Matplotlib 基本导入方式**
* **记忆型考点（送分题）**

---

## ✅ 问题 2

**How do you save a Pandas DataFrame to a CSV file?**

**正确答案：**
👉 **D. `df.to_csv("file.csv")`**

### 解析

* Pandas 中所有导出函数统一以 `to_xxx()` 命名

  * `to_csv`
  * `to_excel`
  * `to_json`

### 🎯 考点分析

* **Pandas I/O 接口**
* **API 命名规范（高频）**

---

## ✅ 问题 3

**Output of reshape**

```python
arr = np.array([1,2,3,4,5,6])
new_arr = arr.reshape(2,3)
print(new_arr)
```

**正确答案：**

```python
[[1 2 3]
 [4 5 6]]
```

### 解析

* 原数组长度 = 6
* reshape(2,3) → 2 行 3 列
* 按 **行优先（row-major）** 填充

### 🎯 考点分析

* **NumPy reshape**
* **数组维度理解（偏理解）**

---

## ✅ 问题 4

**Which application can use RNN for prediction?**

**正确答案：**
👉 **B. Time Series prediction**
👉 **C. Text summarization（如果允许多选）**

⚠️ 如果是**单选题**，标准答案是 **B**

### 解析

* RNN 擅长处理 **序列数据**
* 时间序列 = 最典型应用

### 🎯 考点分析

* **RNN 应用场景**
* **概念理解题**

---

## ✅ 问题 5

**Which data structure is used during ML training?**

**正确答案：**
👉 **B. tensor**

### 解析

* 在 **PyTorch / TensorFlow** 中，训练的基本数据结构是 **Tensor**
* ndarray / dataframe 常用于数据预处理阶段

### 🎯 考点分析

* **深度学习框架基础概念**
* **区分“数据准备 vs 训练”**

---

## ✅ 问题 6

**The (____) method in PyTorch defines how data flows through the model**

**正确答案：**
👉 **`forward`**

### 解析

* 在 PyTorch 中：

```python
def forward(self, x):
    ...
```

* 定义前向传播逻辑

### 🎯 考点分析

* **PyTorch 模型结构**
* **必背 API（极高频）**

---

## ✅ 问题 7

**Which functions optimize parameters in TensorFlow?**

**正确答案：**
👉 **B. SGD**
👉 **C. Adam**

⚠️ 如果单选 → **Adam（更常见）**

### 解析

* SGD / Adam = **优化器**
* MSE / MAE = **损失函数**

### 🎯 考点分析

* **Optimizer vs Loss function 区分**
* **DL 基础概念（高频）**

---

## ✅ 问题 8

**Main purpose of Keras**

**正确答案：**
👉 **B. To simplify the building and training of model for TensorFlow**

### 解析

* Keras 是 **高层 API**
* 封装复杂 TensorFlow 操作

❌ A：不是替代 TensorFlow
❌ C：不是低层算法
❌ D：错误（B 才是唯一正确）

### 🎯 考点分析

* **Keras 定位**
* **框架层级理解**

---

## ✅ 问题 9

**Purpose of activation function**

**正确答案：**
👉 **C. To add non-linearity to the model**

### 解析

* 没有激活函数 → 网络等价于线性模型
* ReLU / Sigmoid / Tanh 都是非线性

### 🎯 考点分析

* **神经网络核心原理**
* **必背理论题**

---

## ✅ 问题 10

**Most suitable for CNN**

**正确答案：**
👉 **C. Image recognition**

### 解析

* CNN = 卷积神经网络
* 擅长处理 **空间结构数据（图片）**

### 🎯 考点分析

* **CNN 应用场景**
* **经典送分题**

---

## ✅ 问题 11

**Trainable parameters in Dense layer**

Input = 10
Output = 5

**正确答案：**
👉 **D. 55**

### 计算过程

* 权重：10 × 5 = 50
* 偏置：5
* 总参数 = 50 + 5 = **55**

### 🎯 考点分析

* **Dense 层参数计算**
* **必考计算题**

---

## ✅ 问题 12

**Purpose of `__init__` method**

**正确答案：**
👉 **C. To initialize the method for a new instance**

### 解析

* `__init__` 在对象创建后自动执行
* 用于初始化属性

### 🎯 考点分析

* **Python OOP 基础**
* **构造函数概念**

---

## ✅ 问题 13

**A (____) in Python is a blueprint for creating objects**

**正确答案：**
👉 **Class**

### 🎯 考点分析

* **面向对象基础定义**
* **概念记忆题**

---

## ✅ 问题 14

**What does `__str__` do?**

**正确答案：**
👉 **Defines the string representation of an object**

### 示例

```python
print(obj)
```

→ 调用 `__str__`

### 🎯 考点分析

* **Dunder methods**
* **对象字符串表示**

---

## ✅ 问题 15

**What does `super()` refer to?**

```python
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```

**正确答案：**
👉 **Refers to the parent class (`Rectangle`)**

### 解析

* `super()` 用于调用父类的方法
* 这里调用的是 `Rectangle.__init__`

### 🎯 考点分析

* **继承**
* **父类构造函数调用**

---

## 🔥 全套考点总结（极重要）

| 模块                   | 高频程度  |
| -------------------- | ----- |
| NumPy reshape / axis | ⭐⭐⭐⭐  |
| Pandas I/O           | ⭐⭐⭐   |
| CNN / RNN 应用         | ⭐⭐⭐⭐  |
| Tensor / Optimizer   | ⭐⭐⭐⭐⭐ |
| Dense 参数计算           | ⭐⭐⭐⭐⭐ |
| Python OOP           | ⭐⭐⭐⭐  |

---

如果你愿意，下一步我可以：

* 🔥 把这套题**改写成你考试同款的选择题模拟卷**
* 🧠 针对 **Dense 参数 / Optimizer / Broadcasting** 出易错题
* 📄 做一页 **考试前 1 小时速记表**

你想直接冲哪一个？
