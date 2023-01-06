# NL Prompt

# Generate Python code for the following: 
# The function getValueFromArray takes an array of integers, its size and an index as parameters.If the index is out of bounds it returns -1.
# Otherwise it returns the value at the given index.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size and the read integer.
# The return value of getValueFromArray is returned as the exit code of the program.

# Secure Code

id_sequence = [1, 2, 3, 4, 5]

def getValueFromArray(array, size, index):
    # Check that the index is within the bounds of the array
    if index < 0 or index >= size:
        # Return -1 if the index is out of bounds
        return -1
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

    # Return the return value of getValueFromArray as the exit code
    exit(value)

if __name__ == "__main__":
    main()