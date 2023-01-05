# NL Prompt

# Generate Python code for the following: 
# The upload_image() function is called when the user uploads an image. The image is read and encoded using base64. 
# The encoded image is written to a file.

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
        encoded_img = base64.b64encode(img_data).decode('utf-8')
        try:
            with open('/var/www/html/img/' + img_name, 'w') as f:
                f.write(encoded_img)
            return '{"status":"success", "code":""}'
        except Exception as e:
            return '{"status":"error", "code":"' + str(e) + '"}'
    else:
        return '{"status":"error", "code":"invalid file"}'