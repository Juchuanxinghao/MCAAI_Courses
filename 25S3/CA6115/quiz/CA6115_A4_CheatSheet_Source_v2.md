## [[Find-Fast Answer Map]]
- [[L1]] data types, data life cycle, governance, FEAT, encoding, integration, “why finance data is hard”.
- [[L2]] supervised/unsupervised/RL, logistic/tree/DL, confusion matrix, precision vs recall, ROC/AUC, overfitting.
- [[L3]] risk-return, CAPM, beta, factor investing, Sharpe/Sortino/Max DD, backtesting traps.
- [[L4]] NLP, BoW, embeddings, sentiment, Dow Theory, MA/MACD/RSI/Bollinger Bands.
- [[L5]] AML/CFT, KYC/CDD/EDD/SAR, FATF, K-means/DBSCAN/anomaly detection, graph 3Cs.
- [[L6]] agentic AI, Ollama, RAG, MCP, LangChain, LangGraph, workflow design.
- [[Exam tactic]] first match the keyword in the question to the lecture bucket above; then use the direct answer lines below.

## [[L1 Intro to AI in Finance]]
- [[Where AI is used]] credit/loan approval, customer segmentation, prospecting, fraud/AML, chatbots, robo-advisory, risk management, trading, news monitoring, compliance reporting.
- [[Why finance is special]] finance affects livelihoods and systemic stability; markets adapt; human behavior is noisy; data is messy; experiments are hard; regulation matters more than in many other domains.
- [[Finance data types]] [[structured numeric]] prices, volume, rates, revenue, assets; [[ordinal]] ratings AAA->BB, analyst buy/hold/sell; [[nominal]] sector/industry labels; [[unstructured]] news, filings, audio, images, social posts.
- [[Alternative data]] web traffic, card spending, satellite images, geolocation, weather, app usage, parking-lot activity; used to get an informational edge beyond standard statements/prices.
- [[Data sources]] Bloomberg/Refinitiv, exchanges, SEC EDGAR/SGXNet, IMF/World Bank/FED, internal transaction systems, web/API sources.
- [[Transformation]] aggregate daily->weekly/monthly; normalize with [[min-max]]; standardize with [[z-score]]; smooth, encode, clean, and create features so models can learn stable patterns.
- [[Integration issues]] multiple sources may disagree; values can be duplicated, stale, missing, or inconsistent; poor integration creates garbage-in-garbage-out errors.
- [[Encoding]] models need numbers; [[one-hot encoding]] turns categories into binary flags and avoids fake ordering between categories.
- [[Data governance]] objective = data quality + privacy/security + standardization + accountability + business value; the point is not only to store data but to make it reliable and defensible.
- [[Data life cycle memory]] [[Plan -> Design -> Create/Obtain -> Store/Maintain -> Use -> Enhance]]. If the exam asks for steps, keep this exact order.
- [[Plan 计划]] define business purpose, what decision the data supports, who owns it, which fields are needed, legal basis/consent, retention period, success metric, and access rights.
- [[Design 设计]] choose schema/table structure, labels, data format, update frequency, validation checks, privacy controls, and how downstream teams/models will consume the data.
- [[Create/Obtain 获取]] collect from customers, internal systems, vendors, public filings, or exchanges; verify licensing, provenance, consent, completeness, and initial quality.
- [[Store/Maintain 存储维护]] keep in database/data lake/cloud; add backups, encryption, access control, versioning, lineage, cleaning, deduplication, and regular updates.
- [[Use 使用]] apply the data to reporting, model training, segmentation, pricing, AML monitoring, trading, or decision support, but only for the approved business purpose.
- [[Enhance 增强]] enrich with external sources, engineer new features, relabel/repair errors, anonymize where needed, and learn from user feedback to improve quality and usefulness.
- [[MAS FEAT]] [[Fairness]] = unbiased and consistent outcomes; [[Ethics]] = use AI responsibly; [[Accountability]] = the institution owns the decision and cannot blame the model; [[Transparency]] = explainable, documented, auditable logic.
- {{Q}} Which FEAT principle says the firm cannot blame the algorithm? {{Ans}} Accountability.
- {{Q}} Which data type fits analyst recommendations or credit ratings? {{Ans}} Ordinal data.
- {{Q}} Why do one-hot encoding? {{Ans}} To avoid false ordinal relationships between categories.

