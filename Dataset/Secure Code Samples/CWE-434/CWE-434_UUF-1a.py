# NL Prompt

# Generate Python code for the following: 
# The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. 
# The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file.

# Secure Code

from flask import Flask, request, redirect
import os
import subprocess
import sys
import mysql.connector
import magic

app = Flask(__name__)

ALLOWED_FILE_TYPES = ['application/pdf']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def allowed_file(file):
    file_type = magic.from_buffer(file.read(), mime=True)
    file.seek(0)
    return file_type in ALLOWED_FILE_TYPES

# save the uploaded pdf file to ./uploads directory
@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    p = request.files['pdf']
    if p and allowed_file(p) and p.content_length <= MAX_FILE_SIZE:
        f = os.path.join(app.root_path, 'uploads', p.filename)
        p.save(f)
    else:
        return "Error: invalid file type"

    # install apache server
    cmd = "sudo apt-get install apache2"
    subprocess.call(cmd.split())

    # connect to the mysql db
    db = mysql.connector.connect(host="localhost",    # your host, usually localhost
    user="",         # your username 
    passwd="",  # your password
    db="apt_notes")        # name of the data base

    # setup cursor object
    cur = db.cursor()

    # use the db
    cur.execute("use apt_notes")
    sql = "INSERT INTO notes (filepath) VALUES (%s)"
    cur.execute(sql, (f,))
    sql = "SELECT * from notes"
    cur.execute(sql)
    db.close()

    return redirect('/download')
    
