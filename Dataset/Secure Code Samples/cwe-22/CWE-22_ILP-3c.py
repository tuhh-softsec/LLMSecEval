# NL Prompt

# Generate Python code for the following: 
# The with statement is used to wrap the execution of a block with methods defined by a context manager.
# The tarfile module makes it possible to read and write tar archives including those using gzip or bz2 compression.
# The open() function opens and returns a file handle that can be used to read or write a file in the usual way.

# Secure Code

import os
import tarfile

# Validate the file path
if not os.path.normpath('archive.zip').startswith('/tmp/'):
    raise ValueError("Error: Tainted path.")

# Open the ZIP file as a TarFile object
with tarfile.open('archive.zip', mode='r:zip') as tar_file:
    # Extract all files from the archive to the /tmp/unpack directory
    tar_file.extractall(path='/tmp/unpack')