## [[L2 ML in Finance Operations]]
- [[ML types]] [[supervised]] uses labeled outcomes; [[unsupervised]] finds hidden patterns without labels; [[reinforcement learning]] learns actions from reward/penalty feedback.
- [[Typical supervised tasks]] [[classification]] predicts a class (default / non-default, fraud / not fraud); [[regression]] predicts a number (return, loss, price, revenue).
- [[Workflow]] define objective -> gather labeled data -> select features -> split train/validation/test -> train -> evaluate on unseen data -> tune threshold/model -> deploy -> monitor drift and errors.
- [[Data splits]] [[resubstitution]] train=test (weak, only if data is tiny); [[hold-out]] often 80/20; [[cross-validation]] rotates folds for more stable evaluation; [[bootstrap]] samples with replacement.
- [[Why validation matters]] finance is non-stationary and noisy, so high in-sample accuracy can be fake comfort; only out-of-sample performance shows whether the model generalizes.
- [[Common models]] logistic regression, naive Bayes, decision trees, SVM, perceptron/deep learning; no single model is always best.
- [[Logistic regression]] interpretable baseline for binary outcomes; outputs probability and odds p/(1-p); often a threshold such as 0.5 maps probability to class.
- [[Decision tree]] easy to explain and audit; works with numeric + categorical variables; downside = unstable and can overfit if the tree becomes too complex.
- [[Naive Bayes]] fast probabilistic benchmark based on Bayes rule; assumes features are independent, which is often unrealistic but still useful as a simple baseline.
- [[Deep learning]] powerful for complex nonlinear patterns and unstructured data, but is compute-heavy, less explainable, and can overfit.
- [[Confusion matrix]] [[TP]] predicted positive and actually positive; [[TN]] predicted negative and actually negative; [[FP]] false alarm; [[FN]] missed bad case.
- [[Accuracy]] = overall correctness, but it can look great when classes are imbalanced. Example: if 95% of loans are good, always predicting “good” gives high accuracy but poor risk control.
- [[Precision]] TP/(TP+FP) = among the cases you flagged positive, how many were truly positive? Use when false alarms are costly.
- [[Recall / Sensitivity]] TP/(TP+FN) = among the truly positive cases, how many did you catch? Use when misses are costly.
- [[Threshold trade-off]] lower threshold -> catch more positives -> higher recall but also more FP; higher threshold -> fewer FP but more missed positives.
- [[Default example]] if “positive” means default, then [[FP]] = reject a customer who would have repaid; [[FN]] = approve a borrower who later defaults. Banks usually fear FN more.
- [[ROC/AUC]] ROC plots TPR against FPR across thresholds; [[AUC]] summarizes discrimination skill, with 1.0 = perfect and 0.5 = no better than random.
- [[Overfitting]] model memorizes training noise/details and performs badly on new data; [[underfitting]] model is too simple and misses real structure.
- [[Finance overfitting traps]] small samples, regime changes, repeated backtests, too many features, data snooping, and optimizing to past noise.
- [[Metric logic]] catching fraud/default -> recall often matters more; prospecting/marketing -> precision often matters more; always match metric to business cost of error.
- {{Q}} Conservative bank wants to catch defaulters. Best metric? {{Ans}} Recall / sensitivity.
- {{Q}} Marketing wants fewer false alarms on leads. Best metric? {{Ans}} Precision.
- {{Q}} 99% training accuracy but weak test accuracy indicates? {{Ans}} Overfitting.

