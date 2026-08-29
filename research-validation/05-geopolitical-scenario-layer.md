# P1-1 · Geopolitical Scenario Layer v0.1

> **Status:** Research-side scenario extension; not part of the frozen 32-chapter formal report.  
> **Goal:** convert geopolitics from a background constraint into explicit, observable scenario variables that can change S1–S4 weights.

## 1. Why the existing framework is incomplete

The formal report already covers:
- U.S. export controls;
- China’s production-grade parallel stack;
- autonomous frontier closure;
- industrial policy;
- regional semiconductor redundancy.

But in the current S1–S4 system, geopolitics mostly enters as a static boundary condition.

For a 2026–2036 analysis, this is insufficient.

The relevant question is not:

> “Will geopolitics matter?”

It is:

> **Which geopolitical state is materializing, through which physical layer, and how does that change supply elasticity, substitution, financing, power, and capital allocation?**

---

## 2. Five explicit geopolitical state variables

### G1 — Taiwan Continuity

Tracks continuity of:
- advanced logic production;
- packaging / logistics;
- supplier staffing and maintenance;
- electricity / water / port access;
- cross-strait commercial flow.

States:

- **G1-A — Normal continuity:** ordinary political risk, no material production interruption;
- **G1-B — Elevated friction:** exercises, logistics delays, insurance/transport repricing, but production remains broadly continuous;
- **G1-C — Partial disruption:** temporary material interruptions to logistics, utilities, production or supplier access;
- **G1-D — Severe discontinuity:** sustained disruption of advanced-node and/or packaging output.

Hard rule:

> “Taiwan risk rises” is not itself a supply shock. The scenario must specify the physical transmission channel.

### G2 — Advanced-Computing Export-Control Regime

Tracks:
- chip performance / bandwidth thresholds;
- licensing policy;
- end-user restrictions;
- remote/cloud access rules;
- geographic allocation;
- enforcement and diversion controls.

States:

- **G2-A — Managed access / selective licensing**
- **G2-B — Stable strategic restriction**
- **G2-C — Material tightening**
- **G2-D — Broad technology denial / cross-border compute restriction**

The 2026 baseline is not a simple “total ban.” BIS revised policy in January 2026 to case-by-case review for some H200/MI325X-class exports subject to conditions, while the broader EAR still contains advanced-computing, end-use and geographic restrictions.

Therefore export controls must be modeled as a **policy state machine**, not a permanent binary variable.

### G3 — Allied Coordination / Fragmentation

Tracks alignment among:
- United States;
- Netherlands;
- Japan;
- Korea;
- Taiwan;
- other key equipment/material jurisdictions.

States:

- **G3-A — fragmented implementation**
- **G3-B — partial coordination**
- **G3-C — high coordination**
- **G3-D — coordinated expansion across chips + SME + HBM + services**

Why it matters:

A U.S.-only restriction and a multi-jurisdiction equipment/material restriction do not produce the same physical effect.

### G4 — China Autonomous Frontier Closure

This connects directly to the report’s existing H19.

Tracks whether China can sustain across generations:
- advanced-node logic;
- HBM-class memory;
- packaging;
- interconnect;
- EDA;
- equipment;
- materials;
- maintenance/service;
- system software.

States:

- **G4-A — external dependency remains binding**
- **G4-B — partial indigenous closure**
- **G4-C — production-grade multi-layer closure**
- **G4-D — autonomous frontier-scale closure**

CSIS’s 2026 analysis is important because it emphasizes a two-sided effect:

> controls can constrain access while simultaneously accelerating localization.

So export-control intensity and China substitution capability must not be treated as the same variable.

### G5 — Technology-Bloc Fragmentation

Tracks whether the global AI stack remains:
- commercially integrated;
- selectively segmented;
- dual-stack;
- deeply regionalized.

