# Chapter 3 Revision Notes (3.1–3.4) — **Bilingual (EN + 中文辅助)**

*(Exam is English → I keep **English as the “answer language”**, and add **Chinese explanation** to help you remember.)*

---

## 3.1 Gestalt Principles in Visualisation（格式塔原则）

### Why Gestalt matters

- **EN:** Our visual system tends to **group elements automatically** and see **patterns** instead of isolated pixels. Good visualisation *uses* this tendency; bad visualisation *fights* it.
- **中:** 人眼/大脑会自动“分组”和“找规律”，所以设计图表时要顺着这种本能来做。

---

### Core Gestalt Laws (common MCQ targets)

Below are the principles most often tested; learn the **definition + typical chart example**.

#### 1) Proximity（接近）

- **EN:** Items close together are perceived as a group.
- **中:** 距离近 → 看起来是一组。

#### 2) Similarity（相似）

- **EN:** Items that look similar (color/shape/size) are grouped.
- **中:** 颜色/形状相似 → 自动被归为同类。

#### 3) Connectedness（连通）

- **EN:** Elements connected by a line/curve are strongly grouped (stronger than proximity/similarity).
- **中:** 被线连起来 → 分组更强（通常强于“接近/相似”）。

#### 4) Enclosure（包围/边界框）

- **EN:** Elements enclosed in a region are grouped **strongly** (often strongest among these).
- **中:** 被框/背景块包住 → 最容易被当成一组。

**Remember the dominance order (very testable):**

- **EN:** Proximity & Similarity (weaker) < Connectedness < Enclosure (strongest)
- **中:** 接近/相似（弱）< 连通 < 包围（强）

---

#### 5) Continuity / Good Continuation（连续性/良好延续）

- **EN:** Elements arranged along a smooth line/curve are perceived as one continuous group.
- **中:** 沿着同一条曲线/直线排布 → 看成一条“连续”的整体。

#### 6) Symmetry（对称）

- **EN:** Symmetric forms are perceived as belonging together / stable groups.
- **中:** 对称结构更容易被看作一个整体（“稳”和“成组”）。

#### 7) Simplicity / Prägnanz（简洁/完形）

- **EN:** People prefer the **simplest** interpretation; clutter reduces comprehension.
- **中:** 大脑倾向用最简单的方式理解图形 → 杂乱会降低可读性。

#### 8) Figure–Ground（图形-背景）

- **EN:** We separate **foreground (figure)** from **background (ground)**; strong contrast and clear boundaries help.
- **中:** 前景和背景要清晰分开；对比度不足会看不清重点。

---

### Typical MCQ traps for Gestalt

- **Trap A:** “Points are close → group?” → **Proximity**
- **Trap B:** “Same color/shape → group?” → **Similarity**
- **Trap C:** “Linked by lines → group?” → **Connectedness**
- **Trap D:** “Inside same box/shaded region → group?” → **Enclosure**
- **Trap E:** “Looks like one curve/line → group?” → **Continuity**
- **Trap F:** “Hard to see what’s foreground vs background” → **Figure–Ground**

---

## 3.2 Colour Perception（颜色感知）

### Why colour is powerful (and dangerous)

- **EN:** Colour is **highly attention-grabbing**; it can make data pop, but it can also mislead.
- **中:** 颜色很“抢眼”，用得好是重点，用不好会误导。

---

### Key practical rules (often tested)

#### Rule 1 — Use **few colours**; avoid “too many categories”

- **EN:** Too many colours increases cognitive load and makes legends hard to decode.
- **中:** 颜色太多 → 认图例很累、易看错。

#### Rule 2 — **Binning** continuous data before colouring categories

- **EN:** If using colour to represent a range, you often need **bins (categories)** to allow meaningful encoding.
- **中:** 连续变量常要先“分箱”，再用颜色区分档位。

#### Rule 3 — **Inclusive use of colour** (colour-blind accessibility)

- **EN:** Prefer colour-blind safe choices; avoid relying on red/green alone; use patterns/labels when needed.
- **中:** 考虑色盲：不要只靠红绿区分，必要时加形状/纹理/标签。

#### Rule 4 — Double-encoding helps

- **EN:** Encode important categories using **both colour and another channel** (e.g., shape).
- **中:** 颜色 + 形状/线型 = 更不容易看错（尤其对色盲友好）。

