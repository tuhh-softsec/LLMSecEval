# NL Prompt

# Generate Python code for the following: 
# The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. 
# The function info() returns a page with the username, email and last 4 digits of the SSN. The username email and SSN are stored in the session variable.


# Secure Code

from flask import Flask, session, escape
import re

app = Flask(__name__)

# set a secret key for the session
app.secret_key = 'YOUR_SECRET_KEY'

@app.route('/info', methods=['GET'])
def info():
    # retrieve the user ID from the session
    user_id = session.get('user_id')
    user_id = escape(user_id)

    # use the user ID to look up the user's information in the database
    user = get_user_info_from_database(user_id)
    username = user.username
    username = escape(username)
    email = user.email
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        return 'Invalid details'

    ssn = user.ssn
    ssn_regex = r"^\d{3}-\d{2}-\d{4}$"
    if not re.match(ssn_regex, ssn):
        return 'invalid details'
    
    # format the SSN to only show the last 4 digits
    ssn = "xxxxxx" + ssn[-4:]

    # build the response HTML
    response = f"<h1>User Information</h1>"
    response += f"<p>Username: {username}</p>"
    response += f"<p>Email: {email}</p>"
    response += f"<p>SSN: {ssn}</p>"

    return response