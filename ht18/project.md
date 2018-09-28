---
menu: project
title: 'About your main assignment'
---

<blockquote class="task">

<p data-mark="Background"><b>Background</b>: For many diseases with
known causative mutations, screening methods have been developed to
detect whether people have a high risk of becoming sick, even before
the onset of the actual disease.</p>

<p> Over the last few years, the cost of full genome sequencing has
gone down so that, in some cases, it might be cheaper to collect the
complete genome sequence of patients with a high risk of carrying
variants associated with the disease, rather than using targeted
screening procedures.</p>

<p> Cystic fibrosis is a complex disease, where patients often
manifest the following symptoms: problems with lung functions,
diabetes and infertility. From a genetic point of view, there are
several mutations associated with this disease. In particular, the
CFTR gene (short for Cystic Fibrosis Transmembrane Conductance
Regulator) encodes an ion channel protein acting in epithelial cells,
and carries several non-synonymous genetic variants, with alterations
leading to premature stop codons, that are known to cause the
disease.</p>

<hr/>

<p data-mark="Goal"><b>Goal</b>: In this assignment, you have access
to the human reference genome as well as the genome annotation. In
addition, you have full genome sequence data from five individuals
from a family at risk of carrying mutations related to the
disease.</p>

<p> Your task is to write a Python program that will extract the CFTR
gene, translate the gene sequence to its corresponding amino-acid
sequence and based on the reference amino-acid sequence determine
whether any of the five given individuals is affected.</p>

</blockquote>

# Fetch the appropriate files {#fetch-files}