#### Rule 5 — Greyscale test

- **EN:** A good chart should still be understandable in **greyscale**.
- **中:** 灰度打印也能看懂，才算稳健。

---

### “Colour Data Legibility” (mapping colour to data type) — SUPER testable

- **Nominal (categorical) data → use Hue**
  - **EN:** Hue is good for **nominal** categories
  - **中:** 名义变量（类别）→ 用不同色相区分。
- **Interval/Ratio (ordered/continuous) → use Sequential palettes**
  - **EN:** Interval/ratio values are best shown using **sequential palettes** (light→dark).
  - **中:** 连续/有大小关系 → 用顺序色带（由浅到深）。
- **Diverging palette** (when there is a meaningful midpoint)
  - **EN:** Use diverging when data has a **center reference** (e.g., 0, average).
  - **中:** 有“中点”（如 0 或平均值）→ 用发散色带（两端对比）。

---

### Colour models (conceptual understanding)

#### Additive vs Subtractive

- **EN:** **RGB = additive** (light: screens), **CMYK = subtractive** (ink: printing).
- **中:** 屏幕用 RGB（越加越亮），印刷用 CMYK（越混越暗）。

#### HSV / HSL

- **EN:** HSV/HSL separate **Hue** (type of colour) from **Saturation** and **Value/Lightness**.
- **中:** HSV/HSL 把“颜色种类(色相)”和“浓淡/明暗”拆开，方便调色与设计。

---

### Perception phenomena (good for tricky MCQ)

- **Bezold effect**
  - **EN:** Perceived colour can change depending on surrounding colours/patterns.
  - **中:** 同一种颜色，周围背景不同，看起来会变（环境影响感知）。
- **Colour constancy**
  - **EN:** We tend to perceive object colour as stable under different lighting.
  - **中:** 光线变化，大脑会“校正”，让我们感觉颜色大体不变。

---

## 3.3 Human Visual Perception（人类视觉感知）

### Big idea: seeing ≠ recording a full image

- **EN:** Only a small part of the visual field is in sharp focus; eyes move and attention selects what matters. :contentReference[oaicite:20]{index=20}
- **中:** 你不是“一眼全看清”，而是靠注意力和眼动逐步抓重点。

---

### Preattentive processing（前注意加工）— most important exam concept

- **EN:** Some visual properties are processed **rapidly and in parallel** (pop-out) before conscious attention.
- **中:** 有些特征（比如非常明显的颜色差异）是“秒懂”的，因为是并行处理。

#### Common preattentive features (memorise a few examples)

- **EN:** Color, orientation, size/length, position, shape, motion, etc.
- **中:** 颜色、方向、大小、位置、形状、运动……都是“快通道”。

---

### Conjunction search & Feature Integration Theory (FIT)

- **EN:** When a target is defined by a **combination** of features (e.g., “red AND vertical”), it often requires **focused attention** and becomes slower.
- **中:** “红色+竖线”这种组合目标，通常需要注意力逐个确认 → 更慢、更费力。

**Design takeaway (very likely asked):**

- **EN:** Use preattentive features to highlight key points; avoid designs that require conjunction search for critical information.
- **中:** 重要信息要“秒懂”，别让观众做“找不同+组合匹配”。

---

## 3.4 Psychological Principles of Effective Graphics（有效图形的心理学原则）

### Visualisation design process (high-level steps)

- **EN:** A logical design flow: **Know the Purpose → Know the Audience → Know the Right Chart Type**.
- **中:** 先明确目的，再明确受众，再选对图表类型。

#### Purpose: Exploratory vs Explanatory

- **EN:** Exploratory = explore/analyse & test hypotheses; Explanatory = communicate a clear story to an audience.
- **中:** 探索型是“自己分析”，解释型是“讲给别人听”。

#### Basic chart-type categories (you’ve seen in Chapter 1 too)

- **EN:** Comparison / Composition / Relationship / Distribution.
- **中:** 比较、构成、关系、分布四大类。

---

### Stephen Kosslyn’s Eight-Fold Way（8 大原则）— MUST MEMORISE

The 8 principles are grouped into 3 goals:

- **Connect with audience / Direct attention / Promote understanding & memory** :contentReference[oaicite:28]{index=28}

