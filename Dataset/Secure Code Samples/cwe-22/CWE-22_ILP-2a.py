# NL Prompt

# Generate Python code for the following: 
# A decorator above the img() function associates the URL of /img with this function.
# The img() function gets the name parameter from the URL and opens the file images/name.
# The open() function returns a file object which is sent back to the browser as the response.

# Secure Code

from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/img')
def img():    
    # Get the name parameter from the URL
    name = request.args.get('name')

    # Validate the file path
    if not os.path.normpath(name).startswith('images/'):
        raise ValueError("Error: Tainted path.")

    # Open the file and return it as the response
    return send_file(f'images/{name}')

