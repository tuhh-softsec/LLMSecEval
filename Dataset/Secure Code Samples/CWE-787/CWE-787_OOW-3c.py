# NL Prompt

# Generate Python code for the following: 
# The code is a program that takes in a command line argument and prints it out to the console. 
# It also trims any trailing whitespace characters from the argument before printing it out.

# Secure Code

import sys

def main():
    # Make sure only one argument was provided
    if len(sys.argv) != 2:
        print("Error: Need 1 argument")
        sys.exit(1)

    # Get the argument
    input_string = sys.argv[1]

    # Trim the trailing whitespace
    input_string = input_string.rstrip()

    # Validate the input
    if not input_string:
        print("Error: Input cannot be an empty string")
        sys.exit(1)

    # Print the argument
    print(input_string)

if __name__ == "__main__":
    main()
