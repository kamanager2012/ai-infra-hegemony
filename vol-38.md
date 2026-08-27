# 第三十八卷：AI 时代劳动市场重构——从任务暴露到岗位、工资与组织结构

## 1. 研究问题：AI 首先改变的是任务，而不是岗位名称

AI 对劳动市场的影响，不能直接用“多少岗位会消失”来描述。现有公开研究更支持一个分阶段过程：模型先改变可自动化任务的边界，企业随后根据成本、质量、合规和责任约束重写工作流，最后才体现为岗位数量、工资、晋升路径和组织层级的变化。

因此，本卷采用 **Task-to-Job Translation Layer（任务到岗位转换层）** 作为统一分析框架：

```text
Task Exposure
→ Adoption Economics
→ Workflow Redesign
→ Responsibility Constraint
→ Employment / Wage Outcome
```

其中：

- **Task Exposure**：模型在技术上能否完成某项任务；
- **Adoption Economics**：AI 成本、质量、迁移成本和合规成本是否优于人工；
- **Workflow Redesign**：企业是否真正重构业务流程，而不仅是增加一个 AI 助手；
- **Responsibility Constraint**：签字、执照、现场责任、人身安全和法律责任是否允许完全无人化；
- **Employment / Wage Outcome**：岗位数量、工资、晋升路径和组织结构最终如何变化。

这意味着“某职业 70% 暴露于 AI”不能直接翻译为“70% 岗位消失”；同样，“总就业尚未下降”也不能证明冲击很小，因为任务结构、初级岗位入口、晋升梯子和工资分布可能已经发生变化。

## 2. 公开劳动研究的共同结论：暴露不等于失业

国际劳工组织（ILO）2026 年研究简报 *Workers' exposure to AI: What indicators tell us – and what they don't* 明确指出，AI exposure 指标衡量的是技术上哪些任务可能被自动化，而不是自动化是否具有经济性、能否产生生产率提升，或最终如何影响就业。

ILO 同时强调，这类指标不应直接用于预测岗位损失，更适合作为识别“哪些职业的任务内容最可能发生变化”的早期预警工具。

ILO 2025 refined global index 进一步显示，全球约四分之一就业岗位处于某种程度的生成式 AI 暴露之中，但最高暴露等级约占全球就业 **3.3%**。其核心判断仍然是：多数岗位更可能被**重构**，而不是直接冗余。

国际货币基金组织（IMF）2024 年 Staff Discussion Note *Gen-AI: Artificial Intelligence and the Future of Work* 给出的同样是暴露，而不是失业预测：

- 全球约 **40%** 的就业岗位暴露于 AI；
- 发达经济体约 **60%**；
- 新兴市场约 **40%**；
- 低收入国家约 **26%**。

IMF 进一步将高暴露岗位区分为高互补和低互补两类。发达经济体中，高暴露且高互补岗位约占就业 **27%**，高暴露且低互补岗位约占 **33%**。这说明同样的 AI 能力，对不同职业可能分别表现为生产率增强和替代压力。

OECD 的相关研究也观察到，AI 当前进展最明显的领域主要集中在非常规认知任务，因此认知、分析、行政和管理类岗位暴露更高；但到相关研究发表时，OECD 国家尚未出现可归因于 AI 的显著总量就业下降。

三类机构研究共同支持一个结论：**AI 劳动冲击首先表现为任务重构和组织调整，而不是一张可以直接换算成失业率的技术暴露表。**

## 3. 企业为什么有动力重构劳动：AI Software Unit Economics

劳动替代并不由模型能力单独决定，核心仍是单位经济。

传统 SaaS “毛利率从 85% 降到 55%”只能作为压力测试，不应被写成行业已发生事实。本报告统一采用第二十七卷提出的 **AI Software Unit Economics**：

AI 产品的单位成本至少包括：

- inference；
- retrieval / storage；
- tool / API calls；
- human review；
- AI-specific cloud compute；
- workflow orchestration。

