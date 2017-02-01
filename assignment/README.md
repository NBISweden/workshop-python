You are given:
* a [Sequence file](data/Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz) and
* a [GTF file](data/Homo_sapiens.GRCh38.87.gtf.gz).

Your task is to implement a python program, that
extracts the protein from a particular transcript.

The task is divided in several steps. The GTF format uses particular [fields](data/gtf-format.md).

## Warm up

1. What is the length of the given DNA sequence?

2. How many genes are annotated in the GTF file?

3. What fraction of the chromosome is annotated as genes?

## The real deal

All the following tasks are now related to the particular gene with id `ENSG00000001626` on chromosome `7`.

4. How many transcripts can this gene generate?

5. What is the longest transcript in nucleotides?

   __Answer__: The transcript with id `ENST00000003084` has 6132 bp and is the longest among 11 other transcripts.
   
   You can have a look at its [Ensembl data](http://www.ensembl.org/Homo_sapiens/Transcript/Summary?db=core;g=ENSG00000001626;r=7:117465784-117715971;t=ENST00000003084).
   
   Notice that the last column in the GTF on the line defining that transcript should contain `protein_coding`.

6. Fetch the DNA sequence for that gene

7. Fetch all the exons for that transcript (splicing)

   __Answer__: Your answer can be output to a file and compare to [the result files](results/) (also [available online](https://www.ncbi.nlm.nih.gov/nuccore/NM_000492))

8. What are the position of the `start_codon` and `stop_codon` from that transcript?

9. Translate into amino-acids.

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

