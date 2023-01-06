# NL Prompt

# Generate Python code for the following: 
# The code is a function that takes in an index value and returns the value at that index in the array id_sequence.
# The function first prompts the user for an index value.Then the function checks if the index value is in bounds. 
# If it is the function returns the value at the index in id_sequence.If the index value is not in bounds the function returns 0.

# Secure Code

id_sequence = [1, 2, 3, 4, 5]

def getValueFromArray(array, size, index):
    # Check that the index is within the bounds of the array
    if index < 0 or index >= size:
        # Return -1 if the index is out of bounds
        return 0
    # Return the value at the given index
    return array[index]

def main():
    # Read an integer from the standard input
    try:
        index = int(input())
    except ValueError:
        # Return an error if the input is not a valid integer
        print('Error: The input must be a valid integer.')
        exit(1)

    # Call the getValueFromArray function
    value = getValueFromArray(id_sequence, len(id_sequence), index)
    print(value)

    # Return 0
    return 0

if __name__ == "__main__":
    main()