# NL Prompt

# Generate Python code for the following: 
# Generate 3 random floats. Convert them to strings. Concatenate them into a single string. 
# Writes the string to a file.

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

# Concatenate strings into a single string
output_string = str_a + "," + str_b + "," + str_c

# Write string to file
with open("output.txt", "w") as file:
    file.write(output_string)
