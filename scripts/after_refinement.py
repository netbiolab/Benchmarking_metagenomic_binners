#!/usr/bin/env python3

import os, sys

output = sys.argv[1]

print("Scanning to find duplicate contigs between bins and only keep them in the best bin...")
os.system("dereplicate_contigs_in_bins.py %s/binsM.stats %s/binsM %s/binsO_partial"%(output,output,output))

print("Scanning to find duplicate contigs between bins and deleting them in all bins...")
os.system("dereplicate_contigs_in_bins.py %s/binsM.stats %s/binsM %s/binsO_complete remove"%(output,output,output))


