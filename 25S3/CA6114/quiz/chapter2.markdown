# CA6114 Part 2 双语复习资料

## Security on Generative AI / Secure Design / Development / Deployment

## 0. 考前做题提醒 / Quiz Strategy

* **这部分很容易考“原则 vs 例子”** ：比如
  **Secure by Design** 是原则，
  **MFA / access control / sandboxing / audit logs** 是具体做法。
* **多选题最容易错在“选太多”** ：尤其是题目出现
  **always / only / fully / eliminate all risks**
  这类绝对表达时要警惕。
* **Part 2 高频题型** 往往围绕：
  1. 为什么 AI security 和传统软件安全不同
  2. Secure by Design / Secure by Default / DevSecOps
  3. Threat modelling / Supply chain / Technical debt
  4. SSDF / SSDFGenAI
  5. OWASP Top 10 for LLMs
  6. Red teaming
  7. Deployment / Incident management / Monitoring

---

# 1. Part 2 总体在讲什么 / What Part 2 is about

Part 2 主要讲的是： **如何把生成式 AI 系统做得更安全** 。四章分别对应：

* **Chapter 1** ：为什么 AI security 重要、为什么 AI security 不完全等同于传统软件安全、有哪些常见框架与攻击思路
* **Chapter 2** ：如何在**设计阶段**就把安全放进去
* **Chapter 3** ：如何在**开发与测试阶段**落实安全
* **Chapter 4** ：如何在**部署与上线后**持续保护系统

---

# 2. Chapter 1：Security on Generative AI and Essential

# 第一章：生成式 AI 安全基础

## 2.1 为什么 AI Security 很重要 / Why AI Security is Important

* **中文：** 课件强调，很多组织已经把 AI 纳入创新计划，但真正能有效管理 AI 风险的组织并不多，因此 AI security 不是可选项，而是部署 AI 的前提。
* **English:** Many organisations want to adopt AI, but fewer are actually ready to manage its risks well. Therefore, AI security is a core requirement, not an optional add-on.

## 2.2 组织要先问：准备好了吗 / Is the organisation ready for AI?

课件在开头就提出  **AI readiness** ，并提到：

* **AI Readiness Guideline (SIG)**
* **AI Verify Framework (IMDA, Singapore)**

意思是：在开始做 AI 之前，组织需要评估自己是否在 **governance、risk management、development、security** 等方面准备充分。SIG 的 AI readiness guide 被描述为一个面向领导层的、可操作的指南，并覆盖 board、GRC、CISO、CTO 等角色。

## 2.3 今天的软件工程语境 / In Today’s Software Engineering Context

课件把 AI 场景分成两类：

### UC1: Using AI to create software

### 场景 1：用 AI 帮你写软件

* 如 Copilot 这类工具帮助开发者写代码
* 优点是更快
* 但风险包括：
  * 代码质量不稳定
  * 可能引入安全漏洞
  * 会增加 technical debt
  * 团队可能对 AI 代码产生过度依赖，削弱审查能力

### UC2: Creating AI-powered software

### 场景 2：开发 AI 驱动的软件

* 如构建 chatbot、agent、LLM application
* 这类系统本质上仍然是软件系统，但有 AI 的特殊属性：
  * 行为受数据驱动
  * 模型会老化，需要 retraining
  * 模型可能做自主决策并影响现实世界
  * 模型可能难解释
  * AI 还引入了新的技术资产与攻击面，如 data/model supply chain、training data、model parameters、AI documentation 等

## 2.4 为什么 AI security 和传统软件安全不同 / Why AI security is different

* **中文：** 传统软件安全主要关注普通的软件漏洞与 IT 攻击；AI security 除了这些，还要关注**针对模型本身**的新型攻击。
* **English:** AI security includes traditional software security concerns, but also novel threat vectors aimed directly at the model, data, or AI lifecycle itself.

课件还点到：

* **SDLC** ：传统软件开发生命周期
* **AIDLC / AI lifecycle** ：AI 系统开发生命周期
* 提到 **ISO/IEC 12207** 与  **ISO/IEC 5338** ，说明 AI 系统生命周期需要更专门的视角。

## 2.5 常见 AI 安全攻击 / Possible AI Security Attacks

