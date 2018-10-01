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

    # Use exon start and end to extract exon sequences from fasta
    mrna = ''
    for exon in exons:
        mrna += (s[exon[0]-1:exon[1]])

    # Translate to aminoacids
    start = start_codon - exons[0][0]  # use start of exon to start counting at beginning of mrna

    aaSeq = ''
    j = 0
    while j < len(mrna[start:]):
        codon = mrna[start+j:start+3+j]
        aa    = rna.RNATranslationTable().translate(codon)
        if aa == '*':
            break
        aaSeq += aa
        j       += 3
    
    return aaSeq

def findStartStopCodons(file, trans_id):
    fh = open(file, 'r')
    for line in fh:
        if not line.startswith('#'):
            cols = line.strip().split('\t')
            if cols[2] == 'start_codon' or cols[2] == 'stop_codon':
                attr = cols[8].strip().split(';')
                transId = attr[2].strip().split()[1]
                if transId == trans_id:
                    if cols[2] == 'start_codon':
                        start_codon = int(cols[3])
                    elif cols[2] == 'stop_codon':
                        stop_codon = int(cols[3])
    fh.close()
    
    return start_codon, stop_codon


def findExonPositions(file, trans_id):
    fh = open(file,'r')
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


# check number of input files
if len(sys.argv) < 4:
  print('ERROR: Not enough input files')
  print('\nUSAGE:\nFinds truncated proteins. Input: GTF file, Fasta reference, optional number of patient fasta files')
  sys.exit()

# identify start and stop codon positions
file                    = sys.argv[1]
start_codon, stop_codon = findStartStopCodons(file, '"ENST00000003084"')


# identify exons positions for transcript
file = sys.argv[1]
exons = findExonPositions(file, '"ENST00000003084"')


# save the aa sequence for the reference
file     = sys.argv[2]
aaSeqRef = translate(file, exons, start_codon)

    
# do the same for the 5 input patient files
aaSeq_list = []
i = 0
while i < len(sys.argv[3:]):
    # Build one aa sequence per patient
    file  = sys.argv[3+i]
    aaSeq = translate(file, exons, start_codon)
    aaSeq_list.append(aaSeq) 
    i += 1 
    
# compare patient seq to ref seq
for sequence in aaSeq_list:
    if not len(sequence) == len(aaSeqRef):
        print('Patient '+str(aaSeq_list.index(sequence)+1)+' has a different protein sequence')
        print('Reference sequence:')
        print(aaSeqRef+'\n')
        print('Patient '+str(aaSeq_list.index(sequence)+1)+' sequence:')
        print(sequence)
