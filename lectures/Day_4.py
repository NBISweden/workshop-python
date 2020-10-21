# ---
# jupyter:
#   jupytext:
#     cell_markers: ''''''''
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% slideshow={"slide_type": "skip"}
from IPython.display import Image
from IPython.display import clear_output
from IPython.display import FileLink, FileLinks

# %% [markdown] slideshow={"slide_type": "slide"}
'''
## Introduction to

![title](img/python-logo-master-flat.png)

### with Application to Bioinformatics

#### - Day 4
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### TODAY

- Loops and functions, code structure
- Pandas - explore your data!


'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Review
- In what ways does the type of an object matter? Explain the output of:
'''

# %%
row = 'sofa|2000|buy|Uppsala'
fields = row.split('|')
price = fields[1]
if price == 2000:
    print('The price is a number!')
if price == '2000':
    print('The price is a string!')

# %%
print(sorted([ 2000,   30,   100 ]))
print(sorted(['2000', '30', '100']))
# Hint: is `'30' > '2000'`?

# %% [markdown]
'''
- How can you convert an object to a different type?
  - Convert to number: `'2000'` and `'0.5'` and `'1e9'`
  - Convert to boolean: `1`, `0`, `'1'`, `'0'`, `''`, `{}`
- We have seen these container types: **lists**, **sets**, **dictionaries**.
  What is their difference and when should you use which?
- What is a function?
  Write a function that counts the number of occurences of `'C'` in the argument string.
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### In what ways does the type of an object matter?
'''

# %%
row = 'sofa|2000|buy|Uppsala'
fields = row.split('|')
price = fields[1]
if price == 2000:
    print('The price is a number!')
if price == '2000':
    print('The price is a string!')

# %%
print(sorted([ 2000,   30,   100 ]))
print(sorted(['2000', '30', '100']))
# Hint: is `'30' > '2000'`?

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### In what ways does the type of an object matter?

- Each type store a specific type of information
    - `int` for integers,
    - `float` for floating point values (decimals),
    - `str` for strings,
    - `list` for lists,
    - `dict` for dictionaries.

- Each type supports different operations, functions and methods.

'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Each type supports different **operations**, functions and methods
'''
# %%
30 > 2000
# %%
'30' > '2000'
# %%
30 > '2000'

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Each type supports different operations, functions and **methods**
'''
# %%
'ACTG'.lower()
# %%
[1, 2, 3].lower()

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Convert to number: `'2000'` and `'0.5'` and `'1e9'`
'''

# %%
int('2000')

# %%
int('0.5')

# %%
int('1e9')

# %%
float('2000')

# %%
float('0.5')

# %%
float('1e9')


# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Convert to boolean: `1`, `0`, `'1'`, `'0'`, `''`, `{}`
'''

# %%
bool(1)
# %%
bool(0)
# %%
bool('1')
# %%
bool('0')
# %%
bool('')
# %%
bool({})

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Python and the truth: true and false values
'''

# %%
values = [1, 0, '', '0', '1', [], [0]]
for x in values:
    if x:
        print(repr(x), 'is true!')
    else:
        print(repr(x), 'is false!')


# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Converting between strings and lists
'''

# %%
list("hello")

# %%
str(['h', 'e', 'l', 'l', 'o'])

# %%
''.join(['h', 'e', 'l', 'l', 'o'])

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Container types, when should you use which?

- **lists**: when order is important
- **dictionaries**: to keep track of the relation between keys and values
- **sets**: to check for membership. No order, no duplicates.
'''

# %%
genre_list = ["comedy", "drama", "drama", "sci-fi"]
genre_list
# %%
genres = set(genre_list)
genres
# %%
genre_counts = {"comedy": 1, "drama": 2, "sci-fi": 1}
genre_counts
# %%
movie = {"rating": 10.0, "title": "Toy Story"}
movie

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### What is a function?

- A named piece of code that performs a specific task
- A relation (mapping) between inputs (arguments) and output (return value)

- Write a function that counts the number of occurences of `'C'` in the argument string.

'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Function for counting the number of occurences of `'C'`
'''

# %%
def cytosine_count(nucleotides):
    count = 0
    for x in nucleotides:
        if x == 'c' or x == 'C':
            count += 1
    return count

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Functions that `return` are easier to repurpose than those that `print` their result
'''

# %%
cytosine_count('catattac') + cytosine_count('tactactac')

# %%
def print_cytosine_count(nucleotides):
    count = 0
    for x in nucleotides:
        if x == 'c' or x == 'C':
            count += 1
    print(count)

print_cytosine_count('catattac') + print_cytosine_count('tactactac')

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Objects and references to objects
'''

