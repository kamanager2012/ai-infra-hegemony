# Part I · 第5章：HBM 与存储资源重构


## 1. HBM 已从 GPU 配件变成系统级资源

在 frontier AI system 中，HBM 同时影响模型容量、batch、context、并发、communication pattern 与 accelerator utilization。GB200 NVL72 官方配置包含 **13.4 TB HBM3E/rack**。[^1] 这说明采购单位上移到 rack scale 后，memory intensity 必须从“每颗 GPU 多少 GB”上移到“每个 rack / cluster 的总 memory footprint”。

只有在真实 shipment / deployment count 已知时，才能进一步讨论 fleet-level PB demand。

因此 HBM 的产业影响不只发生在 accelerator BOM，还会传导到 DRAM wafer allocation、cleanroom space、advanced packaging、memory-vendor product mix 与 conventional DRAM residual supply。

## 2. Micron 的约 3× 是当前最重要的一手物理锚

Micron FY24 Q2 prepared remarks 给出了明确适用边界：在 **same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^2] Micron FY25 10-K 又确认，生产相同比特的 HBM 需要更多 wafers 与 cleanroom space。[^3]

因此这条证据可以支持：

- HBM3E 对制造投入的占用高于同 bit DDR5；
- HBM 扩张会更强地占用 DRAM wafer / cleanroom input；
- conventional DRAM 的有效 residual capacity 可能受到更大压力。

但它**不能**被改写成 HBM 售价是 DDR5 的 3×，也不能当作每座 fab、每一代 HBM 都固定不变的“3:1 定律”。Micron 对 HBM4 的公开表述只是 trade ratio 预计进一步上升；具体 HBM4/HBM4E 数值仍需未来 vendor disclosure。

## 3. 51% 是 2026E DRAM bit-supply 预测，不是 HBM 实绩

TrendForce **预计**，2026 年 **HBM + RDIMM 合计约占 DRAM bit supply 的 51%**。[^4]这是一条 B 级机构前向预测，必须同时保留三个边界：

1. 51% 包含 HBM **和 RDIMM**，不能写成“51% DRAM 都是 HBM”；
2. 它是 **bit supply**，不是 wafer share；
3. 它是 **2026E forecast**，不是已经完成的全年 actual。

这条预测与 Micron 的同-bit wafer trade ratio 结合后，给出一个更重要的机制：**bit share 不能完整反映制造投入压力。** 当一部分高价值 bit 需要更多 wafer/cleanroom input 时，它对制造资源的吸收可能高于其 bit 占比。

## 4. Non-AI Residual Capacity 在 memory 层如何形成

memory 资源重分配可以写成一条清晰链条：

**AI/server memory demand 上升 → HBM/RDIMM product mix 上升 → wafer / cleanroom / packaging input 向高价值产品倾斜 → conventional DDR/LPDDR residual capacity 收紧 → 非 AI 终端更容易承受价格与配置压力。**

这里的关键变量不是全球 DRAM 总产能，而是 AI/server demand 吸收之后，消费电子和其他传统 workload 实际能获得多少有效供给。

因此，本报告把 memory 层的核心指标定义为 **Non-AI Residual Capacity**，而不是简单用“DRAM 总产能增长”判断传统市场是否恢复宽松。

## 5. SK hynix 的 FY25 财务显示 HBM 已经改变产品经济性

SK hynix FY25 官方结果为：Revenue **KRW 97.1467T**、Operating profit **KRW 47.2063T**、Operating margin **49%**、Net income **KRW 42.9479T**，且公司披露 HBM revenue 同比超过一倍。[^5]

这些数据不能证明 HBM 单独贡献全部利润，但足以说明高价值 memory product mix 已显著改善 memory-vendor economics。与此同时，conventional server memory demand 仍然重要，这进一步说明 HBM 与 DDR5/RDIMM 并非完全隔离的资本和制造体系。

## 6. HBM 供给集中，但不制造未经披露的精确份额表

高端 HBM 供给主要集中在 SK hynix、Samsung 与 Micron。真正的进入壁垒不仅是 DRAM fab CapEx，还包括：

- TSV / stacking；
- yield learning；
- advanced-packaging integration；
- customer qualification；
- generation timing；
- high-volume manufacturing stability。

公开一手资料不足以支持一张完全同口径、可审计的三厂精确 HBM market-share 表，因此本报告不把媒体或卖方估算升级为公司官方份额。

### 6.1 价格反馈：HBM 的资源虹吸不是无限单向过程

