# 第三卷：AI Resource Gravity 与非 AI 剩余产能

## 1. “AI 虹吸”真正发生在哪一层

AI 基础设施扩张并不会把全球所有半导体产能同时抽走。真正发生变化的是部分稀缺层的资源分配顺序。

本报告将这种机制定义为 **AI Resource Gravity**：当 AI 系统能够支付更高价格、提供更长订单、接受预付款并持续扩大采购时，资本与产能会向 AI 相关的高价值环节移动。

被影响最明显的不是所有芯片，而是：

- advanced logic；
- HBM；
- RDIMM/server DRAM；
- advanced packaging；
- high-speed networking；
- power-management components；
- data-center power。

因此，更准确的分析对象是 **Non-AI Residual Capacity（非 AI 有效残余产能）**。

## 2. Rack-scale system 把需求变成可计算的物理量

GB200 NVL72 官方配置：

- 72 Blackwell GPU
- 36 Grace CPU
- 13.4 TB HBM3E
- 17 TB LPDDR5X

来源：https://www.nvidia.com/en-us/data-center/gb200-nvl72/

如果 rack 出货量为 (R)，则仅内存需求就满足：

```text
HBM = 13.4 	ext{TB} 	imes R
```

```text
LPDDR = 17 	ext{TB} 	imes R
```

因此：

| 情景 rack 数 | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

这些数字是**情景算术，不是实际出货量**。NVIDIA 没有公开全年 NVL72 rack shipment，因此不能反向用 Data Center revenue 推算 rack 数。

## 3. HBM 对 DRAM 供给的影响大于 bit share 本身

Micron FY24 Q3 prepared remarks 明确披露：

> HBM3E 在相同 technology node、生产相同比特时，约需要 DDR5 **3× 的 wafer supply**。

因此，HBM 对 DRAM 供给结构的影响不能只看 bit share。

TrendForce 预计 2026 年 HBM + RDIMM 约占 DRAM bits 的 **51%**。如果高价值 HBM 同时需要更高 wafer supply，那么 conventional DRAM 的剩余供给受到的压力可能大于“51% bit share”这一数字本身。

这构成存储领域的 **Observed Crowding-out**：

AI/server demand 上升  
→ HBM/RDIMM 占用更多资本与 wafer input  
→ conventional DRAM residual supply 下降  
→ consumer/PC/general-server memory 更容易出现价格上行或配置调整。

## 4. Advanced packaging 是另一条独立约束

Blackwell-class GPU 不是只依赖先进逻辑 wafer，还依赖 advanced packaging。

报告使用一个 D 级几何压力测试：

```text
72 	ext{GPU packages} ÷ 13.4 	ext{packages/wafer}
≈ 5.39 	ext{CoWoS wafers/rack}
```

其中：

- 72：官方 rack 配置；
- 13.4 packages/wafer：几何工作假设；
- 5.39：报告压力测试结果。

这个数字**不是 TSMC 官方 yield，也不是前道 logic wafer consumption**。

因此绝不能使用：

```text
15M 	ext{TSMC annual wafers} ÷ 5.39
```

来推导全球可生产多少 rack。TSMC 全年 wafer shipments 包含大量 smartphone、automotive、IoT 和 mature-node 产品，物理池完全不同。

## 5. 谁最先承受 residual-capacity pressure

### 5.1 PC / gaming

NVIDIA FY26 10-K 的可核表述是：FY26 Gaming revenue 同比增长 **41%**，同时公司预计 **supply constraints will be a headwind to Gaming in FY27 Q1 and beyond**。这支持消费 GPU 侧存在供应约束，但不能把约束原因直接写成“Data Center 抢走了 Gaming 配额”。消费 GPU 与 Data Center 产品确实共享部分先进逻辑、memory 与供应链资源，因此 PC/gaming 可作为 residual-capacity pressure 的观察市场。来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm 。

### 5.2 General server

General server 不一定需要 HBM，但会使用 DDR5 RDIMM。由于 RDIMM 本身已经进入 AI/server demand 的主要内存池，传统服务器并不存在完全独立的“安全 DRAM 河流”。

### 5.3 Smartphone

Smartphone 仍是 TSMC 第二大 platform。TSMC 2025 smartphone revenue share 为 **29%**，同比仍增长。

因此，AI 并没有“挤掉手机”。

更准确的变化是：HPC 增长速度明显更快，新增先进资本和先进封装资源更偏向 AI/HPC。

### 5.4 Automotive

Automotive 具有更长认证周期，也大量使用成熟节点，因此不会与 frontier AI system 完全重叠。

其风险主要来自部分共享器件：

- power management；
- advanced compute；
- memory；
- selected packaging capacity。

所以汽车更可能受到**选择性冲击**，而不是行业级全面停产。

## 6. 资源分配不是按行业平均进行

AI Resource Gravity 的核心不是“AI 需求最大”，而是**AI 订单具有更高资源竞争能力**。

资源分配会同时受到：

- price；
- long-duration order；
- prepayment；
- customer credit；
- utilization；
- roadmap certainty；
- supplier diversification；
- geopolitics

影响。

因此，消费电子不是因为“地位低”被挤压，而是其单位资源能够承受的价格、订单期限和预付款结构不同。

## 7. 中国供给不能与全球 frontier AI 直接相加

中国在 smartphone 与部分 consumer computing 上已经具备更完整的平行供给能力。

但 frontier AI system 需要同时获得：

- advanced logic；
- HBM-class memory；
- advanced packaging；
- high-speed interconnect；
- mature software stack。

因此，中国 consumer-electronics supply 增长不能直接抵消全球 frontier AI bottleneck。

反过来，中国如果在这些 advanced layers 上形成足够规模，则会产生第二个资源重力中心，而不是简单成为原有全球供应链的“剩余产能接收方”。

## 8. 当前判断

截至 2026 年 8 月，可以确认的是：

- AI/HPC 已成为先进半导体增量需求的核心驱动力；
- HBM/RDIMM 正在重塑 DRAM supply mix；
- advanced packaging 仍处于紧张状态；
- consumer market 并未消失，但部分品类开始承受 residual-capacity pressure；
- 这种挤压具有**层级性和选择性**，不是“所有芯片都被 AI 抢走”。

未来最重要的观察指标是 Non-AI Residual Capacity 是否继续下降，以及这种下降是否从 memory/packaging 扩散到更多传统终端市场。
