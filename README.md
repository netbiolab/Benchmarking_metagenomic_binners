# Benchmarking metagenomic binners

This repository accompanies the manuscript:

> **Comprehensive benchmarking of metagenomic binning tools reveals key factors for improved genome recovery**
> 

It provides simulation and real datasets, binning outputs, benchmarking metrics, and all scripts used to perform and reproduce the study.

---

## Repository Structure

```text
.
├── datasets/
│   ├── simulation/          # In-house simulated datasets (20 total)
│   └── real/                # Real metagenomic samples (gut, soil, ocean)
├── results/
│   ├── binning_scores/      # Evaluation metrics (TSV)
│   └── result_plots/        # Selected binning results (e.g., completeness, purity, # of NC MAGs)
├── scripts/
│   ├── workflow/            # Main benchmarking pipelines (Linux/Python)
│   └── utilities/           # Scoring and visualization scripts
└── docs/
    └── usage_example.md     # Quick start usage guide
```

---

## Dataset Description

### 1. Simulation Datasets

**Location:** `datasets/simulation/`

- 20 synthetic datasets generated using [CAMISIM](https://github.com/CAMI-challenge/CAMISIM)
- Variable parameters:
  - **Sequencing depth**: 2.4, 5.0, 7.2, 10.0 Gbp
  - **Taxonomic complexity**: 60, 150, 600, 1000, 1500 genomes
- Includes:
  - Paired-end FASTQ files
  - Gold standard assemblies
  - Read-to-reference alignment BAMs

### 2. Real Metagenomic Datasets

**Location:** `datasets/real/`

- Human gut, soil, and ocean samples
- Curated from public repositories (details in `README_dataset.md`)
- All samples have ≥2 Gbp sequencing depth and passed quality control

---

## Benchmarking Outputs

**Location:** `results/`

- **Binning scores** (`binning_scores/*.tsv`)\
  Metrics for each tool and dataset:

  - Number of Near Complete (NC) and Medium Quality (MQ) MAGs
  - ARI, completeness, contamination
  - GUNC filtering results

- **Supplementary figure data** for plotting (Extended Figs)

---

## Benchmarking Pipelines

**Location:** `scripts/`

- Modular Python pipelines for reproducibility
- Supports:
  - Tool wrappers for all 9 binners
  - Evaluation tools (CheckM2, GUNC, AMBER)
- Environment files:
  - `environment.yml` (Conda)
  - `requirements.txt` (pip)

---

## Quick Start

Please refer to [`docs/usage_example.md`](docs/usage_example.md) for:

- How to run a benchmark on a selected dataset
- Required inputs and expected outputs
- Reproducing results shown in the manuscript

---

## Citation

