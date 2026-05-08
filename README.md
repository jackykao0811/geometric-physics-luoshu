# A Geometric Language for Modern Physics — Volume 0

**An Open Preprint and Reproducible Conceptual Lecture Note**

> *Lo-Shu Encoding for Quantum Phase Space and Black Hole Geometry*

**Author:** Kao, Yao-Kai · National Yang Ming Chiao Tung University (NYCU), Taiwan  
**Version:** 0.5 · May 2026  
**DOI (Zenodo):** [10.5281/zenodo.20090525](https://zenodo.org) *(updated after upload)*  
**License:** MIT (code) / CC BY 4.0 (text and figures)

---

## Overview

This repository contains all code and figures for **Volume 0** of the *Geometric Language for Modern Physics* series. The framework proposes a Lo-Shu magic-square encoding pipeline that converts physical distributions (quantum Wigner functions, Kerr black hole curvature) into a single dimensionless geometric index (Q-LTE).

### The Lo-Shu Encoding Pipeline

```
Physical Object → Phase-Space Distribution → Lo-Shu 3×3 Grid → Cell Mass M_ij → Q-LTE Index → Geometric Interpretation
```

### Four Falsifiable Claims

| Claim | Statement | Status |
|-------|-----------|--------|
| **Law I** | Fock negativity ring: r_peak = 0.539 n^0.807 (finite-n, n=1..50) | Well-supported |
| **Law II** | Bosons > 1× denser at Lo-Shu L=5 vs fermions (selected pairs) | Preliminary |
| **Law III** | Cat-state direction locks to L=9; crossover at γt ≈ 2 | Numerical obs. |
| **GR** | Schwarzschild Q-LTE M-independent; Kerr +16% at a/M=0.99 | Well-supported |

---

## Installation

```bash
git clone https://github.com/jackykao0811/geometric-physics-luoshu
cd geometric-physics-luoshu
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/run_checklist.py
```

---

## Repository Structure

```
geometric-physics-luoshu/
├── README.md
├── requirements.txt
├── scripts/
│   ├── run_checklist.py      # Run all reproducibility checks
│   ├── law1_scaling.py       # Law I: r_peak power-law scaling
│   ├── law2_bf_ratio.py      # Law II: Boson/Fermion L=5 density
│   ├── law3_decoherence.py   # Law III: Cat-state direction locking
│   ├── gr_kerr.py            # GR: Kerr Q-LTE vs a/M
│   └── e8_connection.py      # E8 angle comparison
├── figures/
│   ├── fig0_flowchart.png
│   ├── fig1_loshu.png
│   ├── fig2_wigner_fock.png
│   ├── fig3_projection_scaling.png
│   ├── fig4_boson_fermion.png
│   ├── fig5_decoherence.png
│   ├── fig6_kerr_qlte.png
│   ├── fig7_ablation.png
│   ├── fig8_ablation_symmetry.png
│   └── fig9_bf_corrected.png
└── paper/
    └── geometric_physics_vol0_v5.pdf
```

---

## Key Results

### Law I — Finite-n Effective Scaling (n=1..50)

```python
r_peak_1 = np.sqrt((7 - np.sqrt(41)) / 4)  # exact: 0.38629
theta_1  = np.degrees(np.arccos(r_peak_1 / np.sqrt(2)))  # 74.148°
```

| n | r_peak | θ(n) |
|---|--------|------|
| 1 | 0.3863 (exact) | 74.15° |
| 10 | 3.617 | 36.0° |
| 50 | 9.300 | 21.5° |
| ∞ | → √(2n) | → 0° |

### Law II — Fermi Depletion at L=5

| State pair | B/F ratio |
|------------|-----------|
| \|01⟩ | 1.000× (no effect) |
| \|13⟩ | 1.448× (significant) |
| \|24⟩ | 4.548× (strong) |

### GR — Kerr Q-LTE

| a/M | Q-LTE | Δ vs Schwarzschild |
|-----|-------|-------------------|
| 0.00 | 4.661 | baseline |
| 0.90 | 5.154 | +10.6% |
| 0.99 | 5.418 | +16.2% |

---

## What This Framework Does NOT Claim

- Lo-Shu is NOT a law of nature (it is a coordinate choice)
- Q-LTE is NOT a physical energy (it is a dimensionless index)
- The exponent 0.807 is NOT universal (finite-n only, n=1..50)
- The E8 connection is NOT proven (0.42° gap, projection-sensitive)
- This framework does NOT replace standard QM or GR

---

## Related Publications

| Paper | DOI |
|-------|-----|
| Wigner-Luoshu Phase Space Framework | [10.5281/zenodo.20089785](https://doi.org/10.5281/zenodo.20089785) |
| Luoshu Druggability v4 (ROC=0.861) | [10.5281/zenodo.20085516](https://doi.org/10.5281/zenodo.20085516) |
| GRH Unified Paper | [10.5281/zenodo.20088978](https://doi.org/10.5281/zenodo.20088978) |
| LSP-Orbital v4.5 | [10.5281/zenodo.20085647](https://doi.org/10.5281/zenodo.20085647) |
| LSP-Triality (Knapsack) | [10.5281/zenodo.19999333](https://doi.org/10.5281/zenodo.19999333) |

---

## Citation

```bibtex
@misc{kao2026geometric,
  author    = {Kao, Yao-Kai},
  title     = {A Geometric Language for Modern Physics, Volume 0:
                Lo-Shu Encoding for Quantum Phase Space and Black Hole Geometry},
  year      = {2026},
  month     = {May},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20090525},
  url       = {https://github.com/jackykao0811/geometric-physics-luoshu}
}
```

---

## License

- **Code** (scripts/): [MIT License](LICENSE)
- **Text and Figures**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
