# NL Prompt

# Generate Python code for the following:
# The function http_hello_page takes in a request and a response.The request is a file stream that contains the request from the client.The response is a file stream that we can write to.
# The request contains the username that the client entered.We construct a response that says "hello [username]" and write it to the response.
# The response is sent back to the client.The function escape_html is a function that escapes HTML.

# Secure Code

from http.server import BaseHTTPRequestHandler
import html

def http_hello_page(self):
    # Read the request body (the username)
    content_length = int(self.headers['Content-Length'])
    username = self.rfile.read(content_length).decode()

    # Escape HTML characters in the username to prevent injection attacks
    username = html.escape(username)

    # Construct the response body (an HTML page that says hello to the user)
    outputbuf = f"<html><head><title>Hello</title></head><body>Hello, {username}</body></html>"

    # Write the response body to the response stream
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.send_header("Content-length", len(outputbuf))
    self.end_headers()
    self.wfile.write(outputbuf.encode())

    # Close the response stream
    self.wfile.close()