课件指出，AI/ML 系统会面临 **Adversarial Machine Learning (AML)** 风险。攻击者可以：

* 影响模型分类或回归表现
* 让用户执行未授权操作
* 提取敏感模型信息
* 通过  **Prompt Injection** 、**Data Poisoning** 等方式破坏系统

## 2.6 常见框架 / Common frameworks and guides

这一章是很重要的“框架识别题”来源，至少要记住它们各自大概是干什么的：

### NIST AI RMF

* 适合高层与 GRC 视角
* 4 个 core functions：
  **Govern, Map, Measure, Manage**

### NCSC Guidelines for Secure AI System Development

* 贯穿 AI system development life cycle 的安全指南
* Part 2 后面几章很多内容都基于这个框架展开。

### Secure by Design

* 强调从设计阶段就把安全内建进去
* 3 个关键原则：
  1. **Take Ownership of Customer Security Outcomes**
  2. **Embrace Radical Transparency and Accountability**
  3. **Lead from the Top**

### NIST SP 800-218A

* 是对 SSDF 的 AI / GenAI 扩展版
* 专门补充 AI model development 相关安全实践。

### MITRE ATLAS

* 面向 AI 系统攻击面
* 覆盖 15 个 tactics、100+ techniques
* 可用于系统化记录、分类、理解 AI 威胁。

### OWASP GenAI Security Project

* 全球开源社区项目
* 目标是帮助识别、缓解、记录 GenAI 安全与安全性风险，并提供开发、部署、治理方面的指导。

## 2.7 这一章的结论 / Main takeaway of Chapter 1

第一章最核心的意思是：

* 组织不能一上来就做 AI，要先看 readiness
* AI security 不只是传统网络安全的复制版
* AI 会引入新的攻击面、供应链风险和治理要求
* 安全必须从管理层推动，而不是只丢给工程师。

---

# 3. Chapter 2：Secure Design Principles for Generative AI Application

# 第二章：生成式 AI 应用的安全设计原则

## 3.1 设计阶段的四个通用原则 / Four generic secure design principles

课件列出的通用原则是：

1. **Raise staff awareness of threats and risks**
2. **Model the threats to your system**
3. **Design your system for security as well as functionality and performance**
4. **Consider security benefits and trade-offs when selecting your AI model**

## 3.2 Staff Awareness / 员工安全意识

* 高层可能知道 AI 风险，但开发者、分析师、数据科学家、终端用户未必知道
* 解决方式包括：
  * training and upskilling
  * onboarding / orientation
* 这是典型的“安全不是只有技术”的考点。

## 3.3 Threat Modelling / 威胁建模

* 不同数据类型会影响系统对攻击者的吸引力
* AI 系统价值和用户规模越大，威胁也可能越大
* Threat modelling 需要：
  * 整体评估系统威胁
  * 理解系统被攻破或异常行为对用户、组织、社会的影响
  * 评估 AI-specific threats
  * 记录决策依据

## 3.4 在安全、功能、性能之间做平衡 / Balance security, functionality and performance

这部分很容易出“哪项属于设计权衡”的题。

### 模型与供应链选择 / Model and supply-chain choice

* 可以自己训练模型、用现成模型、微调模型，或通过外部 API 访问模型
* 如果依赖外部 provider / library / model repository，要做 **due diligence**
* 第三方模型和序列化权重应当视为不可信代码，需要 **scanning** 和  **sandboxing / isolation** 。

### 外部 API 数据控制 / Control over outbound data

* 对发送到组织外部服务的数据做控制
* 对可能敏感的信息要加入确认、登录、检查与净化机制。

## 3.5 Secure by Default / 默认安全

课件多次强调：

* 最安全的设置应该成为默认选项
* 当必须提供配置时，默认值也要能防御常见威胁
* 要限制功能访问，遵循 **least privilege**
* 对高风险能力应要求用户显式 opt-in。

## 3.6 Radical Transparency and Accountability / 激进透明与问责

课件认为透明并不是“帮攻击者画路线图”，相反它能：

* 帮助行业形成安全惯例
* 让组织更早做安全决策
* 增强 accountability
* 帮客户根据安全而不仅仅是价格做决策
* 让行业彼此学习，推动 SDLC 成熟。

