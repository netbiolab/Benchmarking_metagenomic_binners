#!/usr/bin/env python3
import sys
# This script summarizes the statistics of each bin by parsing 
# the checkm_folder/storage/bin_stats_ext.tsv file of the CheckM output


if len(sys.argv)==3: 
    binner=sys.argv[2]
    print("bin\tcompleteness\tcontamination\tCompleteness_Model_Used\tbinner")
elif len(sys.argv)==4:
    source={}
    for line in open(sys.argv[3]):
        cut=line.strip().split("\t")
        source[cut[0]]=cut[4]
    print("bin\tcompleteness\tcontamination\tCompleteness_Model_Used\tbinner")
else:
    print("bin\tcompleteness\tcontamination\tCompleteness_Model_Used")


for line in open(sys.argv[1]):
    if line[0:4] == 'Name': continue
    name=line.split("\t")[0]
    name, Completeness, Contamination, Completeness_Model_Used, _,*notes = line.split("\t")

    if len(sys.argv)==3:	
        print("\t".join([name, str(Completeness),str(Contamination), Completeness_Model_Used, binner]))

    elif len(sys.argv)==4:
        print("\t".join([name, str(Completeness),str(Contamination),Completeness_Model_Used, source[name]]))

    else:
        print("\t".join([name, str(Completeness),str(Contamination), Completeness_Model_Used]))
