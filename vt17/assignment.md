---
menu: project
title: 'About your main assignment'
---

<blockquote class="task">

<p data-mark="Background"><b>Background</b>: With the emergence of
cheap full genome sequence technologies, there has been vast
improvements in our ability to detect genetic diseases prior to the
onset of the disease. Sometimes, there are known causative mutations
that can be the targets of genetic screens for the disease. This is
the case for Cystic fibrosis, a complex disease that leads to problems
with lung function, diabetes and causes infertility, among other
symptoms.</p>

<p> A set of mutations have been associated with this disease, on a
particular gene named the CFTR gene (short for Cystic Fibrosis
Transmembrane Conductance Regulator). This gene encodes an ion channel
protein acting in epithelial cells. Both amino-acid altering mutations
and premature stop-codons have been identified to cause the disease.
</p>

<hr/>

<p data-mark="Goal"><b>Goal</b>: In this assignment, you have access
to the human reference genome as well as the genome annotation. In
addition, you have full genome sequence data from five individuals
from a family at risk of carrying mutations related to the
disease.</p>

<p> Your task is to write a Python program that will extract the CFTR
gene, translate the gene sequence to its corresponding amino-acid
sequence and based on the inferred amino-acid sequence determine wether
any of the 5 individuals is affected.</p> 

</blockquote>

The main task is divided in several steps. Answer the following
questions first:

1. What is the length of the given DNA sequence?

2. How many genes are annotated in the GTF file?

3. What fraction of the chromosome is annotated as genes?

All the following tasks are now related to the particular gene with id
`ENSG00000001626` on chromosome `7`.

{:start="4"}
4. How many transcripts can this gene generate?

   <details><summary>Answer</summary><section>11</section></details>

5. What is the longest transcript in nucleotides?

   <details>
   <summary>Answer</summary>
   <section>
   <p>The transcript with id ENST00000003084 has 6132 bp and is the longest among 11 other transcripts</p>
   <p>Check its <a href="http://www.ensembl.org/Homo_sapiens/Transcript/Summary?db=core;g=ENSG00000001626;r=7:117465784-117715971;t=ENST00000003084">Ensembl data</a></p>
   <p>Notice that the last column in the GTF on the line defining that transcript should contain <code>protein_coding</code>.</p>
   </section>
   </details>

6. Fetch the DNA sequence for that gene

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the DNA file with the <code>with</code> statement and read it line by line.</p>
   <p>Ignore the first line and, in a loop, append each line to a list.</p>
   <p>Outside the loop, use the <code>join</code> function to concatenate the lines from the list.</p>
   <p><b>Avoid concatenation</b> <i>inside</i> the loop, as it is slow and wasting memory</p>
   </section>
   </details>

7. Fetch all the exons for that transcript (splicing)

   <details>
   <summary>Answer</summary>
   <section>
   <p>Your answer can be output to a file and compare to <a href="">that given file</a> (also <a href="https://www.ncbi.nlm.nih.gov/nuccore/NM_000492">available online</a>)</p>
   </section>
   </details>

8. What are the position of the `start_codon` and `stop_codon` from that transcript?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Check that the <code>start_codon</code> is <code>ATG</code>, and that the <code>stop_codon</code> corresponds to a proper stop codon</p>
   <p>Make your program throw a warning in case the transcript you are currently translating does not begin with a start-codon and end with a stop-codon</p>
   </section>
   </details>

9. Translate into amino-acids.

   <details>
   <summary>Tip</summary>
   <section>
   <p>The translation table is <a href="http://shawmst.org/biology/article/rna-translation-table/">depicted here</a>, and given to you in the utils.rna package</p>
   <p>You can output your results in different files and check the difference with the <a href="https://github.com/NBISweden/PythonCourse/tree/vt17/assignment/results">given results</a> or online <a href="http://www.uniprot.org/uniprot/A0A024R730.fasta">here</a> or <a href="https://www.ncbi.nlm.nih.gov/nuccore/NM_000492">here</a>.</p>
   <pre class="highlight"><code>diff filename-1 filename-2</code></pre>
   will output nothing when the files are identical.
   </section>
   </details>

1. Use [BioPython](http://biopython.org/wiki/Documentation) for (some of) the above tasks
   
   <details>
   <summary>Procedure</summary>
   <section>
   <p>Start by <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11">parsing a fasta file with BioPython</a>.</p>
   <p>Have a look at <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc24">the transcription step</a>,</p>
   <p>and the <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc25">translation step</a> using the built-in <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc26">translation tables</a>.</p>
   </section>
   </details>


### Extra tasks {#extra-task}

What if the sequence was on the reverse strand?<br>
You need implement that as well!<br>
So ..._no!_ Use the BioPython module, it does that job!