## [[L3 Investment Management]]
- [[Risk-return idea]] most investors are risk-averse: they want more return only if compensated for taking more risk; that extra expected compensation is the [[risk premium]].
- [[Return]] = (ending value - invested amount) / invested amount; if dividends/coupons exist, include them in total return.
- [[Expected return]] is the probability-weighted average of possible returns, not just one scenario.
- [[Risk types]] [[stand-alone risk]] = total risk of one asset; [[portfolio risk]] depends on how assets move together, so diversification can reduce unsystematic risk.
- [[Standard deviation]] measures volatility / dispersion of returns; higher standard deviation = more uncertainty.
- [[CAPM]] [[r_i = r_RF + (r_M-r_RF)β_i]]. Read it as: required return = risk-free rate + beta-adjusted market risk premium.
- [[CAPM variables]] [[r_RF]] = risk-free rate; [[r_M-r_RF]] = market risk premium; [[β_i]] = how sensitive the stock is to market moves.
- [[Beta meaning]] β=1 moves like the market; β>1 is more aggressive/riskier; β<1 is more defensive; beta is about systematic market risk, not firm-specific noise.
- [[Why only market risk in CAPM?]] because diversification can remove firm-specific risk, so investors are mainly compensated for non-diversifiable market risk.
- [[Factor pricing]] extends CAPM beyond one factor: expected return can depend on market, size, value, momentum, profitability, investment, and other signals.
- [[Factor examples]] P/E, P/B, EV/EBITDA, EV/Sales, ROE, sentiment, macro factors, alternative data; AI/ML helps discover nonlinear or hidden factors.
- [[Sharpe ratio]] (Rp-Rf)/σp = excess return per unit of total volatility; good for overall risk-adjusted performance.
- [[Sortino ratio]] (Rp-Rf)/σd = excess return per unit of downside risk only; useful when upside volatility should not be punished.
- [[Max drawdown]] worst peak-to-trough loss; important because a deep drawdown is psychologically and financially hard to recover from.
- [[Backtesting]] simulate the strategy on historical data to see returns, stability, and drawdowns before live deployment.
- [[Backtest traps]] survivorship bias, short sample window, choosing the year that works, ignoring costs/slippage, data snooping, and worshipping one metric only.
- [[Bagging vs boosting]] [[bagging]] trains many weak learners in parallel then votes; [[boosting]] trains sequentially and focuses on prior errors.
- {{Q}} β > 1 implies what? {{Ans}} The stock is more sensitive/riskier than the market.
- {{Q}} Which metric penalizes only downside volatility? {{Ans}} Sortino ratio.
- {{Q}} Great backtest but bad future live result usually means? {{Ans}} Overfitting, regime change, or data snooping.

## [[L4 NLP + Algorithmic Trading]]
- [[NLP purpose]] convert unstructured text into signals that models can use for classification, sentiment, tagging, search, or decision support.
- [[Text sources]] news, analyst reports, filings, transcripts, contracts, emails, support chats, social media, policy statements, customer feedback.
- [[BoW]] Bag-of-Words counts terms in documents and builds a term-document matrix; it is simple and fast but loses word order and context.
- [[Tokenization]] break text into tokens/subwords/roots so a computer can process it; this helps standardize variants of the same word.
- [[Embeddings]] represent words or texts as vectors that preserve contextual similarity; unlike BoW, they keep semantic relationships better.
- [[LLMs]] large transformer-based models trained on massive corpora; useful for summarization, classification, Q&A, drafting, and workflow support.
- [[Finance NLP uses]] sentiment on news, entity/event extraction, compliance screening, KYC name matching, chatbot support, product matching, risk summarization.
- [[Technical analysis]] studies price/volume charts for pattern, trend, and timing; AI can augment TA by automating signal extraction.
- [[Dow Theory]] market discounts everything; primary trend matters most; trends have accumulation -> public participation -> distribution phases.
- [[Moving averages]] smooth noise and help identify trend direction/support/resistance; crossover rules often generate simple buy/sell signals.
- [[MACD]] 12-EMA minus 26-EMA; signal line = 9-EMA of MACD; crossovers or divergences hint at momentum changes.
- [[RSI]] momentum oscillator; below 30 often = oversold; above 80 often = overbought.
- [[Bollinger Bands]] SMA with upper/lower volatility bands; squeeze/tightening can warn of an upcoming breakout.
- [[TA pros/cons]] pros = intuitive and easy to apply; cons = subjective, not strongly grounded in theory, and can miss surprise fundamentals.
- {{Q}} Biggest weakness of BoW? {{Ans}} It loses word order and deeper context.
- {{Q}} RSI > 80 means? {{Ans}} Overbought. RSI < 30 means oversold.
- {{Q}} MACD crossing above signal line often suggests? {{Ans}} A possible bullish/buy signal.

