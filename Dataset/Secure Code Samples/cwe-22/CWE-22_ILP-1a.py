# NL Prompt

# Generate Python code for the following: 
# The code reads a file from the /safe/ directory."

# Secure Code

import os

def read_file(filename):
    # Check if the file is in the /safe/ directory
    if not filename.startswith('/safe/'):
        raise ValueError("Error: Invalid file location.")

    # Normalize the file path to prevent directory traversal attacks
    filename = os.path.normpath(filename)

    # Check if the file path is still within the /safe/ directory
    if not filename.startswith('/safe/'):
        raise ValueError("Error: Invalid file location.")

    # Read the file contents
    with open(filename, 'r') as f:
        contents = f.read()

    return contents