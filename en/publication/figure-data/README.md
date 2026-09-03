# Figure Data

Machine-readable inputs for quantitative publication figures.

## Figure 3 — HBM3E wafer-supply intensity versus DDR5

- File: `fig-03-hbm-wafer-intensity.csv`
- Evidence identity: first-party physical trade ratio.
- Source: Micron Technology FY24 Q2 Prepared Remarks, 2024-03-20.
- Boundary: same technology node / same number of bits. The ≈3× value is a wafer-supply trade ratio, not a price multiple and not a permanent constant for every HBM generation.

## Figure 4 — NVIDIA forward supply / capacity commitment family in 2026

- File: `fig-04-nvidia-forward-commitments.csv`
- Evidence identity: first-party filing data.
- Values admitted by the report: US$95.2B (2026-01-25), US$119B (2026-04-26), US$279B (2026-07-26).
- Boundary: this is a cross-reporting-date **forward supply / capacity commitment family**, not a homogeneous accounting line. The FY26 Form 10-K labels the January amount as manufacturing, supply, and capacity commitments; the FY27 Q2 Form 10-Q labels the July amount as supply and capacity commitments and reports the US$119B prior-quarter level retrospectively. Underlying mix and duration are not assumed identical. Public filings do not provide a supplier-level split. Commitments are not equivalent to realized supplier revenue, physical capacity delivered, or utilization.

## Reproducibility rule

A numeric SVG must be regenerated from the corresponding CSV whenever an admitted value changes. Do not hand-edit a chart value without updating its machine-readable input and the underlying chapter evidence at the same time.

## Figure 7 — TSMC 2Q26 demand and technology mix

- File: `fig-07-tsmc-2q26-mix.csv`
- Evidence identity: first-party actual data.
- Source: TSMC 2Q26 Quarterly Results / Earnings Conference.
- Boundary: the two panels intentionally preserve different denominators. HPC 66% and smartphone 22% are platform shares of total revenue; 7 nm and below 77% is a technology share of wafer revenue. These values must not be combined into customer-level wafer allocation.

The SVG should preserve the panel separation whenever the source values are updated.