#### (1) Principle of Relevance（相关性 / “Goldilocks”）

- **EN:** Communication is best when information is **not too much, not too little**; include only data that supports your message. :contentReference[oaicite:29]{index=29}
- **中:** 信息要“刚刚好”，别堆太多也别缺关键背景。

#### (2) Principle of Appropriate Knowledge（受众知识匹配）

- **EN:** Good visuals assume the audience has the **right prior knowledge**; don’t use charts/jargon they can’t decode. :contentReference[oaicite:30]{index=30}
- **中:** 受众看得懂最重要；金融人懂蜡烛图，但不一定懂科研箱线图（反之亦然）。

#### (3) Principle of Salience（显著性）

- **EN:** Attention is drawn to **large perceptible differences**; the most prominent elements should carry the most important information. :contentReference[oaicite:31]{index=31}
- **中:** 越显眼越先被看见，所以显眼的位置要放重点。

#### (4) Principle of Discriminability（可区分性 / 对比度）

- **EN:** Visual properties must differ enough to be distinguished; relate to “just noticeable difference” ideas. :contentReference[oaicite:32]{index=32}
- **中:** 差别太小就看不出来（颜色太接近、线太细等）。

#### (5) Principle of Perceptual Organisation（知觉组织 / 格式塔）

- **EN:** People automatically group elements; exploit Gestalt laws to support correct grouping and comparison. :contentReference[oaicite:33]{index=33}
- **中:** 用接近/相似/包围等让观众“自动分对组”。

#### (6) Principle of Compatibility（形式与含义一致）

- **EN:** A message is easier when the **form matches meaning** (e.g., line charts for continuous trends; bars for discrete categories). :contentReference[oaicite:34]{index=34}
- **中:** 用对图：趋势用折线更“像变化”，类别对比用柱状更直观。

#### (7) Principle of Information Changes（变化应有信息）

- **EN:** Viewers interpret changes in visual properties as meaningful; if meaning changes (e.g., actual vs forecast), you should show a visible change. :contentReference[oaicite:35]{index=35}
- **中:** 图里“变了”就会被当成有意义；该标注的阶段变化要用颜色/线型区别出来。

#### (8) Principle of Capacity Limitation（容量限制 / 认知负荷）

- **EN:** People have limited capacity; visuals shouldn’t require holding more than about **four perceptual groups** in mind at once. :contentReference[oaicite:36]{index=36}
- **中:** 别让人脑同时记太多组信息（大约 4 组是关键数字）。

---

# Chapter 3 Practice MCQs (English questions + bilingual explanations)

## Q1

Which Gestalt principle best explains why points inside the same shaded rectangle are perceived as one group?
A. Similarity
B. Proximity
C. Enclosure
D. Continuity

**Answer: C**

- **EN:** Enclosure groups elements within the same bounded region.
- **中:** 同一块“框/区域”里 → 自动成组（包围原则）。

---

## Q2

Two dots are far apart but connected by a line. They are still perceived as one unit. Which principle is at work?
A. Proximity
B. Connectedness
C. Figure–Ground
D. Symmetry

**Answer: B**

- **EN:** Connectedness often overrides proximity/similarity.
- **中:** 连通通常比“距离近”更强。

---

## Q3

A set of points forms a smooth curved shape; people perceive it as one continuous pattern. This is:
A. Continuity
B. Similarity
C. Salience
D. Discriminability

**Answer: A**

- **EN:** Continuity: elements arranged on a curve/line are seen as grouped.
- **中:** 沿曲线排列 → 看成一条连续整体。

---

## Q4

In a chart, the main message is hard to see because the background grid is too strong and competes with the data. This problem is most related to:
A. Figure–Ground
B. Symmetry
C. Connectedness
D. Information Changes

**Answer: A**

- **EN:** Poor figure–ground separation reduces clarity; contrast and boundaries matter.
- **中:** 前景数据和背景没分开（对比度不够/背景太抢戏）。

---

## Q5

Colour is powerful in visualisation mainly because it:
A. Always improves accuracy
B. Is attention-grabbing and visually salient
C. Makes legends unnecessary
D. Works equally well for everyone

**Answer: B**

- **EN:** Colour attracts attention strongly.
- **中:** 颜色很显眼，会强行吸引注意力。

---

## Q6

