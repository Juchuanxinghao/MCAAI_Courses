# Chapter 4 (4.1–4.3) Quiz Revision Notes — **Bilingual (EN + 中文)**

*(Exam in English →  **English first** , then **中文解释** for记忆。)*

---

## 4.1 Human-Centred AI (HCAI)

### 4.1.1 What is Human-centred AI?

**EN**

* **Human-centred AI (HCAI)** = AI development that **prioritises human needs, values, and capabilities** at the core of design and operations.
* Goals: **increase** self-efficacy, creativity, responsibility, social connectedness; **reduce** malicious actors, biased data, flawed software.
* HCAI matters because understanding AI’s value  **fosters trust and acceptance** , which is essential for adoption; it aims to  **augment humans rather than replace them** .

**中文**

* HCAI 核心：以“人”为中心（需求/价值/能力），不是只追求自动化效率。它强调增强人类能力、责任与信任。

---

### 4.1.2 Traditional AI vs HCAI

**EN**

* **Traditional AI** : emphasises **task automation** for efficiency/productivity.
* **HCAI** : prioritises **human needs/values/capabilities** → seeks to **augment** people instead of replacing them.

**中文**

* 传统AI更像“自动化机器”；HCAI更像“人类增强系统”。

---

### 4.1.3 Rationalism vs Empiricism (Design philosophy)

**Key contrasts**
**EN**

* **Rationalism (Socrates)** : knowledge mainly from  **intellectual reasoning + logical analysis** .
* **Empiricism (Da Vinci)** : knowledge mainly from **sensory exploration** of the real world.
* Example (Roomba): rationalist thinking → Roomba “does the job on its own” with minimal UI; empiricist thinking → give users  **control and anticipation** .

**Implications for AI design**

* Rationalists tend to favour **autonomous designs** that operate reliably  **without human oversight** .
* Empiricist-driven HCAI: humans must have **meaningful control** and be clearly **responsible** for outcomes; designs should support  **anticipation** ,  **predictability** , and  **adequate control** .
* Empiricist HCAI designers focus on users via **observations in natural settings** +  **participatory design** .

**中文记忆**

* 理性主义：相信规则/逻辑/模型能做到“最优自动化”；
* 经验主义：强调真实世界复杂性 + 观察/反馈 + 让用户能预期并掌控结果。

---

### 4.1.4 Desirable attributes of HCAI systems (Shneiderman)

**EN (3 attributes)**

1. **Reliable** : expected responses; built via sound engineering (audit trails, rigorous testing, explainable outcomes).
2. **Safety culture** : stakeholders’ safety culture guides operations, reviews, and conformance to standards.
3. **Trustworthy** : trusted when independently assessed/certified by established agencies.

**中文**

* 可靠=能按预期工作（审计轨迹/测试/可解释）；安全文化=流程与标准；可信=第三方评估认证。

---

### 4.1.5 Human control vs Computer automation (1D vs 2D view)

**EN**

* **1-dimensional view** : more automation ⇒ less human control (a trade-off).
* **2-dimensional HCAI framework** : decouples this constraint; you can aim for  **high automation AND high human control** .

**中文**

* 关键考点：不是“自动化越高人越没控制”，2D框架允许同时把两者都做高。

---

### 4.1.6 The 2-Dimensional HCAI Framework (Quadrants + examples)

Axes: **Human control (low→high)** and  **Computer automation (low→high)** .

#### (A) Top-right: **Reliable, Safe & Trustworthy** (High control, High automation)

* Where many life-critical systems should be (e.g., airbag deployment, ABS, pacemakers).
* Requires careful design/testing.

#### (B) Bottom-right: **Computer Control** (Low control, High automation)

* For rapid actions beyond human capability; also stable/accurate/predictable processes/sensors.

#### (C) Top-left: **Human Mastery** (High control, Low automation)

* Skill mastery via exploration; **error is part of engaging experience** (guitar, cycling, baking).

#### (D) Bottom-left: **Low Interactive, Non-Smart** (Low control, Low automation)

* Minimal intelligence/interactivity (music boxes, simple clocks, mousetraps).

**中文速记（四象限）**

* 右上：关键系统“又自动又可控”→可靠安全可信
* 右下：机器全权控制→快速/稳定场景
* 左上：人类掌控练技能→允许试错
* 左下：非智能低交互→普通工具/装置

---

