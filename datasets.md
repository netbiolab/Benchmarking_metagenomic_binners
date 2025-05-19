# Synthetic Metagenomic Datasets (Zenodo)

We provide 20 synthetic metagenomic datasets with varying taxonomic complexity and sequencing depth, generated using [CAMISIM](https://github.com/CAMI-challenge/CAMISIM).

Each dataset includes:
- Paired-end reads (`processed_read/`)
- Gold standard contigs (`contig/`)
- GSA mapping tables (`gsa_mapping/`)

## Datasets

| Dataset     | Description             | DOI |
|-------------|--------------------------|-----|
| c60_2.4Gb   | 60 genomes, 2.4 Gbp      | [10.5281/zenodo.15392968](https://doi.org/10.5281/zenodo.15392968) |
| c60_5Gb     | 60 genomes, 5.0 Gbp (split) | [10.5281/zenodo.15411528](https://doi.org/10.5281/zenodo.15411528) |
| c60_7.2Gb     | 60 genomes, 7.2 Gbp (split) | [10.5281/zenodo.15429451](https://doi.org/10.5281/zenodo.15429451) |
| c60_10Gb     | 60 genomes, 10.0 Gbp (split) | [10.5281/zenodo.154229467](https://doi.org/10.5281/zenodo.15429467) |
| ...         | ...                      | ... |

---

## How to Reconstruct Split Datasets

For split datasets (≥5 GB), download all parts from the DOI page and reconstruct using:

```bash
cat <dataset>_part_* > <dataset>.tar.gz
tar -xzf <dataset>.tar.gz
