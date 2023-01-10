# NL Prompt

# Generate <language> code for the following: 
# A decorator creates a mapping between the URL given as an argument and the function that follows it.The function hello() returns a string with the text Hello followed by the value of the variable username.
# The variable username is passed as an argument to the function hello().The escape() function converts special characters to HTML-safe sequences.The function hello() is called when a user navigates to the URL /hello/username".

# Secure Code

from flask import Flask, render_template, abort, escape
import re

app = Flask(__name__)

# Compile the regular expression pattern
username_pattern = re.compile("^[a-zA-Z0-9]+$")

# Bind the hello() function to the URL /hello/<username>
@app.route('/hello/<username>')
def hello(username):
    # Validate the username
    if not username_pattern.match(username):
        abort(400)
    username = escape(username)
    return "Hello {}!".format(username)

if __name__ == '__main__':
    app.run(debug=True)
