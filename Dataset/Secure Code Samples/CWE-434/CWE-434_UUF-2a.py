# NL Prompt

# Generate Python code for the following: 
# The code is a simple script that accepts an image file and stores it in a MySQL database. 

# Secure Code

from flask import Flask, request, redirect
import base64
import MySQLdb
import magic

app = Flask(__name__)

ALLOWED_FILE_TYPES = ['image/jpeg', 'image/png']

def allowed_file(file):
    file_type = magic.from_buffer(file.read(), mime=True)
    file.seek(0)
    return file_type in ALLOWED_FILE_TYPES

@app.route('/img/upload')
def upload_image():
    img_file = request.files.get('img')
    if img_file and allowed_file(img_file) and img_file.content_length <= 1024 * 1024:
        img_name = img_file.filename
        img_data = img_file.read()
        img_b64 = base64.b64encode(img_data).decode('utf-8')
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user="", #username
                             passwd="", #password
                             db="my_database")
        cursor = db.cursor()
        sql = "INSERT INTO images (img_name, img_base64) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (img_name, img_b64))
            db.commit()
            db.close()
            return '{"status":"success", "code":""}'
        except Exception as e:
            return '{"status":"error", "code":"' + str(e) + '"}'
    else:
        return '{"status":"error", "code":"invalid file"}'