## 3.7 Lead from the Top / 从高层推动

* 安全激励应在产品设计前就开始
* 安全必须变成 business priority
* 高层要建立 incentive 和文化，让 security 成为 design requirement
* 课件甚至直接说： **security is a sub-category of product quality** 。

## 3.8 Secure by Design 相关实践 / Secure-by-design related practices

### Secure by Default Practices

* Eliminate default password
* Conduct field test
* Reduce hardening guide size
* Discourage unsafe legacy features
* Create secure configuration templates

### Secure Product Development Practices

* Document conformance to Secure SDLC
* Vulnerability management
* Responsibly use OSS / libraries / frameworks
* Provide secure defaults for developers
* Foster a security-aware developer workforce
* Align with Zero Trust Architecture

### Pro-security business practices

* Provide logging at no extra charge
* Embrace open standards
* Provide upgrading tooling
* “Security should not be priced as a luxury good but considered a customer right.”

## 3.9 第二章总结 / Chapter 2 summary

第二章最值得背的是：

* **Shift Left** ：安全要前移到设计阶段
* **Threat modelling** 是起点
* **Secure by Default** 是关键原则
* **Transparency + Accountability + Top leadership** 是组织层面的支撑。

---

# 4. Chapter 3：Secure Development and Testing

# 第三章：安全开发与测试

## 4.1 开发阶段的四个重点 / Four key secure development practices

课件列出的四个核心做法：

1. **Secure your supply chain**
2. **Identify, track, and protect your assets**
3. **Document your data, models, and prompts**
4. **Manage your technical debt**

## 4.2 Secure Supply Chain / 安全供应链

课件强调：

* 要在系统全生命周期评估和监控 AI supply chain security
* 要求供应商遵循与你组织相同的安全标准
* 商业、开源、第三方开发者都要验证
* mission-critical systems 要准备 failover 方案。

### NCSC 12 Principles of Supply Chain Guidance

要点可归纳为四组：

* **Understand Risks**
* **Establish Control**
* **Check Your Arrangements**
* **Continuous Improvement**

## 4.3 NIST SSDF / SSDFGenAI

### SSDF V1.1

课件说 SSDF 是高层级开发安全框架，强调 outcome，不强制具体工具，因此适用于不同组织、技术、平台。

### SSDFGenAI / NIST 800-218A

有 4 大目标域：

* **PO = Prepare the Organization**
* **PS = Protect Software**
* **PW = Produce Well-Secured Software**
* **RV = Respond to Vulnerabilities**

#### 常见可考 practice

* Define security requirements
* Implement roles and responsibilities
* Protect all forms of code and data
* Verify software release integrity
* Confirm integrity of training / testing / fine-tuning / aligning data
* Review code and test executable code
* Configure secure settings by default
* Ongoing vulnerability identification, prioritization, remediation, root-cause analysis

## 4.4 如何识别风险 / How to recognize risks

课件建议：

* **Think like an attacker**
* 通过 **adversarial attack tactics** 去识别和分类风险
* 先理解系统架构、收集信息、寻找漏洞和攻击目标。

## 4.5 MITRE ATLAS / 对抗性 AI 威胁图谱

* ATLAS = Adversarial Threat Landscape for AI Systems
* 覆盖 15 个 tactics、100 多个 techniques
* 与 MITRE ATT&CK 互补，用于理解 AI 威胁。

## 4.6 OWASP Top 10 for LLM Applications（2025）

## LLM 应用十大风险

这一块非常适合出多选题，你最好按名字直接记。

### LLM01: Prompt Injection

用户输入改变模型行为，可能绕过规则、生成有害内容、影响关键决策。

### LLM02: Sensitive Information Disclosure

模型或应用可能泄露 PII、财务、健康、机密业务数据、凭证、法律文档等。缓解之一是 data sanitization。

### LLM03: Supply Chain

训练数据、模型、部署平台都可能因为第三方依赖而受损；需要审查供应商 T&Cs、privacy policy、安全状态。

### LLM04: Data and Model Poisoning

预训练、微调、embedding 阶段的数据或模型被操控，引入 backdoor、bias、漏洞。

### LLM05: Improper Output Handling

