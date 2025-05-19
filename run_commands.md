# Commands Used to Run Each Tool

This document lists the exact commands used to run each binning tool in our benchmarking workflow.
Placeholders like `sample.fasta` and `sample.bam` should be replaced with actual input file names.

---

## binny

```bash
yq eval -i '.raws.assembly = sample.fasta' binny_config.yaml
yq eval -i '.raws.metagenomics_alignment = sample.bam' binny_config.yaml
yq eval -i '.sample = sample' binny_config.yaml
yq eval -i '.outputdir =result_dir' binny_config.yaml
./binny -l -t threads -n BINNY -r config.yaml
```

---

## COMEBin

```bash
run_comebin.sh -t threads -a sample.fasta -p sample.bam -o result_dir
```

---

## CONCOCT

```bash
cut_up_fasta.py sample.fasta -c 10000 -o -0 --merge_last -b contigs_10K.bed > contigs_10K.fa
concoct_coverage_table.py contigs_10K.bed sample.bam > coverage_table.tsv
concoct --composition_file contigs_10K.fa --coverage_file coverage_table.tsv -b concoct_output
merge_cutup_clustering.py concoct_output/clustering_gt1000.csv > concoct_output/clustering_merged.csv
extract_fasta_bins.py sample.fasta concoct_output/clustering_merged.csv --output_path result_dir
```

---

## MaxBin2

```bash
jgi_summarize_bam_contig_depths --outputDepth sample_depth.txt sample.bam
cut -f 1,3 sample_depth.txt | tail -n+2 > sample_abundance.txt
run_MaxBin.pl --thread threads -contig sample.fasta -abund sample_abundance.txt --out result_dir
```

---

## MetaBAT2

```bash
jgi_summarize_bam_contig_depth --outputDepth sample_depth.txt sample.bam
metabat2 -t threads -i sample.fasta -a sample_depth.txt -o result_dir
```

---

## MetaBinner

```bash
bash gen_coverage_file.sh -a sample.fasta -o tmpdir -b sample.bam -f .1.fa.gz -r .2.fa.gz read1.fa.gz read2.fa.gz
python Filter_tooshort.py sample.fasta 1000
python gen_kmer.py sample_1000.fa 1000 4
bash run_metabinner.sh -a sample_1000.fa -o result_dir -d coverage_profile_f1000.tsv -k contigs_kmer_4_f1000.csv -p metabinner_path -t threads

```

---

## MetaDecoder

```bash
metadecoder coverage -s sample.sam -o METADECODER.COVERAGE
metadecoder seed --threads thread -f sample.fasta -o METADECODER.SEED
metadecoder cluster -f sample.fasta -c METADECODER.COVERAGE -s METADECODER.SEED -o result_dir --disable_gpu
```

---

## SemiBin2

### Single-sample mode

```bash
SemiBin single_easy_bin --threads threads -i sample.fasta -b sample.bam -o result_dir --self-supervised --tmpdir tmpdir
```

### Multi-sample mode

```bash
SemiBin multi_easy_bin --threads threads -i concatenated.fa -b concat.bam -o result_dir --self-supervised --tmpdir tmpdir
```

---

## VAMB

### Single-sample mode

```bash
jgi_summarize_bam_contig_depths --outputDepth sample_depth.txt sample.bam
vamb -m 2000 -p threads --outdir result_dir --fasta sample.fasta --jgi sample_depth.txt --minfasta 200000
```

### Multi-sample mode

```bash
vamb -m 2000 -p threads --minfasta 200000 --fasta concatenated.fa" --bamfiles concat.bam --outdir result_dir -o :
```
