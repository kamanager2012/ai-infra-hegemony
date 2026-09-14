# Phase II · 需求侧反身性层 v0.2

> **状态：** 研究侧支撑材料。需求侧反身性机制现已写入正式正文——第24章 §7B、第29章 Dashboard I（需求腿）、第30章 §5/§10、第32章 §10——正式冻结于 2026-09-14 被明确重开一次（`04-research-transparency.md` §8A 第 8 项）。本文件不改变正式报告的 2026-08-28 证据截止日；**本文件与正式正文冲突时，以正式正文为准。**  
> **目的：** 把 financing reflexivity 的需求侧对应物显式化——AI 驱动的劳动收入压缩是否会削弱最终为 AI 基础设施付费的需求，以及哪些可观察变量会在该通道抵达现有五类 clearing 信号族之前先显示出来。  
> **外部校准参照：** Citrini Research / Alap Shah《2028 全球智能危机》（2026-02）——一篇自述为 scenario（“a scenario, not a prediction”）的文章——此处仅作为情景形态输入，并连同其公开反驳一并列出。本文件不复述、不复制、不采用该文的数字；以下全部为本报告自有的 2026–2036 条件化构造。  
> **英文 canonical：** [14-demand-side-reflexivity.md](14-demand-side-reflexivity.md)（本文件为派生中文译本）

## 0. 归属契约 v0.2（A2 重构）

**A2 重构后的归属：** 机制及其论断由正式正文拥有（第24章 §7B；第29章 Dashboard I；第30章 §5/§10；第32章 §10）。本文件只拥有该机制**背后的研究侧细节**——面板、时钟、闸门与证伪条件——并在任何冲突上以正式正文为准。

在这一支撑角色下，本文件拥有：

- **需求侧反身性回路**的研究侧细节（劳动收入 → 消费 → 企业现金生成 → AI 变现 → 资本清算）；
- task 级劳动证据（由 `07` 拥有）与总量需求传导之间的边界；
- 需求侧状态变量及其时钟；
- S4 证据中需求腿的整合规则。

本文件**不**拥有：task / workflow 级劳动证据（`07`）、workflow 成本与价值单位（`03`）、融资结构与 financing reflexivity（`11`、`04A`–`04D`）、情景聚合（`10`）、实时清算裁定（`01A`）。

**为什么必须新增 owner 而不是复用既有层。** 正式报告已允许 S4 由 “real-economy clearing” 在 accounting impairment 之前确认（Ch24 §9、Ch29 §10 / §12、Ch30 §5、Ch32 §9）。但没有任何既有层拥有总量需求侧可观察变量：`07` 的劳动链终止于 employment / wage outcome，不回流到需求；`03` 拥有 workflow 级的验证与成本；`04`/`11` 拥有融资的供给与结构，不拥有家庭收入与消费；`10` 聚合状态但不拥有事实。缺少本文件，S4 的需求腿有规则、没有变量。

## 1. 正式链条没有承载的那个回路

正式报告的需求侧闭环链（Ch32 §10）是：

> Physical Infrastructure → System Delivery → Workflow Economics → Verified Output → Adoption / Cash Flow → Utilization → Capital Reinvestment

在该链条中，“Adoption / Cash Flow”是输入：报告问企业是否会为可验证的 workflow 产出付费，并监测资本形成能否由利用率与现金生成验证。

需求侧回路使这一输入的一部分变为劳动市场的**输出**：

```text
        AI adoption / task substitution
                    │
                    ▼
              employment & labor income
                    │
                    ▼
               consumption ──────────────► enterprise revenue
                    │                              │
                    ▼                              ▼
            household credit          AI budgets / monetization
                    │                              │
                    └──────────► capital clearing ◄┘
```

该回路与 financing reflexivity（`11`）有两点结构性差异：

1. **它攻击需求腿，而非融资腿。** 供应商支持、担保与第三方资本可以在变现疲弱时延长时间；而家庭收入压缩会同时降低支付能力与扩张意愿。
2. **它的时钟长且层叠。** 报告现有的 clearing 信号族大多按季度可观察（guidance、清算价格、利差）；本回路第一腿（招聘）按月可观察，后几腿（工资、消费、信用、财政）按年累积。十年窗口可以承载完整序列，但序列在任何单一时点都不构成自身的证据。

