---
menu: project
title: 'About your main assignment'
---

<blockquote class="task">
Given a <a
href="https://raw.githubusercontent.com/NBISweden/PythonCourse/vt17/assignment/data/Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz">Sequence
file</a> and a <a
href="https://raw.githubusercontent.com/NBISweden/PythonCourse/vt17/assignment/data/Homo_sapiens.GRCh38.87.gtf.gz">GTF
file</a>, your task is to implement a python program, that
extracts the protein from a particular transcript.
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
   <p>Check that the <code>start_codon</code> is <code>ATG</code>, and <code>stop_codon</code> is <code>TTT</code></p>
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

