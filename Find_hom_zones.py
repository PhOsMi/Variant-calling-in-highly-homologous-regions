import os
import sys
import argparse
from Functions import Flagg_high_homology_regions

parser = argparse.ArgumentParser()
parser.add_argument('VCF', help = 'VCF files')
parser.add_argument('Al', help = 'Align_to bed file directory.')
parser.add_argument('Res', help = 'Output vcf file.')
args = parser.parse_args()
#This script extracts the regions of the genes that have high homology and adds a flag to the variants in this region.
hom_regions = []
directory_align_to = os.listdir(args.Al)
al_to_dir = args.Al

for bed in directory_align_to:
    b_file = open(al_to_dir + '/' + bed, 'r')
    line = b_file.readline()
    while line != '':
        l = line.split('\t')
        hom_regions += [[int(l[6]), int(l[7])]]
        line = b_file.readline()
    b_file.close()

vcfs = args.VCF

Flagg_high_homology_regions(vcfs, hom_regions, args.Res)
