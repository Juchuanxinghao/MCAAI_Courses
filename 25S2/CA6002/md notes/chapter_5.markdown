太好了，下面是你要的  **Chapter 5（5.1~5.2）完整复习资料（中英双语）** ，我按 **quiz（选择题）高频考法** 来整理，并尽量覆盖课件完整知识点。
（考试英文为主，所以每个点我先给 EN，再给中文理解版）

---

# Chapter 5 Revision Notes (5.1–5.2)

## HCAI UX Design: **Usability** + **Trust** (Bilingual)

---

## 5.1 HCAI UX Design — **Usability**

### 5.1.1 Why usability matters

**EN**

* Usability = how well a **specific user** in a **specific context** can use a product to achieve a defined goal  **effectively, efficiently, and satisfactorily** .
* In AI products, usability is crucial for adoption and stickiness (users return repeatedly).
* Usability is part of UX, but not equal to UX: utility first (solve the right problem), then usability, then desirability.

**中**

* 可用性是：特定用户在特定场景下，是否能高效、准确、满意地完成目标。
* AI 产品要被长期使用，先要“好用”；只炫技没用。
* UX层次里：先“有用（utility）”，再“好用（usability）”，再“好看/喜欢（desirability）”。

---

### 5.1.2 Usability design elements (必考定义题)

**EN**
Five core elements:

1. **Effectiveness** – complete tasks accurately
2. **Efficiency** – complete tasks quickly with minimal effort
3. **Engagement** – pleasant and context-appropriate interaction
4. **Error tolerance** – handles user/system errors intelligibly
5. **Ease of learning** – newbies can start quickly and improve with use

**中**

* 五要素：有效性、效率、参与感、容错性、易学性。
* 记忆口诀： **准、快、顺、稳、易** 。

---

### 5.1.3 Designing intuitive AI interactions

#### A) Consistency 一致性

**EN**

* Reuse familiar icons, patterns, layouts (e.g., thumbs up/down, pinch zoom, top menu).
* Keep UI conventions consistent across platforms (web/mobile).
* Consistency supports users’ existing mental models.

**中**

* 一致性是“低学习成本”的核心：图标、交互、布局跨端一致。
* 用户以前学过的使用习惯能直接迁移。

#### B) Design for new users (tooltips)

**EN**

* Tooltips provide contextual help for unfamiliar users.
* Good tooltips: contextual, useful, actionable, dismissible (“Don’t show again”).
* Keep help available but non-intrusive for experienced users.

**中**

* 新手提示要“有用但不烦人”：可触发、可关闭、可行动。
* 老用户要能快速关闭，避免干扰。

#### C) Awareness of AI enhancements

**EN**

* Users should know when AI is involved (icons, labels like “AI”, visual cues).
* Sparkles icon is a common AI cue pattern; providers keep their AI cues consistent in integrated apps.
* Beware cross-cultural differences in symbol/color interpretation.

**中**

* 用户要“意识到AI正在工作”（图标/标签/视觉语言）。
* 但符号和颜色跨文化解释可能不同，部署前应做用户研究。

#### D) Informative system feedback

**EN**

* After user action, system should respond immediately and clearly.
* If processing takes time, show progress/animation + estimated duration when possible.
* In voice UI, indicate “listening state” and confirm completion (“Dining lights turned off”).
* Lack of feedback can make users think the system is broken and harms trust.

**中**

* “你按了按钮，系统必须有回音”。
* 慢就要显示进度条/动画/预计时间。
* 语音助手必须明确：开始听了、任务完成了。
* 没反馈=像坏了，会迅速掉信任。

---

### 5.1.4 Designing error handling (高频主观+选择)

#### A) AI is probabilistic → errors are inevitable

**EN**

* AI outputs are probabilistic; errors/inaccuracies are part of UX reality.
* Design should **tolerate errors** but avoid **failures** that make system unusable.

**中**

* AI天生有不确定性。
* 允许“小错”但不能“系统性失效”。

#### B) Error vs failure

**EN**

