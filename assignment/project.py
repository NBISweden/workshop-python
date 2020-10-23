
from utils.rna import translate_dna
from utils import check_answers

from pprint import pprint
import re

def parse_gtf(lines):
    '''
    Parses lines from a GTF file and returns a list of dictionaries
    with the data. Note that the dicts take more memory than just
    iterating over lines so if you have many lines but are only
    interested in a few of them try filtering them first to avoid
    creating too many dicts.
    '''
    rows = []

    for line in lines:
        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        d = {}
        # print(line, fields)
        d['seqname'] = fields[0]
        d['source']  = fields[1]
        d['feature'] = fields[2]
        d['start']   = fields[3]
        d['end']     = fields[4]
        d['score']   = fields[5]
        d['strand']  = fields[6]
        d['frame']   = fields[7]
        attributes = fields[8]
        for attribute in re.split(';\s*', attributes.strip(';')):
            # attribute looks like 'gene_version "5"'
            key_and_value = attribute.split(' ', maxsplit=1)
            key = key_and_value[0]
            value = key_and_value[1]
            d[key] = value
        # clean up data:
        for key in d:
            d[key] = d[key].strip('"')
            if re.match('^\d+$', d[key]):
                d[key] = int(d[key])
        rows.append(d)

    return rows

example_line = '1\thavana\tgene\t11869\t14409\t.\t+\t.\tgene_id "ENSG00000223972"; gene_version "5"; gene_name "DDX11L1"; gene_source "havana"; gene_biotype "transcribed_unprocessed_pseudogene";'

# pprint([parse_gtf([example_line])], sort_dicts=False)

CFTR_gene_id = 'ENSG00000001626'
CFTR_lines = []

fh = open('./data/Homo_sapiens.GRCh38.93.gtf', 'r')
for line in fh:
    if CFTR_gene_id in line:
        CFTR_lines.append(line)
fh.close()

rows = parse_gtf(CFTR_lines)

# pprint(rows[:2], sort_dicts=False)

num_transcripts = 0
for row in rows:
    if row['feature'] == 'transcript' and row['gene_id'] == CFTR_gene_id:
        num_transcripts += 1

print(f'''
1. How many transcripts can the CFTR gene generate?
    {num_transcripts = }
''')

longest_length = 0
longest_row = None
for row in rows:
    if row['feature'] == 'transcript' and row['gene_id'] == CFTR_gene_id:
        length = row['end'] - row['start'] + 1
        if length > longest_length:
            longest_length = length
            longest_row = row

print(f'''
2. Which of these transcripts is the longest transcript in nucleotides?
    {longest_length = }
    {longest_row['transcript_id'] = }
''')

def fasta_subsequence(filename, start, end):
    '''
    Opens a fasta file with only one sequence in it and returns
    the subsequence from start to end inclusive
    using 1-indexing.
    '''
    fh = open(filename, 'r')
    seq = ''
    for line in fh:
        if line.startswith('>'):
            continue
        seq += line.strip()
    fh.close()
    return seq[start - 1: end]

def fasta_subsequences(filename, start_end_list):
    '''
    Opens a fasta file with only one sequence in it and returns
    the concatenation of subsequences of start to end inclusive
    using 1-indexing in the list start_end_list .
    '''
    fh = open(filename, 'r')
    seq = ''
    for line in fh:
        if line.startswith('>'):
            continue
        seq += line.strip()
    fh.close()
    out = ''
    for start_end in start_end_list:
        start = start_end[0]
        end = start_end[1]
        out += seq[start - 1: end]
    return out

c7_filename = './data/Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa'

longest_seq = fasta_subsequence(c7_filename, longest_row['start'], longest_row['end'])
print(f'''
3. Fetch the DNA sequence for that transcript.
    {longest_seq[:10] = }
    {len(longest_seq) = }
''')

fh = open('longest_seq.txt', 'w')
fh.write(longest_seq)
fh.close()
check_answers.ex3('longest_seq.txt')

exons_pos = []
for row in rows:
    if row['feature'] == 'exon' and row['transcript_id'] == longest_row['transcript_id']:
        exons_pos.append([row['start'], row['end']])

mrna_seq = fasta_subsequences(c7_filename, exons_pos)

print(f'''
4. Fetch the DNA sequences of all exons for that transcript, spliced together to one sequence.
    {exons_pos[:2]  = }
    {len(exons_pos) = }
    {mrna_seq[:10]  = }
    {len(mrna_seq)  = }
''')

fh = open('mrna_seq.txt', 'w')
fh.write(mrna_seq)
fh.close()
check_answers.ex4('mrna_seq.txt')

for row in rows:
    if row.get('transcript_id') == longest_row['transcript_id']:
        if row['feature'] == 'start_codon':
            start_codon_row = row
        if row['feature'] == 'stop_codon':
            stop_codon_row = row

start_codon_seq = fasta_subsequence(c7_filename, start_codon_row['start'], start_codon_row['end'])
stop_codon_seq = fasta_subsequence(c7_filename, stop_codon_row['start'], stop_codon_row['end'])

print(f'''
5. What are the start positions and sequences of the start_codon and stop_codon for that transcript?
    {start_codon_row['start'] = } {start_codon_seq = }
    {stop_codon_row['start']  = } {stop_codon_seq  = }
''')

first_exon_pos = exons_pos[0]
first_exon_start = first_exon_pos[0]
first_exon_stop = first_exon_pos[1]
cds_pos = [[start_codon_row['start'], first_exon_stop]] + exons_pos[1:]
cds = fasta_subsequences(c7_filename, cds_pos)

protein = translate_dna(cds)

print(f'''
6. Translate the above sequence of all exons into amino acids
    {cds_pos[:2]  = }
    {len(cds_pos) = }
    {cds[:10]     = }
    {len(cds)     = }
    {protein[:10] = }
    {len(protein) = }
''')

fh = open('protein.txt', 'w')
fh.write(protein)
fh.close()
check_answers.ex6('protein.txt')

files = [
    './data/Patient1.fa',
    './data/Patient2.fa',
    './data/Patient3.fa',
    './data/Patient4.fa',
    './data/Patient5.fa',
]

print('=== FINAL REPORT ===')
for patient_file in files:
    patient_cds = fasta_subsequences(patient_file, cds_pos)
    patient_protein = translate_dna(patient_cds)
    if len(patient_protein) < len(protein):
        print(f'{patient_file} is at risk')
print('=== END OF REPORT ===')