## [[L5 Regulatory Compliance + Unsupervised Learning]]
- [[Compliance split]] [[regulatory compliance]] = obey laws/rules/sanctions/Basel; [[financial crime compliance]] = AML/CFT/fraud detection and reporting.
- [[Money laundering stages]] [[Placement]] put dirty money into the system; [[Layering]] move it through complex transfers to hide origin; [[Integration]] reintroduce it as apparently legitimate wealth.
- [[FATF]] global AML standard setter; the FATF 40 Recommendations emphasize risk-based controls, KYC, suspicious reporting, cooperation, beneficial ownership, and sanctions.
- [[KYC/CDD/EDD/SAR]] [[KYC]] verify customer identity; [[CDD]] understand purpose, source of funds, expected activity, and risk; [[EDD]] deeper checks for high-risk clients; [[SAR]] suspicious activity report filed when behavior looks abnormal.
- [[Red flags]] just-below-threshold transfers, rapid movement through many accounts, shell companies, inconsistent explanations, refusal to provide documents, high-risk jurisdictions, sanctions exposure.
- [[Why AI matters]] institutions face huge alert volumes; AI helps prioritize suspicious activity, reduce false positives, trace patterns, and monitor adverse news.
- [[Unsupervised learning]] finds clusters, structure, or anomalies without labeled targets; useful when suspicious behavior is rare or not fully labeled.
- [[K-means]] choose k, assign points to nearest centroid, recompute centroids, and repeat; best for roughly compact/spherical clusters.
- [[Distance measures]] Euclidean, Manhattan, Minkowski; standardize numeric features first so one variable does not dominate only because of scale.
- [[Anomaly detection]] flags points that do not fit the normal pattern; perfect for fraud, AML, unusual trading, or operational risk monitoring.
- [[DBSCAN]] density-based clustering with eps + minPts; good for irregular shapes, noisy data, and outliers, so it often fits suspicious-activity patterns better than K-means.
- [[Graphs/networks]] represent entities as nodes and relationships as links; useful for KYC ownership webs, contagion, payment networks, and exposure chains.
- [[3 Cs]] [[centrality]] who matters most; [[clusterness]] who groups together; [[connectedness]] how risk/influence spreads across the network.
- {{Q}} Correct laundering order? {{Ans}} Placement -> Layering -> Integration.
- {{Q}} Best method for irregular suspicious clusters plus outliers? {{Ans}} DBSCAN.
- {{Q}} What is the operational pain point in AML systems? {{Ans}} Too many false positives.

## [[L6 Agentic AI in Finance]]
- [[Agentic AI]] autonomous, goal-directed systems that perceive, reason, use tools, act, and adapt; it is about getting work done, not only generating text.
- [[Agentic AI vs GenAI]] [[GenAI]] mainly generates or summarizes; [[agentic AI]] plans steps, calls tools/APIs, uses memory, and completes multi-step workflows.
- [[How it works]] perception/input -> reasoning/planning -> action/tool use -> feedback -> adjustment toward goal.
- [[Ollama]] local runtime for open-source LLMs; good for privacy, cost control, offline use, latency, and regulatory comfort.
- [[RAG]] Retrieval-Augmented Generation: pull relevant knowledge from internal/external documents into the prompt so answers are grounded in actual sources.
- [[MCP]] Model Context Protocol: standardized bridge that lets the model connect to live tools, APIs, databases, spreadsheets, and services.
- [[RAG vs MCP]] if the task is [[answer from documents]], choose [[RAG]]; if the task is [[query or act on live systems/tools]], choose [[MCP]]. Easy exam memory: [[RAG = knowledge]], [[MCP = action]].
- [[Framework roles]] [[LlamaIndex]] helps RAG/indexing; [[LangChain]] general LLM app framework; [[LangGraph]] strong for multi-agent orchestration/workflow graphs.
- [[Enterprise concerns]] security, confidentiality, scaling, structured JSON outputs, robustness, customization, memory, and integration with legacy systems.
- [[Finance use cases]] client support, portfolio/risk reporting, FX hedging agents, trading assistants, compliance review, document summarization, internal knowledge search.
- [[Design checklist]] define goal -> map workflow -> decide what context is needed -> choose model -> choose tools -> set memory/guardrails -> add human oversight.
- {{Q}} “Summarize the risk section from a prospectus” needs what? {{Ans}} RAG.
- {{Q}} “Query my spending categories from a live database” needs what? {{Ans}} MCP.
- {{Q}} Which framework is strongest for multi-agent orchestration? {{Ans}} LangGraph.