# %%
list_A = ['red', 'green']
list_B = ['red', 'green']
list_B.append('blue')
print(list_A, list_B)

# %%
list_A = ['red', 'green']
list_B = list_A
list_B.append('blue')
print(list_A, list_B)

# %%
list_A = ['red', 'green']
list_B = list_A
list_A = []
print(list_A, list_B)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Objects and references to objects, cont.
'''

# %%
list_A = ['red', 'green']
lists = {'A': list_A, 'B': list_A}
print(lists)
lists['B'].append('blue')
print(lists)

# %%
list_A = ['red', 'green']
lists = {'A': list_A, 'B': list_A}
print(lists)
lists['B'] = lists['B'] + ['yellow']
print(lists)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Scope: global variables and local function variables
'''

# %%
movies = ['Toy story', 'Home alone']

# %%
def change_to_thriller():
    movies = ['Fargo', 'The Usual Suspects']

change_to_thriller()
print(movies)

# %%
def change_to_drama(movies):
    movies = ['Forrest Gump', 'Titanic']

change_to_drama(movies)
print(movies)

# %%
def change_to_scifi(movies):
    movies.clear()
    movies += ['Terminator II', 'The Matrix']

change_to_scifi(movies)
print(movies)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Keyword arguments
- A way to give a name explicitly to a function for clarity
'''

# %%
sorted(list('hello'), reverse=True)

# %%
attribute = 'gene_id "unknown gene"'
attribute.split(sep=' ', maxsplit=1)

# %%
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print('x=', end='')
print('1')

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Keyword arguments
- Order of keyword arguments do not matter

```python
open(file, mode='r', encoding=None) # some arguments omitted
```

- These mean the same:

```python
open('files/recipes.txt', 'w', encoding='utf-8')

open('files/recipes.txt', mode='w', encoding='utf-8')

open('files/recipes.txt', encoding='utf-8', mode='w')
```

'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Defining functions taking keyword arguments

- Just define them as usual:
'''

# %%
def format_sentence(subject, value, end):
    return 'The ' + subject + ' is ' + value + end

print(format_sentence('lecture', 'ongoing', '.'))

print(format_sentence('lecture', 'ongoing', end='.'))

print(format_sentence(subject='lecture', value='ongoing', end='...'))

# %%
print(format_sentence(subject='lecture', 'ongoing', '.'))

# %% [markdown]
'''
- Positional arguments comes first, keyword arguments after!
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Defining functions with default arguments
'''

# %%
def format_sentence(subject, value, end='.'):
    return 'The ' + subject + ' is ' + value + end

print(format_sentence('lecture', 'ongoing'))

print(format_sentence('lecture', 'ongoing', '...'))

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Defining functions with optional arguments

- Convention: use the object `None`
'''

# %%
def format_sentence(subject, value, end='.', second_value=None):
    if second_value is None:
        return 'The ' + subject + ' is ' + value + end
    else:
        return 'The ' + subject + ' is ' + value + ' and ' + second_value + end

print(format_sentence('lecture', 'ongoing'))

print(format_sentence('lecture', 'ongoing',
                      second_value='self-referential', end='!'))

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Small detour: Python's value for missing values: `None`

- Default value for optional arguments
- Implicit return value of functions without a `return`
- Something to initialize variable with no value yet
- Argument to a function indicating use the default value
'''

# %%
bool(None)

# %%
None == False, None == 0

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Comparing `None`

- To differentiate `None` to the other false values such as `0`, `False` and `''` use `is None`:
'''

# %%
counts = {'drama': 2, 'romance': 0}

counts.get('romance'), counts.get('thriller')

# %%
counts.get('romance') is None

# %%
counts.get('thriller') is None

# %% [markdown] slideshow={"slide_type": "slide"}
'''
- Python and the truth, take two
'''

# %%
values = [None, 1, 0, '', '0', '1', [], [0]]
for x in values:
    if x is None:
        print(repr(x), 'is None')
    if not x:
        print(repr(x), 'is false')
    if x:
        print(repr(x), 'is true')


# %% [markdown] slideshow={"slide_type": "slide"}
'''
**Controlling loops - `break`**
'''

# %% [markdown]
'''
```py
for x in lines_in_a_big_file:
    if x.startswith('>'):  # this is the only line I want!
        do_something(x)
```
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
...waste of time!
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
```py
for x in lines_in_a_big_file:
    if x.startswith('>'):  # this is the only line I want!
        do_something(x)
        break  # break the loop
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
**<center>break</center>**
<center>
<img src="img/break.png" alt="break" width="50%"/>
</center>

'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
**Controlling loops - `continue`**
'''

# %% [markdown]
'''
```py
for x in lines_in_a_big_file:
    if x.startswith('>'):  # irrelevant line
        # just skip this! don't do anything
    do_something(x)
