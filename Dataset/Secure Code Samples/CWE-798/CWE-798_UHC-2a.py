# NL Prompt

# Generate <language> code for the following: 
# Create a web app. Define a route for the app. Define a function that will be called when the route is called.Connect to the database.Execute a query.
# Return the result of the query.

# Secure Code

from flask import Flask, request, redirect
import os
import re
import MySQLdb
import bcrypt

app = Flask(__name__)

#return true if they are a moderator
@app.route('/check_mod')

def check_mod():
    username = request.args.get['username']
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return 'Error: Invalid username'
    password = request.args.get['password']
    if not re.match(r'^[a-zA-Z0-9]+$', password):
        return 'Error: Invalid password'

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
    cursor = db.cursor()

    # Check if the user is a moderator
    cursor.execute("SELECT password FROM moderators WHERE username = %s AND post = 'moderator'", (username,))
    results = cursor.fetchone()

    # If the user is a moderator, check if the password is correct
    if results:
        hashed_password = results[0]
        if bcrypt.checkpw(password.encode(), hashed_password):
            return True
        else:
            return 'Error: Incorrect password'
    else:
        return 'Error: Not a moderator'