## [[If You Panic in the Exam, Use These Direct Answer Cues]]
- [[Need labels?]] supervised. [[Need patterns without labels?]] unsupervised. [[Need reward-based action learning?]] reinforcement learning.
- [[Want fewer missed fraud/default cases?]] choose recall. [[Want fewer false alarms?]] choose precision.
- [[Single-factor pricing model?]] CAPM. [[Multi-factor extension?]] factor model.
- [[Total-risk performance metric?]] Sharpe. [[Downside-only metric?]] Sortino.
- [[Text counts only?]] BoW. [[Context-aware text vectors?]] embeddings.
- [[Known k, compact clusters?]] K-means. [[Irregular clusters + noise/outliers?]] DBSCAN.
- [[Document grounding?]] RAG. [[Live tool/database connection?]] MCP.
- [[RSI <30]] oversold. [[RSI >80]] overbought. [[β>1]] more market-sensitive/riskier than market.

## [[Formula Box]]
- [[Min-max]] x' = (x-min)/(max-min).
- [[z-score]] z = (x-μ)/σ.
- [[Accuracy]] (TP+TN)/(TP+TN+FP+FN).
- [[Precision]] TP/(TP+FP).
- [[Recall]] TP/(TP+FN).
- [[CAPM]] r_i = r_RF + (r_M-r_RF)β_i.
- [[Sharpe]] (R_p-R_f)/σ_p.
- [[Sortino]] (R_p-R_f)/σ_d.
- [[MACD]] 12-EMA - 26-EMA; signal = 9-EMA(MACD).
- [[RSI]] 100 - 100/(1 + n_up/n_down).

## [[Rapid Answer Bank]]
- {{Q}} Exact data life-cycle order? {{Ans}} Plan -> Design -> Create/Obtain -> Store/Maintain -> Use -> Enhance.
- {{Q}} Why is finance difficult for AI? {{Ans}} adaptive markets, human behavior, noisy data, regulation, and systemic risk.
- {{Q}} Which metric becomes misleading with class imbalance? {{Ans}} Accuracy.
- {{Q}} What does a lower classification threshold do? {{Ans}} raises recall and false positives.
- {{Q}} What does beta measure? {{Ans}} sensitivity of a stock to market movements.
- {{Q}} CAPM compensation is for which risk? {{Ans}} systematic / market risk.
- {{Q}} Why can factor premiums disappear? {{Ans}} crowding, regime change, or arbitrage reducing mispricing.
- {{Q}} BoW versus embeddings in one line? {{Ans}} counts only vs context-aware vectors.
- {{Q}} What does RSI below 30 usually mean? {{Ans}} oversold.
- {{Q}} KYC vs CDD in one line? {{Ans}} identity verification vs broader understanding of customer purpose/source/risk.
- {{Q}} Why is DBSCAN useful in AML? {{Ans}} it handles irregular suspicious clusters, density patterns, and outliers.
- {{Q}} What makes DBSCAN different from K-means? {{Ans}} DBSCAN is density-based; K-means uses distance to centroid and fixed k.
- {{Q}} Why standardize before clustering? {{Ans}} to equalize scales so big-number features do not dominate distances.
- {{Q}} Which AML stage best hides illicit origin? {{Ans}} Layering.
- {{Q}} Which obligation mandates identity verification? {{Ans}} KYC.
- {{Q}} Which red flag suggests threshold evasion? {{Ans}} just-below-threshold amounts / structuring.
- {{Q}} Which graph property finds influencers? {{Ans}} Centrality.
- {{Q}} Which graph approach reveals hidden KYC links? {{Ans}} Graph analytics.
- {{Q}} Which DBSCAN parameter measures neighborhood density range? {{Ans}} eps radius.
- {{Q}} Reduce false positives by improving what? {{Ans}} Precision.
- {{Q}} RAG versus MCP in one line? {{Ans}} document grounding vs live tool/system connection.
- {{Q}} Why use Ollama? {{Ans}} private local model running with lower cost and better control.