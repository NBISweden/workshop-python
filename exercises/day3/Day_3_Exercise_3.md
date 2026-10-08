# Day 3 exercise 3: working with data in python

The following are realistic scenarios from working with python in bioinformatics. Work methodically by:
- breaking down the question/problem into the smallest reasonable parts that you think you will be able to express in a function and create pseudocode
- refer to documentation, ask questions
- examine input data and explore it using python
- save your solution in a file and compare the output to example output in instruction

## 1. revisit day 2 exercise 1
In this exercise you were parsing a vcf file. Your colleague has asked that you write a python script that will print the line that was the solution for any given input vcf file.

- adapt the code to use the `with` keyword to open the file
- create at least 2 functions, it is OK if the functions are nested
- try to adapt your solution to use f-strings if you are not already using that
- optional: for a bit more challenge, find a way to return a helpful usage message when the executable is run without the input
- optional2: hard mode, the original suggested solution will crash if the code is run on a vcf file that doesn't contain the specific locus due to a ZeroDivisionError, adapt your script to deal with this situation and print something helpful to the user.

Expected output:
```sh
pixi run python exercises/day3/vcf_snooper.py downloads/genotypes_small.vcf
The frequency of the rs4988235 SNP is: 0.783
```

Make sure you can rename the file and get the same output:
```sh
❯ head -10000 downloads/genotypes_small.vcf > trunc_copy_genotypes.vcf
❯ pixi run python exercises/day3/vcf_snooper.py trunc_copy_genotypes.vcf
The frequency of the rs4988235 SNP is: 0.783
```

## 2. IMDB data parsing

Create a script that does the following:
1. Print number of movies per genre in the dataset `downloads/250.imdb`

2. Print average length of movies per genre?
3. (challenging) make a script that takes a genre as the first argument and an output filename as the second argument, print the top 10 highest rated movies along with their ratings to the specified output file in either CSV or TSV format.

### Example solutions and expected output

Try your own solution first, then compare your output to the examples below.

Question 1 reference implementation is in `exercises/day3/imdb_1.py`.

Expected output (`downloads/250.imdb`):
```text
action  31
adventure       55
animation       17
biography       25
comedy  46
crime   62
drama   182
family  24
fantasy 29
film-noir       7
historical      1
history 18
horror  5
music   3
musical 5
mystery 41
romance 24
sci-fi  28
sport   7
thriller        65
war     30
western 8
```

Question 2 reference implementation is in `exercises/day3/imdb_2.py`.

Expected output (`downloads/250.imdb`):
```text
action  138.5 min
adventure       132.5 min
animation       99.9 min
biography       149.9 min
comedy  113.0 min
crime   130.9 min
drama   133.9 min
family  104.4 min
fantasy 121.6 min
film-noir       103.4 min
historical      158.0 min
history 167.3 min
horror  118.6 min
music   144.0 min
musical 116.6 min
mystery 122.8 min
romance 122.0 min
sci-fi  126.1 min
sport   136.9 min
thriller        130.5 min
war     150.0 min
western 130.6 min
```

Question 3 reference implementation is in `exercises/day3/imdb_3.py`.

If run with genre `thriller`, expected terminal message:
```text
Wrote 10 movies to top10_thriller.tsv
```

Expected output file (`top10_thriller.tsv`):
```tsv
title	rating
The Dark Knight	9.0
Inception	8.8
Léon: The Professional	8.6
Se7en	8.6
The Silence of the Lambs	8.6
The Usual Suspects	8.6
The Departed	8.5
Rear Window	8.5
Memento	8.5
Drishyam	8.5
```