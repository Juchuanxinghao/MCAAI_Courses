太好了，你这个“ **中英文全面一点** ”我明白了。下面我直接给你做成 **第5章完整版（中英双语、覆盖细、可直接备考）** ，并且把你前面四章的知识自然串起来，方便你做期末综合题。

---

# 第5章完整复习资料（中英文双语）

## Chapter 5: Data Governance, Responsible AI, Secure Storage, and End-to-End Ethical Pipeline

基于你上传的三份 Week 5 课件整理：

* **Week5_data governance_legalframeworks_issues**
* **Week5_data governance-Part 2**
* **Week5_End to end ethical pipeline**

---

## 0) 本章总览 | Big Picture

**中文**
第5章核心是：模型不是只看分数（accuracy/F1）就可以上线，必须满足 **治理（governance）+ 法律合规（compliance）+ 伦理（ethics）+ 安全（security）+ 可问责（accountability）** 。
一句话：**“能做（technical feasible）不等于该做（ethically/legal acceptable）。”**

**English**
Chapter 5 emphasizes that good model metrics are not enough. AI systems must be governed across legality, ethics, security, and accountability.
Key message: **“Technically possible ≠ ethically or legally acceptable.”**

---

## 1) 什么是 Data Governance（数据治理）

### 1.1 定义 | Definition

**中文**
Data governance 是一套政策、流程、角色、控制和技术，用来确保数据：

* 合法（lawful）
* 合伦理（ethical）
* 安全（secure）
* 可追溯（traceable）
* 可问责（accountable）

**English**
Data governance is a framework of policies, processes, roles, controls, and technologies ensuring data is lawful, ethical, secure, traceable, and accountable.

---

### 1.2 为什么存在 | Why it exists

**中文**
传统软件错误通常可见且可修；AI错误往往是概率性的、滞后暴露的、带偏见或违法风险的。
因此治理本质上是**“限制模型能学什么、能做什么”**。

**English**
In AI, failures are often probabilistic, invisible early, and discovered after deployment. Governance acts as a control system over what AI is allowed to learn and do.

---

### 1.3 为什么 AI 时代更难 | Why harder in AI

* 数据会被反复复用（reuse）
* 模型会“记住”数据模式（even after raw data deletion risks may remain）
* 伤害常是群体统计层面的（indirect harm）。

---

## 2) Data Governance 核心原则（考试必背）

课件核心原则可归纳为以下 8 个：

1. **Lawfulness & Legitimacy** （合法性与正当性）
2. **Accountability & Responsibility** （问责）
3. **Security & Protection** （保护）
4. **Purpose Limitation** （目的限制）
5. **Data Minimization** （最小化采集）
6. **Consent Management** （动态同意，支持撤回）
7. **Data Quality & Integrity** （质量与完整性）
8. **Ownership / Stewardship / Custodianship 分工清晰** （责任角色明确）

---

## 3) 角色分工：Owner / Steward / Custodian

### 3.1 Data Owner（数据所有者）

* 法律与治理责任主体（legal accountability）

### 3.2 Data Steward（数据管家）

* 跨业务、法律、技术三方
* 保证定义一致、标签一致、公平检查、访问控制执行
* 覆盖从采集、标注、特征工程、训练到监控的全过程
  （这一点课件特别强调 data steward 的“桥梁角色”）

### 3.3 Data Custodian（数据托管）

* 基础设施、存储、系统层面的实施责任

---

## 4) 治理失败会发生什么（高频问答）

**中文**
没有治理常见后果：

* 合规处罚（罚款、下线）
* 数据质量下降、业务决策劣化
* 安全漏洞与泄漏
* 组织协作失效（部门口径不一致）
* 信任受损。

**English**
Without governance: legal penalties, operational failures, poor data quality, security incidents, and trust erosion.

---

## 5) 法律框架对比（GDPR / PDPA / HIPAA）

课件对比维度非常考试化，建议记忆这几个关键词：

* **GDPR (EU)** ：强调个人权利、透明性、问责、严格跨境
* **PDPA (Singapore)** ：强调同意、目的限制、保护义务（新加坡课程高频）
* **HIPAA (US Healthcare)** ：聚焦 PHI（健康信息）访问与安全规则。

 **中文记忆法** ：

* GDPR：权利导向最强
* PDPA：目的+同意+保护
* HIPAA：医疗隐私专法

---

## 6) 新加坡教育研究场景（你考试很可能会考）

课件给了教育研究的数据治理要求（非常重要）：

1. **显式知情同意** （非强迫，尤其要处理师生权力不对等）
2. **教学用途 ≠ 研究用途** （purpose limitation，二次用途需新同意或伦理审批）
3. **IRB/ERC 审查要求**
4. **最小化采集与匿名化/假名化优先**
5. **退出不应有惩罚（opt-out without penalty）** 。

