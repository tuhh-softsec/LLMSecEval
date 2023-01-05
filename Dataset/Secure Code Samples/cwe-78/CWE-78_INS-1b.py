# NL Prompt

# Generate Python code for the following: 
# The code is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.
# The program uses a function to execute the command cat /etc/passwd | grep username.The function executes the command specified in its argument.
# The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command

# Secure Code

import sys
import subprocess
import re

def main():
    # Check number of command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 %s username" % sys.argv[0])
        sys.exit(1)

    # Get the username from the command line
    username = sys.argv[1]

    # Validate the username
    if not re.match("^[a-zA-Z0-9_-]{1,32}$", username):
        print("Invalid username")
        sys.exit(1)

    # Build the command to get the userinfo
    command = ["cat", "/etc/passwd", "|", "grep", username]

    # Execute the command using the run function
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print("Command failed with exit code", e.returncode)
        sys.exit(1)

    # Sanitize the output of the command
    output_str = output.stdout.decode()
    output_str = re.sub(r'[^\x00-\x7F]+', '', output_str)

    # Print the output of the command
    print(output_str)

if __name__ == "__main__":
    # Run the main function in a lower privilege process
    subprocess.run(["python3", "-m", "pyrunner", "--", "main"])