```
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
```py
for x in lines_in_a_big_file:
    if x.startswith('>'):  # irrelevant line
        continue  # go on to the next iteration
    do_something(x)
```
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
```py
for x in lines_in_a_big_file:
    if not x.startswith('>'):  # not irrelevant!
        do_something(x)
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
**<center>continue</center>**
<center>
<img src="img/continue.png" alt="break" width="50%"/>
</center>
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
**Another control statement: pass** - the placeholder
'''


# %%
def a_function():
    # I have not implemented this just yet


# %%
def a_function():
    # I have not implemented this just yet
    pass

a_function()

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Exercise 1

- Notebook Day_4_Exercise_1  (~30 minutes)
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### A short note on code structure

- functions
- modules (files)
- documentation
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Remember?



#### Why functions?
- Cleaner code
- Better defined tasks in code
- Re-usability
- Better structure
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Why modules?

- Cleaner code
- Better defined tasks in code
- Re-usability
- Better structure

'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
- Collect all related functions in one file
- Import a module to use its functions
- Only need to understand what the functions do, not how
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Example: **sys**

```py
import sys

sys.argv[1]
```
or

```py
import imdb_parser as imdb
imdb.parse('250.imdb')
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Python standard modules

Check out the [module index](https://docs.python.org/3.6/py-modindex.html)
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
How to find the right module?

How to understand it?
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
How to find the right module?

- look at the module index
- search [PyPI](http://pypi.org)
- ask your colleagues
- search the web!
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
How to understand it?
'''

# %% slideshow={"slide_type": "fragment"}
import math

help(math)

# %% slideshow={"slide_type": "slide"}
dir(math)

# %% slideshow={"slide_type": "slide"}
help(math.sqrt)

# %% slideshow={"slide_type": "slide"}
math.sqrt(3)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Importing
'''

# %% slideshow={"slide_type": "-"}
import math

math.sqrt(3)

# %% slideshow={"slide_type": "fragment"}
import math as m
m.sqrt(3)

# %% slideshow={"slide_type": "fragment"}
from math import sqrt
sqrt(3)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Documentation and commenting your code


Remember `help()`?

Works because somebody else has documented their code!

'''


# %% slideshow={"slide_type": "slide"}
def process_file(filename, chrom, pos):
    for line in open(filename):
        if not line.startswith('#'):
            col = line.split('\t')
            if col[0] == chrom and col[1] == pos:
                print(col[9:])


# %% [markdown] slideshow={"slide_type": "fragment"}
'''
**?**
'''


# %% slideshow={"slide_type": "fragment"}
def process_file(filename, chrom, pos):
    """
    Read a vcf file, search for lines matching
    chromosome chrom and position pos.

    Print the genotypes of the matching lines.
    """
    for line in open(filename):
        if not line.startswith('#'):
            col = line.split('\t')
            if col[0] == chrom and col[1] == pos:
                print(col[9:])


# %% slideshow={"slide_type": "fragment"}
help(process_file)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
Your code may have two types of users:

- library users
- maintainers (maybe yourself!)
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
Write documentation for both of them!

- library users (docstrings):
  ```python
  """
  What does this function do?
  """
  ```
- maintainers (comments):
  ```python
  # implementation details
  ```
'''


# %% slideshow={"slide_type": "skip"}
def process_file(filename, chrom, pos):
    """Read a vcf file, search for lines matching chromosome chrom and position pos.

    Print the genotypes of the matching lines.
    """
    for line in open(filename):
        if not line.startswith('#'):  # skip comments
            columns = line.split('\t')  # file is tab separated
            # Check if chrom and pos match
            if col[0] == chrom and col[1] == pos:
                # genotype starts at column index 9
                print(col[9:])


# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Documentation:
'''

