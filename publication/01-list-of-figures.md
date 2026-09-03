# 图表目录

> 核心 Figure 按出版顺序编号。所有 quantitative figure 与英文 canonical edition 共用同一 evidence identity、denominator boundary 与 time identity；数值层以英文版 `en/publication/figure-data/` 中的机器可读输入为准。

1. [图 1 — 竞争单位已经从 Chip 上移到 System Stack](figures/fig-01-system-stack.svg)  
   **类型：** report framework。**主要分析位置：** 第 2、12、32 章。

2. [图 2 — Non-AI Residual Capacity（NARC）](figures/fig-02-narc-mechanism.svg)  
   **类型：** report-side analytical definition。**主要分析位置：** 第 3、8、21、32 章。

3. [图 3 — HBM3E 相对 DDR5 的 wafer-supply intensity](figures/fig-03-hbm-wafer-intensity.svg)  
   **类型：** first-party physical trade ratio。**Source：** Micron FY24 Q2 Prepared Remarks。  
   **Boundary：** same technology node / same number of bits；≈3× wafer supply 不是价格倍数，也不是所有 HBM generation 的永久常数。

4. [图 4 — NVIDIA 2026 年 forward supply / capacity commitment family](figures/fig-04-nvidia-forward-commitments.svg)  
   **类型：** first-party filing data。**数值：** US$95.2B（2026-01-25）、US$119B（2026-04-26）、US$279B（2026-07-26）。  
   **Boundary：** 各报告时点的 disclosure label、mix 与 duration 并不完全相同；没有 supplier-level split；commitment 不等于 realized supplier revenue 或 delivered capacity。

5. [图 5 — Power / LPS delivery-state model](figures/fig-05-power-state-machine.svg)  
   **类型：** report framework。**主要分析位置：** 第 7、8、29、32 章。  
   **Boundary：** secured / contracted ≠ energized ≠ utilized；IT-GW ≠ generation GW ≠ PPA capacity。

6. [图 6 — S1–S4 scenario map](figures/fig-06-s1-s4-scenario-map.svg)  
   **类型：** report scenario framework。**主要分析位置：** 第 30 章。  
   **Boundary：** 四个 scenario 是 parallel conditional states，不带固定 probability；S2 只表示截至 2026 年 8 月的 current evidence baseline。

7. [图 7 — TSMC 2026 Q2 demand 与 technology mix](figures/fig-07-tsmc-2q26-mix.svg)  
   **类型：** first-party actual data，保留两个独立 denominator。**主要分析位置：** 第 4 章。  
   **Boundary：** HPC 66% 与 smartphone 22% 是 total revenue 的 platform share；7 nm 及以下 77% 是 wafer revenue 的 technology share；均不是 customer-level wafer allocation。

8. [图 8 — Rolling Bottleneck Cascade](figures/fig-08-rolling-bottleneck-cascade.svg)  
   **类型：** report framework。**主要分析位置：** 第 6–8、19、24、30 章。  
   **Boundary：** causal schematic，不是确定性 sequence 或 timing forecast。

9. [图 9 — Anchor demand 与 Financing Reflexivity](figures/fig-09-financing-reflexivity.svg)  
   **类型：** report financing framework。**主要分析位置：** 第 13、23、24 章。  
   **Boundary：** seller-assisted financing 既不能自动判定为健康，也不能自动判定为 artificial；必须结合 utilization、monetization、independent risk capital 与 refinancing conditions。

10. [图 10 — Verified workflow output 构成 demand-side closure](figures/fig-10-verified-workflow-loop.svg)  
    **类型：** report economic framework。**主要分析位置：** 第 14、19、24、32 章。  
    **Boundary：** verified workflow output 是 long-run economic criterion，不是截至 evidence cutoff 已完成 empirical calibration 的 fact metric。

11. [图 11 — Production-Grade Parallel Stack 与 Autonomous Frontier Closure](figures/fig-11-china-closure-gates.svg)  
    **类型：** report closure-test framework。**主要分析位置：** 第 17、32 章。  
    **Boundary：** production-grade substitution ≠ full technological autonomy；存在 import dependence 也不等于不存在 production-grade parallel stack。

## 出版说明

这些 Figure 属于 publication layer，不重新打开已经冻结的 32 章研究逻辑。未来任何需要新增 denominator、新 estimate 或新 factual claim 的 quantitative figure，都必须作为新的研究输入处理，而不是以“编辑性插图”的名义直接加入。