### 4.1.7 Failure modes: Excessive automation vs Excessive human control

**Excessive automation**

* Full autonomy can lead to deadly outcomes if designers wrongly believe it cannot fail; lack of manual override/contingency planning (Boeing 737 MAX MCAS example).

**Excessive human control**

* Too much human control over complex systems can increase human errors due to confusion/uncertain defaults.
* Mitigations: safe power-up defaults, interlocks/guards, formal methods + software constraints (e.g., range checking).

**中文**

* 自动化过度：系统一旦错，人没有“兜底手动接管/应急方案”就会出大事故。
* 人控过度：复杂系统靠人手动容易误操作；需要默认安全设置+联锁保护+输入约束。

---

### 4.1.8 Case study: Analgesia (pain killer) delivery system

Purpose: show design options across the 4 quadrants.

* Low control + low automation: simple morphine drip bag.
* Low control + high automation: pre-programmed dosage based on vitals/time/activity but  **no assessment of current pain** .
* High control + low automation: patient squeezes trigger when in pain (patient-guided dispenser).
* High control + high automation: patient control + well-tested AI chooses dosage; prevent overdosing via interlocks limiting dosage/frequency.

---

## 4.2 Human and AI Centred (Human + AI partnership)

### 4.2.1 Human + AI = Symbiotic relationship (not adversaries)

**EN**

* Common narrative: humans vs AI competing for jobs, but this distracts from  **positive collaborations** .
* Human-AI can be  **symbiotic partners** : AI improves human capabilities/services; humans help AI improve performance.
* Example: Netflix recommendation helps users find movies; AI improves by learning from user behaviour/preferences.

**中文**

* 考点：Human+AI 不是对立，而是互相增强（AI给人能力；人给AI反馈数据）。

---

### 4.2.2 What AI is good at (4 themes)

**EN**

1. **Monotonous maestro** : routine/repetitive tasks, consistently, fast, tirelessly.
2. **Ubiquitous presence** : accessible anywhere on multiple devices.
3. **Distributive spread** : easily replicated, share info instantly; one learns → all benefit.
4. **Big data** : analyse huge data, spot hidden patterns faster; time-sensitive prediction/anomaly detection.

**中文口诀**

* AI强项： **重复快稳不累** 、 **随处可用** 、 **可复制共享学习** 、 **大数据找模式/异常** 。

---

### 4.2.3 What humans do better (5 themes)

**EN**

* **VUCA scenarios** : interpret/adapt quickly in volatile, uncertain, complex, ambiguous contexts.
* **Valued judgement** : ethical values, payoff vs utility considerations.
* **Small data learning** : learn fast with few examples.
* **Physical dexterity** : agility/coordination in dynamic physical world.
* **Social engagement** : interpret social/emotional/non-verbal cues.

**中文**

* 人类强项：复杂不确定情境的理解、价值判断、少样本学习、动手能力、社交与情绪识别。

---

### 4.2.4 The “Missing Middle” (Daugherty & Wilson)

**EN**

* Biggest performance boost when humans and AI work together as allies; collaboration happens in the **missing middle** between human-only and machine-only.
* Six roles in the missing middle were identified.

**Roles of Humans (in missing middle)**

* **Train AI** ,  **Explain AI outcomes** ,  **Sustain AI responsibly** .

**Roles of AI (in missing middle)**

* **Amplify** human insight/intuition/creativity
* **Interact** with humans at scale via novel interfaces
* **Embody** physical attributes that extend people’s capabilities

**Examples you should remember**

* Trainers: humans reduce hallucinations / improve answers via RLHF (example shown).
* Explainers: experts who explain complex algorithms for accountability.
* Sustainers: ethics compliance manager ensuring proper use/functioning.
* AI “superpowers”: generative design chair; smart glasses overlay; Agent Assist (NLP + FAQ retrieval); co-bot for lifting/fit.

**中文**

* Missing middle = 人与AI协作的“黄金区间”。人负责训练/解释/治理；AI负责放大能力/大规模交互/物理扩展。

---

## 4.3 Finding AI Opportunities

### 4.3.1 Roles for AI (Levels of control)

**EN**

* AI roles change with  **levels of control** : from tool (more human control) to autonomously managing humans (less control).

**Three key roles (plus Manager)**

