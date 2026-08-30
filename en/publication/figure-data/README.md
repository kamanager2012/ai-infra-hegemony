# Figure Data

Machine-readable inputs for quantitative publication figures.

## Figure 3 — HBM3E wafer-supply intensity versus DDR5

- File: `fig-03-hbm-wafer-intensity.csv`
- Evidence identity: first-party physical trade ratio.
- Source: Micron Technology FY24 Q2 Prepared Remarks, 2024-03-20.
- Boundary: same technology node / same number of bits. The ≈3× value is a wafer-supply trade ratio, not a price multiple and not a permanent constant for every HBM generation.

## Figure 4 — NVIDIA forward commitments in 2026

- File: `fig-04-nvidia-forward-commitments.csv`
- Evidence identity: first-party filing data.
- Values admitted by the report: US$95.2B (2026-01-25), US$119B (2026-04-26), US$279B (2026-07-26).
- Boundary: aggregate manufacturing, supply, and capacity commitments. Public filings do not provide a supplier-level split. Commitments are not equivalent to realized supplier revenue, physical capacity delivered, or utilization.

## Reproducibility rule

A numeric SVG must be regenerated from the corresponding CSV whenever an admitted value changes. Do not hand-edit a chart value without updating its machine-readable input and the underlying chapter evidence at the same time.
