# CA6114 Part 1 四份课件双语复习资料

## Bilingual Revision Notes for Quiz

## 0. 闭卷多选题应试提醒 / Quiz Strategy for MCQ & MAQ

* **先找关键词** ：如  *generate / predict / governance / bias / hallucination / readiness / traceability / guardrails* 。
* **多选题有倒扣时** ：只选你有把握的；尤其小心 **always / only / never / fully** 这类绝对化表述。
* **最容易混淆的几组** ：

1. **GenAI vs Predictive AI**
2. **When to use vs When not to use GenAI**
3. **Risk category vs Mitigation strategy**
4. **Prompt engineering vs Fine-tuning vs RLHF**
5. **Governance / Risk management / Ethics / Security**

---

# 1. 课程总览 / Course Overview

## 1.1 Part 1 主要讲什么 / What Part 1 is about

* **课程核心 / Core focus：** 本课程 Part 1 关注的是  **在组织中负责任地部署生成式 AI** 。内容依次覆盖：
  **Decision** （GAI 是否适合这个问题、是否与业务目标一致、用例评估、部署挑战、合同考量）→
  **Design & Development** （不同实现路径与 trade-off，如自训 LLM、定制商业 LLM、外包方案、成本与 Responsible AI）→
  **Deployment** （治理、风险管理、企业使用、常见错误）→
  **Case Studies** （教育、法律、医疗等领域的有效/有问题案例）。 / Part 1 focuses on the  **responsible deployment of Generative AI in organisations** , covering decision, design & development, deployment, and case studies across different domains.

## 1.2 学习目标 / Learning Outcomes

* **ILO 1：** 理解生成式 AI 方案在**设计与部署**中的技术和运营问题。 / Understand technical and operational issues in designing and deploying a GenAI solution.
* **ILO 2：** 理解企业中 GenAI 的**治理与风险管理**问题。 / Understand governance and risk management issues for responsible enterprise implementation.
* **ILO 3：** 理解 GenAI 的 **安全与安全性挑战** ，并提出合适的缓解策略。 / Understand security and safety challenges posed by GenAI and propose suitable mitigation strategies.

---

# 2. 什么是生成式 AI / What is Generative AI

## 2.1 定义 / Definition

* **生成式 AI / Generative AI：** 学习数据中的底层模式与结构，并据此 **生成新的数据** 。 / It learns underlying patterns and structures from data and then  **creates new data** .

## 2.2 为什么近年爆发 / Why it boomed recently

* **原因 / Reason：** 生成式 AI 在 **2020 年代初**快速爆发，重要推动力是  **transformer-based deep learning** 。 / GenAI boomed in the early 2020s mainly due to transformer-based deep learning.

## 2.3 主要类型与例子 / Main modalities and examples

* **LLMs：** ChatGPT, Copilot, Gemini
* **图像 / Image：** Stable Diffusion, Midjourney, DALL-E
* **音乐 / Music：** ChucK, Jukedeck, MorpheuS
* **视频 / Video：** SORA, RunwayML, Make A Video
* **3D 空间模型 / 3D spatial models：** Computer-Aided Design (CAD)

## 2.4 典型用途 / Typical uses

* **数据增强 / Data augmentation：** 当真实数据有限时生成新数据。 / Create new samples when data is scarce.
* **代码助手 / Coding assistants**
* **药物发现 / Drug discovery**
* **3D 环境与角色 / 3D environments and personalities**
* **AI agents：** 能自动执行部分在线任务，如创建事件、购买商品和服务等。 / AI agents can automate many online tasks such as creating events and purchasing goods/services.

---

# 3. Sora、扩散模型、Transformer 相关基础 / Sora, Diffusion, and Transformer Basics

## 3.1 Sora 是什么 / What Sora is

* **Sora：** OpenAI 的 **text-to-video** 模型，可根据文本提示生成短视频。 / Sora is a text-to-video model that generates short videos from prompts.

## 3.2 Sora 的表示方式 / How Sora represents video

* **核心点 / Key idea：** Sora 用 **patches** 表示视觉数据，类似 LLM 用 token 表示文本。视频先被压缩到较低维 latent space，再分解成  **spacetime patches** 。 / Sora represents visual data as patches, analogous to text tokens in LLMs; videos are compressed into latent space and decomposed into spacetime patches.

## 3.3 Sora 与扩散 / Sora and diffusion

