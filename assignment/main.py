#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from utils import time_me, print_args, print_retval
from utils import get_gtf_value
from utils.rna import RNATranslationTable
import re
#from os.path import splitext

import logging
logger = logging.getLogger() # root logger
logging.basicConfig(level=logging.INFO,format='%(message)s')

@time_me
@print_args
def get_all_transcripts(filename="Homo_sapiens.GRCh38.87.gtf", chromosome='7', gene='ENSG00000001626'):
    
    transcripts = {}
    
    # First pass: Fetch all transcripts for the given gene and chromosome
    # ===================================================================
    logger.debug('First pass on file %s' % filename)
    logger.debug('Chr %s | Gene %s' % (chromosome,gene))
    with open(filename, mode="rt") as gtf:
        #gene_id = 'gene_id "%s"' % gene
        gene_re = re.compile(r'gene_id\s+"?{}"?'.format(gene))
        for line in gtf:
            blocks = line.split("\t")
            # Only that chromosome and 
            if (
                len(blocks) < 9 or             # no comments, please
                blocks[0] != chromosome or     # only that chromosome. Careful: not comparing integers!
                blocks[2] != 'transcript' or   # the line should be a transcript
                not gene_re.search(blocks[8])  # Is that the right gene?
            ): 
                continue # skip to the next line
            
            # Otherwise, it is a transcript for the given gene and chromosome
            attributes = blocks[8]
            transcript_id = get_gtf_value('transcript_id',attributes)
            
            assert( transcript_id ) # is not None
            assert (transcript_id not in transcripts), ("How come I see transcript %s already? \n\nLine:\n\n%s" % (transcript_id,line))
            
            start  = int(blocks[3])
            end    = int(blocks[4])
            strand = 1 if blocks[6] == '+' else -1
            
            # Adding it to the table
            transcripts[transcript_id] = {
                'start':start,
                'end':end,
                'strand':strand,
                'exons':{}, # exons will be added in the second pass. Empty so far.
                'start_codon': None,
                'stop_codon': None
            }
            logger.debug('Added record: {} => {}'.format(transcript_id,transcripts[transcript_id]))
    
    logger.debug('Transcripts after first pass')
    logger.debug(transcripts)
    
    # Second pass, fetching the exons for those transcripts
    # Must rescan, can't reuse the gtf iterator: it's at the end already.
    # ===================================================================
    logger.debug('Second pass')
    with open(filename, mode="rt") as gtf:
        for line in gtf:
            blocks = line.split("\t")
            
            if (
                len(blocks) < 9 or          # no comments, please
                blocks[0] != chromosome or  # only that chromosome
                not (blocks[2] == "exon" or blocks[2] == "start_codon" or blocks[2] == "stop_codon")
            ): 
                continue # Skip that line
            
            feature = blocks[2]
            attributes = blocks[8]
            
            transcript_id = get_gtf_value('transcript_id',attributes)
            
            if transcript_id not in transcripts: # checking the keys
                continue # Skip cuz not a transcript for that given gene
            
            if not gene_re.search(attributes):
                print("Weird! I should have a gene_id {gene} in {attr}".format(gene=gene,attr=attributes))
            
            
            if feature == "exon":
                logger.debug('Found an exon')
                exon_id = get_gtf_value('exon_id',attributes)
                exons = transcripts[transcript_id].get('exons',None)
                assert( exons is not None )
                if exon_id in exons:
                    print("Weird! Have I seen that exon %s before?" % exon_id) 
                
                start  = int(blocks[3])
                end    = int(blocks[4])
                strand = 1 if blocks[6] == '+' else -1
                exons[exon_id]={'start':start, 'end':end, 'strand':strand }
                # No need to update the transcripts table, it's a hashtable
            
            if feature == "start_codon" or feature == "stop_codon":
                logger.debug('Found a start/stop codon')
                start  = int(blocks[3])
                end    = int(blocks[4])
                strand = 1 if blocks[6] == '+' else -1
                
                assert( transcripts[transcript_id].get(feature,None) is None ) # Note: that should not return None!
                transcripts[transcript_id][feature] = {'start':start, 'end':end, 'strand':strand }
            
    return transcripts

