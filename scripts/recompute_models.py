#!/usr/bin/env python3
"""Recompute D-grade report models from versioned inputs."""
from __future__ import annotations
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "model-inputs.json"

def load():
    return json.loads(INPUT.read_text(encoding="utf-8"))["models"]

def main():
    m = load()
    nvl = m["nvl72"]
    cowos = m["cowos_geometry"]

    wafers_per_rack = cowos["packages_per_rack"] / cowos["packages_per_wafer_assumption"]
    print(f"CoWoS geometry wafers/rack: {wafers_per_rack:.2f}")
    assert math.isclose(wafers_per_rack, 5.373134328358209, rel_tol=1e-12)

    print("Rack memory scenarios:")
    for racks in m["scenario_racks"]:
        hbm_pb = nvl["hbm_tb_per_rack"] * racks / 1000.0
        lpddr_pb = nvl["lpddr_tb_per_rack"] * racks / 1000.0
        print(f"  {racks:>6,} racks -> HBM {hbm_pb:.1f} PB; LPDDR {lpddr_pb:.1f} PB")

    power_mw = nvl["rack_power_kw"] * m["power_scenario_racks"] / 1000.0
    print(f"Rack-level full-load power: {m[\"power_scenario_racks\"]} racks -> {power_mw:.1f} MW")
    assert math.isclose(power_mw, 60.0)

    s = m["elasticity_sensitivity"]
    uri = s["unit_resource_intensity_ratio"]
    price = s["effective_price_ratio"]
    print("Elasticity sensitivity:")
    expected = {0.5:0.8485281374, 1.0:1.2, 1.2:1.3784380259, 1.5:1.6970562748}
    for eps in s["elasticities"]:
        workload = price ** (-eps)
        demand = uri * workload
        delta = demand - 1.0
        print(f"  eps={eps:.1f}: workload={workload:.3f}x demand={demand:.3f}x delta={delta:+.1%}")
        assert math.isclose(demand, expected[eps], rel_tol=5e-4)

if __name__ == "__main__":
    main()