---

## 7) 真实案例（考“治理失效映射”非常常见）

## 7.1 Cambridge Analytica（数据滥用）

* 失败点：同意不透明、第三方访问管控不足、目的限制失效
* 结果：政治操纵、公众信任危机
* 预防：API 最小权限、访问审计、清晰同意机制。

## 7.2 Microsoft Tay（数据投毒）

* 失败点：输入校验不足、速率限制不足、无人类监督、部署治理缺失
* 结果：短时间输出有害内容，系统下线
* 预防：输入过滤、监控告警、人类在环、回滚机制。

---

## 8) Responsible AI（负责 AI）与 Data Governance 区别

**中文**

* Data Governance：管“数据怎么被管理、保护、审计”
* Responsible AI：管“AI 行为是否对人公平、可解释、可干预、可问责”

两者关系：Governance 是底座，RAI 是行为规范层。

**English**
Governance manages data controls; Responsible AI manages how model behavior affects people. They are complementary.

---

## 9) Responsible AI 核心伦理维度（必背）

1. Human-centricity（人类中心，AI 辅助不是取代）
2. Privacy（隐私保护）
3. Security & Robustness（鲁棒与安全）
4. Accountability（问责）
5. Fairness & Non-discrimination（公平与非歧视）
6. Transparency & Explainability（透明与可解释）。

---

## 10) 贯穿数据科学流水线的 Responsible AI 问题（考试高频配对）

* Problem definition：这件事该不该自动化？
* Data collection：同意是否充分且公平？
* Feature engineering：是否编码了偏见代理变量？
* Model training：是否做了 subgroup 测试？
* Deployment：是否有人类监督？
* Monitoring：是否有新伤害出现？

---

## 11) AI Data Storage（AI 数据存储）——技术与治理结合点

### 11.1 为什么是治理议题

AI 训练需要巨量、低延迟、可扩展存储；但越快越大，泄露与滥用风险越大。
治理要求把“性能”和“合规”一起设计。

### 11.2 关键技术点（可出填空/比较题）

* HDD: ~5–10 ms
* SATA SSD: ~100 μs
* NVMe SSD: ~10–20 μs
  NVMe 低延迟可减少 GPU 饥饿（GPU starvation），提升训练效率。

### 11.3 成本优化三件套

* Deduplication
* Compression
* Tiering（hot/warm/cold）

### 11.4 安全支柱

* RBAC 访问控制
* 加密**（at rest / in transit）**
* 数据隔离（训练/测试/生产分离）
* 审计日志 + 持续监控
* 安全保留与删除（删除后可能需模型重训）。

---

## 12) Zero Trust Architecture（零信任）要点

 **Never trust, always verify** ：

* 身份优先
* 持续验证
* 最小权限
* 每个流水线阶段单独认证
* 全链路加密。

---

## 13) 非合规风险总表（适合简答题）

* 法律/财务：罚款、停运
* 运营：模型失效、重训成本
* 声誉：信任损失
* 伦理：歧视与社会伤害
* 安全：泄露、推理攻击
* 治理：责任不清，甩锅给“算法”。

---

## 14) 高阶专题（Synthetic Data / DP / Federated Learning）

## 14.1 Synthetic Data（合成数据）

* 用途：隐私保护、稀缺场景补充、测试
* 风险：继承原始偏差；若完全脱离真实数据可能模型坍塌（model collapse）
* 要求：目标明确、原始数据预处理、高质量验证（fidelity + utility）、持续文档化。

## 14.2 Differential Privacy（差分隐私）

* 核心：加噪保护个体不可识别
* 权衡：噪声越大隐私越强但可用性下降
* 备注：可保护个体，但群体模式仍可能被推断。

## 14.3 Federated Learning（联邦学习）

* 优点：数据不出本地，减少原始数据流动
* 误区：不代表不用治理
* 风险：模型更新本身可能泄露，需要安全聚合、认证和监控。

---

## 15) End-to-End Ethical Pipeline（端到端伦理流水线）——考试重点中的重点

课件用“学生支持预警模型”给了完整模板，非常适合考试案例题。

### Step 1 Extraction（抽取）

* 风险：purpose creep、敏感代理、原始行为暴露
* 控制：目的限制、最小化（周级聚合代替细粒度日志）、分层权限

### Step 2 Cleaning（清洗）

* 风险：把结构性缺失当噪声直接删行，系统性伤害弱势群体
* 控制：missingness indicator + 稳健插补 + 元数据跟踪

### Step 3 Transformation（变换）

* 风险：特征工程编码偏见；时间泄漏
* 控制：feature fairness review + time-aware window（只用历史窗口）

