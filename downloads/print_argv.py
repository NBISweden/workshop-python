#!/usr/bin/env python
import sys

print(f"size of sys.argv = {len(sys.argv)}")
print(f"program_name = {sys.argv[0]}")

counter = 1
while counter < len(sys.argv):
    print(f"arg{counter} = {sys.argv[counter]}")
    counter += 1

