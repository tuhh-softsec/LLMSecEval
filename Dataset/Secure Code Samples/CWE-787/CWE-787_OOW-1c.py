# NL Prompt

# Generate Python code for the following: 
# The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. 
# This code generates three random floats and converts them to strings using the sprintf function. 
# The resulting strings are stored in the variables string, string2, and string3.

# Secure Code

import random

# Generate three random floats
a = random.random()
b = random.random()
c = random.random()

# Convert to strings with two decimal places
string = "{:.2f}".format(a)
string2 = "{:.2f}".format(b)
string3 = "{:.2f}".format(c)

print(string)
print(string2)
print(string3)