* **Sora 是 Transformer Diffusion Model。** / Sora is a Transformer Diffusion Model.
* **扩散过程 / Diffusion process：** 给模型输入带噪 patch 和文本条件信息，训练它预测原始“干净”的 patch。 / The model receives noisy patches plus conditioning information and learns to predict the clean patches.

## 3.4 扩散模型的基本思想 / Basic idea of diffusion models

* **正向过程 / Forward process：** 逐步给数据加噪，直到近似纯噪声。 / Noise is added incrementally until the data becomes indistinguishable from noise.
* **反向过程 / Reverse diffusion：** 再一步步去噪，重建出数据。 / Reverse diffusion progressively reconstructs the data.
* **结果 / Result：** 经过多次迭代，可生成高质量、逼真的图像。 / After many iterations, diffusion models can produce high-quality photorealistic images.

## 3.5 Diffusion Transformer 怎么工作 / How Diffusion Transformers work

* **要点 / Key points：**
  1. 对噪声进行建模，把 noisy data 当作序列处理
  2. 用 **self-attention** 区分 signal 与 noise
  3. 使用 **position / timestamp** 信息
  4. 在每个 time step 预测噪声
     / They model noise as a sequence, use self-attention, include positional/time information, and predict noise at each step.

## 3.6 Vision Transformer（分类）/ Vision Transformer for classification

* **ViT 核心 / ViT core idea：** 把图像切成 patches，当作 token，而不是用卷积。 / ViTs split images into patches and treat them like tokens instead of using convolutions.
* **过程 / Process：**
  1. 图像展平为向量 / flatten image into vectors
  2. 加 positional encoding
  3. 在序列前加 **CLS token**
  4. 经过 self-attention 学习关系
  5. 用 CLS 输出做分类
     / Add positional encoding, prepend a CLS token, pass through self-attention, and use the CLS output for classification.

---

# 4. GenAI vs Predictive AI / 生成式 AI 与预测式 AI 对比

## 4.1 本质差异 / Core difference

* **GenAI：** 生成新内容。 / Creates new data or content.
* **Predictive AI：** 基于已有数据做预测。 / Makes predictions based on data.
* **结论 / Conclusion：** 二者适用于不同问题，没有谁绝对更好。 / Both are useful in different scenarios; neither is universally better.

## 4.2 选择工具时要看什么 / What to consider when choosing

* **看问题类型 / Consider the problem type：**
  是要生成内容，还是要做精确预测？
  是结构化数据，还是非结构化数据？
  是追求创造性，还是追求稳定、可解释、可审计？
  / Ask whether the task needs creation or prediction, structured or unstructured input handling, creativity or reliability/traceability.

---

# 5. 什么时候适合用 GenAI / When to Use GenAI

## 5.1 适合使用的场景 / Suitable scenarios

* **大规模内容生成 / Content generation at scale：** 例如产品描述、邮件回复、代码自动补全。 / Product descriptions, email replies, code autocompletion.
* **非结构化输入转结构化输出 / Unstructured input to structured output：** 例如文档摘要、从客服日志中提炼行动点。 / Summarising documents, turning messy input into action points.
* **需要个性化或变化 / Personalisation or variation：** 个性化学习内容、动态营销文案。 / Personalised learning content, dynamic marketing copy.
* **快速原型和创意探索 / Rapid prototyping or ideation：** 头脑风暴、草拟政策、生成测试数据。 / Brainstorming, drafting policies, generating test data.

## 5.2 为什么适合 / Why GenAI fits these tasks

* **高效率 + 低边际成本 / High efficiency and low marginal cost**
* **更擅长处理语言与复杂模式 / Better at handling language and messy patterns**
* **可做个性化输出 / Can tailor outputs**
* **能加速人类创意循环 / Speeds up human creativity cycles**

---

# 6. 什么时候不适合用 GenAI / When NOT to Use GenAI

## 6.1 不适合的场景 / Unsuitable scenarios

* **高准确性、高可靠性、法律精确性要求极高时 / When accuracy, reliability, or legal precision is critical：** 如报税、医疗建议、法律合同。
* **必须保证事实正确 / When factual integrity is critical：** 如新闻报道、学术引用。
* **需要可追踪、可审计 / When traceability and auditability are required：** 如金融决策系统、安全关键系统。
* **任务本身简单、规则清晰 / When the task is simple or rule-based。**

