# Variant calling in highly homologous regions
This pipeline is designed to perform variant calling on regions with high homology to a pseudogene by masking all of them with the exeption of one that will represent the rest.

## Required Input
This pipeline requires:
  - A reference genome.
  - A gff3 annotation of the reference genome.
  - A fastq file with the reads we want to do variant calling on.
  
## How to use it?
All the steps the pipeline have been divided in 3 different python scripts that can be run individually or together with Execute_all.py. If you want to run them individually here are the steps you must follow:

  -**STEP_01 ** First of all you must 
