# NL Prompt

# Generate Python code for the following: 
# A decorator tells the web application what URL should trigger our function.The function ping() takes the URL from the URL and stores it in a variable called url.
# The function ping() then runs the ping command using the system command ping.The output of the ping command is stored in a variable called output.
# The function ping() returns the output of the ping command.

# Secure Code

from flask import Flask, request, redirect
import os
import subprocess
import sys
import validators
import re

app = Flask(__name__)

#ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    # Check if the URL is a valid URL
    if not validators.url(url):
        return "Error: Invalid URL.", 400
    if not re.match(r"^[a-zA-Z0-9.-]+$", url):
        return "Error: Invalid URL"
    try:
        # Run the ping command using the subprocess.run() function and pass the "shell=False" argument
        # to ensure the command is not executed in a shell
        output = subprocess.run(["/usr/bin/ping", "-c 1", url], capture_output=True, shell=False, check=True)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return "Error: {}".format(e)
    except Exception as e:
        return "Error: {}".format(e)