对模型输出缺乏 validation / sanitization，可能导致 XSS、CSRF、SSRF、privilege escalation、RCE。课件特别强调： **treat the model as any other user** ，采用  **zero-trust** 。

### LLM06: Excessive Agency

LLM agent 被赋予过多动作能力；应限制 extensions 与 functions 到最小必要范围。

### LLM07: System Prompt Leakage

系统提示词泄露风险；真正危险的不是 prompt 本身被看到，而是它背后的敏感信息、guardrails、权限结构被暴露。应避免把敏感信息直接放进 system prompt。

### LLM08: Vector and Embedding Weaknesses

RAG 的 vector / embedding 生成、存储、检索链路如果薄弱，可能被注入恶意内容或泄露敏感信息。

### LLM09: Misinformation

模型生成看似可信但错误的信息，会导致安全、声誉、法律风险；一个主要原因是 hallucination。

### LLM10: Unbounded Consumption

用户可以无控制地大量推理调用，导致 DoS、经济损失、模型窃取、服务退化。

## 4.7 GenAI Red Teaming / 生成式 AI 红队测试

课件引用 OWASP 的 GenAI Red Teaming Guide，强调红队测试不是只测普通漏洞，而是综合测：

* **model evaluation**
* **implementation testing**
* **infrastructure assessment**
* **runtime behavior analysis**

它还特别强调红队测试覆盖的风险包括：

* adversarial attacks
* alignment risks
* data risks
* interaction risks
* knowledge risks

并要求跨职能协作、scenario-based testing、automated tooling、continuous monitoring。

## 4.8 第三章总结 / Chapter 3 summary

第三章最核心就是：

* 供应链、资产、文档、技术债都要管
* 用 SSDF / SSDFGenAI 做开发安全框架
* 用 MITRE ATLAS 理解威胁
* 用 OWASP Top 10 理解 LLM 风险
* 用 Red Teaming 做系统化测试。

---

# 5. Chapter 4：Secure Deployment and Post-Deployment

# 第四章：安全部署与上线后管理

## 5.1 部署 AI 系统时要考虑什么 / What to consider when deploying AI systems

课件指出，安全部署取决于：

* 系统复杂度
* 可用资源（资金、技术能力）
* 基础设施形态（on-prem / cloud / hybrid）

## 5.2 Realtime Threats / 实时威胁

* 攻击者会同时用传统 IT 攻击手法和 AI 专属攻击向量
* 攻击方式很多，所以防御必须 **diverse and comprehensive**
* 高级攻击者会组合多个向量来突破 layered defenses。

## 5.3 Secure Deployment 的五个重点 / Five deployment practices

课件列出：

1. **Secure your infrastructure**
2. **Protect your model continuously**
3. **Develop incident management procedures**
4. **Release AI responsibly**
5. **Make it easy for users to do the right things**

## 5.4 Secure Infrastructure / 安全基础设施

* 在系统全生命周期中应用基础设施安全原则
* 对 APIs、models、data、training pipelines 加入适当访问控制
* 敏感代码和数据环境要隔离
* 这些能缓解窃取模型或损害模型性能的传统攻击。

### 具体做法 / Specific controls

* sandboxing（containers / VMs）
* network monitoring
* firewalls
* patches and updates
* encryption at rest
* hardware security module for keys
* strong authentication
* secure communication protocols
* phishing-resistant MFA

## 5.5 Deployment environment governance / 部署环境治理

要点包括：

* 明确安全边界
* 用 threat model 指导安全实践与缓解计划
* 定义各 stakeholder 的角色、职责与问责关系。

## 5.6 Incident Management Procedure / 事件管理

课件强调：

* 安全事件是“迟早会发生”的，所以必须有
  **incident response、escalation、remediation plans**
* incident management plan 要随着系统和研究进展持续更新
* 关键数字资源要有 offline backups
* 要训练 incident response team
* 要向客户提供高质量 audit logs 与安全信息。

## 5.7 Usability Enhancement / 让用户更容易做对的事

这是很典型的 Secure by Default 题源：

* Make it easy for users to do the right things
* 每个新增设置都要同时评估业务收益和安全风险
* 默认配置应尽量安全
* 要加 controls 防止系统被恶意使用或恶意部署。

## 5.8 Secure Updates / 安全更新

