import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-R', '--REFERENCE', help = 'Reference sequence in fasta format.')
parser.add_argument('-A', '--Annotation', help = 'GFF3 annotation file.')
parser.add_argument('-I', '--input', help = 'Fastq file of the reads were variant calling will be performed (just one fastq).')
parser.add_argument('-ID', '--ID_RG', help = 'ID of the RG group of the reads (If not specified C will be used).', default = 'C')
parser.add_argument('-SM', '--SM_RG', help = 'SM of the RG group of the reads (If not specified C will be used).', default = 'C')
parser.add_argument('-O', '--output', help = 'Directory were the results will be kept in vcf format (Current working directory by default).', default = os.getcwd())
parser.add_argument('-t', '--threads', help = 'Number of threads (1 by default).', default = '1')
args = parser.parse_args()

#Checking that all the files necessary to run the pipeline are present and in the correct format.

if(args.REFERENCE == None):
    print('ERROR: Reference sequence required.')
    sys.exit()
elif (args.REFERENCE.split('.')[-1] != 'fa'):
    if args.REFERENCE.split('.')[-1] != 'fasta':
        print('WARNING: Reference sequence must be in .fasta format.')

if(args.Annotation == None):
    print('ERROR: Annotation file required.')
    sys.exit()
elif (args.Annotation.split('.')[-1] != 'gff3'):
    if (args.Annotation.split('.')[-1] != 'gff'):
        print('WARNING: Annotation file must be in .gff3 or .gff format.')

if(args.input == None):
    print('ERROR: Fastq file of reads required.')
    sys.exit()
elif(args.input.split('.')[-1] != 'fastq'):
    if(args.input.split('.')[-1] != 'fq'):
        print('WARNING: Input must be in .fastq format.')

os.system('mkdir TEMPORAL_FILES')
os.system('mkdir TEMPORAL_FILES/Align_to')
os.system('mkdir TEMPORAL_FILES/Realign')

#Creating the blast gene database our script will use.
os.system('bash Init.sh ' + args.Annotation + ' ' + args.REFERENCE + ' ' + 'TEMPORAL_FILES')

#Creating align to beds and realign beds
os.system('python createCamogroups_3.py -fp TEMPORAL_FILES/Pseudogenes.fasta -bl TEMPORAL_FILES/Blast_Database/GENE_DATABASE -OM TEMPORAL_FILES/Align_to -OR TEMPORAL_FILES/Realign')
#Variant calling
os.system('python Mask_dir_3.py -I ' + args.input + ' -ID ' + args.ID_RG + ' -SM ' + args.SM_RG + ' -t ' + args.threads + ' -O ' + args.output + ' -real TEMPORAL_FILES/Realign -Al_to TEMPORAL_FILES/Align_to -R ' + args.REFERENCE)
#extracting variants from the requested region.

#Finding high homology regions.

os.system('rm -r TEMPORAL_FILES')