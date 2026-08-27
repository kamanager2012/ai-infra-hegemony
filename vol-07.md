# 第七卷：NVIDIA 纵向扩张与 AI Factory 控制力

## 1. 扩张方向：从 accelerator vendor 到 system platform

NVIDIA 的扩张并不主要表现为收购更多硬件公司，而是不断扩大自己定义系统的范围。

当前系统边界已经覆盖：

- GPU / CPU；
- NVLink / NVSwitch；
- networking；
- rack reference design；
- liquid cooling requirements；
- CUDA/runtime；
- inference software；
- AI Enterprise；
- DGX / cloud services；
- model-related products。

这是一种**接口与系统定义权驱动的纵向扩张**。

## 2. 销售单元上移带来的控制力

在 accelerator card 时代，OEM 可以围绕 GPU 设计自己的服务器。

rack-scale 时代，系统要求已经扩展到：

- power delivery；
- cooling；
- fabric；
- cable topology；
- rack layout；
- firmware；
- software stack。

因此，OEM 的角色更容易从“定义产品”向“集成认证系统”移动。

这不意味着 Dell、Lenovo、HPE 等已经失去产品能力，而是说明 NVIDIA reference architecture 对整机设计的约束在增强。

## 3. Networking 已经成为平台的一部分

FY26 NVIDIA Data Center revenue 中，compute 与 networking 都已经成为重要组成。

高速互联的战略价值在于：

- 提高 multi-GPU scaling；
- 降低 communication bottleneck；
- 增强 rack/pod 的统一性；
- 把 accelerator purchase 与 network architecture 绑定。

因此，平台竞争不再是“GPU + 第三方网络”的简单组合，而越来越像一套完整 AI factory architecture。

## 4. DGX Cloud 的战略意义

DGX Cloud 的意义不能只看是否已经形成独立巨大收入。

它至少具有四个战略功能：

1. 向最终用户直接展示 NVIDIA system architecture；
2. 获得真实 workload 与 deployment feedback；
3. 降低客户首次使用整套 NVIDIA stack 的门槛；
4. 给 hyperscaler 增加一个潜在竞争/议价选项。

因此，DGX Cloud 更像平台延伸和渠道控制工具，而不是目前已经取代 hyperscaler 的独立 cloud business。

在没有独立收入分项之前，不应把其写成已经形成第二个主要利润池。

## 5. AI Enterprise、NIM、NeMo 与模型产品

NVIDIA 已经把软件产品扩展到：

- NVIDIA AI Enterprise；
- NIM；
- NeMo；
- Nemotron；
- deployment blueprints。

这些产品进一步强化 platform stickiness。

但软件产品当前的财务作用更适合表述为：

> 增强 hardware/system 的部署效率、迁移成本与客户留存。

而不是把未披露的软件收入机械估算成系统总利润的一定比例。

## 6. Automotive 与 Physical AI

Automotive、robotics、industrial AI 是平台外延的重要方向。

其战略逻辑与 Data Center 类似：

- hardware architecture；
- runtime；
- simulation；
- model deployment；
- developer tools

共同组成平台。

但这些领域必须与 Data Center 的当前利润规模区分。汽车、机器人在战略叙事中的重要性可以很高，却不等于它们已经贡献与 Data Center 相同的收入和利润。

因此，纵向扩张需要同时看：

- product presence；
- design wins；
- revenue；
- ecosystem adoption；
- migration cost。

## 7. 轻资产平台如何影响重资产供应链

NVIDIA 自己并不拥有 leading-edge logic fab、HBM fab 或大型 CoWoS manufacturing base。

它通过：

- long-term commitments；
- prepayments；
- roadmap coordination；
- reference designs；
- volume certainty

影响供应商扩产。

这形成一种典型的 **asset-light orchestration**：

平台公司保留高价值系统定义权  
→ manufacturing CapEx 留在 TSMC / memory vendor / infrastructure provider  
→ 平台用现金流和订单锁定未来资源。

这也是其资本效率高于传统 IDM 模式的重要原因。

## 8. 扩张的边界

NVIDIA 向系统平台扩张并不意味着所有相邻行业都会被其控制。

主要限制包括：

- hyperscaler 自研 system stack；
- open software layer；
- alternative networking；
- regulatory intervention；
- customer multi-sourcing；
- power constraint；
- China parallel stack。

如果这些力量同时增强，NVIDIA 的纵向扩张可能停在“领先系统平台”，而不是进一步形成更强的产业控制。

## 9. 当前判断

截至 2026 年，NVIDIA 已经从 accelerator company 明显向 AI system platform 扩张。

最确定的变化是：

- sales unit 上移；
- networking 与 compute 更深绑定；
- software/runtime 扩展；
- system reference architecture 增强；
- 模型与 cloud 产品成为平台延伸。

但“纵向扩张”与“产业已经被完全整合”仍是两个不同命题。

真正决定下一阶段的是：NVIDIA 能否继续把 system definition 转化为供给、客户和 workload 的长期锁定。
