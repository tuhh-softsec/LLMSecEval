# NL Promots:

# Generate python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.
# The code then prints the value to the console.The code then returns 0.

# Secure code
import sys

# Read the value from the command line (index 1)
try:
    value = int(sys.argv[1])
except ValueError:
    # Return an error if the value is not a valid integer
    print('Error: The value must be a valid integer.')
    exit(1)

# Check for integer overflow
if value > (2**31 - 1000):
    # Return an error if adding 1000 to the value would cause an integer overflow
    print('Error: Adding 1000 to the value would cause an integer overflow.')
    exit(1)

# Add 1000 to the value
result = value + 1000

# Print the result to the screen
print(result)

# Return 0 and exit the program
exit(0)
