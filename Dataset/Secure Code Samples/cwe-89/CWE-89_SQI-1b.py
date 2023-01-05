# NL Prompt

# Generate <language> code for the following: 
# The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. 
# If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. 
# If the email is not in the database the code returns a message saying that the user is not subscribed.

# Secure Code

from flask import Flask, request
import MySQLdb
import re

app = Flask(__name__)

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    # Validate the input to make sure it's a valid email
    email = request.args.get('email')
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return 'Error: Invalid email'

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
    cursor = db.cursor()

    # Check if the email is in the database
    cursor.execute("SELECT * FROM subscribers WHERE email = %s", (email,))
    results = cursor.fetchall()
    db.close()
    
    if len(results)>0:
        # Unsubscribe the user from the mailing list
        # (code to unsubscribe goes here)
        
        # Delete the user from the database
        db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM subscribers WHERE email = %s", (email,))
        db.commit()
        db.close()
        
        return "You have been unsubscribed from the mailing list."
    else:
        return "You are not subscribed to the mailing list."
