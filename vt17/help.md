---
menu: help
title: 'Python 3 - Cheat Sheet'
---

# Types
{:.collapse-trigger}

| Type  	| Example  	| Convert to type using |
|-----------|:---------:|:---------------------:|
| Integer  	|  0, 1, 100 	|  int() 	|
| Float  	|  0.0, .5, 10.453 	|  float() 	|
| String  	|  'hello' 	| str()  	|

Create your own type using `class`


# Iterating through list elements
{:.collapse-trigger}

```python
for item in aList:
	print('List item: ', item)
```
		
It is not necessary to iterate list items via their position.
You _rarely_ need to do:

```python
for i in range(len(aList)):
	print('List item: ', aList[i])
```

If you are looking for an element in a list and cannot find it, you can use the `else` clause.
For example, we are searching for the first integer in `aList` that is bigger than 10.

```python
aList = [ 1, 4, 7, 6, 3, 4, 32, 17, 18, 10, 8]
for item in aList:
	if item > 10:
		return item
else:
	return None
```

		
# Iterating through a dictionary
{:.collapse-trigger}

```python
for key in dictionary:
	print('Key item: ', key)
```

Same as

```python
for key in dictionary.keys():
	print('Key item: ', key)
```

For the values only

```python
for v in dictionary.values():
	print('Value item: ', v)
```

For both keys and values

```python
for k,v in dictionary.items():
	print('Key item :', k, ' | Value item: ', v)
```

# Read a file line by line
{:.collapse-trigger}

```python
with open("filename","r") as f:
	for line in f:
		print('Line: ', line)
```

The `with` statement takes care of closing the file in case an error occurs in the `for` loop.

# Defining a function 
{:.collapse-trigger}

```python
def functionName(arg1, arg2, arg3=None, arg4='', arg5=0):
	# body of the function
```

`arg1` and `arg2` are positioned arguments, required when calling the function.

`arg3`, `arg4`, `arg5` are named arguments with a default value (respectively `None`, the empty string, and the interger `0`)

# Importing a function from a module
{:.collapse-trigger}

```python
from moduleName import functionName
```

Or if we want to _rename_ locally the function:

```python
from moduleName import functionName as newName
```

# Testing a condition
{:.collapse-trigger}

We need boolean logic to compare values. We have of course < >, <=, >=, to compare integers, floats or even strings.
If we compare objects, Python will compare their size (by calling `__len__()`).

The comparator `==` and `!=` checks the _values_, while `is` checks
the id (ie _are the same object?_). Obviously, when `v1 is v2`, it
implies `v1 == v2`.

A condition can combine expressions with the above comparators, using
the logical `and` and `or` operators, and `not condition` is its
negation.


```python
if condition:
	print('Condition is true')
else:
	print('Condition is false')
```

We can pass an object as the condition. This is very convenient as Python will check if the object is "False".

False objects are:

* the keywords `None`, `False`,
* the values `0`, `0.0`,
* the empty string `''`,
* the empty list `[]`, the empty tuple `()`
* the empty dictionary `{}`, 

If you define your own class, you'll have to add the function
`__bool__()` (or `__len__()`, since Python defaults to `__len__` when
`__bool__` is not present)

For example, when calling a function where arguments have default values

```python
def functionName(arg1=None):
	
	if arg1:
		print('arg1 was None')
	
	# Body of the function
```
	  
# Catching errors
{:.collapse-trigger}

```python
try:
	#
	# Do something
	#
except ErrorName:
	print("An error of type ErrorName occured")

print('Continue after the error')
```