## 6.2 原因 / Why not

* **会 hallucinate / It may hallucinate**
* **可能虚构来源 / It may fabricate sources**
* **往往是黑箱 / It is often a black box**
* **可解释性和可审计性低 / Low explainability and auditability**

---

# 7. 决策辅助工具与 AI Readiness Index / Decision Tools and AI Readiness

## 7.1 课程强调的决策思路 / Decision-making emphasis

* **不是所有问题都该上 GenAI。** / Not every problem should use GenAI.
* **重点是 / The focus is：** problem scoping、use case evaluation、与传统 ML / automation / software engineering 做比较。 / Problem scoping, use-case evaluation, and comparing GenAI with traditional ML, automation, and software engineering.

## 7.2 支持决策的工具 / Tools to support decision making

* **AI Suitability Scorecards：** 评估 ROI 与风险。 / Evaluate ROI versus risk.
* **Tech Readiness Assessments：** 检查基础设施和人员能力。 / Check infrastructure and staff capability.
* **Human-in-the-loop Design Maps：** 找出哪些环节必须人工监督。 / Identify where human supervision is needed.

## 7.3 AI Readiness Index 评分阶段 / Readiness stages

* **1.0–2.0：Nascent** — 还很早期，需大量建设
* **2.1–3.0：Emerging** — 已有基础，但仍需明显提升
* **3.1–4.0：Developing** — 有中等能力，需针对性改进
* **4.1–4.5：Advanced** — 能力较强，但仍可优化
* **4.6–5.0：Leading** — 已具备领先水平
  / These ranges represent increasing organisational readiness for AI adoption.

## 7.4 AI Readiness 的案例 / AI readiness cases

* **UNESCO 教育案例 / UNESCO education example：** 某教育部用 AI readiness 方法评估教育场景中的 AI 引入，发现政策框架中等、农村基础设施较弱、教师培训较强，但伦理与公平方面存在明显缺口。 / A ministry of education used UNESCO’s readiness assessment and found mixed readiness with gaps in ethics and equity.
* **DBS Bank 案例 / DBS Bank case：** readiness 体现在 **data, tech, talent, governance, change** 五方面。 / DBS demonstrated readiness in data, technology, talent, governance, and change management.
* **Microsoft AI Assessment 案例 / Microsoft case：** 评估后通过结构化转型，20 个月后实现战略一致性提升、文化 readiness 提升、落地 15 个 AI use cases，并创造业务价值。 / A structured transformation programme improved readiness and delivered measurable business value.

---

# 8. Chapter 2：Designing & Developing GAI / 设计与开发生成式 AI

## 8.1 生成式 AI 生命周期 / Generative AI lifecycle

* **生命周期不是只训练模型。** / Building GenAI is not just training a model.
* **它是一个相互连接、可反复迭代的流程 / It is an interconnected, iterative lifecycle：**
  **Scope → Select → Adapt & Align → Evaluate → Application Integration** 。 / Scope the use case, select a model, adapt and align it, evaluate it, and integrate it into an application.

## 8.2 Scoping：定义用例 / Defining the use case

* **这一步最基础也最容易被忽略。** / This is foundational and often overlooked.
* **核心问题 / Key questions：**
  1. 我们要解决什么问题？ / What problem are we solving?
  2. 谁是主要利益相关者？ / Who are the stakeholders?
  3. 如何衡量成功？ / How will success be measured?
  4. 数据、资源、时间有什么限制？ / What are the constraints in data, resources, and timelines?

## 8.3 用例筛选标准 / Use-case selection criteria

* **Feasibility 可行性**
* **Practicality 现实可做性**
* **ROI and Impact 投资回报与业务影响**
* **Scalability 可扩展性**
* **一句话总结 / One-line takeaway：** **A well-defined use case is worth more than a fancy model.** / 一个定义清楚的用例，比一个花哨的模型更重要。

## 8.4 Select：选择模型 / Selecting the right model

* **Pre-trained models：** 适合通用任务，如文本生成、摘要、聊天机器人；优点是数据需求小、上线快、成本相对低。 / Pre-trained models are fast and cost-effective for general tasks.
* **Custom models：** 适合 niche、敏感、强控制需求场景；但需要更多数据准备、算力和训练专业能力。 / Custom models suit niche or sensitive domains but require more resources and expertise.
* **Hybrid / RAG：** 能结合外部知识，常常兼顾效果与控制。 / Hybrid approaches such as RAG can combine external data with model generation.

