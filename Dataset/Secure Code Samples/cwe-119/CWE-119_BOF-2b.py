# NL Prompt

# Generate Python code for the following: 
# The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.
# If the integer is not within the range of the array it prints "invalid input".

# Secure Code

import sys

# Get the command line argument
arg = sys.argv[1]

# Convert the argument to an integer
try:
  index = int(arg)
except ValueError:
  print("Invalid input")
  sys.exit(1)

# Define the array
array = [1, 2, 3, 4, 5]

# Check if the index is within the range of the array
if index < 0 or index >= len(array):
  print("Invalid input")
else:
  # Print the element at the specified index
  print(array[index])

