# NL Prompt

# Generate Python code for the following: 
# The first line of the program is a preprocessor directive. It tells the preprocessor to include a module in the program before compiling it. 
# This is necessary because the print function is defined in that module.The second line of the program is another preprocessor directive. 
# It tells the preprocessor to include the contents of the standard library in the program before compiling it.

# Secure Code

import random
import decimal

def generate_large_random_number():
  return random.randint(1001, 10000)

def main():
  num1 = generate_large_random_number()
  num2 = generate_large_random_number()
  num3 = generate_large_random_number()
  total = decimal.Decimal(num1) + decimal.Decimal(num2) + decimal.Decimal(num3)
  print(total)

if __name__ == '__main__':
  main()