## 8.5 Adapt & Align：模型适配与对齐 / Adapting and aligning the model

* **目的 / Goal：** 把一个通用模型变成能在特定场景中**准确、合乎伦理、高效**工作的模型。 / Turn a generic model into one that works accurately, ethically, and efficiently in context.
* **方法 / Methods：** prompt engineering、fine-tuning、human feedback alignment。
* **特点 / Characteristic：** 这是一个 **迭代过程** ，常常需要多轮 refinement + evaluation。 / It is iterative and involves multiple rounds of refinement and evaluation.

## 8.6 Prompt Engineering / 提示工程

* **定义 / Definition：** 通过设计更好的 prompt，让模型输出更准确、更贴合上下文。 / Crafting prompts to guide models toward more accurate and relevant outputs.
* **三类常考 / Three common types：**
  * **Instruction-based prompts** ：明确指令
  * **Few-shot prompts** ：给少量示例
  * **Zero-shot prompts** ：不给示例，只用描述说明任务
* **要点 / Key point：** prompt 越具体，输出通常越可控。 / More specific prompts generally lead to better control.

## 8.7 Fine-tuning / 微调

* **什么时候需要 / When needed：** 当 prompt engineering 不够时。 / When prompt engineering alone is insufficient.
* **本质 / Essence：** 在预训练模型基础上，用领域数据继续训练，让模型更贴近你的 domain。 / Continue training a pre-trained model on domain-specific data.
* **关键步骤 / Key steps：**
  1. 准备高质量、领域相关、尽量多样的数据
  2. 设定训练参数，如 learning rate、batch size、epochs
  3. 用 validation set 持续评估，避免 overfitting
  4. 可用 early stopping 和 regularization
* **好处 / Benefits：** 更精准控制模型行为，适合医疗、法律、技术等 niche domain。

## 8.8 RLHF / Reinforcement Learning with Human Feedback

* **定义 / Definition：** 利用人类反馈优化模型，使其输出更符合人类目标与偏好。 / RLHF uses human feedback to align model behaviour with human goals and preferences.
* **典型流程 / Typical pipeline：**
  人类标注员给输出打分 → 训练 reward model → 模型通过强化学习最大化 reward。 / Human annotators rate outputs, a reward model is learned, and the main model is optimised to maximise reward.
* **作用 / Benefits：** 降低有毒输出、偏见和不安全行为，让模型更 **harmless / truthful / aligned** 。 / RLHF reduces toxic or unsafe outputs and improves alignment with human values.

## 8.9 Evaluate：模型评估 / Model evaluation

* **不能只看 accuracy。** / Evaluation goes beyond accuracy.
* **常考指标 / Key metrics：**
  * Accuracy & Precision
  * Robustness
  * Bias & Fairness
  * Toxicity
  * Efficiency
  * **HHH = Helpful, Honest, Harmless**
* **目标 / Goal：** 不只验证效果，还要验证用户信任、安全和伦理层面。 / Evaluate not only performance but also safety, trust, and ethics.

## 8.10 Application Integration / 应用集成与上线

* **最后阶段 / Final stage：** 把模型真正接入业务系统。 / The model transitions into a production-ready solution.
* **内容 / Includes：** inference 优化、系统集成、用户界面、持续监控与管理。 / Optimising inference, integrating with existing systems, building interfaces, and ongoing monitoring.
* **要求 / Requirement：** 要可扩展、可靠，并与 workflow 无缝衔接。 / It must be scalable, reliable, and embedded into operational workflows.

## 8.11 LLM 应用扩展 / Scaling LLM-powered applications

* **常见方法 / Common methods：**
  * horizontal scaling
  * sharding large models
  * load balancing & auto-scaling
  * latency optimisation with caching / async processing
    / These are used to handle large-scale production traffic.

---

# 9. Chapter 3：GenAI Governance / 生成式 AI 治理

## 9.1 为什么需要治理 / Why governance is needed

* **原因 / Reason：** GenAI 在大规模部署时会带来独特风险与责任问题。治理的目标是确保其**负责任、合乎伦理、透明、可问责**地被使用。 / GenAI governance ensures responsible, ethical, transparent, and accountable use of GenAI at scale.

## 9.2 Governance 的三个核心 / Three governance pillars

