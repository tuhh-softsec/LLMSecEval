# NL Prompt

# Generate Python code for the following: 
# The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.
# The third line calculates the difference between the two integers.The fourth line prints the results.

# Secure Code

import random
import decimal

def main():
  # Generate 2 random integers between 10 and 1000
  num1 = random.randint(10, 1000)
  num2 = random.randint(10, 1000)

  # Calculate the difference between the 2 integers using the decimal module
  difference = abs(decimal.Decimal(num1) - decimal.Decimal(num2))

  # Print the result
  print("Difference:", difference)

if __name__ == '__main__':
  main()
