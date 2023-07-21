from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
rows = int(input())
for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")

    print()

for i in range(rows - 2, -1, -1):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")

    print()
