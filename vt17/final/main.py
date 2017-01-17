#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from utils import time_function, RNATranslationTable
import re
from pprint import pprint

@time_function
def dna_length():

    with open("Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa", mode="rt") as fasta:
        count=0
        for line in fasta:
            if not line.startswith('>'):
                count+=len(line)
        print("Chr7 length: %d" % (count))

@time_function
def count_genes():

    with open("Homo_sapiens.GRCh38.87.gtf", mode="rt") as gtf:
        counter=0
        for line in gtf:
            blocks = line.split("\t")
            if ( 
                    len(blocks) == 9        # not a comment, thanks
                    and blocks[0] == "7"    # for Chr7 
                    and blocks[2] == "gene" # only gene, please
            ): 
                counter+=1
        print("%d genes for chromosome 7" % counter)

# awk '$1 == "7" && $3 == "gene" {count++} END{print count}' Homo_sapiens.GRCh38.87.gtf
# 

regexps = {
    'transcript_id': re.compile(r'transcript_id\s+"?(\w+)"?'),
    'exon_id': re.compile(r'exon_id\s+"?(\w+)"?')
}

def get_value(v,attr):
    regex = regexps.get(v,None)
    if re:
        match=regex.search(attr)
        if match:
            return match.group(1)
    return None


longest_transcript = None

def get_longest_transcript(chr='7',gene='ENSG00000001626'):
    
    global longest_transcript
    if longest_transcript:
        return

    transcripts = {}
    
    # First pass: Fetch all transcripts for that gene
    with open("Homo_sapiens.GRCh38.87.gtf", mode="rt") as gtf:
        #gene_id = 'gene_id "%s"' % gene
        gene_re = re.compile(r'gene_id\s+"?{}"?'.format(gene))
        for line in gtf:
            blocks = line.split("\t")
            # Only Chr 7 and no comments, please
            if (
                    len(blocks) < 9 or
                    blocks[0] != chr or
                    blocks[2] != 'transcript' or
                    not gene_re.search(blocks[8])
            ): 
                continue
            
            attributes = blocks[8]
            transcript_id = get_value('transcript_id',attributes)

            assert( transcript_id ) # is not None
            assert (transcript_id not in transcripts), ("How come I see transcript %s already? \n\nLine:\n\n%s" % (transcript_id,line))

            start=int(blocks[3])
            end=int(blocks[4])
            strand = 1
            if blocks[6] == '-':
                strand = -1
            # exons will be added in the second pass
            transcripts[transcript_id]={'start':start, 'end':end, 'strand':strand,
                                        'exons':{}, 'start_codon':None, 'stop_codon':None }

    # Second pass, fetching the exons for those transcripts
    with open("Homo_sapiens.GRCh38.87.gtf", mode="rt") as gtf:
        for line in gtf:
            blocks = line.split("\t")
            # Only Chr 7 and no comments, please
            if (
                    len(blocks) < 9 or
                    blocks[0] != chr or
                    not (blocks[2] == "exon" or blocks[2] == "start_codon" or blocks[2] == "stop_codon")
            ): 
                continue

            feature = blocks[2]
            attributes = blocks[8]

            transcript_id = get_value('transcript_id',attributes)

            if transcript_id not in transcripts: # checking the keys
                continue
                
            assert( gene_re.search(attributes) )

            if feature == "exon":
                exon_id = get_value('exon_id',attributes)
                exons = transcripts[transcript_id].get('exons',None)
                assert( exons is not None )
                if exon_id in exons:
                    print("Weird! Have I seen that exon %s before?" % exon_id) 

                start=int(blocks[3])
                end=int(blocks[4])
                strand = 1
                if blocks[6] == '-':
                    strand = -1
                record = {'start':start, 'end':end, 'strand':strand }
                exons[exon_id]=record
                # No need to update the transcripts dict, it's a hashtable

            if feature == "start_codon" or feature == "stop_codon":
                start=int(blocks[3])
                end=int(blocks[4])
                strand = 1
                if blocks[6] == '-':
                    strand = -1
                record = {'start':start, 'end':end, 'strand':strand }
                assert( transcripts[transcript_id].get(feature,None) is None )
                transcripts[transcript_id][feature] = record

    # Find the longest transcript
    transcript_count = len(transcripts.keys())
    longest_transcript_id=None
    longest=0

    for transcript_id,transcript_info in transcripts.items():
        transcript_start = transcript_info['start']
        transcript_end = transcript_info['end']
        transcript_exons = transcript_info['exons']

        transcript_length=0
        for exon_info in transcript_exons.values():
            exon_start = exon_info['start']
            exon_end = exon_info['end']

            start = max(exon_start,transcript_start)
            end = min(exon_end,transcript_end)

            assert( exon_info['strand'] > 0 and transcript_info['strand'] > 0 )
            transcript_length+=abs(end-start+1)

        if transcript_length > longest:
            longest = transcript_length
            longest_transcript_id = transcript_id
 

    assert( longest_transcript_id is not None )
    longest_transcript = transcripts.get(longest_transcript_id)

    print("%d transcripts for gene %s (on Chr %s)" % (transcript_count,gene,chr))
    print("Transcript %s has the longest mRNA (%d bp)" % (longest_transcript_id,longest))
    #pprint(longest_transcript)

