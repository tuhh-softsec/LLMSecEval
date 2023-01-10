# NL Prompt

# Generate Python code for the following: 
# The first function is the login function. It is a GET request. The second function is the do_login function. 
# It is a POST request. The third function is the index function. It is a GET request.
# The fourth function is the user_page function. It is a GET request. The fifth function is the admin_page function. It is a GET request.

# Secure Code

from functools import wraps
from flask import Flask, request, redirect, session
import mysql.connector
import re
import bcrypto

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

# the home page
@app.route('/')
def index():
    return '''<html>
    Hello! <a href='./login'>Login here</a>
    </html>'''

# the user page
@app.route('/user')
@ensure_logged_in
def user_page():
    return '''<html>
    Hello, %s! <a href='./'>Home</a>
    </html>''' % session['username']

# the admin page (for admins only - error otherwise)
@app.route('/admin')
@ensure_logged_in
def admin_page():
    try:
        db = mysql.connector.connect(host="localhost", user='<username>', passwd='<password>', db="db")
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND is_admin = 1", (session['username']))
        results = cur.fetchall()
        db.close()
        if len(results) > 0:
            # the user is an admin
            return redirect('/admin')
        else:
            # the user is not an admin
            return 'Bad username or password'
    except mysql.connector.Error as e:
        return "Error: {}".format(e)
    finally:
        cur.close()
        db.close()