@time_me
@print_args
def get_longest_transcript(filename="Homo_sapiens.GRCh38.87.gtf", chromosome='7', gene='ENSG00000001626'):
    
    logger.info('Searching for longest transcript')
    transcripts = get_all_transcripts(**locals())
    
    logger.debug('Got transcripts')
    # Find the longest transcript
    # ============================
    # We have a temporary variable that keeps the longest we've seen so far,
    # we scan the others and update if we find a longer one.
    longest_transcript_id=None
    longest=-1
    
    for transcript_id,transcript_info in transcripts.items():
        logger.debug('Going through transcript %s => %s' % (transcript_id,transcript_info))
        transcript_start = transcript_info['start']
        transcript_end = transcript_info['end']
        transcript_exons = transcript_info['exons']
        
        transcript_length=0
        for exon_info in transcript_exons.values():
            logger.debug('\tGoing through exon %s' % (exon_info))
            exon_start = exon_info['start']
            exon_end = exon_info['end']
            
            start = max(exon_start,transcript_start)
            end = min(exon_end,transcript_end)
            
            assert( exon_info['strand'] > 0 and transcript_info['strand'] > 0 )
            transcript_length+=abs(end-start+1)
        
        if transcript_length > longest: # Got a longer one
            logger.debug('\tfound a longer one')
            longest = transcript_length
            longest_transcript_id = transcript_id
    
    assert( longest > 0 )
    assert( longest_transcript_id is not None )
    return transcripts.get(longest_transcript_id)

@time_me
@print_args
def fetch_dna(filename="Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa",chromosome=7,output=None):
    
    logger.info('Fetching DNA as string')
    dna = None # if problem opening file
    # Get DNA as a looooooooooooooong string
    with open(filename, mode="rt") as fasta:
        # Filter out the line that starts with >
        # I'm safe here, there is only one, the rest is the DNA sequence
        dna = ''.join(line.strip(' \n') for line in fasta if not line.startswith('>'))
    
    if output:
        with open(output,'wt') as f:
            f.write(dna)
    
    return dna


@time_me
@print_args
def get_mRNA(dna_filename="Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa", 
             gtf_filename="Homo_sapiens.GRCh38.87.gtf",
             chromosome='7',
             gene='ENSG00000001626',
             transcript=None,
             cds=False,
             mRNA_output=None):
    
    if cds:
        logger.info('From DNA to CDS')
    else:
        logger.info('From DNA to mRNA')
    
    dna = fetch_dna(filename=dna_filename, chromosome=chromosome)
    #print("Length of Chr %d: %d" % (chromosome,len(dna)))
    
    # If we are not given a transcript data structure: go get the one for the longest transcript
    if transcript is None:
        transcript = get_longest_transcript(filename=gtf_filename, chromosome=chromosome, gene=gene)
        # transcript should be id 'ENST00000003084'
    
    logger.debug('Using transcript: %s' % transcript)
    
    start_codon = transcript['start_codon']['start'] # It should have those keys
    stop_codon = transcript['stop_codon']['end']
    exons = transcript['exons'] 
    sorted_exons = sorted(exons.values(), # Iterate through the exon dicts
                          key=lambda exon: exon['start']
    )
    
    logger.debug('Concatenating exons')
    
    if cds: # I cut the little bits before and after the start/stop codons
        content = ''.join(dna[
            max(start_codon, exon['start']) - 1
            :
            min(stop_codon, exon['end']) # +1 -1
        ] for exon in sorted_exons)
    else: # I take the whole concatenation of the exons
        content = ''.join(dna[
            exon['start']-1
            :
            exon['end']
        ] for exon in sorted_exons)
    # Note: we need to shift the index to the left, since the string 'dna' is zero-based.
    
    return content.upper()

@time_me
@print_args
def get_protein(dna_filename="Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa", 
                gtf_filename="Homo_sapiens.GRCh38.87.gtf",
                chromosome='7',
                gene='ENSG00000001626',
                transcript = None
):
    
    # Using **locals() does unfortunately bring output with it...
    cds = get_mRNA( dna_filename=dna_filename,
                    gtf_filename=gtf_filename,
                    chromosome=chromosome,
                    gene=gene,
                    transcript = None,
                    cds=True)
    
    logger.debug("\n===== CDS: %d (mod 3: %d)" % (len(cds),len(cds) % 3))
    
    logger.info('From CDS to PROTEIN')
    
    codons = [cds[i:i+3] for i in range(0, len(cds), 3)]
    # print("\n===== Codons ======")
    # pprint(codons)
    
    #if table is None:
    table = RNATranslationTable()
    #table.print()
    
    AminoAcids=[]
    for codon in codons:
        AminoAcid = table.translate(codon) # uppercase already
        if AminoAcid == '*': # Stoping if meeting a stop codon
            break
        AminoAcids.append(AminoAcid)
    
    return ''.join( AminoAcids )