1. **Tools** : most human control; user can accept/ignore output (e.g., Google Lens translation).
2. **Assistants** : respond to requests but more **proactive** and context-sensitive (e.g., Grammarly).
3. **Peers** : AI completes independent function; humans collaborate with cognitive division of labour (e.g., human + robot in assembly).
4. **Manager** : AI organises human activities / assigns & coordinates tasks (e.g., AI traffic lights optimising flow).

**中文**

* 控制权越少，AI越“自主”：工具→助手→同事(同伴)→经理。

---

### 4.3.2 Breaking down jobs into tasks

**EN**

* **Job** = way of accomplishing a goal.
* **Task** = unit of activity to get the job done; most jobs consist of multiple tasks.
* To find AI opportunities: identify jobs → break into tasks (manageable chunks).

**Example (marathon + trainer) tasks**
Training plan, equipment, motivation, reminders, progress feedback, update plan.

**中文**

* 找AI机会的第一步：先别急着“上模型”，先把“工作目标”拆成“可操作任务清单”。

---

### 4.3.3 Mapping User Journey (Journey map)

**EN**

* After tasks, create a **user journey** (task flow/workflow).
* Walking through the journey helps decide tasks to **augment** vs  **automate** .
* Journey map: steps users go through to achieve a goal; built from interviews/research/observation; maps a specific product/service + persona to find pain points; events chronological; captures phases/actions/mindsets/emotions.
* “AI opportunities” can be found by thinking of **phases as jobs** and  **actions as tasks** .
* Common journey map fields: persona/actor, scenario, expectations, actions, mindsets, emotions, journey phases, opportunities.

**中文**

* Journey map就是把用户从开始到完成目标的全过程画出来：做什么、怎么想、情绪如何波动、哪里痛点 → 这些地方最容易找到AI机会。

---

### 4.3.4 Problem analysis — When NOT to use AI

**EN: “No sense to use AI” cases**

* **Errors can be costly** (e.g., misdiagnosing rare medical condition).
* **Complete transparency required** (e.g., criminal sentencing; deep models hard to explain).
* **Limited data availability** (“No data, no AI”).
  Other reasons:
* **Rapid time to market / low cost product** : robust AI takes time/resources/compute/data.
* **Social interactions** requiring high social intelligence/empathy; AI poor at subtle/non-verbal cues.
* **People resistant to AI** (opaque/rigid/emotionless/adversarial); resistance strategies exist.

**中文**

* 不适合用AI的高频考点：高代价错误、必须透明可解释、没数据、赶工低成本、强社交共情、用户对AI抗拒。

---

### 4.3.5 Problem analysis — When it MAKES sense to use AI

**EN: “Make sense to use AI”**

* **Personalisation** (needs user profiles/behaviour data).
* **Recommendation & ranking** (surface options users can’t find; require clear ranking logic).
* **Recognition & categorisation** (faces, auto-tagging; sorting defective products; grouping customer behaviour).
* **Detect anomalies** (unexpected changes; fraud spending).
* **Natural language understanding** (translate; speech-to-text; voice assistants).
* **Generate new data** (Generative AI creates multimodal content + styles).

---

### 4.3.6 Considerations before building an AI solution

**EN**

* **Data** : representative data; access; quality; correct labels.
* **Cost/time/effort** : data collection, manpower, compute, maintenance vs value; time to train/test/deploy; justified value proposition.

**中文**

* AI项目可行性常考：数据是否存在可获得且质量好；成本/时间/人力/算力/维护是否>收益。

---

### 4.3.7 Augmentation vs Automation (very important MCQ topic)

**EN**

* Decide: should AI **automate** (do independently) or **augment** (extend human ability)?

#### A) Tasks suitable for **Augmentation**

* **Personally valuable** (user enjoys task, e.g., poetry) → AI supports not replaces.
* **High stakes** (e.g., surgery) → AI assists with precision + enhanced info overlays.
* **Personal responsibility / empathy needed** (appraisal, sentencing) → AI recommends; humans judge/do.
* **Ill-defined tasks** (taste, interior design) → keep human control, AI recommends options.

#### B) Tasks suitable for **Automation**

* **Boring & repetitive** (categorise photos, tax returns, transcription).
* **Low stakes** (occasional errors acceptable vs benefit; movie recs).
* **Dangerous/uncomfortable** (e.g., façade crack inspection via drones).
* **Superior to humans** (resource optimisation, parsing big data; consistency/speed/distributed data).

#### C) Example table (marathon tasks → action)