dna = None
def fetch_dna(chr=7):

    global dna
    if dna:
        return

    # Get DNA as a looooooooooooooong string
    with open("Homo_sapiens.GRCh38.dna_sm.chromosome.%d.fa" % chr, mode="rt") as fasta:
        # Filter out the line that starts with >
        # I'm safe here, there is only one, the rest is the DNA sequence
        dna = ''.join(item.strip(' \n') for item in fasta if not item.startswith('>'))
        
    print("Length of Chr %d: %d" % (chr,len(dna)))
    with open('dna.fa','w') as f:
        f.write(dna)
    

mRNA = None
def get_mRNA(just_protein=False):

    global mRNA
    if mRNA:
        return

    global dna
    fetch_dna()

    global longest_transcript
    get_longest_transcript()

    start_codon = longest_transcript['start_codon']['start'] # It should have those keys
    stop_codon = longest_transcript['stop_codon']['end']
    exons = longest_transcript['exons'] 
    sorted_exons = sorted(exons.values(), # Iterate through the exon dicts
                          key=lambda exon: exon['start']
                          )

    #print("Exons from the longest transcript")
    #pprint(sorted_exons)

    if just_protein:
        mRNA = ''.join(dna[
            max(start_codon, exon['start']) - 1
            :
            min(stop_codon, exon['end']) # +1 -1
        ] for exon in sorted_exons)
    else:
        mRNA = ''.join(dna[ exon['start']-1 : (exon['end']) ] for exon in sorted_exons)

    name = 'mRNA.fasta'
    if just_protein:
        name = 'mRNA.protein.fasta'
        #mRNA = mRNA.replace('T','U')

    with open(name,'w') as f:
        f.write(mRNA)
        f.write('\n')

codons = []
AminoAcids = []
def get_protein():

    global AminoAcids
    if AminoAcids:
        return

    get_mRNA(just_protein=True)

    # print("\n===== mRNA: %d (mod 3: %d)" % (len(mRNA),len(mRNA) % 3))
    
    global codons
    codons = [mRNA[i:i+3] for i in range(0, len(mRNA), 3)]
    # print("\n===== Codons ======")
    # pprint(codons)

    table = RNATranslationTable()

    for codon in codons:
        AminoAcid = table.translate(codon)
        if AminoAcid == '*': # Stoping if meeting a stop codon
            break
        AminoAcids.append(AminoAcid)

    protein = ''.join( AminoAcids )

    print("Protein length %d" % ( len(protein) ))
    with open('protein.fasta','w') as f:
        f.write(protein)
        f.write('\n')
    

# if __name__ == "__main__":
#     start = time.time()
#     #count_genes()
#     #fasta_length()
#     get_mRNA()
#     end = time.time()
#     print("Time for mRNA: %.2f seconds" % (end-start))