The main task is divided in several steps. The first step is to fetch
the reference sequence file (in `fasta` format) and the appropriate reference annotation
file (in `GTF` format) from
the [Ensembl database](http://www.ensembl.org/info/data/ftp/index.html).

The CTFR gene is located on chromosome `7`. After downloading the files, read up on how the files are structured.

Human reference DNA for chromosome 7 (fasta):
- Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz

Human GTF annotation file:
- Homo_sapiens.GRCh38.93.gtf.gz

# Warmup {#warmup}

1. What is the length of chr7 on the reference sequence??

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the reference fasta file and read it line by line.</p>
   <p>Ignore the first line and, in a loop, get the length of each line (from which you remove the trailing newline character).</p>
   <p>Sum up all the lengths you found.</p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>Chromosome 7 has 159.345.973 base pairs.</p>
   </section>
   </details>


2. How many genes are annotated in the GTF file?

   <details>
   <summary>Tip</summary>
   <section>
   <p>You need to understand the structure of a GTF-formatted file.</p>
   <p>The GTF format uses several tab-delimited fields, for which we give you a <a href="https://github.com/NBISweden/PythonCourse/blob/ht17/assignment/data/gtf-format.md">short a description</a>.</p>
   <p>Alternatively, you can <a href="https://en.wikipedia.org/wiki/Gene_transfer_format">search online</a>.</p>
   <p>Then, only count entries of type gene</p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>There are 58.395 genes annotated in the GTF file</p>
   </section>
   </details>


# Architect a method {#method}

All the following tasks are now related to the CTFR gene.

In the annotation file (from the Ensembl database), that gene has the
id `ENSG00000001626` on chromosome `7`.


3. How many transcripts can this gene generate?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Again, think about the structure of the GTF file</p>
   </section>
   <summary>Answer</summary>
   <section>This gene can produce 11 different transcripts</section>
   </details>

4. What is the longest transcript in nucleotides?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Use start and stop positions for each transcript of the gene</p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>The transcript with id ENST00000003084 is the longest among 11 other transcripts, and spans 188.703 bases</p>
   </section>
   </details>

5. Fetch the DNA sequence for that transcript

   <details>
   <summary>Tip</summary>
   <section>
   <p>Similarly to step 1 from the Warmup, open the reference file.</p>
   <p>Ignore the first line and, in a loop, append each line to a list.</p>
   <p>Remember to strip the trailing newline character.</p>
   <p>Outside the loop, use the <code>join</code> function to concatenate the lines from the list.</p>
   <p><b>Avoid concatenation</b> <i>inside</i> the loop, as it is slow and wasting memory</p>
   <p>Use the start and stop positions extracted from the transcript, but think about where the index starts from</p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>The entire sequence can be found here</p>
   </section>
   </details>

6. Fetch all the exons for that transcript, spliced together to one sequence

   <details>
   <summary>Tip</summary>
   <section>
   <p>First you need to save the start and stop positions of all exons of that transcript.</p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>The correct sequence can be found here<a href="https://raw.githubusercontent.com/NBISweden/PythonCourse/ht17/assignment/results/mrna.ncbi.fasta">that given result</a> (also <a href="https://www.ncbi.nlm.nih.gov/nuccore/NM_000492">available online</a>)</p>
   </section>
   </details>

7. What are the position and sequence of the `start_codon` and `stop_codon` from that transcript?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Check that the <code>start_codon</code> is <code>ATG</code>, and that the <code>stop_codon</code> corresponds to a proper stop codon</p>
   <p>Make your program print a warning message in case the transcript does not begin with a start-codon and end with a stop-codon</p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>Position of start codon is 117.480.095</p>
   <p>Position of stop codon is 117.667.106</p>
   </section>
   </details>

8. Translate into amino-acids, using an implementation of the <a href="http://shawmst.org/biology/article/rna-translation-table/">translation table</a> from <a href="https://github.com/NBISweden/PythonCourse/tree/ht17/assignment"><code>utils.rna</code> package</a>.

   <details>
   <summary>Tip</summary>
   <section>
   <p>Use start codon position to start translating from</p>
   <p></p>
   </section>
   <summary>Answer</summary>
   <section>
   <p>You can output your results in different files and check the difference with the <a href="https://raw.githubusercontent.com/NBISweden/PythonCourse/ht17/assignment/results/protein.ncbi.fasta">given result</a> or online <a href="http://www.uniprot.org/uniprot/A0A024R730.fasta">here</a> or <a href="https://www.ncbi.nlm.nih.gov/nuccore/NM_000492">here</a>.</p>
   <pre class="highlight"><code>diff filename-1 filename-2</code></pre>
   will output nothing when the files are identical.
   <p>Moreover, have a look at the <a href="https://docs.python.org/3.5/library/stdtypes.html#ranges"><code>range</code> function</a>, which can take an extra <code>step</code> parameter.</p>
   </section>
   </details>


<hr />

# Find the patients at risk {#main-task}

We are reaching the goal for this assignment!

Using the python program you have designed above, find which one of
the following 5 patients
([patient-1](https://github.com/NBISweden/PythonCourse/raw/ht17/assignment/data/Patient1.fa.gz),
[patient-2](https://github.com/NBISweden/PythonCourse/raw/ht17/assignment/data/Patient2.fa.gz),
[patient-3](https://github.com/NBISweden/PythonCourse/raw/ht17/assignment/data/Patient3.fa.gz),
[patient-4](https://github.com/NBISweden/PythonCourse/raw/ht17/assignment/data/Patient4.fa.gz),
and
[patient-5](https://github.com/NBISweden/PythonCourse/raw/ht17/assignment/data/Patient5.fa.gz))
carries a mutation on the CFTR gene, that can cause cystic fibrosis.

There might be several.

# Extra tasks {#extra-task}

1. Use [BioPython](http://biopython.org/wiki/Documentation) for (some of) the above tasks

   <details>
   <summary>Procedure</summary>
   <section>
   <p>Start by <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11">parsing a fasta file with BioPython</a>.</p>
   <p>Have a look at <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc24">the transcription step</a>,</p>
   <p>and the <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc25">translation step</a> using the built-in <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc26">translation tables</a>.</p>
   </section>
   </details>

2. What if the sequence was on the reverse strand? You need implement that as well!

  <details>
  <summary>Tip</summary>
  <section>
  So ..._no!_ Use the BioPython module, it does that job!
  </section>
  </details>