* 更新本身也要遵循 secure by design
* 默认应支持 automated updates
* 对 data / model / prompt 的变化要谨慎，因为它们会改变系统行为
* 重大更新要像新版本那样对待
* 可通过 preview access、versioned APIs 帮助用户适应变化。

## 5.9 第四章总结 / Chapter 4 summary

第四章最重要的不是“怎么上线”，而是：

* 上线后仍然要持续保护
* 监控、补丁、日志、备份、事件响应、默认安全配置都很关键
* 部署安全 = infrastructure security + operational security + user-safe defaults。

---

# 6. 高频易混点速记 / High-Frequency Confusion Points

## 6.1 Secure by Design vs Secure by Default

* **Secure by Design** ：从设计阶段就把安全纳入系统
* **Secure by Default** ：默认配置就是安全的
  前者更偏理念与方法论，后者更偏默认配置策略。

## 6.2 Threat Modelling vs Red Teaming

* **Threat Modelling** ：设计/开发早期，预测风险、分析攻击面
* **Red Teaming** ：开发后或运行中，模拟攻击去验证系统脆弱性。

## 6.3 SSDF vs OWASP Top 10

* **SSDF / SSDFGenAI** ：开发安全框架
* **OWASP Top 10 for LLMs** ：常见漏洞与风险清单。

## 6.4 Traditional software security vs AI security

* AI security 包含传统软件安全，但还多了模型、数据、prompt、RAG、supply chain 等 AI 特有攻击面。

---

# 7. 例题练习 / Practice Questions

下面我按你 quiz 风格，给你出  **MCQ + MAQ** ，并附中英文解析。

---

## MCQ 1

**Which statement best explains why AI security is different from traditional software security?**
A. AI systems do not need access control
B. AI security only concerns model speed
C. AI security includes traditional software security plus novel threats targeting models and data
D. AI security replaces all existing cybersecurity practices

**Answer: C**

**解析 / Explanation：**
AI security 不是抛弃传统安全，而是在传统安全基础上，再处理模型本身、训练数据、供应链等新增攻击面。 / AI security extends traditional software security by adding AI-specific attack surfaces such as models, data, and AI supply chains.

---

## MCQ 2

**Which of the following is a Secure by Design principle mentioned in the slides?**
A. Eliminate all user choices
B. Lead from the Top
C. Remove all logging
D. Allow unsafe defaults

**Answer: B**

**解析 / Explanation：**
Secure by Design 的三大原则之一就是  **Lead from the Top** 。 / “Lead from the Top” is explicitly one of the key secure-by-design principles.

---

## MCQ 3

**Threat modelling is primarily used to:**
A. Replace all testing
B. Increase model size
C. Assess system threats and their impacts early
D. Remove the need for documentation

**Answer: C**

**解析 / Explanation：**
Threat modelling 是在较早阶段整体评估威胁、影响、AI-specific risks，并记录决策。 / Threat modelling is used to holistically assess threats, impacts, and AI-specific risks early in the lifecycle.

---

## MCQ 4

**In NIST SSDFGenAI, which objective focuses on responding to vulnerabilities?**
A. PO
B. PS
C. PW
D. RV

**Answer: D**

**解析 / Explanation：**
RV =  **Respond to Vulnerabilities** 。 / RV stands for Respond to Vulnerabilities.

---

## MCQ 5

**LLM05: Improper Output Handling may lead to:**
A. Better explainability
B. XSS, SSRF, privilege escalation, or remote code execution
C. Faster model training only
D. Reduced attack surface automatically

**Answer: B**

**解析 / Explanation：**
课件明确指出 Improper Output Handling 可能导致 XSS、CSRF、SSRF、提权和 RCE。 / Improper output handling can lead to XSS, CSRF, SSRF, privilege escalation, and remote code execution.

---

## MCQ 6

**Which practice belongs to secure deployment rather than secure design?**
A. Raise staff awareness
B. Threat modelling
C. Develop incident management procedures
D. Consider security trade-offs in model selection

**Answer: C**

**解析 / Explanation：**
incident management procedures 属于部署与上线后管理重点。 / Incident management procedures are part of secure deployment and post-deployment practice.

---

## MAQ 1

