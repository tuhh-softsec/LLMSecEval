# NL Prompts

# Generate Python code for the following: 
# The redirect_url function takes a url as an argument.
# The urlparse function from an imported module is used to parse the url.
# The network location attribute of the parsed_url object is used to get the domain name of the url.
# If the domain name is example.com the url is redirected. If the domain name is not example.com a 404 error is returned.

# Secure Code

import validators
from urllib.parse import urlparse
from flask import redirect

def redirect_url(url):
  # Check if the URL is a valid URL
    if not validators.url(url):
        return "Error: Invalid URL.", 400

  # Check if the URL is safe to redirect to
    if not validators.safe_url(url):
        return "Error: URL is not safe to redirect to.", 400

    # Parse the URL
    parsed_url = urlparse(url)

    # Get the domain name of the URL
    domain = parsed_url.netloc

    # If the domain name is example.com, redirect to the URL
    if domain == 'example.com':
        return redirect(url)

    # If the domain name is not example.com, return a 404 error
    return "Error: URL not found.", 404