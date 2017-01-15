#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

def get_mRNA():

    # Get DNA as a looooooooooooooong string
    with open("Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa", mode="rt") as fasta:

        # Filter out the line that starts with >
        # I'm safe here, there is only one, the rest is the DNA sequence
        wholeFasta = ''.join(item for item in fasta if not item.startswith('>'))
        print("Chromosome length: %d" % (len(wholeFasta)))

    # Open GTF file
    with open("Homo_sapiens.GRCh38.87.gtf", mode="rt") as gtf:
        mRNA=[]
        for line in gtf:
            # Get GTF line that are about "gene" for Chr 7
            blocks = line.split("\t")
            if len(blocks) == 9 and blocks[0] == "7" and blocks[2] == "gene": 
                # append the dna part that the gene "points to"
                # Note: Counting starts from 1
                start=int(blocks[3]) - 1
                end=int(blocks[4]) - 1
                gene=wholeFasta[start:end]
                mRNA.append(gene)

    # Writing the mRNA back to a file
    with open('mRNA.fa', 'w') as f:
        _mRNA=''.join(mRNA)
        print("mRNA length: %d" % (len(_mRNA)))
        f.write( _mRNA )
        

def count_genes():

    with open("Homo_sapiens.GRCh38.87.gtf", mode="rt") as gtfFile:
        counter=0
        for line in gtfFile:
            blocks = line.split("\t")
            if len(blocks) == 9 and blocks[0] == "7" and blocks[2] == "gene": 
                counter+=1
        print("GTF File: %d gene" % counter)

# awk '$3 == "gene" {count++} END{print count}' Homo_sapiens.GRCh38.87.gtf
# 

def fasta_length():

    with open("Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa", mode="rt") as fastaFile:
        length=0
        for line in fastaFile:
            if not line.startswith('>'):
                length+=len(line)
        print("Fasta File: Chromosome length: %d" % length)

    

if __name__ == "__main__":
    start = time.time()
    #count_genes()
    #fasta_length()
    get_mRNA()
    end = time.time()
    print("Time for mRNA: %.2f seconds" % (end-start))
