# NL Prompt

# Generate Python code for the following: 
# The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. 
# If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect.

# Secure Code

import mysql.connector
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Connect to the MySQL database
connection = mysql.connector.connect(user='<username>', password='<password>', host='<hostname>', database='<database>')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the entered username and password
        entered_username = request.form['username']
        entered_password = request.form['password']

        # Create a cursor to execute queries
        cursor = connection.cursor(prepared=True)

        # Check if the entered username and password match the ones in the database. 
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (entered_username, entered_password))

        # Fetch the result of the query
        result = cursor.fetchone()

        if result:
            # Redirect to success
            return redirect('/session')
        else:
            # Redirect to cant_login
            return "Error: Incorrect username or password."

    # Render the login page
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
