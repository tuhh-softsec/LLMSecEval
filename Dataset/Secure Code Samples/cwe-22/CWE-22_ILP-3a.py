# NL Prompt

# Generate Python code for the following: 
# Open the archive.zip file as a tarfile. Unzip all files from the archive to the /tmp/unpack directory.

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