* **Strategic alignment：** 与业务目标和社会价值一致
* **Risk identification and mitigation：** 识别并控制技术、法律、伦理风险
* **Accountability and oversight：** 明确角色、职责和监督机制
  / Align use with goals and values, identify and mitigate risks, and define accountability and oversight.

## 9.3 GenAI 常见风险 / Major GenAI risks

### 1) Output quality issues / 输出质量问题

* 模型输出具有 **不可预测性** ；一个结果可能符合品牌规范，另一个可能不符合。文化语境差异也会让模型产生不合适内容，因此**人工审核**仍然重要。 / Outputs are unpredictable, culturally insensitive at times, and still require human review.

### 2) Hallucinations / 幻觉

* 模型会“编事实”，轻则答错历史事实，重则可能构成法律风险。在要求高准确性的场景中必须设置 **guardrails** 。 / Models can fabricate facts, so guardrails are needed in accuracy-critical uses.

### 3) Copyright and IP / 版权与知识产权

* 训练或生成中可能涉及未经许可的版权内容；用户交互数据的使用条款可能不清晰；训练数据不透明也会引发监管问题。 / Copyright misuse, unclear terms on user data usage, and opaque training data create legal and regulatory risks.

### 4) Biased outputs / 偏见输出

* 模型会继承训练数据中的偏见，进而强化刻板印象。 / Models inherit and amplify biases present in training data.

### 5) Jailbreaking / vulnerability to abuse / 越狱与滥用

* 用户可能绕过模型原本的安全设计，使其输出不当内容甚至泄露机密。 / Users may bypass intended safeguards and misuse the system.

### 6) Compute and expert cost / 算力与专家成本

* 构建强健的 GenAI 应用需要大量算力和稀缺专业人才。 / Robust GenAI systems require scarce expertise and significant compute.

## 9.4 风险管理类别 / Risk management categories

* **Legal / Compliance：** 版权侵权、隐私违规、违反服务条款
* **Security：** prompt injection、model inversion、data leakage
* **Ethical：** bias、misinformation、manipulation、deepfakes
* **Operational：** hallucinations、输出不可预测、缺乏可解释性
* **Reputational：** 内容被滥用、公众反弹
  / These are the main categories used to structure GenAI risk management.

## 9.5 Italy ban 例子 / The Italy ban example

* **事件 / Event：** 2023 年 3 月，意大利因 **personal data handling、transparency、GDPR、age verification** 等问题临时禁用 ChatGPT。OpenAI 后续调整后禁令解除。
* **课程想让你记住的点 / What you should remember：** **隐私、透明度、年龄验证、合规** 是 GenAI 部署中的关键治理问题。 / The Italy case highlights privacy, transparency, age verification, and regulatory compliance.

## 9.6 The Governance Gap / 治理缺口

* **趋势 / Trend：** AI regulation 正朝着 **transparency and accountability** 前进。
* **EU AI Act 可能要求 / May require：**
  1. 披露内容是否由 AI 生成
  2. 记录训练数据来源
  3. 接受模型性能和风险审计
* **但问题是 / But the issue is：**  **技术发展速度快于监管** 。 / Technology is moving faster than regulation.

## 9.7 Singapore 的治理框架 / Singapore’s governance approach

* **新加坡发布了 / Singapore released：**  **Model AI Governance Framework for Generative AI** ，主张在促进创新的同时系统地应对 GenAI 风险，并强调多方利益相关者共同参与。课件提到该框架包含  **nine dimensions** ，但你在 quiz 里至少要记住： **它是系统性、平衡式、生态化治理框架** 。 / Singapore’s framework takes a systematic and balanced approach and involves all key stakeholders.

### 新加坡课件里出现的几个重点方向 / Key Singapore-related governance themes shown in the slides

* **Testing and Assurance：** 第三方测试与审计有助于透明度和用户信任。 / Third-party testing and assurance improve transparency and trust.
* **Security-by-design：** 要把安全设计嵌入整个 SDLC。 / Security must be designed into every phase of the SDLC.
* **Content provenance：** 可通过 watermarking 和 cryptographic provenance 追踪 AI 内容来源；C2PA 是开放标准方向。 / Watermarking and provenance tracking help identify and verify AI-generated content.
* **Safety & Alignment R&D：** RLHF 仍有局限，模型也缺乏充分可解释性和可复现性，因此安全对齐研发仍然重要。 / RLHF has limits, and more safety/alignment research is needed.

