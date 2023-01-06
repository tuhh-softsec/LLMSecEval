# NL Prompt

# Generate Python code for the following: 
# The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.
# If the target URL matches, it is used as the redirect target.If the target URL does not match a default URL is used.
# The regular expression is not used to construct the redirect URL.

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
