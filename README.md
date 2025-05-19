# Benchmarking metagenomic binners

This repository accompanies the manuscript:

> **Comprehensive benchmarking of metagenomic binning tools reveals key factors for improved genome recovery**
> 

It provides simulation and real datasets, binning outputs, benchmarking metrics, and all scripts used to perform and reproduce the study.

---

## Repository Structure

```text
.
├── benchmark_results/       # Provided TSV files with binning evaluation metrics
├── scripts/                 # Scripts for scoring, plotting, and dataset handling
├── run_commands.md          # Commands used for running each binning tool
├── datasets.md              # Zenodo download links and reconstruction instructions
└── README.md                # Project overview and navigation
```

---

## Quick Links

- [Download datasets from Zenodo](datasets.md)
- [View run commands for each tool](run_commands.md)

---

## Dataset Description

### 1. Simulation Datasets

20 synthetic metagenomic datasets generated using [CAMISIM](https://github.com/CAMI-challenge/CAMISIM)
- Variable parameters:
  - **Sequencing depth**: 2.4, 5.0, 7.2, 10.0 Gbp
  - **Taxonomic complexity**: 60, 150, 600, 1000, 1500 genomes
- Includes:
  - Paired-end FASTQ files
  - Gold standard assemblies (contigs)
  - GSA mapping tables

See [datasets.md](datasets.md) for download links and reconstruction instructions.


### 2. Real Metagenomic Datasets

Human gut, soil, and ocean metagenomic samples
| Dataset       | Accession |
|---------------|-----------|
| gut_2.9Gb     | [PRJNA797994](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA797994) |
| gut_4.5Gb     | [PRJEB27005](https://www.ebi.ac.uk/ena/browser/view/PRJEB27005) |
| gut_7.2Gb     | [PRJEB33013](https://www.ebi.ac.uk/ena/browser/view/PRJEB33013) |
| gut_8.5Gb     | [PRJEB39223](https://www.ebi.ac.uk/ena/browser/view/PRJEB39223) |
| gut_9.4Gb     | [PRJDB4525](https://www.ncbi.nlm.nih.gov/bioproject/PRJDB4525) |
| gut_11.6Gb    | [PRJNA624763](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA624763) |
| ocean         | [PRJNA273799](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA273799) |
| soil          | [PRJNA261849](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA261849) |

---

## Benchmarking Outputs

**Location:** `benchmark_results/`

We provide evaluation metrics (`.tsv` format) for all binning tools across both synthetic and real datasets.

- `synthetic_binning_result.tsv`: Results for synthetic datasets from Zenodo
- `real_binning_result.tsv`: Results for public metagenomic datasets (gut, soil, ocean)

Each file includes:
- Number of Near Complete (NC) MAGs (≥90% completeness, ≤5% contamination)
- Number of Medium Quality (MQ) MAGs (≥50% completeness, ≤10% contamination)


---

## Citation
