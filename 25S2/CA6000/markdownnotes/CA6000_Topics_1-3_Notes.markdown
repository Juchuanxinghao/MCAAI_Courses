# 🧠 CA6000 Programming Notes (Topic 1--3)

*Expanded with examples and explanations*

------------------------------------------------------------------------

## 🧩 **Topic 1 -- Python Basics / Python 基础**

### 1️⃣ Python Overview / Python 概述

Python 是一种易于学习、跨平台的语言，广泛用于 AI 和数据科学领域。

``` python
# Example: Print a message
print("Hello, Python!")
print("Python is powerful for AI and ML.")
#print输出默认会换行，如果连续输出两个值想要中间不换行，需要带上:end=""
print("Hello, Python!",end="")
print("Python is powerful for AI and ML.")

'''
results:

Hello, Python!
Python is powerful for AI and ML.
Hello, Python!Python is powerful for AI and ML.
'''
```

------------------------------------------------------------------------

### 2️⃣ User Input / Output / 用户输入输出

``` python
# Output
print("Welcome to Python programming!")

# Input
name = input("What is your name? ")
print("Hello " + name)

# Casting input (string → float)
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
print("Sum:", x + y)
'''
results:

Welcome to Python programming!
What is your name?  JU
Hello JU
Enter a number:  123
Enter another number:  1230
Sum: 1353.0
'''
```

------------------------------------------------------------------------

### 3️⃣ Variables, Constants, and Comments / 变量、常量、注释
#### 注释：
python中单行注释以 # 开头;

多行用：''' or """
#### 
``` python
"""
多行语句:
可以用 \ 实现多行语句
"""
a = sum_1 +\
    sum_2 +\
    sum_3
# 在{},[]或()中的多行语句不需要用\来分行
```
``` python
# Variable assignment
a = "Hello"
b = 5
print(a, b)

# Reassign with a different type
a = 10.5
print(a)

# Constant (convention: uppercase)
PI = 3.14159
MAX_SCORE = 100

# Comments
# This is a single-line comment
'''
This is a multi-line comment (docstring)
Used to describe functions or modules.
'''
```

------------------------------------------------------------------------

### 4️⃣ Data Types / 数据类型

``` python
'''
there are 4 type of number in python:4种数字类型
int:整数
bool:true/false
float:浮点数，如1.23，3E-2
complex：复数（实数+虚数），形式为a+bj，如1+2j，1.1+2.2j
'''
```
```python
text = "Hello"
number = 42
decimal = 3.14
is_valid = True
fruits = ["apple", "banana"]
person = {"name": "Nick", "age": 25}

print(type(text), type(number), type(decimal), type(is_valid), type(fruits), type(person))

'''
results:
<class 'str'> <class 'int'> <class 'float'> <class 'bool'> <class 'list'> <class 'dict'>
'''
```

------------------------------------------------------------------------

### 5️⃣ String Manipulation / 字符串操作

``` python
text = "  Hello World!  "
print(text[0])          # Indexing
print(text[0:5])        # Slicing
print(len(text))        # Length
print(text.strip())     # Remove spaces 移除空白
print(text.lower())     # Lowercase 全部小写
print(text.upper())     # Uppercase 全部大写
print(text.find("World"))  # Find substring
print("My age is {}".format(22))  # Format string

'''
results:

  Hel
16
Hello World!
  hello world!  
  HELLO WORLD!  
