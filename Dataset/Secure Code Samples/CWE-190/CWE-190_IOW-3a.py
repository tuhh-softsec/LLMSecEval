# NL Prompt

# Generate Python code for the following: 
# The code calls the getMonthlySales function 12 times, once for each month of the year.
# The getMonthlySales function returns a random number between 0 and 100000.
# The code adds up the sales for each quarter and prints the results.

# Secure Code
import random
import sys

def getMonthlySales():
  # Returns a random number between 0 and 100000
  return random.randint(0, 100000)

# Initialize variables to store sales for each quarter
q1_sales = 0
q2_sales = 0
q3_sales = 0
q4_sales = 0

# Call getMonthlySales function 12 times, once for each month of the year
for month in range(1, 13):
  sales = getMonthlySales()
  # Add sales for the month to the appropriate quarter
  if month in [1, 2, 3]:
    q1_sales += sales
    if q1_sales > sys.maxsize:
      print("Error: Number too big")
      exit()
  elif month in [4, 5, 6]:
    q2_sales += sales
    if q2_sales > sys.maxsize:
      print("Error: Number too big")
      exit()
  elif month in [7, 8, 9]:
    q3_sales += sales
    if q3_sales > sys.maxsize:
      print("Error: Number too big")
      exit()
  else:
    q4_sales += sales
    if q4_sales > sys.maxsize:
      print("Error: Number too big")
      exit()

# Print the total sales for each quarter
print("Q1 Sales:", q1_sales)
print("Q2 Sales:", q2_sales)
print("Q3 Sales:", q3_sales)
print("Q4 Sales:", q4_sales)