@time_me
@print_args
@print_retval
def dna_length(filename="Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa"):
    
    with open(filename, mode="rt") as fasta:
        return sum( 
            # Generator expression
            (len(line.strip(' \n')) for line in fasta if not line.startswith('>')),
            0 # start value
        )
    return -1 # if problem opening file

@time_me
@print_args
@print_retval
def genes_count(filename="Homo_sapiens.GRCh38.87.gtf",chromosome='7',gene='ENSG00000001626'):
    
    with open(filename, mode="rt") as gtf:
        counter=0
        for line in gtf:
            blocks = line.split("\t")
            if ( 
                    len(blocks) == 9        # not a comment, thanks
                    and blocks[0] == "7"    # for Chr7 
                    and blocks[2] == "gene" # only gene, please
            ): 
                counter+=1
        return counter
    return -1 # if problem opening file

if __name__ == "__main__":
    import argparse
    #_ = genes_count() # ignore the value
    # Compare that to the 58s of:
    # awk '$1 == "7" && $3 == "gene" {count++} END{print count}' Homo_sapiens.GRCh38.87.gtf
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug','-d', action='store_true', help='Adds debug messages to the output (stdout and/or file)',    default=False )
    parser.add_argument('--quiet','-q', action='store_true', help='Suppress debug messages (from stdout)',                     default=False )
    parser.add_argument('--log',        action='store',      help='Where to log the output',                                   default=None  )
    
    
    parser.add_argument('--dna-file',         action='store', default="Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa", help='DNA file [Default: %(default)s]' )
    parser.add_argument('--gtf-file',         action='store', default="Homo_sapiens.GRCh38.87.gtf",                 help='GTF file [Default: %(default)s]' )
    parser.add_argument('--chromosome', '-c', action='store', default='7',               help='Chromosome Number [Default: %(default)s]', type=str         )
    parser.add_argument('--gene', '-g',       action='store', default='ENSG00000001626', help='Gene ID [Default: %(default)s]'                             )
    
    #parser.add_argument('--transcript', '-t', action='store', default=None,              help='Transcript. If not specified, it finds the longest one'     )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--mRNA',             action='store', default=None,         help='output nRNA to file'                         )
    group.add_argument('--protein',          action='store', default=None,         help='Output protein to file (Note: --cds is on)'  )
    # Either you pass --mRNA or you pass --protein, but you need one!
    parser.add_argument('--cds',              action='store_true', default=False,  help='output the CDS part of the mRNA'             )
    
    args = parser.parse_args()
    
    logger.debug(args)
    
    if args.quiet:
        #logger.setLevel(logging.CRITICAL)
        #logger.propagate = False
        logger.handlers = [logging.NullHandler()]
    
    if args.log:
        logger.addHandler(logging.FileHandler(args.log, 'a'))
        
    if args.debug:
        #logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:\t%(message)s')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s:\t%(message)s')
        for ch in logger.handlers:
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
    
    logger.debug('==== Starting the job')
    
    if args.mRNA:
        mRNA = get_mRNA( dna_filename=args.dna_file, 
                         gtf_filename=args.gtf_file,
                         chromosome=args.chromosome,
                         gene=args.gene,
                         transcript=None,
                         #transcript=args.transcript,
                         cds=args.cds)
        if args.cds:
            logger.debug('Outputing CDS to file: %s' % args.mRNA)
        else:
            logger.debug('Outputing mRNA to file: %s' % args.mRNA)
        # # Get the .ext at the end
        # # put .mrna.ext or .cds.ext 
        # v = splitext(mRNA_output)
        # output = "%s.cds%s" % v if cds else "%s.mrna%s" % v
        with open(args.mRNA,'wt') as f:
            f.write(mRNA)
            f.write('\n')
            if args.cds:
                print('CDS file created: %s' % args.mRNA)
            else:
                print('mRNA file created: %s' % args.mRNA)
    
    
    if args.protein:
        protein = get_protein(dna_filename=args.dna_file, 
                              gtf_filename=args.gtf_file,
                              chromosome=args.chromosome,
                              gene=args.gene,
                              transcript=None,
                              #transcript=args.transcript,
                              )
        
        logger.debug('Outputing protein to file: %s' % args.protein)
        with open(args.protein,'wt') as f:
            f.write(protein)
            f.write('\n')
            print('Protein file created: %s' % args.protein)
    
    logger.debug('==== Job done!')