## 2. 2026 基线：条件化通道，不是基准情形

报告既有的劳动证据已经固定了起点，本文件复用而不重新推导：

- **未观察到全经济范围 displacement。** `07` §2（evidence note A）记录的 Stanford / ADP payroll 证据显示：22–25 岁、处于高 AI exposure 职业的劳动者就业约比低 exposure 同龄人路径低 19%，且主要通过 **reduced hiring 而非 increased separations** 发生；作者明确将其表述为描述性结果，而非因果估计。
- **采用 ≠ 替代。** `07` §2（evidence note B）的 Census BTOS 证据：约 18% 企业在至少一个业务职能中使用 AI，约 66% 的采用者主要报告 task augmentation，仅约 2% 的企业报告就业减少。
- **高管报告的未来影响大于已实现影响。** `07` §2（evidence note C）的跨国调查：约 69% 企业已在积极使用 AI，而超过 80% 报告过去三年没有就业或生产率影响。
- **Exposure 不是结果。** ILO 与 IMF 的 exposure 口径（Ch25 §2）不能换算为失业率。

因此在 2026-08-28 截止日前，**下文 G1 门未打开**；存在的是集中于早期职业、高 exposure 职业的 hiring-pipeline 信号。本文件把完整回路视为 2026–2036 的条件化通道，而不是当前状态或预测。

## 3. 回路必须通过的门

每一道门都可以独立终止回路。没有一道门是固定数值阈值；每一道都是需要观察的状态。

**G1 — 替代深度。** AI 替代可验证工作的速度超过新 task 与新类别的创造速度。上游由 `03` 拥有；本文件消费而不重新推导该状态。

**G2 — 收入落点。** 哪些群体失去收入、他们承载多少总量消费。落在低消费倾向群体上的 displacement 与落在高消费倾向群体上的，是不同的需求事件。常被重复的“最高收入十分位驱动不成比例消费”在本文中只是**情景假设，不是事实**，除非给出其自身同分母来源。

**G3 — 信用缓冲。** 家庭债务偿付与 delinquency 状态定义了收入损失到需求损失之间的滞后。缓冲把流量冲击变成带延迟的存量问题；缓冲耗尽后则按季度传导。

**G4 — 价格与利润的传导方向。** AI 成本节省是以扩大销量的降价形式到达（`02` 的弹性问题：更便宜的 intelligence 可以扩大总需求），还是以保留利润 + 减少 headcount 的形式保留（压缩需求）。这道门决定回路自身的成本节省能否抵消其需求破坏。

**G5 — 替代需求与政策。** 新工作类别、公共部门吸收、转移支付与税制设计是回路闭合变量。在立法并观察到之前它们是情景变量；提案与政治冲突不是证据。

**G6 — 时钟层叠。** 招聘（月）→ 工资（1–3 年）→ 消费（收入下降后即刻，但收入下降缓慢）→ 信用（持续收入损失后 1–3 年）→ 财政（税基移动之后）。回路严重度取决于：前几腿是否在后续腿尚未响应时仍在移动。

## 4. 状态变量与时钟

需求腿的公开代理。全部为研究侧；不替代任何正式报告事实，且不得与 `04`/`11` 重复计算（见 §5）。