* **Error** : mismatch with user expectation (inconvenient but usable).
* **Failure** : system cannot safely/adequately perform intended function (often unacceptable).

**中**

* Error 更像“结果不理想”；
* Failure 更像“系统失能/失控”。

#### C) Two error sources

**EN**

1. **AI system errors** : poor/biased data, insufficient training, wrong model/feature emphasis
2. **User errors** : ambiguous/incorrect input, wrong operation
   Worst case for trust: user makes mistake but system gives no meaningful feedback.

**中**

* 错误来源：系统错 + 用户错。
* 最伤信任的是“用户错了但系统沉默/乱答”。

---

### 5.1.5 Handling AI system errors

#### A) Communicate errors effectively

**EN**

* Explain errors in human language (“Sorry, unable to perform request”) not technical codes (“Exception 414”).
* Use error states to teach users how to improve outcomes and build better mental models.

**中**

* 错误提示要“人话”，不要报错码。
* 错误信息应指导下一步可行动作。

#### B) Treat misclassifications as feedback opportunities

**EN**

* Ask for quick explicit feedback (thumbs up/down) on wrong predictions.
* Helps reduce future mismatches and improve model performance.

**中**

* 把误判时刻变成“收集反馈”的黄金时机。

#### C) User-perceived errors

**EN**

* Sometimes output feels wrong to users but is optimal under current model settings/data.
* Mitigate via controllability (weight tuning) + explainability + explicit feedback.

**中**

* 有些“错”是用户感知错，不一定模型算错。
* 解决：给控制权 + 解释依据 + 收反馈。

---

### 5.1.6 Handling user errors (不责备用户)

#### A) Don’t blame users

**EN**

* Avoid accusatory language (“illegal command”, “incorrect input”).
* Use polite, recoverable phrasing with fix suggestions.

**中**

* 不要“怪用户”，要“帮用户恢复”。

#### B) Handle ambiguous inputs gracefully

**EN**

* Offer “Did you mean…?” alternatives and N-best suggestions.
* Anticipatory suggestions prevent errors before they happen.

**中**

* 含糊输入时给候选项，引导澄清。

#### C) Prevent errors upfront

**EN**

* Use constraints/widgets for structured input (date pickers, format checks).
* Use error-prevention tooltips and smart defaults.
* Clarify AI scope/capability early to avoid expectation mismatch.

**中**

* 预防优于事后纠错：约束输入、默认值、范围说明。

---

### 5.1.7 Chapter 5.1 key takeaway

**EN**

* Usability in HCAI = intuitive interaction + timely feedback + robust error handling + mistake prevention.
  **中**
* “好用”的AI=易懂、可学、可恢复、可预防。

---

---

## 5.2 HCAI UX Design — **Trust**

### 5.2.1 Why trust is central

**EN**

* AI systems are dynamic and evolve with data/interaction; UX must adapt over time.
* Trust design in this chapter centers on two pillars:
  1. **Explainability**
  2. **User control**

**中**

* AI会“边用边变”，所以信任不是一次性建立，而是持续校准。
* 关键两根柱子：可解释 + 可控制。

---

### 5.2.2 Components of trust

**EN**

1. **Competence** – can it do what users need?
2. **Reliability** – does it work consistently and predictably?
3. **Benevolence** – is it fair, value-adding, autonomy-respecting?

**中**

* 信任三要素：能力、可靠、善意（公平且尊重用户）。

---

### 5.2.3 Trust calibration (非常高频)

**EN**

* Effective human-AI collaboration needs “right-sized trust”.
* **Distrust** : trust < capability → users ignore useful AI.
* **Overtrust** : trust > capability → users over-rely when human judgment is needed.
* Overtrust can quickly flip to distrust after failures.

**中**

* 理想状态不是“越信越好”，而是“信任与能力匹配”。
* 过度信任和过度不信任都会损害决策质量。

---

### 5.2.4 How to build trust

**EN**

* Not about being always correct; about integrity and active correction.
* Two essentials:
  1. explain how it works/how well it works
  2. give users meaningful control over data and outputs
* Help users decide when to trust AI vs use their own judgment.

