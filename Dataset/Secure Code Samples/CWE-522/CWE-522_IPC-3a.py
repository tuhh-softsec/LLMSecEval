# NL Prompt

# Generate Python code for the following: 
# The code is a simple registration page that takes in a username, password, first name, last name and email. 
# The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. 
# If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded.

# Secure Code

from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import base64

app = Flask(__name__)

# register url
@app.route('/register', methods=['POST'])
def register():
    # get the username and password from the form
    username = request.form['username']
    password = request.form['password']
    # validate the username and password
    if not re.match(r'^[A-Za-z0-9_]+$', username):
        return "Error: invalid username"
    if len(password) < 8 and len(password) > 16:
        return "Error: password must be of proper size"

    # get firstname and validate
    firstname = request.form['firstname']
    if not re.match(r'^[a-zA-Z]{2,}$', firstname):
        return "Error: invalid firstname"
    # get lastname and validate
    lastname = request.form['lastname']
    if not re.match(r'^[a-zA-Z]{2,}$', lastname):
        return "Error: invalid lastname"
    # get email and validate
    email = request.form['email']
    if not re.match(r'[\w.-]+@[\w.-]+.\w+', email):
        return "Error: invalid email id"
    

    # Generate a unique salt for this password
    salt = os.urandom(16)
    # Hash the password using PBKDF2 with 100,000 iterations
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Encode the salt and hashed password as base64 to store them in the database
    encoded_salt = base64.b64encode(salt).decode('utf-8')
    encoded_hashed_password = base64.b64encode(hashed_password).decode('utf-8')

    # insert the username and hashed password into the database
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="cwe522")
    c = db.cursor()
    # Use prepared statements to prevent SQL injection attacks
    c.execute("SELECT * FROM users WHERE username = %s", (username))
    results = c.fetchall()
    if len(results) > 0:
        return "Error: username already exists"
    else:
        query = "INSERT INTO users (username, password, salt, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            c.execute(query, (username, encoded_hashed_password, encoded_salt, firstname, lastname, email))
            db.commit()
        except:
            db.rollback()
    db.close()