Observable dimensions:
- cloud-region restrictions;
- chip availability by geography;
- cross-border model/API access;
- standards/interfaces;
- sovereign-compute procurement;
- capital and supplier localization.

States:

- **G5-A — high integration**
- **G5-B — selective segmentation**
- **G5-C — durable dual-stack**
- **G5-D — deep bloc fragmentation**

---

## 3. Current 2026 factual anchors

### 3.1 Export controls remain dynamic, not monotonic

BIS in January 2026 moved certain H200 / MI325X and similar exports to China to **case-by-case licensing** under specified conditions.

At the same time:
- advanced-computing controls remain embedded in the EAR;
- advanced-node / supercomputer end-use restrictions remain;
- geographic allocation and due-diligence rules remain relevant;
- prior controls on semiconductor manufacturing equipment and HBM remain part of the broader regime.

Therefore the correct baseline is:

> **adaptive strategic restriction**, not “controls only tighten” and not “controls are gone.”

### 3.2 Localization is an endogenous response

CSIS in March 2026 argued that allied export controls have:
- disrupted some Chinese access to advanced chips/equipment;
- also accelerated indigenous-equipment adoption and localization efforts.

This creates a dynamic feedback:

```text
Restriction
→ near-term access loss
→ localization incentive
→ possible long-run substitution
→ future control effectiveness changes
```

A ten-year model must include both sides.

---

## 4. Geopolitical transmission map

### Taiwan continuity shock

```text
G1 deterioration
→ advanced logic / packaging / logistics availability
→ lead time / allocation / price
→ system delivery
→ cloud / model-company deployment
→ CapEx timing / revenue
```

### Export-control tightening

```text
G2 deterioration
→ accessible accelerator / SME / HBM set changes
→ regional substitution / stockpiling / compliance cost
→ China stack localization pressure
→ global supplier revenue mix / capacity allocation changes
```

### Allied coordination

```text
G3 strengthening
→ fewer substitution jurisdictions
→ higher near-term control effectiveness
→ stronger localization incentive
→ potentially faster long-run indigenous replacement
```

### Bloc fragmentation

```text
G5 deterioration
→ duplicated infrastructure / standards / capital
→ lower global sharing efficiency
→ higher redundancy CapEx
→ lower interoperability
→ potentially higher total physical investment despite lower global integration
```

---

## 5. Interaction with S1–S4

### S1 — Competitive Expansion

Geopolitical configurations that can raise S1 weight:
- G1 continuity remains high;
- G2 restrictions remain manageable rather than physically fragmenting global supply;
- G4 China closure improves enough to create real alternative system capacity;
- G5 remains integrated enough for multi-sourcing and interoperability.

### S2 — Baseline Concentration

Compatible with:
- persistent but manageable export controls;
- Taiwan continuity;
- partial allied coordination;
- China production-grade substitution without full frontier closure.

### S3 — Resource Hegemony

Geopolitics raises S3 weight when:
- G1 risk increases buyer willingness to reserve scarce capacity;
- G2/G3 reduce alternative access to frontier compute;
- G4 closure remains incomplete;
- G5 segmentation increases scarcity within blocs;
- strategic stockpiling and long-duration reservations intensify.

### S4 — Capital Hard Landing

Geopolitics can produce an S4-like capital outcome through a **different mechanism**:
- disruption destroys or strands demand/capacity;
- sanctions/export restrictions invalidate project assumptions;
- financing/insurance costs spike;
- cross-border customers disappear;
- planned assets become unusable in target markets.

But a geopolitical supply shock can also **raise prices and scarcity**, which is closer to S3 than S4.

Therefore:

> **geopolitical stress does not map mechanically to “bearish.” It can create either scarcity concentration or capital destruction depending on the transmission channel.**

---

## 6. Scenario matrix

