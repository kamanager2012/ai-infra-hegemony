# Volume 23: HBM4, Logic Base Dies, and Memory Capital Density

Chinese source edition: [vol-23.md](../vol-23.md)

> Retrieval and revision cutoff: **2026-08-27**. HBM's strategic scarcity is analyzed through manufacturing input, integration complexity, and qualification—not through a commodity analogy or an unsupported future stack-height formula.

## 1. What gives HBM “new oil” characteristics

Calling HBM the “new oil of AI” is only a metaphor.

The analyzable mechanisms are:

- high bandwidth density;
- stacking complexity;
- wafer-supply tradeoffs;
- advanced-packaging dependence;
- generation-specific qualification.

HBM is strategically valuable because the required manufacturing capability cannot be copied quickly.

That does not mean HBM has the same market structure as oil.

## 2. The physical meaning of Micron's ~3× disclosure

Micron disclosed in FY24 Q3 that HBM3E requires approximately **3× the wafer supply of DDR5** to produce the same number of bits at the same technology node.

Micron's FY25 10-K further confirmed that HBM requires more wafers and cleanroom space for the same bit output.

The correct interpretation is:

> **The same bit demand consumes materially more manufacturing input when delivered as HBM.**

It is not:

> “One HBM wafer permanently equals three DDR5 wafers.”

The ~3× figure is an industry trade ratio under a defined comparison, not a fixed fab-accounting rule.

## 3. Why HBM bit share can understate manufacturing pressure

If HBM has bit share (x), but consumes more manufacturing input per delivered bit than conventional DRAM, then:

```text
Manufacturing Share > Bit Share
```

That means HBM can have an outsized effect on:

- wafer input;
- cleanroom allocation;
- CapEx;
- advanced packaging.

This is why rising HBM demand can reduce conventional-DRAM residual capacity even before HBM becomes a majority of total DRAM bits.

## 4. HBM4 may increase capital density further

Micron has indicated that the HBM4 trade ratio is expected to be higher than HBM3E.

If realized, later generations can require more:

- logic-base complexity;
- stacking;
- packaging;
- wafer input;
- testing.

The exact HBM4 and HBM4E trade ratios, however, must be taken from future vendor disclosures.

The HBM3E ~3× ratio should not be mechanically rewritten as “HBM4 is 4× or 5×.”

## 5. 16-Hi is not a universal production fact without product-level confirmation

HBM can evolve toward taller stacks, but specific values for:

- 12-Hi;
- 16-Hi;
- capacity;
- bandwidth;
- yield;
- production timing;

must be confirmed from vendor product specifications.

A supply-chain forecast or article mentioning 16-Hi is not enough to treat 16-Hi as the universal production configuration for all HBM4.

Generation, product, and qualification status have to remain explicit.

## 6. Logic base dies can tie memory more closely to advanced foundry capacity

HBM is moving from a “pure DRAM stack” toward more complex logic-base integration.

That creates a new dependency chain:

**HBM vendor  
→ logic base die  
→ advanced foundry  
→ advanced packaging**

If the logic base uses a leading-edge process, memory and compute can compete more directly for the same foundry resources.

HBM can therefore evolve from a memory bottleneck into a cross-layer bottleneck spanning memory, logic, and packaging.

## 7. Structural advantages of the three major suppliers

SK hynix, Samsung, and Micron combine:

- DRAM technology;
- TSV and stacking;
- manufacturing scale;
- HBM qualification;
- customer relationships.

That capability cannot be reproduced by adding ordinary DRAM capacity alone.

The HBM entry barrier includes:

- yield learning;
- packaging know-how;
- customer qualification;
- generation timing.

Capital matters, but capital without process learning and qualification is insufficient.

## 8. HBM inventory behaves differently from a commodity inventory

HBM differs from a standardized commodity because:

- product generations move quickly;
- configurations are tied to accelerator generations;
- qualification cycles are long;
- obsolescence risk is high.

The industry can therefore experience:

> **scarcity in one generation and mismatch or excess in another generation at the same time.**

An oversupply of an older HBM product does not automatically resolve a shortage of the next frontier generation.

## 9. Current judgment

HBM's strategic value rests on three simultaneous characteristics:

1. high bandwidth;
2. high manufacturing-input intensity;
3. high integration and qualification complexity.

If HBM4 and later generations continue to raise capital density, memory can remain a core scarce layer of the AI system.

If new memory architectures or algorithmic efficiency materially reduce bandwidth and capacity requirements, the constraint can weaken.

The long-run thesis is therefore not “HBM will always be scarce.”

It is:

> **As long as frontier-system bandwidth demand grows faster than memory-supply elasticity, HBM will retain high strategic value.**
