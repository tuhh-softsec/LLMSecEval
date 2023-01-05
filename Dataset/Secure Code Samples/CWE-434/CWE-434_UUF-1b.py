# NL Prompt

# Generate Python code for the following: 
# There is a form in an html page that allows the user to upload a pdf file. There is a web server that is running on the user's localhost. 
# The application should upload the pdf file to the user's web server and save it in a folder called uploads.

# Secure Code

from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb
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
    p = request.files.get('pdf')
    if p and allowed_file(p) and p.content_length < MAX_FILE_SIZE:
        try:
            p.save('uploads/' + p.filename)
        except Exception as e:
            return "Error: {}".format(e)
    else:
        return "Error: invalid file type"

    return redirect('/download')