只有当某项人工任务可以稳定转换为更低成本、可检查、可回滚的 AI 工作流时，企业才具有持续减少人工投入的经济动机。

这也是为什么“模型更强”与“岗位更少”之间存在显著时滞。很多企业已经部署 Copilot 或 Agent，但如果流程没有重构，AI 只是在原有劳动结构上增加了一层软件成本，并没有真正替代岗位。

## 4. 最先被改写的劳动：可文本化、可验证、可回滚的中间任务

AI 最容易替代的不是“某一个完整职业”，而是职业内部具有以下特征的任务：

- 输入和输出高度文本化；
- 结果可以快速验证；
- 错误可以回滚；
- 不需要现场责任；
- 不要求法定签字或执照；
- 数据和工具接口已经数字化。

典型例子包括：

- 初步信息整理；
- 文档草拟；
- 标准代码生成与修复；
- 常规数据分析；
- 客服与运营流程；
- 标准化研究辅助；
- 部分财务、法务和行政流程。

这些任务过去往往由初级与中级知识工作者承担，因此 AI 的第一轮冲击很可能首先体现在：

1. 初级岗位入口减少；
2. 同一岗位负责的任务数量增加；
3. 中层协调岗位减少；
4. 产出评价从“工作时间”转向“工作流结果”。

岗位名称可能仍然存在，但岗位内部任务组合已经改变。

## 5. 不容易被完全替代的劳动：责任、现场与不可逆风险

AI 对物理世界和高责任行业的替代速度通常更慢。

主要原因并不是模型一定做不到，而是责任不能轻易转移。以下类别仍需要较强的人类在环约束：

- 医疗诊断与临床责任；
- 法律签字与执业责任；
- 结构工程签字；
- 核电运行；
- 电网调度；
- 高风险工业现场；
- 安装、维修和校准；
- 照护与人身安全相关工作。

这类工作即使大量使用 AI，也更可能形成“人负责最终责任、AI 承担分析和执行辅助”的协同结构，而不是直接无人化。

因此，职业执照、行业标准、保险和法律责任会成为 AI 自动化的重要减速带。

## 6. AI 基础设施本身也在创造新的稀缺劳动

AI 对劳动市场的影响不是单向减少岗位。基础设施扩张正在创造一批新的高门槛岗位，其稀缺性来自物理系统而不是提示词能力。

主要包括：

- distributed systems；
- multi-model / multi-accelerator orchestration；
- cluster scheduling；
- HBM / memory system engineering；
- advanced packaging；
- high-speed interconnect；
- liquid cooling；
- power delivery；
- grid interconnection；
- nuclear / energy permitting；
- AI infrastructure operations。

这类岗位的共同特点是：需要同时理解软件、硬件和物理基础设施，培养周期长，且错误成本高。

因此，“AI 人才”不能被简化为 prompt engineering 或单一模型微调。真正具有长期议价能力的岗位，更可能位于**工作流控制权、系统集成和物理基础设施**附近。

## 7. 三层 AI Skills Stack

劳动与教育体系可以进一步拆成三层能力结构。

### 第一层：Model Use

能够使用主流模型完成：

- prompting；
- content generation；
- coding assistance；
- research assistance；
- standard automation。

这一层学习门槛最低，供给增长最快，因此长期技能溢价也最容易下降。

### 第二层：Workflow / Agent Engineering

能够设计：

- multi-step workflow；
- agent orchestration；
- model routing；
- retrieval；
- tool calling；
- evaluation；
- human-in-the-loop；
- cost / latency / reliability trade-off。

这一层的价值来自把模型能力转化为可稳定交付的业务结果。

### 第三层：AI Infrastructure / Systems

能够理解并控制：

- GPU / accelerator architecture；
- HBM；
- compiler/runtime；
- interconnect；
- distributed training；
- rack-scale system；
- liquid cooling；
- power and data-center constraints。

这一层培养周期最长，也是当前供给最难快速扩大的部分。

AI 劳动市场真正的分化，很可能首先发生在这三层之间，而不是简单发生在“AI 岗位”和“非 AI 岗位”之间。

