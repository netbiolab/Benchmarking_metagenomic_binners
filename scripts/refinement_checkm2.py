#!/usr/bin/env python3

import os, sys, glob

# This script is adapted from the metaWRAP bin refinement module:
# https://github.com/bxlab/metaWRAP
# Modifications were made to support CheckM2-derived bin quality statistics.
# Please refer to the original metaWRAP license for terms of use.

##CAUTION###
print('Input bin must have *.fa *.fasta / NOT .fna!!!!metabat2,mexbin2,concoct is ok')
print('Output directory must be empty!!!')


def bin_len(fname):
    f = open(fname, 'r')
    length = 0
    for line in f:
        line = line.strip()
        if line[0] == '>' :continue
        else: length += len(line)
    return length

binsA, binsB, binsC = sys.argv[2], sys.argv[3], sys.argv[4]
output = sys.argv[1]
thread = sys.argv[5]

# 0. preparing directory.(fix_config_naming.py REQUIRED)

idx2alp = {0:'A', 1:'B',2:'C'}

for idx, bin_dir in enumerate([binsA, binsB, binsC]):
    os.system('mkdir -p %s/bins%s'%(output, idx2alp[idx]))
    bins = glob.glob('%s/*.fa*'%bin_dir)
    for b in bins:
        tmp = bin_len(b)
        if tmp > 50000 and tmp < 20000000:
            os.system('cp %s %s/bins%s'%(b, output, idx2alp[idx]))

        else:
            print('%s in %s is not between 50kb and 20Mb'%(b.split('/')[-1], b.split('/')[-2]))


for bin_dir in ['A','B','C']:
    tmp_dir = '%s/bins%s'%(output, bin_dir)
    bins = glob.glob('%s/*.fa*'%tmp_dir)
    for b in bins:
        os.system('fix_config_naming.py %s > %s/tmp.fa'%(b, tmp_dir))
        os.system('mv %s/tmp.fa %s'%(tmp_dir, b))


# 1. Using binning_refiner.py (binning_refiner.py REQUIRED)

os.system('binning_refiner.py -1 %s/binsA -2 %s/binsB -3 %s/binsC -o %s/Refined_ABC'%(output,output,output,output))
os.system('binning_refiner.py -1 %s/binsA -2 %s/binsB -o %s/Refined_AB'%(output,output,output))
os.system('binning_refiner.py -1 %s/binsC -2 %s/binsB -o %s/Refined_BC'%(output,output,output))
os.system('binning_refiner.py -1 %s/binsA -2 %s/binsC -o %s/Refined_AC'%(output,output,output))

os.system('mv %s/Refined_ABC/Refined %s/binsABC'%(output,output))
os.system('mv %s/Refined_AB/Refined %s/binsAB'%(output,output))
os.system('mv %s/Refined_BC/Refined %s/binsBC'%(output,output))
os.system('mv %s/Refined_AC/Refined %s/binsAC'%(output,output))


print("fixing bin naming to .fa convention for consistancy..")
total_bin = glob.glob('%s/bins*/*'%output)
for bins in total_bin:
    pre, ext = os.path.splitext(bins)
    os.rename(bins, pre+'.fa')


# 2. Run checkM2 on all bin sets (checkM2 and summarize_checkm.py REQUIRED)
for bin_dir in ['binsA', 'binsB', 'binsC', 'binsABC', 'binsAB', 'binsBC', 'binsAC']:
    os.system('checkm2 predict --input %s/%s --output-directory %s/%s.checkm -t %s -x fa'%(output, bin_dir, output, bin_dir, thread))
    os.system('summarize_checkm2.py %s/%s.checkm/quality_report.tsv %s > %s/%s.stats'%(output, bin_dir, bin_dir, output, bin_dir))

# 3. Consolidate all bin sets (consolidate_two_sets_of_bins.py REQUIRED)
os.system('cp -r %s/binsA %s/binsM; cp %s/binsA.stats %s/binsM.stats'%(output,output,output,output))
for bin_dir in ['binsA', 'binsB', 'binsC', 'binsABC', 'binsAB', 'binsBC', 'binsAC']:
    os.system('consolidate_two_sets_of_bins.py %s/binsM %s/%s %s/binsM.stats %s/%s.stats %s/binsM1 50 10'%(output,output,bin_dir,output,output,bin_dir,output))
    os.system('rm -r %s/binsM %s/binsM.stats'%(output,output))
    os.system('mv %s/binsM1 %s/binsM; mv %s/binsM1.stats %s/binsM.stats'%(output,output,output,output))

# 4. Dereplication(Default = Partial; dereplicate_contigs_in_bins.py REQUIRED)
'''
if dereplicate == 'False':
    print("Skipping dereplication of contigs between bins...")
    os.system("mv %s/binsM %s/binsO"%(output,output))
    os.system("mv %s/binsM.stats %s/binsO.stats"%(output,output))
'''
print("Scanning to find duplicate contigs between bins and only keep them in the best bin...")
os.system("dereplicate_contigs_in_bins.py %s/binsM.stats %s/binsM %s/binsO_partial"%(output,output,output))

print("Scanning to find duplicate contigs between bins and deleting them in all bins...")
os.system("dereplicate_contigs_in_bins.py %s/binsM.stats %s/binsM %s/binsO_complete remove"%(output,output,output))
