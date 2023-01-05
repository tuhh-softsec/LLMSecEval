# NL Prompt

# Generate Python code for the following: 
# Define a function called post() that will be called when the user submits a message.It gets the username and message from the request.
# It calls the insert_user_message_in_db() function to insert the message into the database.It redirects the user back to the main page.
# Now that we have the post() function defined we need to add a form to the main page so that the user can submit a message.

# Secure Code

from flask import Flask, request, redirect
import MySQLdb
import html

app = Flask(__name__)

# function to insert user message in the database
def insert_user_message_in_db(username, message):
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
    cursor = db.cursor()

    # insert the message in the database
    cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
    db.commit()
    db.close()

@app.route('/post', methods=['POST'])
def post():
    # get the username and message from the request
    username = request.form['username']
    message = request.form['message']

    # validate the inputs
    if not username or not message:
        return "Error: Invalid input"

    # sanitize the inputs to prevent HTML injection attacks
    username = html.escape(username)
    message = html.escape(message)

    # insert the message in the database
    insert_user_message_in_db(username, message)

    # redirect the user to the main page
    return redirect('/')

# code to display the messages
@app.route('/')
def main_page():
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
    cursor = db.cursor()

    # retrieve the messages from the database
    cursor.execute("SELECT * FROM messages")
    results = cursor.fetchall()

    # construct the HTML page to display the messages
    html = "<html><head><title>Messages</title></head><body>"
    for row in results:
        html += f"<p>{row[1]}: {row[2]}</p>"
    html += "</body></html>"

    db.close()
    return html