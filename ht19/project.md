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
several mutations associated with this disease. The gene
CFTR (short for Cystic Fibrosis Transmembrane Conductance
Regulator) encodes an ion channel protein acting in epithelial cells
and is encoded on chromosome 7 of the human genome.
CFTR carries several non-synonymous genetic variants, some of which leading to 
premature stop codons that are known to cause the disease.</p>

<hr/>

<p data-mark="Goal"><b>Goal</b>: In this assignment, you have access
to the human reference genome (chromosome 7) as well as the full genome annotation. In
addition, you have genome sequence data of chromosome 7 from five individuals
from a family at risk of carrying mutations related to the
disease.</p>

<p> Your task is to write a Python program that will extract the correct transcript from the CFTR gene, translate the gene sequence to its corresponding amino-acid sequence and based on the reference amino-acid sequence determine whether any of the five given individuals is affected.</p>

<p> Download the lecture slides from <a href="https://nbisweden.github.io/workshop-python/ht19/404.md">here</a>.</p>

</blockquote>

# Download the appropriate files {#download-files}

The main task is divided into several steps. The first step is to download
the reference sequence file and the appropriate reference annotation file from the Ensembl database:

Human reference DNA for chromosome 7 (`fasta` format):
- [Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz](ftp://ftp.ensembl.org/pub/release-93/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz)

Human reference annotation file (`GTF` format):
- [Homo_sapiens.GRCh38.93.gtf.gz](ftp://ftp.ensembl.org/pub/release-93/gtf/homo_sapiens/Homo_sapiens.GRCh38.93.gtf.gz)

After downloading the files, read up on how the files are structured.

Some of the tasks involve outputting long sequences. To make sure they are correct, use the <code>utils.check_answers</code> package (from the downloads folder from the <a href="https://nbisweden.github.io/workshop-python/ht19/topics">course topics</a> website):
<pre class="highlight"><code>from utils import check_answers</code></pre>

# Warmup {#warmup}

1. What is the length of chromosome 7 on the reference sequence?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the reference fasta file and read it line by line.</p>
   <p>In a loop, ignore the first line and get the length of each following line.</p>
   <p>Don't forget to remove the trailing newline character from each line.</p>
   <p>Sum up all the lengths you found.</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Chromosome 7 has 159,345,973 base pairs.</p>
   </section>
   </details>


2. How many genes are annotated in the GTF file?

   <details>
   <summary>Tip</summary>
   <section>
   <p>You need to understand the structure of a GTF (gene transfer format) file to solve the task.</p>
   <p>Here, you can find a <a href="https://github.com/NBISweden/PythonCourse/blob/ht19/assignment/data/gtf-format.md">short description</a> of the different (tab-delimited) fields of a GTF file.</p>
   <p>You can also do a <a href="https://www.google.com/search?ei=bHWDXcz-EY2Fk74PjqiZqAU&q=gene+transfer+format&oq=gene+transfer+format&gs_l=psy-ab.3..0j0i30j0i8i30.12939.16095..16355...4.3..0.146.1128.11j4......0....1..gws-wiz.......0i71j0i7i30j0i7i10i30j0i8i7i30j0i8i7i10i30j0i7i5i30j0i13j0i13i30.BS3cF3GTV7g&ved=0ahUKEwjM5O6z8tzkAhWNwsQBHQ5UBlUQ4dUDCAo&uact=5">search online</a>.</p>
   <p>Once you are done reading up on the file format, count all features of type `gene`.</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>There are 58,395 genes annotated in the GTF file.</p>
   </section>
   </details>


# Architect a method {#method}

All the following tasks are related to the CFTR gene.

In the annotation file (the GTF file), the CFTR gene has the
id `ENSG00000001626` on chromosome `7`.


1. How many transcripts can the CFTR gene generate?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Again, think about the structure of the GTF file.</p>
   <p>Open the GTF file.</p>
   <p>In a loop, count all `transcript` features for the gene.</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>This gene can produce 11 different transcripts.</section>
   </details>

2. Which of these transcripts is the longest transcript in nucleotides?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the GTF file.</p>
   <p>Fetch the start and stop positions for each transcript of the gene to calculate their lengths.</p>
   <p>Keep in mind that sequence numbering starts at 1 in the GTF file format.</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>The transcript with the id ENST00000003084 is the longest of 11 transcripts and spans 188,703 bases.</p>
   </section>
   </details>

3. Fetch the DNA sequence for that transcript.

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the reference file.</p>
   <p>In a loop, ignore the first line and append each line to a list, removing the trailing newline character.</p>
   <p>Outside the loop, use the <code>join</code> function to concatenate the lines from the list.</p>
   <p><b>Avoid concatenation</b> <i>inside</i> the loop, as it is slow and wastes memory.</p>
   <p>Extract the start and stop positions of the transcript similar to task 2 to fetch the DNA sequence, but think about where the index starts from.</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Write your results to a file and compare it to the correct result using <code>check_answers.ex3("resultsFile")</code>.</p>
   <p>The entire sequence can be also found <a href="https://github.com/NBISweden/PythonCourse/blob/ht19/assignment/results/transcript.ncbi.fasta">here</a>.</p>
   </section>
   </details>

4. Fetch all the exons for that transcript, spliced together to one sequence

   <details>
   <summary>Tip</summary>
   <section>
   <p>First you need to save the start and stop positions of all exons of that transcript.</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Write your results to file and compare with <code>check_answers.ex4(resultsFile)</code> </p>
   <p>The correct sequence can be found <a href="https://github.com/NBISweden/PythonCourse/blob/ht18/assignment/results/mrna.ncbi.fasta">here</a></p>
   </section>
   </details>

5. What are the position and sequence of the `start_codon` and `stop_codon` from that transcript?

   <details>
   <summary>Note</summary>
   <section>
   <p>Check that the <code>start_codon</code> is <code>ATG</code>, and that the <code>stop_codon</code> corresponds to a proper stop codon</p>
   <p>Make your program print a warning message in case the transcript does not begin with a start-codon and end with a stop-codon</p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Position of start codon is 117.480.095</p>
   <p>Position of stop codon is 117.667.106</p>
   </section>
   </details>

6. Translate the above sequence into amino-acids, using an implementation of the translation table from <a href="https://github.com/NBISweden/PythonCourse/tree/ht18/assignment"><code>utils.rna</code> package</a>.

   <details>
   <summary>Tip</summary>
   <section>
   <p>Use start codon position to start translating from</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Write your results to file and compare with <code>check_answers.ex6(resultsFile)</code> </p>
   <p>The correct sequence can be found <a href="https://github.com/NBISweden/PythonCourse/blob/ht18/assignment/results/protein.ncbi.fasta">here</a></p>
   </section>
   </details>


<hr />

# Find the patients at risk {#main-task}

We are reaching the goal for this assignment!

A mutation in the transcript ENST00000003084 causes a premature stop codon to be introduced into the aminoacid sequence. This creates a truncated protein, causing cystic fibrosis.
Using the python program you have designed above, compare the reference sequence to the sequences of the following 5 patients
([patient-1](https://github.com/NBISweden/PythonCourse/raw/ht18/assignment/data/Patient1.fa.gz),
[patient-2](https://github.com/NBISweden/PythonCourse/raw/ht18/assignment/data/Patient2.fa.gz),
[patient-3](https://github.com/NBISweden/PythonCourse/raw/ht18/assignment/data/Patient3.fa.gz),
[patient-4](https://github.com/NBISweden/PythonCourse/raw/ht18/assignment/data/Patient4.fa.gz),
and
[patient-5](https://github.com/NBISweden/PythonCourse/raw/ht18/assignment/data/Patient5.fa.gz))
to determine which one is carrying a mutation in the CFTR gene, causing a truncated protein.

There might be several.

# Extra task {#extra-task}

1. Use [BioPython](http://biopython.org/wiki/Documentation) for (some of) the above tasks

   <details>
   <summary>Procedure</summary>
   <section>
   <p>Start by <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11">parsing a fasta file with BioPython</a>.</p>
   <p>and the <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc25">translation step</a> using the built-in <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc26">translation tables</a>.</p>
   </section>
   </details>

<!---
# Solution {#main-task}

Here are some possible solutions to the assignment. There are of course many correct solutions, we only present one of the alternatives.

[Notebook](http://nbviewer.jupyter.org/github/NBISweden/workshop-python/blob/ht18/assignment/Solutions_project.ipynb)  
[Standalone script](https://raw.githubusercontent.com/NBISweden/workshop-python/ht18/assignment/findTruncations.py)
-->