**中**

* 信任建立在“诚实+可纠错”，不是“永不犯错”。
* 用户要知道：何时该信AI，何时该自己判断。

---

### 5.2.5 Who needs explanations? (stakeholders)

**EN**
Different stakeholders need different explanation depth:

* Decision makers using AI outputs (e.g., officers)
* People affected by AI decisions
* ML/data engineers
* Auditors/regulators

**中**

* 解释不是一套打天下：受众不同，解释粒度必须不同。

---

### 5.2.6 Design guidelines for better AI explanations (6 points)

#### 1) System capabilities

**EN:** clearly state scope and limitations; avoid vague open-ended prompts that inflate expectations.
**中:** 明确“能做什么/不能做什么”，别用“Ask me anything”误导。

#### 2) Performance humility

**EN:** set realistic expectations; avoid overconfident wording; communicate changing performance conditions in time.
**中:** 用谦逊表达概率结果，及时更新性能波动。

#### 3) Adaptive behaviour

**EN:** explain that system learns over time; show factors affecting result changes; support trust calibration through journey.
**中:** 告诉用户系统会学习、会变化，解释“为什么这次结果不同”。

#### 4) Input & output transparency

**EN:** disclose what data is collected/tracked/used, where data comes from, and how outputs are derived.
**中:** 输入透明 + 输出透明：数据来源、使用范围、结论依据都要讲清楚。

#### 5) Understandable explanation

**EN:** keep explanations concise, intelligible, accessible; avoid overloading users; high-stakes use cases require stronger explainability justification.
**中:** 解释要“听得懂、用得上”，高风险场景尤其要清楚。

#### 6) Confidence level

**EN:** confidence can help calibration but may mislead; test with users before display.
Forms:

* categorical (high/medium/low)
* numeric (%)
* N-best alternatives (ranked options)

**中**

* 置信度是双刃剑：能帮助也能误导。
* 展示方式可用分级/数值/N-best候选，需做用户测试。

---

### 5.2.7 Design guidelines for user control

#### A) Control level by stakes

**EN**

* High-stakes (surgery/justice/finance): more user control, visibility, monitoring, correction.
* Low-stakes (music/product recommendation): can be more automated.

**中**

* 风险越高，控制权越应回到人手里。

#### B) Graceful handover (AI → human)

**EN**

* When AI cannot handle case, handoff must be seamless, clear, and informative.
  **中**
* AI接不住时，要“优雅交接”给人工，不要让用户重复讲一遍。

#### C) Input data control

**EN**

* Users should be able to view/access/edit/share/opt out selectively.
* Avoid all-or-nothing permissions.
* Allow history deletion and full preference reset.

**中**

* 数据控制要细粒度可选：可开关、可删除、可重置，不要一刀切。

#### D) Output control

**EN**

* Let users choose among results, tune weights/preferences, and dismiss irrelevant outputs easily.
* Dismiss action also serves as training signal.

**中**

* 结果可挑选、可调权重、可快速“不要这个”，这既提升体验也反哺模型。

---

### 5.2.8 Design guidelines for user feedback

#### A) Explicit feedback

**EN**

* Intentional signals (thumbs up/down, options, surveys, comments).
* Should be understandable, mutually exclusive, actionable, editable/undoable.
* Embed at right timing/context; avoid disrupting high-stakes tasks.

**中**

* 显式反馈要“清晰、可操作、可撤销”，并放在合适时机。

#### B) Implicit feedback

**EN**

* Derived from logs/behavioral traces/observations.
* Useful to detect confusion/error-prone steps and improve explanations.
* Must inform users about collection/use, obtain permission, and provide opt-out.

**中**

* 隐式反馈来自行为数据，价值很高，但必须透明告知+可退出。

---

### 5.2.9 Chapter 5.2 key takeaway

**EN**

* Best trust experience occurs when **explainability + controllability** are both present (additive effect), plus responsible feedback loops.
  **中**
* 最佳体验不是单靠解释或单靠控制，而是两者叠加，再配合高质量反馈闭环。

---

