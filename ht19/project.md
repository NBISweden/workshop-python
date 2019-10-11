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
from a family at risk of carrying mutations related to the disease.</p>

<p> Your task is to write a Python program that will extract a disease-causing transcript from the CFTR gene, translate the gene sequence to its corresponding amino-acid sequence and based on the reference amino-acid sequence determine whether any of the five given individuals is affected.</p>

<p> Download the lecture slides from <a href="https://github.com/NBISweden/workshop-python/raw/gh-pages/ht19/lecture/Project.pdf">here</a>.</p>

</blockquote>

# Download the appropriate files {#download-files}

The main task is divided into several steps. The first step is to download
the reference sequence file and the appropriate reference annotation file from the Ensembl database:

Human reference DNA for chromosome 7 (`fasta` format):
- [Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz](ftp://ftp.ensembl.org/pub/release-93/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna_sm.chromosome.7.fa.gz)

Human reference annotation file (`GTF` format):
- [Homo_sapiens.GRCh38.93.gtf.gz](ftp://ftp.ensembl.org/pub/release-93/gtf/homo_sapiens/Homo_sapiens.GRCh38.93.gtf.gz)

If you are not familiar with the file formats, read up online on how the files are structured. For example, <a href="https://github.com/NBISweden/PythonCourse/blob/ht19/assignment/data/gtf-format.md">here</a> you can find a short description of the different (tab-delimited) fields of a GTF file.

Some of the tasks involve outputting long sequences. To make sure they are correct, use the <code>utils.check_answers</code> package (from the downloads folder from the <a href="https://nbisweden.github.io/workshop-python/ht19/topics">course topics</a> website). You can import it that way:
<pre class="highlight"><code>from utils import check_answers</code></pre>
More detailed instructions are given with each task that uses the package.

# Warmup {#warmup}

1. What is the length of chromosome 7 on the reference sequence?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the reference fasta file and read it line by line.</p>
   <p>In a loop, ignore the first line and get the length of each following line.</p>
   <p>Don't forget to remove the trailing newline character from each line.</p>
   <p>Sum up all the lengths you found.</p>
   <p></p>
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
   <p>You need to understand the structure of a GTF (gene transfer format) file for this project. Take your time and read up on the file format if you are not sure how to solve this task.</p>
   <p>To get the number of genes, open the GTF file and read it line by line.</p>
   <p>In a loop, count all features of type <code>gene</code>.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>There are 58,395 genes annotated in the GTF file.</p>
   </section>
   </details>


# Architect a method {#method}

All following tasks are related to the CFTR gene.

In the annotation file (the GTF file), the CFTR gene has the id `ENSG00000001626` on chromosome `7`.


1. How many transcripts can the CFTR gene generate?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Again, think about the structure of the GTF file.</p>
   <p>Open the GTF file.</p>
   <p>In a loop, count all <code>transcript</code> features for the gene.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>The CFTR gene can produce 11 different transcripts.</section>
   </details>

2. Which of these transcripts is the longest transcript in nucleotides?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the GTF file.</p>
   <p>Fetch the start and stop positions for each transcript of the CFTR gene to calculate its length.</p>
   <p>Keep in mind that sequence numbering starts at 1 in the GTF file format.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>The transcript with the id <code>ENST00000003084</code> is the longest of 11 transcripts and spans 188,703 bases.</p>
   </section>
   </details>

3. Fetch the DNA sequence for that transcript.

   <details>
   <summary>Tip</summary>
   <section>
   <p>Open the reference fasta file.</p>
   <p>In a loop, ignore the first line and append each line to a list, removing the trailing newline character.</p>
   <p>Outside the loop, use the <code>join</code> function to concatenate the lines from the list to get the reference sequence. Avoid concatenation inside the loop, as it is slow and wastes memory.</p>
   <p>Extract the start and stop positions of the longest transcript to fetch its DNA sequence from the reference sequence, but think about where the index starts from.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Write your results to a file and compare it to the correct result using <code>check_answers.ex3("resultsFile.txt")</code>.</p>
   <p>The entire sequence can also be found <a href="https://github.com/NBISweden/PythonCourse/blob/ht19/assignment/results/transcript.ncbi.fasta">here</a>.</p>
   </section>
   </details>

4. Fetch the DNA sequences of all exons for that transcript, spliced together to one sequence.

   <details>
   <summary>Tip</summary>
   <section>
   <p>First, you need to save the start and stop positions of all exons of the longest transcript.</p>
   <p>Then you can use a similar loop to the one you used in task 3 to extract the DNA sequence of each exon.</p>
   <p>Finally, you need to concatenate the DNA sequences of all exons.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Write your results to a file and compare it to the correct result using <code>check_answers.ex4("resultsFile.txt")</code>.</p>
   <p>The correct sequence can also be found <a href="https://github.com/NBISweden/PythonCourse/blob/ht18/assignment/results/mrna.ncbi.fasta">here</a>.</p>
   </section>
   </details>

5. What are the start positions and sequences of the `start_codon` and `stop_codon` for that transcript?

   <details>
   <summary>Tip</summary>
   <section>
   <p>Find the <code>start_codon</code> and <code>stop_codon</code> features of the longest transcript in the GTF file, including the start positions of the start- and stop-codon.</p>
   <p>Check that the <code>start_codon</code> has the sequence <code>ATG</code>, and that the <code>stop_codon</code> corresponds to a proper stop codon.</p>
   <p>Make your program print a warning message in case the transcript does not begin with a start-codon and end with a stop-codon.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>The start codon has the sequence <code>ATG</code> and starts at position 117,480,095.</p>
   <p>The stop codon has the sequence <code>TAG</code> and starts at position 117,667,106.</p>
   </section>
   </details>

6. Translate the above sequence of all exons into amino acids, using an implementation of the translation table from the <code>utils.rna</code> package (from the downloads folder from the <a href="https://nbisweden.github.io/workshop-python/ht19/topics">course topics</a> website).

   <details>
   <summary>Tip</summary>
   <section>
   <p>Translate the DNA sequence of the concatenated exons into amino acids from the start codon position of the transcript on.</p>
   <p></p>
   </section>
   </details>
   <details>
   <summary>Answer</summary>
   <section>
   <p>Write your results to a file and compare it to the correct result using <code>check_answers.ex6("resultsFile.txt")</code> </p>
   <p>The correct sequence can also be found <a href="https://github.com/NBISweden/PythonCourse/blob/ht18/assignment/results/protein.ncbi.fasta">here</a>.</p>
   </section>
   </details>


<hr />

# Find the patients at risk {#main-task}

We are reaching the goal for this assignment!

A mutation in the transcript ENST00000003084 causes a premature stop codon to be introduced into the amino acid sequence. This creates a truncated protein, causing cystic fibrosis.
Use the python code you have written to solve the tasks above and extend it to compare the reference genome sequence of chromosome 7 to the sequences of the following 5 patients in `fasta` format
([Patient1.fa.gz](https://github.com/NBISweden/PythonCourse/raw/ht19/assignment/data/Patient1.fa.gz),
[Patient2.fa.gz](https://github.com/NBISweden/PythonCourse/raw/ht19/assignment/data/Patient2.fa.gz),
[Patient3.fa.gz](https://github.com/NBISweden/PythonCourse/raw/ht19/assignment/data/Patient3.fa.gz),
[Patient4.fa.gz](https://github.com/NBISweden/PythonCourse/raw/ht19/assignment/data/Patient4.fa.gz),
and [Patient5.fa.gz](https://github.com/NBISweden/PythonCourse/raw/ht19/assignment/data/Patient5.fa.gz))
to determine which of them are carrying a mutation in the CFTR gene that causes a truncated protein.

<hr />

# Extra task {#extra-task}

1. Use [BioPython](http://biopython.org/wiki/Documentation) to parse the fasta file and to translate DNA nucleotides into amino acids.

   <details>
   <summary>Tip</summary>
   <section>
   <p>Check the BioPython tutorial on how to <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc11">parse a fasta file</a> with BioPython.</p>
   <p>Read up on the built-in <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc25">translation method</a> and the BioPython <a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc26">translation tables</a>.</p>
   </section>
   </details>

<!---
# Solution {#main-task}

Here are some possible solutions to the assignment. There are of course many correct solutions, we only present some of the alternatives.

[solutions I (notebook)](http://nbviewer.jupyter.org/github/NBISweden/workshop-python/blob/ht19/assignment/Solutions_project.ipynb)  
[solutions II (standalone script)](https://raw.githubusercontent.com/NBISweden/workshop-python/ht19/assignment/findTruncations.py)
-->