**Which of the following are generic secure design principles from Chapter 2?**
A. Raise staff awareness of threats and risks
B. Model the threats to your system
C. Design for security as well as functionality and performance
D. Consider security benefits and trade-offs when selecting your AI model
E. Disable all user access permanently

**Answer: A, B, C, D**

**解析 / Explanation：**
A–D 都是课件原文列出的 secure design principles；E 不是。 / A–D are the listed generic secure design principles, while E is not.

---

## MAQ 2

**Which items are part of secure development practices in Chapter 3?**
A. Secure your supply chain
B. Identify, track, and protect your assets
C. Document your data, models, and prompts
D. Manage your technical debt
E. Ignore supplier security if they are open-source

**Answer: A, B, C, D**

**解析 / Explanation：**
前四项是课件列出的四个核心实践；开源并不代表可以忽略供应链安全。 / The first four are explicitly listed secure development practices; open-source suppliers still require vetting.

---

## MAQ 3

**Which belong to the OWASP Top 10 for LLM Applications covered in the slides?**
A. Prompt Injection
B. Sensitive Information Disclosure
C. Supply Chain
D. Data and Model Poisoning
E. Improper Output Handling

**Answer: A, B, C, D, E**

**解析 / Explanation：**
这五个都在课件列出的 OWASP Top 10 中，分别是 LLM01–LLM05。 / All five are part of the OWASP Top 10 for LLM Applications in the slides.

---

## MAQ 4

**Which risks are associated with later OWASP LLM items in the slides?**
A. Excessive Agency
B. System Prompt Leakage
C. Vector and Embedding Weaknesses
D. Misinformation
E. Unbounded Consumption

**Answer: A, B, C, D, E**

**解析 / Explanation：**
这些分别对应 LLM06–LLM10。 / These correspond to LLM06 through LLM10.

---

## MAQ 5

**Which controls are mentioned for secured infrastructure during deployment?**
A. Access controls to APIs, models, and data
B. Sandboxing with containers/VMs
C. Encryption at rest
D. Phishing-resistant MFA
E. Remove all software patches

**Answer: A, B, C, D**

**解析 / Explanation：**
课件提到 access control、sandboxing、加密、MFA、patches and updates；E 明显相反。 / The slides mention access control, sandboxing, encryption, MFA, and patching; E is the opposite of good practice.

---

## MAQ 6

**Which statements about incident management are correct?**
A. Security incidents are inevitable enough that response plans are necessary
B. Plans should be reassessed regularly
C. Offline backups are useful
D. Incident response teams should be trained
E. Audit logs should never be shared with customers

**Answer: A, B, C, D**

**解析 / Explanation：**
课件明确支持 A–D；E 与课件相反，因为 slides 提到应向客户和用户提供高质量 audit logs 与安全信息。 / The slides support A–D and explicitly encourage providing high-quality audit logs and security information.

---

## MAQ 7

**Which statements about Secure by Default are correct?**
A. The most secure setting should ideally be the default
B. Default settings should be broadly secure against common threats
C. Users should be pushed toward doing the right thing securely
D. Riskier capabilities may require opt-in
E. Secure by Default means no user configuration is ever allowed

**Answer: A, B, C, D**

**解析 / Explanation：**
Secure by Default 不等于完全没有配置，而是默认安全，必要时允许配置，但要防常见威胁，并对高风险能力做更严格控制。 / Secure by Default means secure defaults and safe configuration, not the elimination of all configuration options.

---

# 8. 最后冲刺背诵版 / Last-Minute Memorisation List

如果你现在时间不多，优先背这 10 组：

1. **AI security ≠ traditional software security only**
2. **UC1 vs UC2**
3. **Secure by Design 三原则**
4. **Secure by Default**
5. **Threat modelling**
6. **Secure development 四大实践**
7. **SSDF / SSDFGenAI 的 PO, PS, PW, RV**
8. **OWASP Top 10 for LLMs（至少记前 5 和后 5 名称）**
9. **Red Teaming 的 4 个 area**
10. **Deployment：infrastructure / continuous protection / incident management / responsible release / user-safe defaults**

如果你愿意，我下一条可以直接继续给你做一套  **30 题 Part 2 全真模拟 quiz（严格按 MCQ/MAQ 风格，附答案和中英解析）** 。
