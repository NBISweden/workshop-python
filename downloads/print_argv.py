#!/usr/bin/env python
import sys

print("size of sys.argv = ", len(sys.argv))
print("program_name = ", sys.argv[0])

counter = 1
while counter < len(sys.argv):
    print("arg" + str(counter) + " = ", sys.argv[counter])
    counter += 1

