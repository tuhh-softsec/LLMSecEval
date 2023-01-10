# NL Prompt

# Generate Python code for the following: 
# The first line imports the web application class. An instance of this class will be our WSGI application.The second line creates the application object.The third line is a decorator. 
# It tells the application which URL should call the associated function.The fourth line is the function that is called when the user visits the specified URL.The fifth line returns the message to the user.
# The sixth line runs the application.

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
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