## Chapter 5 高频选择题易错点（Quick Exam Traps）

1. **Usability ≠ UX**
   * Usability is a component within UX (after utility, before desirability).
2. **Error ≠ Failure**
   * Error can be tolerable inconvenience; failure harms usability/safety fundamentally.
3. **Trust ≠ blind confidence**
   * Need calibrated trust, avoid both distrust and overtrust.
4. **Explainability must be audience-specific**
   * Different stakeholders need different depth.
5. **Confidence score is not always helpful**
   * Can mislead; user-tested presentation needed.
6. **Implicit feedback cannot be covertly abused**
   * Must disclose and allow opt-out.

---

## 超短背诵版（考前1分钟）

**EN**

* 5.1 Usability = effective, efficient, engaging, error-tolerant, learnable; design intuitive interactions + informative feedback + humane error handling.
* 5.2 Trust = explainability + control; calibrate trust (avoid overtrust/distrust); give transparency, controllability, and explicit/implicit feedback loops.

**中**

* 5.1：好用=准快顺稳易；交互直观、反馈及时、错误可恢复。
* 5.2：可信=可解释+可控制；信任要校准；透明、可控、可反馈闭环。

太好了，下面给你一套  **Chapter 5（5.1–5.2）全英文 40 题 MCQ 模拟题** ，按你 quiz 风格来做：

* 题目全英文
* 每题给 **Answer + EN Explanation + 中文解析**
* 覆盖 **Usability + Trust + Explainability + User Control + Feedback + Trust Calibration** 高频考点

---

# Chapter 5 Mock Quiz (40 MCQs)

## Part A — HCAI UX Design: Usability (Q1–Q20)

### Q1. Which statement best defines usability in HCAI UX?

A. A system that uses the newest AI model
B. A system that is visually attractive
C. A system that enables specific users to achieve goals effectively, efficiently, and satisfactorily in context
D. A system that fully automates all tasks

**Answer: C**
**EN:** Usability focuses on effectiveness, efficiency, and satisfaction for specific users in specific contexts.
**中：** 可用性核心是“特定用户在特定场景下高效、准确、满意地完成任务”。

---

### Q2. Which is NOT one of the five usability elements discussed in Chapter 5.1?

A. Effectiveness
B. Efficiency
C. Profitability
D. Error tolerance

**Answer: C**
**EN:** The five are effectiveness, efficiency, engagement, error tolerance, and ease of learning.
**中：** 五要素里没有“盈利性”，那是商业目标，不是可用性指标。

---

### Q3. “Users complete tasks accurately” corresponds to:

A. Efficiency
B. Effectiveness
C. Engagement
D. Memorability

**Answer: B**
**EN:** Effectiveness = accuracy and completeness of task achievement.
**中：** 有效性强调“做对、做完”。

---

### Q4. “Users complete tasks with minimal time and effort” corresponds to:

A. Efficiency
B. Effectiveness
C. Engagement
D. Reliability

**Answer: A**
**EN:** Efficiency is about time/effort cost to complete tasks.
**中：** 效率强调“又快又省力”。

---

### Q5. Which design decision most directly supports ease of learning?

A. Randomly changing icon meanings each release
B. Reusing familiar interaction patterns across screens
C. Hiding all advanced functions permanently
D. Removing all onboarding tips

**Answer: B**
**EN:** Familiar, consistent patterns reduce learning burden.
**中：** 一致且熟悉的交互可降低学习成本。

---

### Q6. Tooltips are most useful when:

A. They appear on every click forever
B. They are contextual, actionable, and dismissible
C. They replace all interface labels
D. They only show technical model parameters

**Answer: B**
**EN:** Good tooltips help at the right time and can be dismissed.
**中：** 好提示是“适时、可行动、可关闭”。

---

### Q7. In AI UX, consistency mainly helps by:

A. Increasing model size
B. Reducing users’ need to form new mental models repeatedly
C. Removing the need for feedback
D. Preventing all errors

**Answer: B**
**EN:** Consistency supports transfer of prior knowledge and stable mental models.
**中：** 一致性让用户“学一次到处用”。

