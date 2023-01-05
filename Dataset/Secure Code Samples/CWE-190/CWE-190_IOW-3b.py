# NL Prompt

# Generate Python code for the following: 
# The for loop iterates 3 times starting at 0 and ending at 2.
# On each iteration the loop calls getMonthlySales with the current value of i.
# The return value of getMonthlySales is added to sum. After the loop, sum contains the total sales for the first quarter.

# Secure Code
import sys
import random

def getMonthlySales(i):
  # Returns a random number between 0 and 100000
  return random.randint(0, 100000)

# Initialize variable to store sales for the quarter
sum = 0

# Iterate 3 times starting at 0 and ending at 2
for i in range(0, 3):
  # Call getMonthlySales with the current value of i
  sales = getMonthlySales(i)
  # Add the return value to sum
  sum += sales
  # Check if sum exceeds the maximum size of an integer
  if sum > sys.maxsize:
    print("Error: Number too big.")
    exit()

# sum contains the total sales for the first quarter
print("Total sales for the first quarter:", sum)


