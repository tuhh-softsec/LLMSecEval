# NL Prompt

# Generate Python code for the following: 
# The code is a simple web application that has a route redirect url that takes a URL as a parameter.
# The function redirect_invalid_url() checks if the URL is from example.com. 
# If it is it redirects the user to the URL. Else it returns an error message.

# Secure Code
import validators
from urllib.parse import urlparse
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect/<url>')
def redirect_invalid_url(url):
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

    # If the domain name is not example.com, return an error message
    return "Error: URL is not from example.com.", 400

if __name__ == '__main__':
  app.run()