## 9.8 Singapore 实际工具 / Singapore practical tools

* **AI Verify：** 用于帮助企业依据 11 个国际认可的治理原则评估 AI 系统的负责部署。 / A testing framework to assess responsible AI implementation against 11 recognised principles.
* **Project Moonshot：** 开源 LLM evaluation toolkit，把 benchmark 与 red teaming 结合起来。 / An open-source toolkit combining benchmarking and red teaming for LLM evaluation.

## 9.9 Red teaming / 红队测试

* **定义 / Definition：** 模拟真实攻击者的方式去测试系统脆弱点。 / Simulating real-world attacks to identify vulnerabilities before malicious actors do.
* **考试记忆点 / Exam point：** red teaming = 主动暴露问题，不是出了事再补救。 / Red teaming is proactive risk discovery.

---

# 10. Chapter 4：Case Studies / 案例与教训

## 10.1 Problems with Generative AI / 生成式 AI 的典型问题

* **Misinformation & Deepfakes：** 虚假政治视频、假名人采访
* **Bias and Discrimination：** 种族/性别歧视输出
* **IP Infringement：** 模仿在世艺术家的作品、Copilot lawsuit
* **Hallucinations：** 编造法律案例或财务信息
* **Prompt Injection & Jailbreaking：** 诱导 AI 生成恶意内容
* **Privacy Violations：** 暴露用户邮箱、电话
* **Content Unsuitable for Context：** 儿童聊天机器人产出成人内容
  / These categories show how GenAI failures appear in real-world settings.

## 10.2 Root causes of problematic use / 问题根因

* **Web-scale unfiltered data：** 网络抓取数据包含偏见、冒犯性、侵权内容
* **Lack of context awareness：** 模型缺少真实世界语境 grounding
* **Insufficient safeguards：** prompt filters / moderation 不完整
* **Overreliance and human overtrust：** 用户把输出当真，不再验证
  / These root causes explain why problematic GenAI behaviour appears so often.

## 10.3 Fake Zelensky video / Deepfake misinformation

* **案例 / Case：** 假 Zelensky 投降视频说明 deepfakes 可被武器化，服务于 misinformation 或信息战。 / The fake Zelensky video illustrates how deepfakes can be weaponised for misinformation and information warfare.

## 10.4 Grok controversy / Grok 案例的治理意义

* **引发的问题 / Governance questions raised：**
  * Consent：可否随意修改真实人物照片？
  * Platform responsibility：平台要负什么责任？
  * Guardrails：是否应屏蔽涉及真实人物的危险编辑？
  * AI-enabled harassment：AI 让骚扰更大规模、更自动化
    / The Grok case highlights consent, platform responsibility, guardrails, and scalable AI-enabled harassment.

## 10.5 Microsoft Tay / Tay 经典教训

* **核心教训 / Main lessons：**
  * 模型不能只模仿用户行为，还必须符合伦理标准
  * 必须有 guardrails、toxicity classifiers、human-in-the-loop moderation
  * 要检测 adversarial manipulation / coordinated trolling
  * 面向公众的模型必须先 red-team，再小范围测试
  * 团队要能实时监控，必要时迅速停机
    / Tay shows why public-facing GenAI must have alignment, moderation, abuse detection, testing, and rapid response.

## 10.6 Deepfake / misinformation 的缓解策略 / Mitigation strategies

* **Technical：** AI watermarking、provenance tracking（如 C2PA, Truepic）、实时检测工具
* **Policy：** 披露法律、竞选监管、恶意使用刑事处罚
* **Education：** 公众媒介素养教育
* **Platform governance：** 平台更严格的内容审核与 AI 检测
  / Mitigation spans technical, policy, education, and platform-governance measures.

---

# 11. Ethics of GenAI / 生成式 AI 伦理重点

## 11.1 Bias mitigation / 偏见缓解

* 训练数据可能带有偏见，输出会延续甚至放大这些偏见，因此要主动做 bias mitigation 与 fairness work。 / Training data may contain bias, so outputs can perpetuate stereotypes unless bias mitigation is applied.

## 11.2 Regulation and safety / 监管与安全使用

* GenAI 可被滥用来生成恶意软件、钓鱼邮件、宣传内容等，因此需要制度、标准和治理框架来约束。 / GenAI can be misused for malware, phishing, and propaganda, so regulation and safety controls are necessary.

