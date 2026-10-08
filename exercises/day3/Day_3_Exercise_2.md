# Day 3 Exercise 2: executable scripts

## 1. make a python script that greets its user on the command line
```py
from sys import argv
def myFun(i):
    return <?>
print(myFun(<?>))
```
should run like this:
```sh
pixi run python myScript.py myName
# OUTPUT: hello myName
```
## 2. make your script have 2 functions that do different things depending on how the script is called
hint: you can test items in argv using `if argv[1] == 'something': ...` 