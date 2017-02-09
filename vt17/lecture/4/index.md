---
layout: vt17
menu: topics
title: "Using someone else's code"
---

Writing functions and modules is a way to structure you code, but it
is also naturally a way to avoid repeating the work. Someone else has
maybe written code that you could use.

In fact, there are already plenty of modules that come with Python
when you install it. Have a look at
the
[Python Module Index](https://docs.python.org/3.5/py-modindex.html).


# A small utility
{:.collapse-trigger}

This first part of today's class is a live code demo. We want to
create a small utility that parses a file and print the number of
lines, words and/or characters, depending on the given option, such
that a typical call would be:

```bash
$ mycounter filename --lines
```

If no option is given, the utility displays all three in a table like:

```
	Filename: <filename>
	|--- Lines ------ Words ---- Characters --|
	|    12      |     345    |    67890      |
	-------------------------------------------
```

The resulting code looks like:


```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def _work(filename,search = None):

    lines_counter, words_counter, chars_counter = 0,0,0

    with open(filename,'r',encoding='utf-8') as f:
        
        for line in f:
            
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue

            if search is None or search == '--lines':
                lines_counter += 1

            if search is None or search == '--words':
                words = line.split()
                words_counter += len(words)

            if search is None or search == '--characters':
                chars_counter += len(line) # no leading and trailing whitespaces, no \n

    # Outside the loop, I have now the counters ready.
    # Handling the display:

    if search == '--characters':
        print('{} contains {} characters'.format(filename, chars_counter) )

    if search == '--words':
        print('{} contains {} words'.format(filename, words_counter) )

    if search == '--lines':
        print('{} contains {} lines'.format(filename, lines_counter) )

    if search is None:
        sep = '-' * 64
        print('Filename:',filename.split('/')[-1])
        print(sep)
        print('|{:^20}|{:^20}|{:^20}|'.format('Lines','Words','Characters'))
        print(sep)
        print('|{:^20}|{:^20}|{:^20}|'.format(lines_counter,words_counter,chars_counter))
        print(sep)




def usage():
    print('''\
Usage: code.py <filename> [options]

Options are:
--------
--lines         displays the number of lines only
--words         displays the number of words only
--characters    displays the number of characters only

If no option is given, it displays all in a table like:

     
     Filename: <filename>
     -------------------------------------------
     |   Lines    |    Words   |  Characters   |
     -------------------------------------------
     |    12      |     345    |    67890      |
     -------------------------------------------

''')


if __name__ == '__main__':

    filename = None
    option = None
    
    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    if len(sys.argv) >= 3:
        option = sys.argv[2]

    if not filename or option not in ('--lines','--words','--characters',None):
        usage()
    else:        
        _work(filename, search = option) # option might be None

```

We now put that program in our `PATH` and rename it to `mycounter`.

Note the string formatting for the table. This is what we now
cover. Head to
the
[Format String Syntax](https://docs.python.org/3.5/library/string.html#format-string-syntax) webpage.

# Importing `math`
{:.collapse-trigger}

The
[`math` module](https://docs.python.org/3.5/library/math.html#module-math) provides
mathematical functions. For example, in order to use the cosinus and
sinus functions, you can import `math`, which contains their
implementation.

Given 2 points on a flat surface, with coordinates `(x1,y1)` and
`(x2,y2)`, define a function that calculates the distance between the
2 points.

Secondly, define a function that calculates the angle between the `X`
axis and the segment formed by the 2 points.

Finally, write a small test for the above functions.

# House Database
{:.collapse-trigger}

For the second example
of
[code written by someone else](https://github.com/NBISweden/PythonCourse/raw/vt17/homes/db.py) (yes,
yours truly :) ), we are given
a
[database containing information about Real Estate around Uppsala](https://github.com/NBISweden/PythonCourse/raw/vt17/homes/uppsala.sqlite).

The first step is to download the required files. We must then read
the documentation of that code. We don't know the internals, but there
are surely methods and new defined types (called `class`, but not part
of this course) that we can use for this
assignment. The [documentation](#db-documentation) is at the end of
this page.

What is the price of the cheapest house around a given center and
within 2 kilometers.  The center is given as both:

* latitude: 59.865795990339876
* longitude: 17.64583576202392


You can plot the results to an HTML file, which internally uses Google
Maps (so we'll have
to
[fetch an API key](https://developers.google.com/maps/documentation/javascript/get-api-key) first!). If
you do not have a Google account, or don't want to bother with the API
key, you can always content yourself with the `print` function.

## Another critieria

Change the criteria now, and find the most expensive house per square meters.

<img src="map.jpg" alt="An example of map" style="display:block;width:90%;margin:0 auto;box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.75);border-radius:1em;"/>


# Module documentation {#db-documentation}
{:.collapse-trigger}

The code to produce would typically start by importing the necessary
functions and classes from the `db` module.

```python
from db import HomeDB

# Initilizing the database
database = HomeDB('uppsala.sqlite')
database.connect()
selection = database.select('rooms > 1 and rooms < 3 and area > 58 and rent < 3000')
database.disconnect()

# Looping now through the selection
for home in selection:
	# Do something

# Then plot
```

The above code essentially initializes the database, fetches some
selection, based on some criteria, and plots the result on a map. Yes,
it's visual, it' fun.

<hr class="force" />

You can of course look at the documentation from the sourcecode
itself, using the `help` function.

```
$ python
>>> import db
>>> help(db.plot)
```


The plot function has a few keyword parameters and two first
positional arguments for the selection and Google API key.


```
plot(selection,
     google_key,
     output='selection.html',
     cheapest=None,
     zoom=12,
     latitude=59.83732598851705,
     longitude=17.64549846959149,
     radius=5000)
	

    Outputs the selection to map file. Section is a list of HomeEntry.
    The center is given by latitude and longitude and marked on the map with a blue marker.
    The map draws a radius around the center.
    When the cheapest is used, an extra green marker is ploted in the map.

    Note: this requires you to pass a Google Maps API key.
    You can fetch one here: https://developers.google.com/maps/documentation/javascript/get-api-key
```


For each home, it is possible to call the following functions:

<dl>
<dt><code>home</code>.get_location()</dt>
<dd>returns a pair (latitude,longitude) as a float tuple.</dd>

<dt><code>home</code>.get_price()</dt>
<dd>returns the price that home was sold for, in sek.</dd>

<dt><code>home</code>.get_area()</dt>
<dd>returns its surface in m<sup>2</sup>.</dd>
</dl>

<hr class="force" />

The
[haversine formula](https://en.wikipedia.org/wiki/Haversine_formula)
determines the great-circle distance between two points on a sphere
given their longitudes and latitudes. This will be useful for
filtering the selection using the radius.


```
$ python
>>> import db
>>> help(db.haversine)

Help on function haversine in module db:

haversine(lat1, lon1, lat2, lon2)
    Calculate the great circle distance (in m) between two points
    on the earth (specified in decimal degrees)
```
