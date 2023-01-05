# NL Prompt

# Generate Python code for the following: 
# The user enters the username and password in the login page. 
# The username and password are sent to the login function. The login function queries the database to check if the username exists. 
# If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. 
# If the password is incorrect it returns.

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

        # If there is a match, log the user in and redirect them to the dashboard page
        if result:
            redirect_url = '/'
            # Redirect to dashboard page
        else:
            # Redirect back to the login page
            redirect_url = '/login'

        # Close the cursor
        cursor.close()

    return redirect(redirect_url)

if __name__ == '__main__':
    app.run()
