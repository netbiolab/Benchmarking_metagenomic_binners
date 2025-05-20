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
| c60_10Gb     | 60 genomes, 10.0 Gbp (split) | [10.5281/zenodo.15469705](https://doi.org/10.5281/zenodo.15469705) |
| c150_2.4Gb   | 150 genomes, 2.4 Gbp      | [10.5281/zenodo.15311056](https://doi.org/10.5281/zenodo.15311056) |
| c150_5Gb     | 150 genomes, 5.0 Gbp (split) | [10.5281/zenodo.15469731](https://doi.org/10.5281/zenodo.15469731) |
| c150_7.2Gb     | 150 genomes, 7.2 Gbp (split) | [10.5281/zenodo.15469652](https://doi.org/10.5281/zenodo.15469652) |
| c150_10Gb     | 150 genomes, 10.0 Gbp (split) | [10.5281/zenodo.15469674](https://doi.org/10.5281/zenodo.15469674) |
| c600_2.4Gb   | 600 genomes, 2.4 Gbp      | [10.5281/zenodo.15411007](https://doi.org/10.5281/zenodo.15411007) |
| c600_5Gb     | 600 genomes, 5.0 Gbp (split) | [10.5281/zenodo.15469827](https://doi.org/10.5281/zenodo.15469827) |
| c600_7.2Gb     | 600 genomes, 7.2 Gbp (split) | [10.5281/zenodo.15469815](https://doi.org/10.5281/zenodo.15469815) |
| c600_10Gb     | 600 genomes, 10.0 Gbp (split) | [10.5281/zenodo.15469858](https://doi.org/10.5281/zenodo.15469858) |
| c1000_2.4Gb   | 1000 genomes, 2.4 Gbp      | [10.5281/zenodo.15392757](https://doi.org/10.5281/zenodo.15392757) |
| c1000_5Gb     | 1000 genomes, 5.0 Gbp (split) | [10.5281/zenodo.15470120](https://doi.org/10.5281/zenodo.15470120) |
| c1000_7.2Gb     | 1000 genomes, 7.2 Gbp (split) | [10.5281/zenodo.15470133](https://doi.org/10.5281/zenodo.15470133) |
| c1000_10Gb     | 1000 genomes, 10.0 Gbp (split) | [10.5281/zenodo.15470157](https://doi.org/10.5281/zenodo.15470157) |
| c1500_2.4Gb   | 1500 genomes, 2.4 Gbp      | [10.5281/zenodo.15392852](https://doi.org/10.5281/zenodo.15392852) |
| c1500_5Gb     | 1500 genomes, 5.0 Gbp (split) | [10.5281/zenodo.15470190](https://doi.org/10.5281/zenodo.15470190) |
| c1500_7.2Gb     | 1500 genomes, 7.2 Gbp (split) | [10.5281/zenodo.15470207](https://doi.org/10.5281/zenodo.15470207) |
| c1500_10Gb     | 1500 genomes, 10.0 Gbp (split) | [10.5281/zenodo.15470211](https://doi.org/10.5281/zenodo.15470211) |


---

## How to Reconstruct Split Datasets

For split datasets (≥5 GB), download all parts from the DOI page and reconstruct using:

```bash
cat <dataset>_part_* > <dataset>.tar.gz
tar -xzf <dataset>.tar.gz