### Step 4 Modeling（建模）

* 优先可解释基线
* 输出 risk bands + explanations（而非惩罚分数）
* Human-in-the-loop

### Step 5 Access Control（访问控制）

* Advisor：个体风险+解释
* Instructor：聚合趋势
* Admin：审计日志
* Student：仅本人数据与解释

### Final Action（行动）

* 用于支持干预，不用于纪律惩罚。

---

## 16) Explainability 双轨体系（模型解释 + 系统解释）

课件特别强调：解释不是只有 SHAP/LIME。
要有两条线并行：

1. **Model-level explainability** ：为什么这个预测？
2. **System-level explainability** ：数据怎么来的、如何变换、谁访问了、哪个版本模型做的决策。

系统级治理工件（artifacts）：

* Datasheet
* Feature documentation
* Data contracts
* Lineage & provenance
* Audit logs
* Model card
* Drift & retraining records。

---

## 17) 两个“治理优秀数据集”案例（可做简答加分）

1. **UCI Adult Census**

* 清晰来源、用途明确、特征文档完整、敏感属性显式标注、无直接身份标识、稳定版本。

2. **MIMIC-III / MIMIC-IV**

* 发布前治理设计、IRB 审核、访问前培训、严格去标识化、明确数据使用协议。

---

## 18) 第5章高频易错点（必背）

1. 认为“合法就一定合伦理”
2. 认为“匿名化后就100%无风险”
3. 认为“联邦学习就不用治理”
4. 只做模型解释，不做系统级可追溯
5. 把学生支持模型用于纪律处罚（purpose creep）
6. 删除缺失值时不考虑结构性不公平
7. 只追求 accuracy，不看 subgroup fairness
8. 数据删除后不评估模型是否仍保留敏感信息

---

# Chapter 5 Quiz（混合题型，含答案与解析）

## A) Single Choice（单选）

**Q1.** Which statement best captures data governance?
A. It is only about storage optimization
B. It is only a legal checklist
C. It is a lifecycle control framework for lawful, ethical, secure, traceable data use
D. It is model tuning
**Answer: C**

**Q2.** In educational analytics, “teaching data used for research” without new approval most directly violates:
A. Compression strategy
B. Purpose limitation
C. GPU utilization
D. Model card format
**Answer: B**

**Q3.** Which architecture principle says “Never trust, always verify”?
A. Data lakehouse
B. Zero Trust Architecture
C. Differential privacy
D. Federated averaging
**Answer: B**

---

## B) Fill in the Blanks（填空）

**Q4.** In secure storage, encryption should protect data at ______ and in ______.
**Answer:** rest, transit

**Q5.** AI in banking should provide a risk score, but final decisions should include ______ oversight.
**Answer:** human

**Q6.** In ethical pipeline design, explainability is both model-level and ______-level.
**Answer:** system

---

## C) Multiple Answers（多选）

**Q7.** Which are core security pillars for AI data storage?
A. RBAC
B. Audit logs
C. Data isolation
D. Random label flipping
**Answer:** A, B, C

**Q8.** Which are valid risks of synthetic/federated approaches?
A. Synthetic data may inherit bias
B. Differential privacy has utility-privacy tradeoff
C. Federated learning removes all governance duties
D. Model updates in federated setups can leak information
**Answer:** A, B, D

---

## D) Matching（匹配）

Match artifact to purpose:

1. Datasheet  b. explains dataset origin, allowed/prohibited uses, retention
2. Feature documentation   d. defines feature formula, window, proxy risk, constraints
3. Data contract    c. defines schema, null rules, freshness, drift monitors
4. Model card  e. documents intended use, limitations, subgroup metrics, monitoring plan
5. Audit logs  a. records who accessed what and when

a. records who accessed what and when
b. explains dataset origin, allowed/prohibited uses, retention
c. defines schema, null rules, freshness, drift monitors
d. defines feature formula, window, proxy risk, constraints
e. documents intended use, limitations, subgroup metrics, monitoring plan

**Answer:** 1-b, 2-d, 3-c, 4-e, 5-a

---

## E) True/False（判断）

**Q9.** “Legal = ethical = acceptable” is always true.
**Answer:** False

**Q10.** Federated learning reduces data movement, but governance responsibility remains.
**Answer:** True

**Q11.** Removing proxy features is sometimes ethically better than adding more features.
**Answer:** True

---

如果你同意，我下一条可以直接给你做一份**“五章终极总复习（中英双语）”**，包含：

1. **超全知识点总表（按章节+题型）**
2. **150题期末模拟卷（MCQ/填空/多选/匹配，附解析）**
3. **Respondus 场景下的答题策略（尤其多选负分规避）**
4. **考前30分钟极速背诵版（仅高频易错点）**