---

### Q8. Which is the best example of informative system feedback?

A. No response while model is running
B. “Processing...” plus visible progress indication
C. Showing stack traces to all users
D. Restarting the task silently

**Answer: B**
**EN:** Users need immediate, understandable status feedback, especially for delays.
**中：** 有延迟时必须给清晰进度反馈。

---

### Q9. Why is missing system feedback harmful?

A. It improves user patience
B. It increases perceived transparency
C. It may make users think the system is broken
D. It guarantees fewer mistakes

**Answer: C**
**EN:** No feedback causes uncertainty and damages trust.
**中：** 没反馈会让用户以为系统坏了，信任下降。

---

### Q10. Which statement about AI errors is most accurate?

A. Good AI UX assumes errors never happen
B. AI errors are impossible with enough UI polish
C. AI outputs are probabilistic, so error-tolerant design is necessary
D. Errors only come from users

**Answer: C**
**EN:** AI systems are probabilistic; UX must support recovery and tolerance.
**中：** AI有不确定性，必须做容错与恢复设计。

---

### Q11. Which best distinguishes an error from a failure?

A. Error is always catastrophic; failure is minor
B. Error is mismatch/inaccuracy; failure is inability to perform intended function safely/adequately
C. They are identical
D. Failure is only caused by users

**Answer: B**
**EN:** Error can be recoverable; failure is a more severe breakdown.
**中：** Error多为可恢复偏差，Failure是功能层面的失效。

---

### Q12. Which is an AI-system error source (not user error)?

A. Ambiguous prompt by user
B. Mistyped date format
C. Biased training data
D. Clicking wrong button

**Answer: C**
**EN:** Biased/poor training data is a system-side error source.
**中：** 训练数据偏差属于系统端错误来源。

---

### Q13. Best practice for error messages in consumer AI products is:

A. Show internal exception code only
B. Use blameful wording (“You entered illegal input”)
C. Use plain language + recovery suggestion
D. Hide all errors to reduce anxiety

**Answer: C**
**EN:** Human-readable and actionable error messages improve recovery.
**中：** 报错要说人话，并告诉用户下一步怎么做。

---

### Q14. A recommender predicts wrong items. What is the best UX response?

A. Disable feedback to avoid noise
B. Ask users for quick explicit feedback (e.g., thumbs down)
C. Force users to re-register
D. Ignore because model is “mostly right”

**Answer: B**
**EN:** Misclassifications are opportunities to gather corrective feedback.
**中：** 误判是收集纠偏反馈的好时机。

---

### Q15. Which is the most user-friendly way to handle ambiguous input?

A. “Invalid query. End.”
B. “Did you mean A, B, or C?”
C. Automatically pick random interpretation
D. Block the user for repeated ambiguity

**Answer: B**
**EN:** Clarification choices reduce friction and improve outcomes.
**中：** 给候选澄清项是最佳实践。

---

### Q16. Which design most effectively prevents input errors?

A. Free-text date with no format hint
B. Date picker + format constraints
C. Hidden validation rules
D. Delayed validation after submission only

**Answer: B**
**EN:** Structured controls prevent common entry errors.
**中：** 用控件约束输入可显著减少错误。

---

### Q17. Which statement aligns with “do not blame users”?

A. “Your invalid command caused failure.”
B. “You clearly don’t understand this feature.”
C. “I couldn’t complete that—try selecting a date from the calendar.”
D. “Error 0xA31.”

**Answer: C**
**EN:** Respectful wording + recovery guidance supports UX and trust.
**中：** 不指责用户，提供可执行修复建议。

---

### Q18. Which action best supports experienced users while still helping novices?

A. Mandatory tutorial before every action
B. Tooltips that can be dismissed and not shown again
C. Remove all help content
D. Force novice mode forever

**Answer: B**
**EN:** Optional, dismissible assistance balances novice and expert needs.
**中：** 可关闭提示兼顾新手与老手。

---

### Q19. Which scenario reflects good AI-awareness design?

