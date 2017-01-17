# Tasks

* Find length of DNA.
* Find length of all genes.
* Compare what fraction of the Chr is annotated as genes.

# All tasks are related to gene "blabla"

* Fetch DNA from fasta for gene with id "ENSG00000001626"
* How many transcripts can this gene generate?

* Select the longest transcripts (answer: id ENST00000003084.10, length: 6132 bp)
Ensembl data: http://www.ensembl.org/Homo_sapiens/Transcript/Summary?db=core;g=ENSG00000001626;r=7:117465784-117715971;t=ENST00000003084

$9 should contain "protein_coding"

* Fetch all the exons for that transcript (splicing)
Answer: https://www.ncbi.nlm.nih.gov/nuccore/NM_000492

Transcript [117479963:117668665]

* Extract the start and stop codons from that transcript
** Check that the start_codon is ATG, and stop_codon is TTT 


* Translate to protein, using the given translation table.
Table: http://shawmst.org/biology/article/rna-translation-table/
or from BioPython

start_codon [117480095:117480097]
stop_codon  [117667106:117667108]

http://www.uniprot.org/uniprot/A0A024R730.fasta
https://www.ncbi.nlm.nih.gov/nuccore/NM_000492 (and look for CDS link)

====================================================================
What if the sequence was on the reverse strand?
Gotta implement that as well!
So ...no! Use the BioPython module, it does that job!

* Use the other gene with id



