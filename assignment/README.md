You are given:
* a [DNA file](data/Homo_sapiens.GRCh38.87.gtf.gz) and
* a [GTF file](data/Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz).

Your task is to implement a python program, that
extracts the protein from a particular transcript.

The task is divided in several steps. A description of the fields used in the GTF format is at the bottom of this file.

## Warm up

1. What is the length of the given DNA sequence?

2. How many genes are annotated in the GTF file?

3. What fraction of the chromosome is annotated as genes?

## The real deal

All the following tasks are now related to the particular gene with id `ENSG00000001626` on chromosome `7`.

4. How many transcripts can this gene generate?

5. What is the longest transcript in term of base pairs?

   __Answer__: The transcript with id `ENST00000003084` has 6132 bp and is the longest among 11 other transcripts.
   
   You can have a look at its [Ensembl data](http://www.ensembl.org/Homo_sapiens/Transcript/Summary?db=core;g=ENSG00000001626;r=7:117465784-117715971;t=ENST00000003084).
   
   Notice that the last column in the GTF on the line defining that transcript should contain `protein_coding`.

6. Fetch the DNA sequence for that gene

7. Fetch all the exons for that transcript (splicing)

   __Answer__: Your answer can be output to a file and compare to [the result files](results/) (also [available online](https://www.ncbi.nlm.nih.gov/nuccore/NM_000492))

8. What are the position of the `start_codon` and `stop_codon` from that transcript?

9. Translate to the corresponding protein.

   An implementation of the [translation table](http://shawmst.org/biology/article/rna-translation-table/) is given in the [utils.rna](utils/rna.py) package.
   
   You can output your results in different files and check the difference with the [given results](results/) or online [here](http://www.uniprot.org/uniprot/A0A024R730.fasta) or [here](https://www.ncbi.nlm.nih.gov/nuccore/NM_000492).

10. Use [BioPython](http://biopython.org/wiki/Documentation) for (some of) the above tasks

   __Prodecure__: Start by [parsing a fasta file with BioPython](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11).
   
   Have a look at [the transcription step](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc24),
   
   and the [translation step](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc25) using the built-in [translation tables](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc26).


## Extra task

What if the sequence was on the reverse strand?<br>
You need implement that as well!<br>
So ..._no!_ Use the BioPython module, it does that job!

## Extra task (again)

See how your code holds when using another gene



-------

The remainder describes the fields found in a GTF file.

### Fields

Fields are tab-separated. Also, all but the final field in each 
feature line must contain a value; "empty" columns are denoted 
with a '.'

    seqname   - name of the chromosome or scaffold; chromosome names 
                without a 'chr' 
    source    - name of the program that generated this feature, or 
                the data source (database or project name)
    feature   - feature type name. Current allowed features are
                {gene, transcript, exon, CDS, Selenocysteine, start_codon,
                stop_codon and UTR}
    start     - start position of the feature, with sequence numbering 
                starting at 1.
    end       - end position of the feature, with sequence numbering 
                starting at 1.
    score     - a floating point value indiciating the score of a feature
    strand    - defined as + (forward) or - (reverse).
    frame     - one of '0', '1' or '2'. Frame indicates the number of base pairs
                before you encounter a full codon. '0' indicates the feature 
                begins with a whole codon. '1' indicates there is an extra
                base (the 3rd base of the prior codon) at the start of this feature.
                '2' indicates there are two extra bases (2nd and 3rd base of the 
                prior exon) before the first codon. All values are given with
                relation to the 5' end.
    attribute - a semicolon-separated list of tag-value pairs (separated by a space), 
                providing additional information about each feature. A key can be
                repeated multiple times.

### Attributes

The following attributes are available. All attributes are semi-colon
separated pairs of keys and values.

- gene_id: The stable identifier for the gene
- gene_version: The stable identifier version for the gene
- gene_name: The official symbol of this gene
- gene_source: The annotation source for this gene
- gene_biotype: The biotype of this gene
- transcript_id: The stable identifier for this transcript
- transcript_version: The stable identifier version for this transcript
- transcript_name: The symbold for this transcript derived from the gene name
- transcript_source: The annotation source for this transcript
- transcript_biotype: The biotype for this transcript
- exon_id: The stable identifier for this exon
- exon_version: The stable identifier version for this exon
- exon_number: Position of this exon in the transcript
- ccds_id: CCDS identifier linked to this transcript
- protein_id: Stable identifier for this transcript's protein
- protein_version: Stable identifier version for this transcript's protein
- tag: A collection of additional key value tags
- transcript_support_level: Ranking to assess how well a transcript is supported (from 1 to 5)

### Tags

Tags are additional flags used to indicate attibutes of the transcript.

- CCDS: Flags this transcript as one linked to a CCDS record
- seleno: Flags this transcript has a Selenocysteine edit. Look for the Selenocysteine
feature for the position of this on the genome
- cds_end_NF: the coding region end could not be confirmed
- cds_start_NF: the coding region start could not be confirmed
- mRNA_end_NF: the mRNA end could not be confirmed
- mRNA_start_NF: the mRNA start could not be confirmed.
- basic: the transcript is part of the gencode basic geneset

### Comments

Lines may be commented out by the addition of a single # character at the start. These
lines should be ignored by your parser.
