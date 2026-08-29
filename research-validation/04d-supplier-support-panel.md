# P0-4D · Supplier / Sponsor Support Panel v0.1

> Extracted from P0-4 v0.17. Support is a risk-distribution layer, not an independent copy of end demand.

## 11C. Supplier / Sponsor Support overlay

The project-finance layer now needs an explicit support overlay.

Support is classified separately from borrower debt:

| Support channel | Examples | What to monitor |
|---|---|---|
| Strategic equity | NVIDIA → CoreWeave | recipient liquidity, dilution, whether support substitutes for weaker independent capital |
| Lease / payment guarantee | NVIDIA AI-cloud / LPS guarantees; AMD data-center lease guarantees | maximum exposure, activation conditions, step-down / termination terms |
| Vendor / OEM financing | CoreWeave OEM/software financing; IREN Dell GPU leases | tenor, guarantee, residual value, dependence on vendor credit |
| Third-party capital mobilization | seller-coordinated infrastructure financing platforms | actual third-party risk bearing vs announced capacity |
| Customer prepayment | Microsoft / IREN; take-or-pay colocation | prepayment share, customer concentration, performance obligations |

### 11C.1 Current rule

Seller / sponsor support is **not** negative evidence by itself.

It becomes S4-relevant only when:

```text
Support Dependence ↑
+
Independent Capital Access ↓
+
Customer / Workload Economics ↓
+
Refinancing Terms Worsen
```

Likewise, a guarantee cap is not a funded cash loss.

The overlay therefore records:

- maximum support amount;
- funded vs unfunded;
- conditional vs currently effective;
- guaranteed obligation identity;
- who bears first loss;
- whether support declines as project cash flow matures.

### 11C.2 No-double-counting rule

Do not sum:

```text
customer contract
+ debt raised against contract
+ seller equity
+ guarantee cap
+ customer prepayment
```

as independent demand.

They are separate financing / risk-distribution layers around the same underlying infrastructure expectation.

This overlay is maintained jointly with `11-financing-reflexivity-map.md`.

---


## Related evidence layer

See also [11 · Financing Reflexivity Map](11-financing-reflexivity-map.md), which maintains the 2026 support taxonomy and source-level evidence for strategic equity, guarantees, vendor/OEM finance, third-party capital mobilization, and customer prepayments.
