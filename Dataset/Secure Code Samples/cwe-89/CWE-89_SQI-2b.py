# NL Prompt

# Generate Python code for the following: 
# The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.
# The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page.

# Secure Code

from flask import Flask, request, redirect
import mysql.connector
import re

USER_NAME = '' # read from a config file
PASSWORD = '' # read from a config file
HOST_NAME = '' # read from a config file
app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    # Validate stock name
    if not re.match(r"^[a-zA-Z0-9]{3,20}$", stock_name):
        return "Invalid stock name"
    stock_quantity = request.form['stock_quantity']
    if not stock_quantity.isdigit() or not int(stock_quantity) > 0:
        return "Invalid stock quantity"
    username = request.form['username']
    if not re.match(r"^[a-zA-Z0-9]{3,20}$", username):
        return "Invalid user name"

    # insert the buy order in the database
    db = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD, db="db")
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO Orders(Username,Stock_Name,Stock_Quantity) VALUES (%s,%s,%s)", (username,stock_name,stock_quantity,))
        db.commit()
        return redirect('/stock_view')
    except mysql.connector.Error as e:
        return "Error: {}".format(e)
    finally:
        cursor.close()
        db.close()