资源重分配存在价格反馈。TrendForce 2026-06-02 的模型估算显示，随着 conventional DRAM 自 2025 年下半年起大幅涨价，**DDR5 64GB RDIMM 在 2026 Q1 的 per-wafer revenue 已超过 HBM**；该机构同时估算 HBM profitability 低于 DDR5 64GB RDIMM。[^6]

这是 B 级机构估算，不是 Samsung、SK hynix 或 Micron 披露的产品级实际毛利率。但它揭示了重要的自我修复机制：

> HBM/AI demand 上升 → conventional DRAM residual supply 收紧 → DDR5/RDIMM price 上升 → conventional DRAM per-wafer economics 改善 → 继续向 HBM 转产的相对激励下降 → memory vendor 重新平衡 product mix。

因此，AI Resource Gravity 不是无限的单向抽水机。长期 allocation 取决于不同产品的风险调整后单位稀缺资源回报、qualification、yield、generation transition 与客户合同结构。

## 7. Rack-scale 规格揭示 Memory Intensity，但不能替代 Shipment Data

GB200 NVL72 的 **13.4 TB HBM3E/rack** 是一个有价值的 system-level material identity。[^1]

它说明：当采购单位从单卡上移到 rack-scale system 后，memory demand 也必须按完整系统来理解。

但如果没有公开 rack shipment / deployment count，就不能进一步推出行业实际 HBM consumption。

因此：

> **per-system HBM spec 可以用于理解 memory intensity；行业总需求仍必须由真实 shipment、customer demand 或 memory-vendor supply data 约束。**

这比使用任意假设 rack 数去扩展成 PB 级“需求总量”更适合作为正式行业报告的量化边界。

## 8. HBM4 会提高跨层资本密度，但不能提前编出固定倍率

下一代 HBM 的复杂度不只来自更高 stack count，还可能来自 logic base die、advanced foundry、packaging、testing 与 qualification 的进一步耦合。

如果 logic base 使用更先进 process，memory bottleneck 会进一步向 foundry / packaging 层扩展，形成：

**HBM vendor → logic base die → advanced foundry → advanced packaging → accelerator qualification**。

这意味着 HBM 可能从“memory bottleneck”演化为跨 memory/foundry/packaging 的 system bottleneck。但在 vendor 正式披露之前，不能把 HBM3E 的 ~3× 机械改成 HBM4 4×、5×，也不能把某一种 12-Hi / 16-Hi configuration 当成所有 HBM4 的统一量产规格。

## 9. HBM 的库存属性与标准 commodity 不同

HBM 与标准 commodity memory 的一个重要差别是 generation-specific qualification。产品代际推进快、与具体 accelerator generation 强绑定、qualification 周期长、obsolete risk 高。

因此可以同时出现：

> **旧一代 HBM 出现供给宽松，而下一代 frontier HBM 仍然短缺。**

一代产品的过剩不会自动解决下一代产品的 qualification、yield 与 packaging 约束。

## 10. “推理转向 DDR”不会自动逃离 memory constraint

部分 inference workload 可以用更多 DDR/LPDDR 换取较低单位 memory cost，但 frontier inference 仍受 KV cache、long context、large batch、MoE routing、low-latency serving 与 multi-accelerator communication 影响。

更重要的是，RDIMM 本身已经被计入 TrendForce 的 AI/server memory 前向结构。于是从 HBM 向 DDR5 转移，更像是在同一个更宽 memory resource pool 中改变 cost/bandwidth tradeoff，而不是凭空创造一条完全独立的供给河流。

## 11. 什么会削弱 HBM 的长期战略价值

HBM 的长期稀缺不是必然。以下变化会显著削弱当前机制：

- memory architecture 大幅降低对高带宽堆叠的依赖；
- algorithmic efficiency 持续降低 memory bandwidth / capacity demand；
- HBM wafer/cleanroom trade ratio 显著改善；
- stacking、yield、logic-base 与 advanced packaging 的供给弹性大幅提高；
- conventional DRAM 与 HBM 的制造资源逐渐充分解耦。

因此，长期判断不是“HBM 永远短缺”，而是：

> **只要 frontier-system bandwidth demand 增长快于 HBM supply elasticity，且每 bit 制造投入仍显著高于 conventional DRAM，HBM 就会继续作为 AI infrastructure 的核心 scarce layer。**

## References

[^1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^2]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^3]: Micron Technology, FY25 Form 10-K, HBM wafer and cleanroom requirements, U.S. SEC, https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm
[^4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^5]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^6]: TrendForce, 2026-06-02, per-wafer revenue comparison for HBM and DDR5 64GB RDIMM, https://www.trendforce.com/presscenter/news/20260602-13074.html