| 变量 | 公开代理 | 时钟 | 更新什么 | 不能证明什么 |
|---|---|---|---|---|
| 劳动收入水平 | BLS Employment Cost Index / average hourly earnings（FRED `ECIALLCIV`） | 月度–季度 | G2、G4 | 非分群体；构成变化可掩盖群体损失 |
| 招聘 / 离职 | JOLTS openings、quits、layoffs（FRED `JTSJOL`）；`07` 的年龄–职业 payroll 面板 | 月度 | G1、G6 | openings ≠ 实际 hiring；存量指标滞后 |
| 家庭债务偿付 | NY Fed Household Debt and Credit Report；FRED `TDSP` | 季度 | G3 | 总量口径；构成与再融资条款重要 |
| Delinquency 状态 | NY Fed HHDC delinquency transition rates | 季度 | G3、G6 | 早期流量噪声大；forbearance 可压低观察到的压力 |
| 消费 | BEA Personal Consumption Expenditures；Census retail sales | 月度–季度 | G2、G5 | 总量无法把原因归于 AI |
| 消费相关企业收入 | 卡组织与中介业务量；按 seat / 消费计费的软件披露 | 季度 | G4、G5 | 除一手披露外为 C 级；行业结构变化是混淆项 |
| AI 变现质量 | `04B` / `04D` 面板（仅链接，不归本文件） | 季度 | S4 融资腿 | 不得与融资证据重复计算 |
| 财政位置 | 收入 vs 转移支付、自动稳定器 | 季度–年度 | G5 | 提案是情景变量，不是观察 |

**防越界规则。** 不做 exposure→失业率算术。不用不同分母的账目计算“有产出无收入”的残差。不用单季度触发。不把机构或媒体估计提升为一手事实。

## 5. 与 S1–S4 的交互及防重复计算规则

- **需求侧压缩不自动等于 S4。** 若 G4 走向降价与销量扩张，更便宜的 intelligence 可以扩大总需求——这是与 S1 相容的结果。若压缩缓慢且集中，S2/S3 可以在回路于下方积累时延续。
- **需求侧证据能给 S4 贡献什么。** 它可以提供或强化 **real-economy 腿**——削弱企业现金生成与变现质量——但不能单独确认 S4；后者仍要求跨主体、跨层级的多个因果独立信号族（Ch24 §9、Ch30 §5）。
- **防重复计算规则。** 同一个底层事实只更新融资族（`04`/`11`）或需求族（本文件）中的一个，除非它确实是双面证据（例如既是消费信用恶化、又是融资质量观察）。`11` 的 anti-double-counting 纪律不变。
- **与 financing reflexivity 的交互。** `11` 的 reflexivity 条件是供应商支持上升、同时 utilization、monetization、独立风险偏好与清算走弱。需求侧回路会从另一个方向满足其中的 “monetization weakening” 条款；两者必须记为同一信号族的独立贡献，而不是两次确认。

## 6. 2026–2036 条件化里程碑

对齐 Ch28 的阶段结构；每一行是 `condition → milestone → contrary signal`，不是日历预测。

| 阶段 | 打开回路的条件 | 需要观察的里程碑 | 反向信号 |
|---|---|---|---|
| I · 2026–2027 | 早期职业 hiring-pipeline 分化扩散到 **separations**，或扩散到技术职业之外 | 裁员与离职数据显示 displacement，而非仅入门招聘减少 | separations 平稳；招聘面变宽；augmentation 占比保持主导 |
| II · 2028–2030 | 工资增长与群体收入在入门级之外压缩；消费随收入减速 | 消费相关企业收入走弱，而 AI 预算继续增长（OpEx substitution 形态） | AI 节省以降价 + 销量扩张到达；新类别吸收相关群体 |
| III · 2031–2033 | 家庭信用从存量问题变为流量恶化；财政收入相对转移支付走弱 | 家庭债务偿付与 delinquency 状态趋势性恶化，而非单次冲击 | 政策及时闭合回路；生产率驱动的需求扩张跑赢压缩 |
| IV · 2034–2036 | 压缩要么均衡化为新结构，要么持续 | 劳动份额与消费稳定在新水平，或继续下降 | 工资份额企稳；reallocation 占主导；可验证产出的需求继续增长 |

**明确不在范围内：** 任何带年份的失业率、任何股指点位、任何“2028 年发生危机”的断言。正式报告的时间线纪律（Ch28 §1）原样适用于本层。

## 7. 证伪条件

以下任一可观察项都会削弱或闭合该回路，且都可在上表面板中观察：

