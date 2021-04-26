#!/usr/bin/python3
"""
Given a number X and a large file that contains individual
numbers on each line (e.g 500GiB file), output the largest
X numbers, in descending order (highest first).

Usage:
  ./topX.py 10 <filename>

Output:
  A list of topX integers sorted in descending order.
"""

import logging
import sys

# Maintain topX numbers.
top = []

def open_file(filename):
  """Wrapper for opening the file."""
  return open(filename)

def populate_top(x, val):
  """Seed the top var with 10 initial numbers."""
  if len(top) < x:
    top.append(val)

def construct_top(top, val):
  """Construct the top list."""
  # Iterate through the current top and
  # maintain a list of ints sorted in ascending
  # order, this behaves like a priority queue.
  for index, num in enumerate(top):
      if val > num:
          top[index] = val
          top.sort()
          break

if __name__ == '__main__':
   # Check that 3 arguments are provided otherwise print help text and exit.
   if len(sys.argv) < 3:
     print(("Please check arguments, requires topX range and filename to be opened"
            "\n"
            "Example: ./topn.py 10 numbers.txt"))
     sys.exit()

   # Grab position arguments and assign them to initutive vars.
   x = int(sys.argv[1])
   filename = sys.argv[2]

   # Attempt to open the file, handling common errors.
   try:
       f = open_file(filename)
   except IOError:
       logging.exception("Given file name has produced an IOError.")
       sys.exit()
   else:
       # Read line by line to construct the topX list.
       for line in f:
           populate_top(x, int(line))
           construct_top(top, int(line))
       # Print the final topX list in descending order.
       print(sorted(top, reverse=True))
