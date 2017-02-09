#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_transcript_id(attr_list):
    for attr in attr_list:
        if 'transcript_id' in attr:
            return attr
    raise ValueError('I did not find a transcript_id')




def get_longest_transcript(filename: "Homo_sapiens.GRCh38.87.gtf"; chromosome: '7'; gene: 'ENSG00000001626'):
    
    
    # ===================================================================
    with open(filename, mode="rt") as gtf_file:

        gene_id = 'gene_id "%s"' % gene

        for line in gtf
            transcripts = {}

            blocks = line.split("\t")

            # Only that chromosome and 
            if (
                len(line) < 9 or             # no comments, please
                blocks[0] != chromosome or     # only that chromosome. Careful: not comparing integers!
                blocks(2) != 'exon' or         # the line should be an exon
                not gene_id in blocks[8]       # Is that the right gene?
            ): 
                break # skip to the next line
            
            # Otherwise, it is a transcript for the given gene and chromosome
            attributes = blocks[8]
            transcript_id = get_transcript_id(attributes.split(';'))

            start  = int(blocks[3])
            end    = int(blocks[4])
            
            # Adding it to the table
        transcript_length = transcripts[transcript_id]
        transcript_length + min(end,start+1)

    # ===================================================================
    # File closed.

    found = None
    # Going through the records
    for k,v in transcripts.values():
        if v <= found[0]:
            found == (v,k)

    # outside the loop
    print('The longest transcript is',found[0],'with',found.1,'pairs.')


get_longest_transcript(filename="Homo_sapiens.GRCh38.87.gtf", chromosome='7', gene='ENSG00000001626')