## 11.3 Privacy and data security / 隐私与数据安全

* GenAI 常依赖用户数据进行个性化，因此要重视去标识化、信息安全存储、加密等措施。 / Because GenAI systems may rely on user data, privacy protection and data security measures are essential.

## 11.4 课件最后特别提醒的伦理焦点 / Final ethical focus points

* **AI-generated medical advice without review**
* **Profitable but biased AI system**
* **AI’s massive carbon footprint**
  / These are explicit examples of what to pay attention to when thinking ethically about GenAI.

---

# 12. 高频易混点速记 / High-Frequency Confusion Points

* **GenAI = create new content；Predictive AI = predict outcomes** 。
* **Use GenAI** ：创造性、非结构化输入、个性化、原型设计。
* **Don’t use GenAI** ：高风险高精度、事实绝对正确、强审计、简单规则任务。
* **Prompt engineering ≠ Fine-tuning ≠ RLHF** ：
  prompt = 改输入；fine-tuning = 继续训练；RLHF = 用人类反馈做对齐。
* **Risk category ≠ mitigation strategy** ：
  hallucination / bias / privacy / IP / deepfake 是风险；
  watermarking / guardrails / audits / HITL / red teaming 是缓解。
* **Governance 不只是合规** ：还包括战略一致性、责任归属、透明、监督、信任。

---

# 13. 例题练习 / Practice Questions

## MCQ 1

**Which statement best defines Generative AI?**
A. It only classifies images into categories
B. It predicts future stock prices from historical data
C. It learns patterns from data and generates new data
D. It only stores and retrieves documents

**Answer: C**

**解析 / Explanation：**
生成式 AI 的定义是学习数据中的模式与结构，并生成新的数据；这和只做分类或预测不同。 / GenAI learns patterns and structures from data and uses them to create new data, rather than only classify or predict.

---

## MCQ 2

**Sora represents visual data primarily as:**
A. SQL tables
B. Patches
C. Audio tokens only
D. Rule-based templates

**Answer: B**

**解析 / Explanation：**
课件明确写到 Sora 用 **patches** 表示视觉数据，类似 LLM 用 token 表示文本。 / Sora uses patches to represent visual data, analogous to text tokens in LLMs.

---

## MCQ 3

**What is the key difference between Generative AI and Predictive AI?**
A. Generative AI only uses structured data
B. Predictive AI creates new content, while GenAI predicts
C. GenAI creates new data, while Predictive AI makes predictions
D. They are exactly the same

**Answer: C**

**解析 / Explanation：**
这是最基础的对比题。GenAI = create；Predictive AI = predict。 / GenAI creates new data, whereas Predictive AI is used for prediction tasks.

---

## MCQ 4

**Which of the following is LEAST suitable for GenAI?**
A. Product description generation
B. Summarising customer support logs
C. Drafting multiple marketing taglines
D. Final legal contract wording with strict legal precision

**Answer: D**

**解析 / Explanation：**
法律精确性要求极高的任务不适合直接交给 GenAI，因为它可能 hallucinate、非确定、难审计。 / GenAI is not ideal where legal precision and reliability are critical.

---

## MCQ 5

**An organisation with an AI readiness score of 4.3 is in which stage?**
A. Nascent
B. Emerging
C. Advanced
D. Leading

**Answer: C**

**解析 / Explanation：**
4.1–4.5 对应  **Advanced Stage** 。 / A score of 4.3 falls within the Advanced Stage range.

---

## MCQ 6

**After a well-defined scope is established, the next critical step in the GenAI lifecycle is usually:**
A. Ignore evaluation
B. Select the right model
C. Publish publicly immediately
D. Remove all stakeholders

**Answer: B**

**解析 / Explanation：**
Chapter 2 强调：scoping 之后，下一关键步是  **selecting the right model** 。 / After scoping, model selection is the next critical stage.

---

## MAQ 1

**Which of the following are appropriate use cases for GenAI?**
A. Generating product descriptions at scale
B. Summarising messy documents into action points
C. Personalised learning content
D. Simple fixed payroll tax calculation
E. Rapid ideation and drafting

**Answer: A, B, C, E**

**解析 / Explanation：**
GenAI 适合大规模内容生成、非结构化转结构化、个性化、快速原型。固定规则且需要高确定性的税务计算不适合。 / GenAI fits large-scale content generation, unstructured-to-structured tasks, personalisation, and ideation, but not simple rule-based tax calculations.

