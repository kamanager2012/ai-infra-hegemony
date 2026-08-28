# Reproducible D-Grade Models

The file data/model-inputs.json stores the report-side assumptions used by the main D-grade geometry and sensitivity examples.

Run:

    python scripts/recompute_models.py

The script currently recomputes:

- CoWoS geometry: 72 packages / 13.4 packages per wafer = approximately 5.37 wafers per rack;
- NVL72 HBM and LPDDR scenario demand for 1,000 / 10,000 / 30,000 / 50,000 racks;
- 500 racks x 120 kW = 60 MW rack-level full-load power;
- Chapter 24 efficiency / demand-elasticity sensitivity.

Important boundary: model inputs labeled D-grade are assumptions or geometry. They are not shipment, yield, customer-allocation, or utilization actuals.