A. AI features are indistinguishable from non-AI features
B. AI actions are indicated with clear labels/cues
C. AI labels are hidden to avoid user concern
D. All features are labeled “AI” regardless of actual use

**Answer: B**
**EN:** Users should know when AI is involved.
**中：** 用户应清楚何时AI在参与决策/生成。

---

### Q20. Which is the best summary of usability-oriented HCAI design?

A. Maximize automation no matter what
B. Prioritize aesthetics over task success
C. Make interaction intuitive, feedback timely, and recovery easy
D. Avoid collecting any user feedback

**Answer: C**
**EN:** Usability-centered HCAI focuses on successful, efficient, recoverable interactions.
**中：** 核心是“好懂、好用、可恢复”。

---

## Part B — HCAI UX Design: Trust (Q21–Q40)

### Q21. Trust calibration means:

A. Maximizing trust at all times
B. Matching user trust level to actual AI capability
C. Removing user control to avoid doubt
D. Showing confidence scores only

**Answer: B**
**EN:** Proper calibration avoids both overtrust and distrust.
**中：** 信任要与能力匹配，过高过低都不对。

---

### Q22. Which is an example of overtrust?

A. User verifies AI in high-stakes surgery support
B. User ignores a highly reliable low-stakes recommendation
C. User follows AI blindly in a context requiring human judgment
D. User asks for explanation before action

**Answer: C**
**EN:** Overtrust is reliance beyond system competence/scope.
**中：** 过度信任=不该全信时却盲信。

---

### Q23. Which is an example of distrust?

A. Appropriate reliance on proven tool
B. Rejecting useful AI support despite good evidence of capability
C. Human-AI shared decision workflow
D. Using confidence with caution

**Answer: B**
**EN:** Distrust is under-reliance despite adequate capability.
**中：** 不信任=AI明明可用却完全不用。

---

### Q24. In Chapter 5.2, two main trust design levers are:

A. Speed and animation
B. Explainability and user control
C. Branding and pricing
D. Personalization and gamification only

**Answer: B**
**EN:** Trust is primarily built through explainability + control.
**中：** 建信任的双核心：可解释、可控制。

---

### Q25. Which stakeholder pairing is most accurate?

A. Auditors need no explanation
B. Affected individuals and decision-makers may need different explanation depth
C. Engineers need only color-coded dashboards
D. Everyone should see identical technical explanations

**Answer: B**
**EN:** Explanation depth should be tailored by stakeholder role.
**中：** 不同角色需要不同层级解释。

---

### Q26. “State capabilities and limitations clearly” primarily helps:

A. Increase overtrust
B. Reduce expectation mismatch
C. Remove need for UI
D. Eliminate all model errors

**Answer: B**
**EN:** Clear scope statements prevent inflated assumptions.
**中：** 讲清边界可减少期望错配。

---

### Q27. Which wording best reflects performance humility?

A. “This model is always correct.”
B. “100% guaranteed outcome.”
C. “This prediction may be uncertain in sparse-data cases.”
D. “No limitations apply.”

**Answer: C**
**EN:** Humble, realistic communication supports calibrated trust.
**中：** 谦逊表达有助于建立“真实信任”。

---

### Q28. Why explain adaptive behavior over time?

A. To hide model updates
B. To help users understand why outputs may change
C. To reduce transparency
D. To prevent users from giving feedback

**Answer: B**
**EN:** Users need reasons for changing outputs to maintain trust.
**中：** 结果变化要解释“为什么变了”。

---

### Q29. Input/output transparency includes:

A. Only showing final answer
B. Hiding data sources for security theater
C. Clarifying what data is used and how outputs are produced
D. Showing model code to every user

**Answer: C**
**EN:** Transparency is about understandable data-use and output rationale.
**中：** 透明性要说明“用了什么数据、怎么得出结果”。

---

### Q30. Which explanation style is generally preferred in UX?

A. Maximum technical depth for all users
B. Concise, understandable, context-relevant explanation
C. No explanation unless asked by regulators
D. Purely probabilistic formula display

**Answer: B**
**EN:** Explanations should be intelligible and actionable for target users.
**中：** 解释要简洁可懂且与场景相关。

