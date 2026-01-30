# Chapter 1 (1.1–1.8) Quiz Revision Notes — **Bilingual (EN + 中文)**

*(Exam is in English, so I’ll write  **English first** , then add **中文解释** to help you记忆。)*

---

## 1.1 Introduction — What is Data Visualisation & Why it matters

### Definition

* **Data visualisation** : transforming data into an image using appropriate  **visual encoding strategies** .
* **Visual encoding** : the **mapping from data to image** using **visual marks** +  **visual variables/channels** .

**中文解释**

* 数据可视化就是把数据“变成图”，但关键是要用合适的编码方式（把数据映射成图形元素与视觉属性）。

### Big idea to remember

* A graphic is a **responsibility** in decision-making (Bertin’s quote).

**中文解释**

* 图表会影响决策，所以不是“画得好看”就行，必须准确、负责任。

---

## 1.2 Data Attributes — NOIR scales + data dimensionality + special data types

### A) Stevens’ NOIR scale (Levels of Measurement)

Stevens proposed 4 measurement scales: **Nominal, Ordinal, Interval, Ratio** (NOIR).

#### 1) Nominal (N)

* **Labels/categories** , no order, no numeric meaning.
* Valid operations:  **=, ≠** .
* Common charts: bar, pie (countable).

**中文解释**

* 名义尺度：只是分类标签（性别/颜色/口味），不能比较大小，只能判断相同或不同。

#### 2) Ordinal (O)

* Ordered categories, but  **differences not meaningful** .
* Valid operations:  **=, ≠, <, >** .

**中文解释**

* 顺序尺度：有顺序（评分/等级），但“A比B好多少”没有客观距离。

#### 3) Interval (I)

* Numeric with meaningful  **differences** ,  **no true zero** .
* Valid operations: **=, ≠, <, >, +, −** (but not ×/÷).
* Example: °C/°F, dates.

**中文解释**

* 区间尺度：差值有意义，但0不是“没有”（0°C不是无温度），所以不能做倍数比较。

#### 4) Ratio (R)

* Numeric with  **absolute zero** , supports proportion.

**中文解释**

* 比例尺度：有真实0点（例如长度、重量、人数），可以说“是两倍”。

---

### B) Relational data model & Dimensionality

* Structured data:  **rows = observations** ,  **columns = attributes** .
* Each row is a  **tuple** ; columns can be called  **dimensions** .

**中文解释**

* 表格数据：行=样本，列=特征；一行就是一个tuple（元组/记录）。

**Dimensionality examples**

* **0-D** : single value → gauges/thermometer/bullet graphs.
* **1-D** : one attribute (1 column) → e.g., pie chart.
* **2-D** : two related attributes → chart depends on scales (e.g., ratio+ordinal → line).
* **3-D** : need extra attributes like colour/size/shape.
* **n-D** : use combinations of attributes matched to NOIR (e.g., colour+shape for nominal; position/size for quantitative).

---

### C) Other important data attributes

#### 1) Hierarchy

* Tree-structured data: nodes with children; visualise with  **tree diagram** ,  **treemap** ,  **sunburst** ,  **circle packing** , etc.

#### 2) Temporal

* Time dimension representing state in time, often uniformly spaced; charts include  **line/bar** ,  **stacked area** ,  **scatter** , **polar area** (cyclical).

#### 3) Spatial (Geospatial)

* Location-related attributes; can include coordinates + attributes + sometimes time.
* Maps:  **choropleth** ,  **dot density** ,  **bubble map** ,  **heat map** , etc.

**中文记忆口诀（超好用）**

* **层级**看“组织结构”(tree/treemap)；**时间**看“随时间变化”(line/area)；**空间**看“地图位置”(choropleth/bubble map)。

---

## 1.3 Visual Encoding — Marks + Channels (Visual Variables) + effectiveness

### A) Visual encoding process

* Data visualisation transforms data into an image using  **visual encoding strategies** .

### B) Bertin’s Visual Variables (channels)

Bertin’s 7 main visual variables:

* **position, size, shape, value (intensity), colour, orientation, texture**

**中文解释**

* Bertin提出“视觉变量”= 人眼能感知并用来编码信息的属性，比如位置/大小/颜色深浅等。

### C) Marks vs Channels

* **Marks** : basic geometric elements depicting items/links (points, lines, areas).
* **Channels** : control appearance of marks (position/size/colour/etc.).

Also, Munzner’s mark types:

* **Item marks** depict items; **link marks** show relationships (pairwise/group).

### D) Encoding effectiveness depends on data scale (NOIR)

* Hue is generally **unordered** → best for  **nominal** .
* Value (brightness) can encode **ordered** when discretised, but lacks precision when continuous.
* Interval & ratio are treated as  **quantitative** .

### E) Mackinlay’s effectiveness ranking (idea)

* Mackinlay expanded Bertin and ranked channels by effectiveness for quantitative/ordinal/nominal; effectiveness = how readily info is perceived by audience.

### F) Typical encodings by dimensionality

* **Univariate** : lines/bars, dot plots.
* **Bivariate** : 2D scatter (points); sometimes dual-axis bar (careful).
* **Trivariate** : scatter with dot **area/size** encoding 3rd variable.

### G) Redundant encoding

* Using **>1 channel** (e.g., colour+shape) to encode the  **same variable** ; helps perception faster/easier/more accurate if channels available.

---

## 1.4 Comparison Plots — Compare values across categories or time

### Core purpose

* Comparison plots help compare magnitudes among categories/time (typical: bar/line, etc.). (Covered in comparison plot chapter; key exam focus is correct usage + pitfalls.)

### Key pitfall: misleading comparison