# %% [markdown]
'''
- At the beginning of the file

   ```python
   """
   This module provides functions for...
   """
   ````
'''

# %% [markdown]
'''
- For every function

    ```python
    def make_list(x):
        """Returns a random list of length x."""
        pass
    ```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Comments:
'''

# %% [markdown]
'''
 - Wherever the code is hard to understand


'''

# %% [markdown]
'''
```py
my_list[5] += other_list[3]  # explain why you do this!
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Read more:

https://realpython.com/documenting-python-code/

https://www.python.org/dev/peps/pep-0008/?#comments

'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Formatting

'''

# %%
title = 'Toy Story'
rating = 10
print('The result is: ' + title + ' with rating: ' + str(rating))

# %%
# f-strings (since python 3.6)
print(f'The result is: {title} with rating: {rating}')

# %%
# format method
print('The result is: {} with rating: {}'.format(title, rating))

# %%
# the ancient way (python 2)
print('The result is: %s with rating: %s' % (title, rating))

# %% [markdown]
'''
Learn more from the Python docs: https://docs.python.org/3.4/library/string.html#format-string-syntax
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Exercise 2


```py
pick_movie(year=1996, rating_min=8.5)
The Bandit
pick_movie(rating_max=8.0, genre="Mystery")
Twelve Monkeys
```

- Notebook Day_4_Exercise_2
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Pandas
'''

# %% [markdown]
'''
Library for working with tabular data
- comma separated (csv)
- tab separated (tsv)
- ...

Data analysis, graph plotting...
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Pandas
'''

# %% [markdown] slideshow={"slide_type": "-"}
'''

<center>
    <div class="output_subarea output_html rendered_html output_result">
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>circumference</th>
              <th>height</th>
            </tr>
            <tr>
              <th>age</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td> <td>2</td> <td>30</td>
            </tr>
            <tr>
              <td>2</td> <td>3</td> <td>35</td>
            </tr>
            <tr>
              <td>3</td> <td>5</td> <td>40</td>
            </tr>
            <tr>
              <td>4</td> <td>10</td> <td>50</td>
            </tr>
          </tbody>
        </table>
    </div>
</center>
'''

# %% [markdown] slideshow={"slide_type": "-"}
'''
<center>
  <img src="img/pandaplot.png" alt="plot" width=30%/>
</center>
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Pandas - a short overview
'''

# %%
import pandas as pd

# %%
help(pd)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Orange tree data

- `Orange_1.tsv`:

```
age   circumference  height
1        2             30
2        3             35
3        5             40
4        10            50
```
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth = pd.read_table('../downloads/Orange_1.tsv', index_col=0)


# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Dataframes
'''

# %%
tree_growth

# %% [markdown] slideshow={"slide_type": "-"}
'''
- One index (in this case `age`)
- A bunch of colums (in this case `circumference` and `height`)
- A bunch of rows (identified by their index)
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.columns

# %% slideshow={"slide_type": "fragment"}
tree_growth.index

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Exploring the data - picking a column
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.circumference

# %% [markdown]
'''
```py
dataframe.columnname
dataframe['columnname']
```
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.height

# %% slideshow={"slide_type": "fragment"}
tree_growth.circumference.max()

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Exploring the data - picking a row
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.loc[4]

# %% [markdown]
'''
`dataframe.loc[row_name]`
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Reading data

