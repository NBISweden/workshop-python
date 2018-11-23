"""
Script that finds truncated proteins for the CFTR gene. Can take several \
patient fasta files as input
Usage:
python findTruncations.py <file.gtf> <ref.fasta> <patient1.fasta> <patient2.fasta> ....
"""

from utils import rna
import sys


def translate(file, exons, start_codon):
    fh = open(file, 'r')
    sequence = []
    for line in fh:
        if not line.startswith('>'):
            sequence.append(line.strip())
    fh.close()
    s = ''.join(sequence)  
    mrna = ''
    for exon in exons:
        mrna += (s[exon[0]-1:exon[1]])
    start = start_codon - exons[0][0]  # use start of exon to start counting at beginning of mrna
    aaSeq = rna.translate_dna(mrna[start:])  # Translate to aminoacids
    return aaSeq
    
    
def findStartCodon(file, trans_id):
    fh = open(file, 'r')
    for line in fh:
        if not line.startswith('#'):
            cols = line.strip().split('\t')
            if cols[2] == 'start_codon':
                attr = cols[8].strip().split(';')
                transId = attr[2].strip().split()[1]
                if transId == trans_id:
                    if cols[2] == 'start_codon':
                        start_codon = int(cols[3])
                        break
    fh.close()
    return start_codon
    
    
def findExonPositions(file, trans_id):
    fh    = open(file,'r')
    exons = []
    for line in fh:
        if not line.startswith('#'):
            cols = line.strip().split('\t')
            if cols[2] == 'exon':
                attr     = cols[8].split(';')
                transId = attr[2].strip().split(' ')[1]
                if transId == trans_id:
                    start = int(cols[3])
                    end   = int(cols[4])
                    exons.append((start, end))
    fh.close()     
    return exons
    
    
def translatePatients(patList, exons, start_codon):
    aaSeq_list = []
    i = 0
    while i < len(patList):   # Build one aa sequence per patient
        file  = patList[i]
        aaSeq = translate(file, exons, start_codon)
        aaSeq_list.append(aaSeq) 
        i += 1 
    return aaSeq_list

    
def compareToRef(aaSeq_list, aaSeqRef):   # compare patient seq to ref seq
    for sequence in aaSeq_list:
        if not len(sequence) == len(aaSeqRef):
            print('Patient '+str(aaSeq_list.index(sequence)+1)+' has a different protein sequence')
            print('Reference sequence:')
            print(aaSeqRef+'\n')
            print('Patient '+str(aaSeq_list.index(sequence)+1)+' sequence:')
            print(sequence)


def main():
    start_c    = findStartCodon(sys.argv[1], '"ENST00000003084"')  # identify start and stop codon positions
    exons      = findExonPositions(sys.argv[1], '"ENST00000003084"')  # identify exons positions for transcript
    aaSeqRef   = translate(sys.argv[2], exons, start_c)  # save the aa sequence for the reference
    aaSeq_list = translatePatients(sys.argv[3:], exons, start_c)  # do the same for the 5 input patient files
    compareToRef(aaSeq_list, aaSeqRef)   # compare patient aaseq to ref



if __name__ == "__main__":
    if len(sys.argv) < 4:   # check number of input files
        print('ERROR: Not enough input files')
        print('\nUSAGE:\nFinds truncated proteins. Input: GTF file, Fasta reference, optional number of patient fasta files')
        sys.exit()
    else:
        main()
