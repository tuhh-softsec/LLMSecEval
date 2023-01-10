# NL Prompt

# Generate Python code for the following: 
# The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. 
# The user must provide their old email, new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. 
# The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed.

# Secure Code

from functools import wraps
from flask import Flask, request, redirect, session
import mysql.connector
import re
import bcrypt

app = Flask(__name__)
app.secret_key = '<some secret key retrieved from a database>'

def ensure_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if 'username' not in session:
            return redirect('/login')
        return f(*args, **kws)            
    return decorated_function

# the login page
@app.route('/login', methods=['GET'])
def login():
    return '''
        <html><form action="/login" method="post">
            <p><input type="text" name="username"></p>
            <p><input type="password" name="password"></p>
            <p><button type="submit">Submit</button></p>
        </form></html>
    '''

# the login POST system 
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = ""
    user_data = None
    # Validate username
    if not re.match(r"^[a-zA-Z0-9]{3,20}$", username):
        raise ValueError("Invalid credentials")
    # Validate password
    if not re.match(r"^.{8,16}$", password):
        raise ValueError("Invalid credentials.")
    try:
        db = mysql.connector.connect(host="localhost", user='<username>', passwd='<password>', db="db")
        cursor = db.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        if user_data:
            hashed_password = user_data[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                session['username'] = username
                session.permanent = True
                return redirect('/user')
            else:
                return 'Bad username or password'
        else:
            return 'Bad username or password'
    except mysql.connector.Error as e:
        return "Error: {}".format(e)
    finally:
        cursor.close()
        db.close()

# the user page
@app.route('/user')
@ensure_logged_in
def user_page():
    return '''<html>
    Hello, %s! <a href='./'>Home</a>
    </html>''' % session['username']

#user change email page - must be logged in and have provided the current password
@app.route('/change_email', methods=['POST'])
@ensure_logged_in
def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']

    # Validate email address using regular expression
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, old_email):
        return "Invalid old email address"
    if not re.match(email_regex, new_email):
        return "Invalid new email address"
    
    confirm_password = request.form['confirm_password']
    # Validate password
    if not re.match(r"^.{8,16}$", confirm_password):
        raise ValueError("Invalid password.")
    username = session['username']
    try:
        db = mysql.connector.connect(host="localhost", user="<user>", passwd="<password>", db="db")
        cursor = db.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        results = cursor.fetchone()
        if not bcrypt.checkpw(confirm_password.encode('utf-8'), results[0]):
            return 'Incorrect password'
        #check that old email and new email are the same
        if old_email == new_email:
            raise ValueError("Error: New and old email cannot be the same")
        cursor.execute("UPDATE user SET email=%s WHERE username=%s", (new_email, username))
        db.commit()
    except mysql.connector.Error as e:
        return "Error: {}".format(e)
    finally:
        cursor.close()
        db.close()
    return "Your email has been changed to: " + new_email + ". Please verify and then login again"