1. **separations 在 Phase II 全程平稳**，而 AI 采用持续加深——有采用、无 displacement。
2. **工资增长与消费保持稳定**，同时 `03` 型可验证 workflow 替代规模化——替代没有传导到收入。
3. **降价传导占主导**（G4）：AI 成本节省表现为降价与销量扩张，而非保留利润 + 减少 headcount。
4. **新 task 创造**以可观察规模吸收被替代群体（看招聘构成，而不只是总量就业）。
5. **政策及时闭合回路**（G5）：转移支付、税制设计或公共部门吸收抵消私人收入损失。
6. **企业 AI 预算增速持续快于消费相关收入下降**——变现基础在相关窗口内并不依赖消费者收入。

## 8. 边界规则

- Scenario ≠ prediction。页首的外部参照是一个带公开反驳的情景形态；本文件既不采用、也不争辩其数字。
- 本文件中的每个数字都必须可追溯到报告已使用的分级来源，或 §4 所列面板；本文不创造新的数字身份。
- 2026-08-28 之后的观察仅为研究侧，未经明确 reopen 不得进入冻结章节（Phase II freeze boundary，见 `README`）。
- 本文不做再分配、政治或道德论证；G5 作为情景变量记录，因为它改变需求算术，而不是因为它被主张。

## 9. 整合规则

1. 在本文记录需求侧状态与时钟；发生变化时更新对应行，而不是追加叙事。
2. **已于 2026-09-14 应用（研究侧）：** Dashboard I 的 demand-quality 族现已承载 §4 的行作为带时钟标签的子列表——见 `10` §6D：它修订了 Axis F 与 §6 更新表，并把本文件登记为 `10` §0 中的研究侧 owner。**A2 更新（2026-09-14）：** 正式冻结随后为该机制被明确重开一次，因此正式 Ch29 §10 Dashboard I 现已承载需求腿，机制由正式章节拥有（第24章 §7B；第29章；第30章 §5/§10；第32章 §10）；本文件为支撑材料。
3. 若需求侧证据与融资侧证据同时恶化，`01A` 裁定台账将其记为相互独立的族贡献——绝不乘合成一个指数。
4. **对 §2 各比率的算术在 [`20`](20-demand-side-composition.md)，不在本文件。** 在支撑角色下，本文件拥有该环、状态变量、时钟与闸门的研究侧细节（机制由正式章节拥有），并在拒绝成立之处拒绝对其赋数——§3 闸门 G2 在缺乏同分母来源时拒绝消费倾向主张，而该拒绝**不因 `20` 而放宽**。`20` 所做的是把 §2 的采用率放到同一分母上复合、把漏斗最后一步陈述为未测量的边界、并把入射问题写成一个其唯一自由比值保持为旋钮的恒等式。**归属不变：** 对 §2 某一比率、某个时钟或某个闸门的改动是本文件的改动，`20` 只应重跑而不应被直接编辑。

## Sources

（与英文 canonical 相同；链接见 [14-demand-side-reflexivity.md](14-demand-side-reflexivity.md) §Sources）

- Brynjolfsson, E.; Chandar, B.; Chen, R., *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*, Stanford Digital Economy Lab, revised 2026-08-12（ADP payroll data through June 2026；描述性、非因果）。
- U.S. Census Bureau, Business Trends and Outlook Survey (BTOS), experimental data product。
- Brynjolfsson, E.; Li, D.; Raymond, L., *Generative AI at Work*, NBER Working Paper 31161。
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*。
- ILO, Gmyrek et al., *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*, Working Paper 140, May 2025。
- IMF, *Gen-AI: Artificial Intelligence and the Future of Work*, Staff Discussion Note SDN/2024/001。
- Federal Reserve Bank of New York, *Household Debt and Credit Report*；FRED series TDSP（Household Debt Service Ratio）。
- FRED series ECIALLCIV（Employment Cost Index, total compensation, civilian）；JTSJOL（Job Openings: Total Nonfarm）。
- U.S. Bureau of Economic Analysis, Personal Consumption Expenditures。
- Citrini Research / A. Shah, *The 2028 Global Intelligence Crisis*, 2026-02（scenario, not prediction；仅作校准参照）。
- Citadel Securities 反驳（媒体报道）；*The 2028 Global Intelligence Renaissance*（反方情景）；J. Daly, *The Convergence Problem*。