* Truncated axes or inconsistent baselines can exaggerate differences (common “ethics” test in MCQ).
  *(This idea aligns with “ethical visualisation: use fair and consistent visual encoding”.)*

**中文记忆**

* 对比类图表最怕“截断纵轴/不从0开始/尺度不一致”，会让差异看起来被放大。

---

## 1.5 Composition Plots — Part-to-whole

### Definition

* **Composition plots** : show how categories form a  **whole** ; common examples include pie, stacked bar/area, etc.

### When to use

* Best when you want to show **proportions** (share of total).

### Common pitfalls (MCQ favourite)

* Too many segments → hard to compare.
* Pie/donut: human angle/area comparison is weak (often worse than bars).

---

## 1.6 Relationship Plots — Show relationships/patterns among variables

### A) What relationship plots do

* Help show  **relationships or patterns among variables** .

### B) Scatter plot

* Uses **2D position** of dots to** *represent two numeric variables***; dot patterns reveal correlation/patterns.
* Can reveal  **clusters** ,  **gaps** ,  **outliers** .

### C) Bubble plot

* Encodes a **third variable** by dot size.

### D) Heatmap

* Useful when variables are non-continuous/non-numeric; show relationships via  **grid of coloured values** .
* Choosing palette: diverging palette if meaningful zero; include legend; sequential ramp common.

### E) Trend lines (linear regression, polynomial, LOWESS)

* Trend lines show best fit; Seaborn regplot fits linear regression and shows confidence interval.
* **LOWESS** : non-parametric, computed piecewise using local weighted regressions; neighbourhood fraction `frac` controls window size.

---

## 1.7 Distribution Plots — Understand the distribution of a variable

### Box plot: key elements (must know)

* The box spans **Q1 to Q3** (25th to 75th percentile), middle line is  **median** ; whiskers often extend to  **1.5×IQR** , points beyond are outliers.

**中文解释**

* 箱线图：箱体=Q1到Q3，中线=中位数；IQR=Q3−Q1；超过1.5×IQR通常算异常值。

### Histogram: key concept

* Depends on **bin width/number of bins** (affects perceived shape). (Often asked as “which parameter changes the histogram appearance most?”)

---

## 1.8 Know the Right Chart Type — Choose based on question + data type

A super common MCQ pattern is: **Given a scenario, which chart type is most appropriate?**
Use this decision logic:

### A) What question are you answering?

1. **Comparison** → compare values (bar/line)
2. **Composition** → part-to-whole (stacked, pie sometimes)
3. **Relationship** → correlation/pattern (scatter/bubble/heatmap)
4. **Distribution** → spread/shape/outliers (hist/box/violin)

This matches the chapter structure and the “relation/composition” definitions used across slides.

### B) Data type rules (NOIR → channel choice)

* **Nominal** : hue/shape good; don’t imply order.
* **Ordinal** : value (intensity) can encode order when discretised.
* **Quantitative (Interval/Ratio)** : position/length usually strongest; be careful with area.

---

# High-Yield MCQ Practice (with Answers + Bilingual Explanations)

## Q1

**Which best defines visual encoding?**
A. Sorting data values
B. Mapping data into an image using marks and channels
C. Removing outliers
D. Using charts to decorate a report

✅ **Answer: B**
**Why (EN):** Visual encoding is the mapping from data to image using visual marks + variables.
**中文：** 视觉编码=把数据映射到图像（用marks+channels）。

## Q2

**Which is NOMINAL data?**
A. Temperature in °C
B. Star ratings (1–5)
C. Hair colour
D. Weight (kg)

✅ **Answer: C**
**Why (EN):** Nominal = labels/categories with no order.
**中文：** 名义尺度=纯分类标签，无顺序。

## Q3

**Which operation is valid for ORDINAL data?**
A. Multiplication
B. Division
C. Greater-than (>)
D. Subtraction

✅ **Answer: C**
**Why:** Ordinal supports ordering comparisons (<, >) but not meaningful arithmetic differences.

## Q4

**Why can’t interval data be meaningfully multiplied/divided?**
A. It is not numeric
B. It has no true zero
C. It is unordered
D. It always has outliers

✅ **Answer: B**
**Why:** Interval scale lacks absolute zero, so ×/÷ isn’t valid.

## Q5

**In a relational data model, each row is a _____.**
A. Dimension
B. Tuple
C. Bin
D. Palette

✅ **Answer: B**

## Q6

**Which plot is best to show correlation between two numeric variables?**
A. Pie chart
B. Scatter plot
C. Tree diagram
D. Gauge

✅ **Answer: B**

## Q7

**Bubble plots mainly extend scatter plots by adding:**
A. A confidence interval
B. A third variable using dot size
C. A diverging palette
D. A median line

✅ **Answer: B**

## Q8

**Heatmaps are especially useful when:**
A. Both variables are continuous numeric only
B. Variables are non-continuous or non-numeric categories
C. You only have one value
D. You need to show hierarchy

✅ **Answer: B**

## Q9

**Which describes an OUTLIER in a scatter plot?**
A. A dense group of dots
B. A dot far off from clusters
C. An empty region
D. A trend line

✅ **Answer: B**

## Q10

**In a box plot, the box typically spans:**
A. Mean to median
B. Q1 to Q3
C. Min to max
D. 1.5×IQR only

✅ **Answer: B**

## Q11

**Redundant encoding means:**
A. Removing repeated rows
B. Using more than one visual variable to encode the same data variable
C. Using too many bins
D. Converting ratio to nominal

✅ **Answer: B**

## Q12

**Hue (colour) is normally perceived as:**
A. Ordered → best for ordinal
B. Unordered → best for nominal
C. Always quantitative
D. Always ratio

✅ **Answer: B**
