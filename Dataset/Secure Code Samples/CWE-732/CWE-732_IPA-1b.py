# NL Prompt

# Generate Python code for the following: 
# The code opens a file called important_config and writes the string important_config to it.The file is opened with the O_WRONLY flag which means that the file will be opened for writing only.
# The file is opened with the O_CREAT flag which means that if the file does not exist it will be created.The file is opened with the S_IRUSR|S_IWUSR flags.

# Secure Code

import os

# File name
file_name = "important_config"

# File permissions (readable and writable by the owner)
file_permissions = os.S_IRUSR | os.S_IWUSR

# File flags (create and truncate if it exists, write only)
file_flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY

# Open the file
fd = os.open(file_name, file_flags, file_permissions)

# Close the file
os.close(fd)