* Create plan → automate; reminders → automate; progress/updates may be automate/augment depending on specificity and communication difficulty.

**中文速记**

* **Augment** ：人想做/高风险/需责任共情/任务模糊 → AI“辅助”
* **Automate** ：无聊重复/低风险/危险/AI明显更强 → AI“代劳”

---

### 4.3.8 Cultural traits + AI acceptance (algorithm aversion)

**EN**

* Adoption differs geographically: Western companies 26–36% vs Asian 50–59% reported active AI deployment (as cited in slides).
* Individualist cultures (Western) more likely to see AI as infringing uniqueness/autonomy/privacy; collectivist cultures more likely to see AI facilitating consensus/environment response/privacy protection.
* Framing AI as amplifying uniqueness can improve acceptance for individualists (e.g., personalised recs based on unique preferences).
* **Algorithm aversion** : people reluctant to use imperfect algorithms; giving people even slight control (e.g., ability to modify inputs) can increase satisfaction.
* Cultural traits affect willingness to disclose and anxiety about privacy with AI apps.

**中文**

* 考点：文化影响AI接受度；西方更在意个体自主与隐私；“算法厌恶”可通过给一点点控制权来缓解。

---

## High-Yield MCQ Practice (Single-choice) — Answers + Bilingual explanations

### Q1

**HCAI primarily aims to:**
A. Replace humans for efficiency
B. Prioritise human needs/values/capabilities and augment humans
C. Eliminate all human control
D. Focus only on model accuracy

✅ **Answer: B** — HCAI prioritises humans and seeks augmentation.
中文：以人为中心、增强而非替代。

### Q2

**Which best describes Empiricism in AI design context?**
A. Only logical reasoning matters
B. Sense the real world, expect contextual complexity, use observation and feedback
C. Automate with minimal UI always
D. Assume autonomous systems cannot fail

✅ **Answer: B**
中文：强调真实世界复杂性与观察/反馈。

### Q3

**Which are Shneiderman’s 3 desirable HCAI system attributes?**
A. Fast, cheap, scalable
B. Reliable, safe culture, trustworthy
C. Accurate, autonomous, opaque
D. Beautiful, colourful, modern

✅ **Answer: B**

### Q4

**In the 2-D HCAI framework, the main insight is:**
A. Automation always reduces human control
B. Human control and automation can be simultaneously high
C. Only human control matters
D. Only automation matters

✅ **Answer: B**

### Q5

**“Excessive automation” risk is most associated with:**
A. Too much user freedom and exploration
B. Lack of manual override/contingency, believing system cannot fail
C. Low interactivity devices like clocks
D. Using interlocks and guards

✅ **Answer: B**

### Q6

**Which is an example of what AI is good at (from Chapter 4.2)?**
A. Valued judgement in ethical trade-offs
B. Social engagement and non-verbal cues
C. Distributive spread (replication + instant sharing)
D. Learning quickly from small data

✅ **Answer: C**

### Q7

**The “missing middle” refers to:**
A. AI replacing all jobs
B. Pure human work without machines
C. The collaboration space where humans and AI work together for best outcomes
D. Low-data environments only

✅ **Answer: C**

### Q8

**Which AI role provides the MOST human control?**
A. Manager
B. Peer
C. Assistant
D. Tool

✅ **Answer: D**

### Q9

**A scenario where it makes NO sense to use AI is:**
A. Personalised ranking of many options
B. Anomaly detection in spending streams
C. Critical decisions requiring complete transparency (e.g., sentencing)
D. Speech transcription

✅ **Answer: C**

### Q10

**Which task is MOST suitable for AI automation (not augmentation)?**
A. Writing poetry that the user enjoys
B. Performing surgery (high stakes)
C. Categorising 1000s of photos (boring & repetitive)
D. Giving performance appraisal (needs empathy)

✅ **Answer: C**

---

## One-page memory map (超级高频背诵点)

* **HCAI definition + goals**
* **Rationalism vs Empiricism** (autonomy vs observation/control)
* **Reliable / Safety culture / Trustworthy**
* **2-D HCAI framework (4 quadrants) + excessive automation/human control**
* **Human+AI: AI strengths vs human strengths + Missing middle roles**
* **Finding AI opportunities pipeline** : Roles → Job→Tasks → Journey map → When/When not AI → Augment vs Automate → Culture/algorithm aversion