8
My age is 22
'''
```
```python
text = "Hello_World! "
print(text[0])          # Indexing
print(text[0:5])        # Slicing
print(len(text))        # Length
print(text.strip())     # Remove spaces
print(text.lower())     # Lowercase
print(text.upper())     # Uppercase
print(text.find("World"))  # Find substring
print("My age is {}".format(22))  # Format string

'''
results:
H
Hello
13
Hello_World!
hello_world! 
HELLO_WORLD! 
6
My age is 22
'''
```
------------------------------------------------------------------------

### 6️⃣ Conditional Execution / 条件执行

``` python
a, b = 10, 5
if a > b:
    print("a is greater than b")
elif a == b:
    print("a equals b")
else:
    print("a is smaller than b")

# match-case (Python 3.10+)
grade = "B"
match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good!")
    case _:
        print("Keep trying!")
```

------------------------------------------------------------------------

### 7️⃣ Loops / 循环

``` python
# while loop
i = 1
while i <= 5:
    print("Count:", i)
    i += 1

# for loop
for x in range(3):
    print("Iteration", x)

# Using continue and break
for x in range(10):
    if x == 5:
        continue
    if x == 8:
        break
    print(x)

'''
results:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
Iteration 0
Iteration 1
Iteration 2
0
1
2
3
4
6
7
'''

'''
range()是python内置的一个序列生成器，用来生成一串整数。
语法是：
range([start],stop,[step])
[start],[step]是可选参数
start:起始值(默认为0)
stop:结束值(不包括这个值)
step:步长(默认是1)
e.g：
range(5):[0,1,2,3,4]
range(2,6):[2.3.4.5]
range(1,10,2):[1,3,5,7,9]
'''
```

------------------------------------------------------------------------

## 🧩 **Topic 2 -- Data Structures / 数据结构**

### 1️⃣ List / 列表

``` python
fruits = ["banana", "cherry", "apple"]
print(fruits[0])        # Access by index
fruits.append("durian") # Add item
print(fruits)
fruits.remove("banana") # Remove item
print(fruits)
fruits.sort()           # Sort list
print(fruits)

# List comprehension
new_list = [x.upper() for x in fruits if "a" in x]
print(new_list)

'''
results:
banana
['banana', 'cherry', 'apple', 'durian']
['cherry', 'apple', 'durian']
['apple', 'cherry', 'durian']
['APPLE', 'DURIAN']
'''
```

------------------------------------------------------------------------

### 2️⃣ Tuple / 元组

``` python
t = ("apple", "banana", "cherry")
print(t[1])
print(t.count("apple")) #统计该元素的数目
print(t.count("banana"))
print(t.count("cherry"))
print(t.index("banana")) #找出该元素的位置（从0开始计算）
print(t.index("apple"))
print(t.index("cherry"))

# Tuple → List → modify → Tuple
t = list(t)
t.append("durian")
t = tuple(t)
print(t)


'''
results:
banana
1
1
1
1
0
2
('apple', 'banana', 'cherry', 'durian')
'''
```
------------------------------------------------------------------------

### 3️⃣ Dictionary / 字典

``` python
car = {"brand": "BYD", "model": "SEAL", "year": 2024}
print(car["model"])
car["year"] = 2025
car["color"] = "Red"
print(car.keys(), car.values())

# Dictionary comprehension
fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)
```

------------------------------------------------------------------------

### 4️⃣ Set / 集合

``` python
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "durian"}

print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference

# Remove duplicates from list
nums = [1, 2, 2, 3, 3, 4]
unique_nums = list(set(nums))
print(unique_nums)
```

------------------------------------------------------------------------

## 🧩 **Topic 3 -- Functions / 函数**

### 1️⃣ Defining and Calling Functions / 定义与调用

``` python
def greet():
    print("Hello from a function!")

greet()
```

------------------------------------------------------------------------

### 2️⃣ Parameters and Return Values / 参数与返回值

``` python
def add(x, y):
    return x + y

result = add(5, 10)
print("Sum:", result)

def introduce(name="Nick", age=25):
    return f"My name is {name}, and I am {age} years old."

print(introduce("Chen", 22))
```

------------------------------------------------------------------------

### 3️⃣ Variable Scope / 变量作用域

``` python
x = 10  # Global

def show():
    global x
    x = 20  # modifies global x
    print("Inside function:", x)

show()
print("Outside function:", x)
```

------------------------------------------------------------------------

### 4️⃣ Lambda Function / 匿名函数

``` python
square = lambda x: x**2
print(square(5))

# Using lambda in filter()
nums = [1, 12, 13, 24, 35, 38, 47]
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd)
```

------------------------------------------------------------------------

### 5️⃣ Generator Function / 生成器

``` python
def generator():
    yield "Apple"
    yield "Banana"
    yield "Cherry"

for fruit in generator():
    print(fruit)
```

------------------------------------------------------------------------

### 6️⃣ Decorator Function / 装饰器

``` python
def guard_zero(func):
    def wrapper(x, y):
        if y == 0:
            print("Cannot divide by 0.")
            return
        return func(x, y)
    return wrapper

@guard_zero
def divide(x, y):
    return x / y

print(divide(10, 2))
print(divide(5, 0))
```

------------------------------------------------------------------------

## ✅ Summary

-   **Topic 1:** Python 基础语法、输入输出、控制结构\
-   **Topic 2:** 数据结构：List, Tuple, Dictionary, Set\
-   **Topic 3:** 函数定义、作用域、返回值、Lambda、装饰器、生成器