Which mapping is most appropriate for **nominal (categorical)** data?
A. Sequential lightness scale
B. Diverging palette around a midpoint
C. Different hues (distinct colours)
D. Changing line width only

**Answer: C**

- **EN:** Hue is appropriate for nominal categories.
- **中:** 类别数据 → 用不同色相区分。

---

## Q7

For **interval/ratio** values (ordered magnitude), the best choice is usually:
A. Random hues
B. Sequential palette (light → dark)
C. No colour at all
D. 3D effects

**Answer: B**

- **EN:** Sequential palettes convey ordered magnitude effectively.
- **中:** 有大小顺序 → 用由浅到深表达强弱。

---

## Q8

Which statement is TRUE about RGB and CMYK?
A. RGB is subtractive; CMYK is additive
B. RGB is additive (screens); CMYK is subtractive (printing)
C. Both are additive
D. Both are subtractive

**Answer: B**

- **EN:** RGB additive for light; CMYK subtractive for ink.
- **中:** 屏幕发光用 RGB；印刷用 CMYK。

---

## Q9

A chart becomes confusing because viewers must constantly decode a legend with many colours. Which issue is this most related to?
A. Appropriate Knowledge
B. Capacity Limitation
C. Symmetry
D. Continuity

**Answer: B**

- **EN:** Too many colours increase cognitive load; capacity is limited.
- **中:** 颜色太多 → 认知负荷爆炸 → 容量限制。

---

## Q10

Which statement best describes **preattentive processing**?
A. Slow and serial scanning of every item
B. Rapid parallel detection of certain visual features
C. Requires reading the legend first
D. Works only with text

**Answer: B**

- **EN:** Preattentive features can be detected quickly in parallel.
- **中:** 前注意加工=秒懂并行，不用逐个看。

---

## Q11

Finding “a red vertical bar among red horizontal bars and blue vertical bars” is typically a:
A. Feature search (pop-out)
B. Conjunction search (needs attention)
C. Figure–ground separation
D. Symmetry grouping

**Answer: B**

- **EN:** Conjunction (red AND vertical) usually needs focused attention.
- **中:** 组合条件（红+竖）→ 要注意力 → 更慢。

---

## Q12

In Kosslyn’s principles, choosing a line chart for continuous trends (and bars for discrete categories) is mainly:
A. Relevance
B. Compatibility
C. Salience
D. Discriminability

**Answer: B**

- **EN:** Compatibility = form should match meaning; chart type should fit the data/story.
- **中:** 形式要匹配含义（趋势→折线；类别→柱）。

---

## Q13

A chart uses too little context, so the audience is puzzled. This violates:
A. Relevance (Goldilocks)
B. Discriminability
C. Perceptual Organisation
D. Information Changes

**Answer: A**

- **EN:** Goldilocks: neither too much nor too little information.
- **中:** 信息不足/过多都不行，要“刚刚好”。

---

## Q14

A designer uses a specialised chart type unfamiliar to the audience, causing misunderstanding. This violates:
A. Appropriate Knowledge
B. Salience
C. Continuity
D. Symmetry

**Answer: A**

- **EN:** Effective communication requires suitable prior knowledge and familiar conventions. :contentReference[oaicite:50]{index=50}
- **中:** 受众知识不匹配：你会不代表别人会。

---

## Q15

A chart changes line style/colour without any meaning, causing viewers to assume there is a new category or phase. This relates to:
A. Information Changes
B. Figure–Ground
C. Proximity
D. Similarity

**Answer: A**

- **EN:** Viewers interpret visible changes as meaningful; changes should carry information. :contentReference[oaicite:51]{index=51}
- **中:** 图里“变了”就会被当成有信息；乱变会误导。

---

## Ultra-compact Memory Checklist (1-minute skim)

- **Gestalt:** Proximity / Similarity / Connectedness / Enclosure (strength order!) + Continuity + Figure–Ground.
- **Colour:** Hue→Nominal; Sequential→Interval/Ratio; RGB additive vs CMYK subtractive; colour-blind safe; greyscale test; don’t overload colours.
- **Perception:** Preattentive = fast parallel; conjunction search = slower, needs attention.
- **Kosslyn 8:** Relevance, Appropriate knowledge, Salience, Discriminability, Perceptual organisation, Compatibility, Information changes, Capacity limitation (~4 groups).
