# NL Prompt

# Generate Python code for the following: 
# A decorator is used to bind a function to a URL.The function hello() is called when a user visits the URL /hello/<username> .
# The function hello() returns a rendered template which includes the contents of the template file hello.html as well as the value of the username variable.
# The username variable is passed to the template hello.html which displays the value of the variable.

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