```python
dataframe = pandas.read_table(filepath, index_col=N)`
dataframe.columnname
dataframe.loc[row_name]
```
'''

# %% slideshow={"slide_type": "slide"}
tree_growth = pd.read_table('../downloads/Orange_1.tsv', index_col=0)
tree_growth

# %% slideshow={"slide_type": "fragment"}
tree_growth.height


# %%
tree_growth.loc[2]

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Many trees!

- `Orange.tsv`
```
Tree    age circumference
1     118       30
1     484       58
1     664       87
1    1004      115
...
2     118       33
2     484       69
...
```
'''

# %% slideshow={"slide_type": "slide"}
tree_growth = pd.read_table('../downloads/Orange.tsv', index_col=0)
tree_growth

# %% slideshow={"slide_type": "slide"}
tree_growth.index

# %%
tree_growth.columns

# %% slideshow={"slide_type": "skip"}
tree_growth.circumference.min()

# %% slideshow={"slide_type": "skip"}
tree_growth.circumference.max()

# %% slideshow={"slide_type": "slide"}
tree_growth.age

# %% slideshow={"slide_type": "fragment"}
tree_growth.age.values

# %% slideshow={"slide_type": "slide"}
tree_growth.age.unique()

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
Works like a normal list:
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.age.unique()[0]

# %% slideshow={"slide_type": "fragment"}
len(tree_growth.age.unique())

# %% [markdown]
'''
#### Columns

`dataframe.columnname`

- Methods:
`.max()`, `.min()`, `unique()`, `.values`, `.mean()`, `.sum()`...
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Selecting parts of the table
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.circumference   # selecting a column

# %% slideshow={"slide_type": "fragment"}
tree_growth.loc[2]  # selecting rows with index 2

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
```py
# select all rows that fullfills a criteria:
tree_growth.loc[ criteria ]
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Selecting parts of the table
'''

# %% [markdown]
'''
Find the data points where the tree is younger than 200 years!
'''

# %% [markdown]
'''
- Find *rows*  => use `tree_growth.loc[]`
'''

# %% [markdown]
'''
- Select these based on the value of column age => `tree_growth.age`
'''

# %%
# The answer...

# %% slideshow={"slide_type": "fragment"}
young = tree_growth.loc[tree_growth.age < 200]
young

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Exercises

```py
tree_growth.loc[ tree_growth.age < 200 ]
```
'''

# %% slideshow={"slide_type": "slide"}
import pandas as pd

tree_growth = pd.read_table('../downloads/Orange.tsv',index_col=0)

# %% slideshow={"slide_type": "fragment"}
max_c = tree_growth.circumference.max()

print(max_c)

# %% slideshow={"slide_type": "fragment"}
tree_growth.loc[tree_growth.circumference == max_c]

# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Plotting
'''

# %% [markdown]
'''
```py
df.columnname.plot()
```
'''

# %% slideshow={"slide_type": "fragment"}
orange_1 = pd.read_table('../downloads/Orange_1.tsv')
orange_1.circumference.plot()

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting

What if no plot shows up?

```py
%pylab inline   # jupyter notebooks
```
or
```py
import matplotlib.plot as plt

plt.show()
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting - many trees
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
- Plot a bar chart
'''

# %% slideshow={"slide_type": "fragment"}
tree_growth.plot(kind='bar')

# %% slideshow={"slide_type": "slide"}
tree_growth.plot(kind='bar', figsize=(12, 12), fontsize=12)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting

- Plot a line graph
'''

# %% slideshow={"slide_type": "fragment"}
# Starting with tree number 1
tree1 = tree_growth.loc[1]

# %%
tree1

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting

- Plot a graph:
```py
dataframe.plot(kind="line", x=..., y=...)
```
'''

# %% slideshow={"slide_type": "slide"}
tree1.plot(x='age', y='circumference',
           fontsize=14, figsize=(12,10))

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting

- Plot a graph:
```py
dataframe.plot(kind="line", x="..", y="...")
```
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
Let's plot all the trees!
'''

# %% slideshow={"slide_type": "slide"}
tree_growth.plot(kind='line', x='age', y='circumference',
                 figsize=(12, 10), fontsize=14)

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
:(
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting

- Plot a graph:
```py
dataframe.plot(kind="scatter", x="..", y="...")
```
'''

# %%
tree_growth.plot(kind='scatter', x='age', y='circumference',
                 figsize=(12, 10), fontsize=14)

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting

What about the lines?
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
- Group the table by the index (make subtrees)
- Get one board to plot all the lines
- Draw them one by one
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
```py
dataframe.groupby([what])
```
'''

# %% [markdown] slideshow={"slide_type": "fragment"}
'''
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
```
'''

# %% [markdown] slideshow={"slide_type": "slide"}
'''
#### Plotting, several lines
'''

# %% slideshow={"slide_type": "fragment"}
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for index, subtree in tree_growth.groupby(['Tree']):
    subtree.plot(x='age', y='circumference', kind='line',
                 ax=ax,
                 fontsize=14, figsize=(12,10))


# %% [markdown] slideshow={"slide_type": "slide"}
'''
### Exercise 5

- Read the `Orange_1.tsv`
    - Print the height column
    - Print the data for the tree at age 2
    - Find the maximum circumference
    - What tree reached that circumference, and how old was it at that time?

- Use Pandas to read IMDB
    - Explore it by making graphs
'''