| Geopolitical state | Physical supply | Substitution | Capital effect | Likely scenario pressure |
|---|---|---|---|---|
| G1-A + G2-A/B + G3-B + G4-B/C + G5-A/B | broadly continuous | improving | expansion viable | S1/S2 |
| G1-A + G2-B/C + G3-C + G4-A/B + G5-B/C | supply concentrated | limited | reservation/duplication rises | S2/S3 |
| G1-C/D | severe physical disruption | substitution constrained initially | project delay + scarcity | S3 first; S4 possible downstream |
| G2-D + G3-D + G4-A | China frontier access sharply constrained | weak | regional stranded demand / duplication | S3 fragmentation + local S4 risk |
| G2-C/D + G3-C/D + G4-C/D | strong controls but strong indigenous closure | dual-stack | duplicated CapEx | S1 within blocs / G5-C system |
| G5-D | low integration | bloc-specific | high redundancy, lower sharing efficiency | mixed S3/S4 by region |

---

## 7. Monitoring variables

Quarterly / event-driven panel:

### Taiwan continuity
- fab operation continuity;
- port / air / maritime logistics;
- utility interruptions;
- insurance / shipping repricing;
- supplier access.

### Export controls
- ECCN / threshold changes;
- licensing policy;
- approved/denied product classes;
- end-user / Entity List changes;
- cloud / remote-access restrictions;
- enforcement actions.

### Allied coordination
- Netherlands/Japan/Korea/Taiwan rule alignment;
- equipment/service restrictions;
- HBM / material controls.

### China closure
- domestic equipment qualification;
- production yields where credible;
- HBM-class production;
- packaging/interconnect;
- deployment in real workloads;
- service/maintenance continuity.

### Bloc fragmentation
- sovereign procurement;
- regional data residency;
- cross-border model/API limitations;
- incompatible standards;
- duplicated fabs / data centers / power projects.

---

## 8. Falsification rules

### “Export controls are structurally effective” weakens if:
- indigenous substitutes scale across multiple critical layers;
- production workloads migrate successfully;
- restricted technologies are replaced without persistent cost/reliability penalty.

### “Localization will neutralize controls” weakens if:
- key equipment/material/service dependencies remain generation-binding;
- yield / reliability / scale fail to close;
- production workload economics remain structurally inferior.

### “Taiwan concentration remains the dominant physical geopolitical risk” weakens if:
- meaningful advanced-node and packaging redundancy becomes operational outside Taiwan;
- customer qualification and volume ramp prove durable.

---

## 9. Relationship to the formal scenario system

This geopolitical layer should eventually feed Chapter 30 through **explicit state variables**, not through a narrative paragraph.

Do not assign subjective probabilities in v0.1.

The proper update process is:

```text
Observed geopolitical change
→ identify G-state transition
→ map physical / financial transmission
→ update H variables
→ update S1–S4 relative weight
```

---

## 10. v0.1 conclusion

The report’s geopolitical weakness is not lack of geopolitical discussion.

It is lack of **state-variable integration**.

After this extension, Taiwan continuity, export controls, allied coordination, China autonomous closure and technology-bloc fragmentation can be monitored and mapped into the same scenario engine as supply, demand, substitution and financing.

## Sources

- U.S. BIS, 2026-01-13, revised licensing policy for H200 / MI325X and similar semiconductor exports to China: https://media.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china
- U.S. BIS, EAR Part 748, advanced-computing licensing / certification / geographic-allocation provisions: https://www.bis.gov/regulations/ear/748
- U.S. BIS, 2024-12-02, controls on semiconductor manufacturing equipment, software tools and HBM: https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military
- U.S. BIS, EAR §744.23, supercomputer / advanced-node / semiconductor-manufacturing end-use controls: https://media.bis.gov/regulations/ear/744
- CSIS, 2026-03-24, “China’s Localization Drive in Semiconductors Gains Impetus from Allied Chip Export Controls”: https://www.csis.org/analysis/chinas-localization-drive-semiconductors-gains-impetus-allied-chip-export-controls