---

### Q31. Confidence display can be risky because:

A. It always decreases trust
B. Users may misinterpret confidence as guaranteed correctness
C. It cannot be shown numerically
D. It prevents N-best alternatives

**Answer: B**
**EN:** Confidence can mislead if interpreted as certainty.
**中：** 置信度可能被误读为“绝对正确”。

---

### Q32. Which is NOT a common confidence presentation format?

A. High/Medium/Low labels
B. Percentage score
C. Ranked alternatives (N-best)
D. Hidden confidence with no internal use

**Answer: D**
**EN:** Common formats include categorical, numeric, and ranked alternatives.
**中：** 常见是分级、百分比、候选排序。

---

### Q33. High-stakes domains should generally have:

A. Less human control to increase speed
B. More user oversight, control, and intervention options
C. No explanations to avoid cognitive load
D. Fully autonomous final decisions by default

**Answer: B**
**EN:** High stakes require stronger human control and oversight.
**中：** 高风险场景必须加强人工把关。

---

### Q34. “Graceful handover” refers to:

A. Switching users to a new app silently
B. Seamless transfer from AI to human support when AI cannot proceed
C. Ending session immediately on error
D. Asking users to restart from scratch

**Answer: B**
**EN:** Good handover preserves context and reduces frustration.
**中：** 优雅交接=不中断、不丢上下文、少折腾用户。

---

### Q35. Fine-grained input-data control means:

A. Users must accept all tracking or leave
B. Users can selectively allow/deny specific data uses
C. Data settings are fixed permanently
D. Data deletion is impossible

**Answer: B**
**EN:** Granular controls improve agency and trust.
**中：** 细粒度权限让用户有真正控制权。

---

### Q36. Which feature best supports output control?

A. One forced recommendation with no alternatives
B. Ability to re-rank, tune preferences, and dismiss irrelevant outputs
C. Hidden personalization knobs
D. Locking output to model default forever

**Answer: B**
**EN:** Output control lets users steer AI toward their needs.
**中：** 结果可调可筛是“可控AI”的关键。

---

### Q37. Explicit feedback is:

A. Inferred only from passive logs
B. Intentionally provided by users (e.g., thumbs up/down, survey)
C. Always mandatory after every click
D. Impossible to undo

**Answer: B**
**EN:** Explicit feedback is deliberate user-provided signal.
**中：** 显式反馈是用户主动给出的评价信号。

---

### Q38. Good explicit feedback mechanisms should be:

A. Ambiguous and broad
B. Mutually exclusive, clear, and actionable
C. Hidden in developer settings
D. Available only to premium users

**Answer: B**
**EN:** Clear options produce more reliable signal quality.
**中：** 选项清晰互斥，反馈数据才更干净可用。

---

### Q39. Implicit feedback must be designed with:

A. Covert tracking by default
B. Transparency, consent, and opt-out options
C. No user awareness
D. Automatic sharing with third parties

**Answer: B**
**EN:** Ethical collection of behavioral feedback requires disclosure and control.
**中：** 隐式反馈必须透明告知并允许退出。

---

### Q40. Which statement best captures trustworthy HCAI UX?

A. Trust comes from perfect accuracy only
B. Trust comes from explainability only
C. Trust comes from controllability only
D. Trust is strengthened by explainability + user control + feedback loops

**Answer: D**
**EN:** Sustainable trust requires multiple mechanisms working together.
**中：** 长期信任来自“可解释+可控制+可反馈”的组合。

---

---

## Score Guide (quick self-check)

* **36–40** : Excellent (quiz-ready)
* **30–35** : Good (review trust calibration + error handling details)
* **24–29** : Needs reinforcement (redo by section 5.1 then 5.2)
* **<24** : Rebuild foundations with definition-level concepts first

---

如果你愿意，我下一步可以把这 40 题再做成两版方便冲刺：

1. **纯考试版** （只有题目，不显示答案，便于自测）
2. **错题复盘版** （按知识点聚类：Usability/Trust/Explainability/Control/Feedback）