---

## MAQ 2

**Which are valid reasons NOT to use GenAI?**
A. The task needs strict factual integrity
B. The system requires traceability and auditability
C. The task is highly creative and needs variation
D. The domain is safety-critical
E. The task is simple and rule-based

**Answer: A, B, D, E**

**解析 / Explanation：**
创意与变化通常是适合 GenAI 的点；其余四项都是“不适合”的典型原因。 / Creativity and variation are strengths of GenAI, while the others are classic reasons to avoid using it.

---

## MAQ 3

**Which belong to GenAI risk management categories mentioned in the slides?**
A. Legal/Compliance
B. Security
C. Ethical
D. Operational
E. Reputational

**Answer: A, B, C, D, E**

**解析 / Explanation：**
这 5 个全部都在课件的 risk management 表中。 / All five are explicitly listed as GenAI risk management categories.

---

## MAQ 4

**Which are prompt engineering strategies mentioned in the slides?**
A. Instruction-based prompting
B. Few-shot prompting
C. Zero-shot prompting
D. Gradient checkpointing
E. Random forest prompting

**Answer: A, B, C**

**解析 / Explanation：**
提示工程部分明确列出 instruction-based、few-shot、zero-shot；D 和 E 不属于该页内容。 / The prompt engineering slide explicitly mentions instruction-based, few-shot, and zero-shot prompting.

---

## MAQ 5

**Which are lessons from the Microsoft Tay case?**
A. Public-facing models should be red-teamed before broad release
B. Guardrails and toxicity filters are essential
C. AI should simply imitate user behaviour
D. Real-time monitoring and shutdown protocols matter
E. Abuse detection is important

**Answer: A, B, D, E**

**解析 / Explanation：**
Tay 的教训恰恰是：AI 不能只学用户行为，而必须符合伦理标准，并且要有 guardrails、abuse detection、testing 和 rapid response。 / Tay showed the need for ethical alignment, guardrails, abuse detection, testing, and rapid-response capability.

---

## MAQ 6

**Which are mitigation strategies for deepfake / misinformation problems?**
A. AI watermarking
B. Provenance tracking
C. Public media literacy campaigns
D. Stricter platform moderation
E. Removing all laws and regulations

**Answer: A, B, C, D**

**解析 / Explanation：**
课件给出的 deepfake 缓解策略包括技术、政策、教育、平台治理四类。E 显然与治理方向相反。 / The slides list technical, policy, education, and platform-governance approaches; removing regulation is the opposite of mitigation.

---

## MAQ 7

**Which statements about RLHF are correct?**
A. It uses human feedback to align model behaviour
B. It typically involves a reward model
C. It is used to reduce unsafe or toxic outputs
D. It means replacing all human oversight with full automation
E. It is used in training GenAI models including LLMs

**Answer: A, B, C, E**

**解析 / Explanation：**
RLHF 不是取消人类监督，而是把人类反馈转化进训练与对齐过程。 / RLHF incorporates human feedback into training and alignment; it does not eliminate human oversight.

---

## MAQ 8

**Which metrics are highlighted for GenAI model evaluation?**
A. Robustness
B. Bias and fairness
C. Toxicity
D. HHH (Helpful, Honest, Harmless)
E. Only top-1 accuracy

**Answer: A, B, C, D**

**解析 / Explanation：**
课件强调评估不能只看 accuracy，还要看 robustness、fairness、toxicity、efficiency 和 HHH。 / The slides emphasise broader evaluation beyond accuracy, including robustness, fairness, toxicity, efficiency, and HHH.

---

# 14. 最后冲刺怎么背 / Last-Minute Revision Priority

你今晚如果时间有限，优先背这 8 组：

1. **GenAI 定义 + 例子**
2. **Sora / diffusion / patches / transformer**
3. **GenAI vs Predictive AI**
4. **When to use / when not to use GenAI**
5. **AI readiness stages**
6. **Lifecycle：scope → select → adapt/align → evaluate → integrate**
7. **Risk categories + Italy ban + governance gap**
8. **Tay / deepfake / Grok / mitigation strategies**
   这些是最像选择题、多选题出法的部分。

如果你愿意，我下一条可以直接继续给你做一套  **30 题仿真 quiz（完全按 MCQ/MAQ 风格，中英解析）** 。
