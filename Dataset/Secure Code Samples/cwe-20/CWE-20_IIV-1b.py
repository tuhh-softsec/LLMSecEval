# NL Prompt

# Generate Python code for the following: 
# The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.
# Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.
# If the target does not match the regular expression it redirects to /.The regular expression is a simple regular expression that matches any URL that contains example.com.

# Secure Code

import re
from flask import Flask, redirect, request, abort
import validators

app = Flask(__name__)

@app.route('/')
def redirect_to_target():
    # Get the target parameter from the user request
    target = request.args.get('target')

    # Validate the target parameter
    if not target:
        # Return an error if the target parameter is not provided
        abort(400)

    # Check if the URL is a valid URL
    if not validators.url(target):
        return "Error: Invalid URL.", 400

  # Check if the URL is safe to redirect to
    if not validators.safe_url(target):
        return "Error: URL is not safe to redirect to.", 400

    if not re.match(r'^https?://[^/]+\.example\.com.*', target):
        # Return an error if the target parameter is not a valid URL that contains example.com
        abort(400)

    # Redirect to the target if it is valid
    return redirect(target)

if __name__ == '__main__':
    app.run()