## 8. 中国供给栈与劳动生产率

中国 AI 劳动市场同样受供给层级约束。

在 smartphone 和部分 consumer computing 层，中国能够形成较完整的平行供给，因此相关研发、制造、测试和软件岗位拥有更完整的本地生产工具。

在 frontier AI system stack，先进逻辑、HBM、advanced packaging、high-speed interconnect 和成熟 compiler/runtime 仍然决定工程师能够使用什么工具、在什么规模上训练和部署模型。

这意味着生产率差距不只来自人才能力，也可能来自**工具和基础设施可获得性**。

如果国内平行系统栈持续完善，就会形成第二套工程能力和认证体系；如果关键基础设施长期受限，即使人才数量充足，最高生产率上限仍可能受到系统工具约束。

因此，劳动政策不能只讨论“培养多少 AI 人才”，还要讨论这些人才实际能够获得什么计算、存储、互联和软件环境。

## 9. 未来四类劳动市场情景

### S1：Productivity Expansion

AI 主要提高现有岗位生产率，同时创造足够多的新工作流和基础设施岗位。企业用 AI 降低单位成本，但总需求继续扩大，岗位净减少有限。

关键条件：

- AI 应用收入持续增长；
- 新工作流数量快速增加；
- 企业投资回报率改善；
- 新岗位增长能够吸收部分被重构岗位。

### S2：Task Compression

岗位名称大体保留，但初级岗位和中间任务显著减少。同样数量的产出由更少的人完成，组织结构趋于扁平化。

这是目前最符合现有机构研究和企业部署逻辑的基准情景。

### S3：High-Exposure Displacement

Agent 在一批标准化知识工作流中形成高可靠替代，企业开始直接缩减岗位数量，特别是初级和中级认知岗位。

关键条件：

- Agent reliability 显著提高；
- 单位成本持续低于人工；
- 企业真正完成 workflow redesign；
- 合规与责任限制较低。

### S4：AI Investment Hard Landing

AI 投资回报不足，企业同时削减 AI 项目和相关岗位。劳动市场看到的不是“大规模 AI 替代”，而是“AI 项目收缩”。

这一情景与第三十七卷的资本硬着陆机制相对应。

## 10. 需要持续跟踪的可验证指标

判断劳动市场是否从任务重构进入岗位替代，至少需要观察：

- 企业是否披露具体被 Agent 替代的流程数量；
- AI-related headcount 与传统岗位 headcount 的变化；
- entry-level hiring 是否持续下降；
- 中层管理职位占比是否下降；
- inference cost 是否进入软件公司的 COGS 披露；
- AI-driven productivity 是否形成可重复财务收益；
- workflow/agent/infrastructure 类招聘是否持续增加；
- 现场责任岗位是否出现真正无人化；
- 职业资格和监管规则是否允许进一步自动化。

这些指标比“某模型 benchmark 又提高多少”更接近真实劳动结果。

## 11. 当前判断

截至 2026 年，公开证据不足以支持“AI 已经造成大规模总量失业”的结论，但同样不能据此判断劳动市场影响很小。

更符合当前证据的判断是：

1. AI 已经开始重构认知岗位内部的任务组合；
2. 初级和中级可文本化任务面临更高替代压力；
3. 岗位数量变化滞后于任务变化；
4. 组织结构可能先于总就业发生变化；
5. AI infrastructure、workflow orchestration 和高责任现场岗位的价值正在提高；
6. 劳动结果最终取决于 AI 单位经济、企业流程重构、责任约束和新增需求，而不是模型能力单一变量。

因此，本卷不提供失业率、岗位消失量或工资变化的点预测。相关数字只有在形成可追踪、可比较的公开统计后，才应进入事实层。

---

本卷的劳动统计口径主要参考 ILO、IMF 与 OECD 的公开研究；公司财务与 AI 基础设施数据统一回溯至对应专题卷及公开法定申报。所有“暴露率”均不得直接转换为“失业率”。