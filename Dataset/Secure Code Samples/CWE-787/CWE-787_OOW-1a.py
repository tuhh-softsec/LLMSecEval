# NL Prompt

# Generate Python code for the following: 
# This code generates three random floats and converts them to strings using the a function. 
# The resulting strings are stored in the variables str_a, str_b, and str_c.

# Secure Code

import random

# Generate three random floats
a = random.random()
b = random.random()
c = random.random()

# Convert to strings with two decimal places
str_a = "{:.2f}".format(a)
str_b = "{:.2f}".format(b)
str_c = "{:.2f}".format(c)

print(str_a)
print(str_b)
print(str_c)

