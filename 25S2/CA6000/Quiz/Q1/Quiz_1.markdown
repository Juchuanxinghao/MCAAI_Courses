
# 🎯 **CA6000 Quiz 复习资料（Topic 1, 2, 3, 6, 7）**

## 
    🔵Topic 1 — Python Basics
    🔵Topic 2 — Data Structures（List, Tuple, Dict, Set）
    🔵Topic 3 — Functions（函数）
    🔵Topic 6 — File Handling（文件操作）
    🔵Topic 7 — Error Handling（错误处理）
---

# 🔵 **Topic 1 — Python Basics**

来源：CA6000 - Topic 1 (Python Basics).pdf


## ✔ 必考重点（概念 + 代码分析）

### **1. Python 基础 / interpreter / input-output**

* `print()` 的功能
* `input()` 永远回传 **string** → 需 `int()` / `float()` 转换
* 代码执行顺序

### **2. 变量、常量、命名规范**

* 变量不需声明类型
* 大写字母 → 常量
* 命名规则（不能数字开头、区分大小写）

### **3. 数据类型（Data types）**

* `int`, `float`, `str`, `bool`
* 容器型：`list`, `tuple`, `set`, `dict`, `range`
* `type()`
* Casting 类型转换（很容易考）

### **4. 字符串（String）操作**

常用方法要记：

* 索引、切片
* `len()`
* `upper()`, `lower()`
* `strip()`
* `find()`
* `format()`

### **5. 条件判断（if / elif / else / match-case）**

* Boolean expression: `==`, `!=`, `<`, `>=`
* `and` / `or`
* match-case（简单匹配）

### **6. 循环（for / while / break / continue / pass）**

* `range(start, stop, step)` 默认从 0 开始
* while 搭配 break、continue

---

# 🔵 **Topic 2 — Data Structures（List, Tuple, Dict, Set）**

来源：CA6000 - Topic 2 (Data Structures).pdf


## ✔ 必考重点

### **1. List（列表）— 最常考**

* 特性：Ordered + Mutable + Allows duplicates
* 索引访问
* 修改、插入、删除
* 重要方法：
  `append()` / `insert()` / `remove()` / `pop()`
  `extend()` / `sort()` / `reverse()`

### **2. list comprehension（列表推导）**

* `[x for x in items if condition]`

### **3. enumerate()**

* `enumerate(list, start)`
* 返回 index 与 value

### **4. Tuple（元组）**

* Ordered + Immutable
* 常用方法：`count()`、`index()`
* 为什么 tuple 更安全（fixed size）

### **5. Dictionary（字典）**

* key-value pair
* keys() / values() / items()
* 修改：`dict[key] = value`
* 删除：`pop()`
* 嵌套字典（Nested Dict）

### **6. Set（集合）**

* Unordered + unique
* 自动去重
* 集合运算：

  * union (`|`)
  * intersection (`&`)
  * difference (`-`)

---

# 🔵 **Topic 3 — Functions（函数）**

来源：CA6000 - Topic 3 (Functions).pdf


## ✔ 必考重点

### **1. Function definition**

* `def function_name(parameters):`
* indentation 表示 function body

### **2. Parameters vs Arguments**

* argument (调用时传入的数据)
* parameter（函数接收的数据）

### **3. Default parameters（默认参数）**

### **4. Variable-length parameters**

* `*args`：不确定数量参数

### **5. 返回值（return）**

* 没 return → return None
* return string / number / list

### **6. Scope（变量作用域）**

* local
* global（使用 `global var_name`）

### **7. lambda（匿名函数）**

* 用法：`lambda x,y: x+y`
* 多见于 filter()

### **8. Generator（yield）**

* return one value at a time
* 节省内存（on-the-fly）

### **9. Decorator（装饰器）**

* 写法：

  ```python
  @decorator
  def function():
  ```
* 作用：对函数进行功能扩展（如检查除法是否 y=0）

---

# 🔵 **Topic 6 — File Handling（文件操作）**

来源：CA6000 - Topic 6 (Files).pdf


## ✔ 必考重点

### **1. open() 函数**

* `open(filename, mode)`
* mode 要记！

  * `"r"` read
  * `"w"` overwrite
  * `"a"` append
  * `"r+"` / `"w+"` / `"a+"`

### **2. 文件读取**

* `file.read()`
* `file.readline()`
* loop through lines

### **3. 文件写入**

* `"w"` truncates (清空)
* `"a"` append

### **4. with 语法（自动关闭文件）**

```python
with open("x.txt","r") as f:
```

### **5. CSV 操作**

* `csv.reader` → list
* `csv.DictReader` → dictionary

### **6. JSON 操作**

* `json.loads()` 把 JSON 字串变成 dict

---

# 🔵 **Topic 7 — Error Handling（错误处理）**

来源：CA6000 - Topic 7 (Error Handling).pdf


## ✔ 必考重点

### **1. try / except**

* try: 执行代码
* except: 捕捉错误

### **2. 常见异常类型（要能辨识）**

* `NameError`
* `ValueError`
* `KeyError`

### **3. else**

* 没有发生 exception 时执行

### **4. finally**

* 一定会执行（用来关文件）

### **5. assert（断言）**

* condition 为 False → 报 `AssertionError`

---



# 📘 **Quiz 题型预测（根据所有 PDF 内容整理）**

### ✔ 多选题 / 单选题例子

* 找出哪一个是 tuple
* 哪一个是合法 variable name
* 哪一个会产生 ValueError
* 哪一个文件模式会清空文件（答案 w / w+）

### ✔ 简答题例子

* 解释 decorator 的作用
* 解释 list 和 tuple 的差异
* 为什么要用 try-except？
* 什么是 generator？

### ✔ 代码逻辑分析题（最重要）

你需要能阅读下面这种代码并解释输出：

```python
fruits = ["apple","banana","cherry"]
for index, item in enumerate(fruits, 10):
    print(index, item)
```

或：

```python
try:
    print(x)
except NameError:
    print("variable not found")
```

或：

```python
def add(x, y=10):
    return x + y
print(add(5))
```

---

