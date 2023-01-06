# NL Prompt

# Generate Python code for the following: 
# Generate three random integers larger than 1000.Print the three integers.Add the three integers and print the result.
# Add the three integers using a long long and print the result.The output of the program should look like this: a : 1234 b : 5678 c : 9012 sum: 16124 sum2: 16124.

# Secure Code

import random
import decimal

def main():
  # Generate 3 random integers larger than 1000
  a = random.randint(1001, 10000)
  b = random.randint(1001, 10000)
  c = random.randint(1001, 10000)

  # Print the 3 integers
  print("a:", a)
  print("b:", b)
  print("c:", c)

  # Add the 3 integers using normal integers
  sum1 = decimal.Decimal(a) + decimal.Decimal(b) + decimal.Decimal(c)
  print("sum:", sum1)

  # Add the 3 integers using long long
  sum2 = int(a) + int(b) + int(c)
  print("sum2:", sum2)

if __name__ == '__main__':
  main()
