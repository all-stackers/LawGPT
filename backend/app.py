from dotenv import load_dotenv
load_dotenv()
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad 
import os

import requests
from flask_restful import Resource, reqparse
from flask import jsonify, request, send_file
from flask import Flask, jsonify, request
from flask_restful import Api
from mongo_engine import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from englisttohindi.englisttohindi import EngtoHindi
from resources.translation import Translation
from resources.chat import Chat

app = Flask(__name__)
api = Api(app)
CORS(app)

# app.config["JWT_SECRET_KEY"] = "all_stackers_going_to_win_hackathon"

# jwt = JWTManager(app)

DB_URI = os.getenv("MONGODB_URI")

app.config["MONGODB_HOST"] = DB_URI

db.init_app(app)

api.add_resource(Translation, "/translation")

api.add_resource(Chat, "/chat")

API_KEY = os.environ.get('OCR_API_KEY')
OCR_SPACE_ENDPOINT = 'https://api.ocr.space/parse/image'

# Configure the folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the "uploads" folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create a folder for encrypted files
ENCRYPTED_FOLDER = 'encrypted'
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was included in the request
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename.
    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    # If a file is provided, save it in the "uploads" folder
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        print('File uploaded:', file.filename)

        # Generate an AES key
        aes_key = get_random_bytes(16)
        aes_cipher = AES.new(aes_key, AES.MODE_CBC)

        # Encrypt the uploaded PDF file using the AES key
        encrypted_filename = os.path.join(ENCRYPTED_FOLDER, f"encrypted_{file.filename}")
        with open(filename, "rb") as pdf_file:
            pdf_data = pdf_file.read()
            # Pad the data to a multiple of 16 bytes
            pdf_data = pad(pdf_data, 16)
            ciphertext = aes_cipher.encrypt(pdf_data)

        # Save the encrypted file
        with open(encrypted_filename, "wb") as encrypted_file:
            encrypted_file.write(ciphertext)

        return jsonify({'message': 'File uploaded and encrypted successfully'})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(ENCRYPTED_FOLDER, filename), as_attachment=True)

@app.route('/decrypt/<filename>', methods=['GET'])
def decrypt_file(filename):
    # Load the AES key (you may need to securely store the key)
    aes_key = get_random_bytes(16)
    aes_cipher = AES.new(aes_key, AES.MODE_CBC)

    # Load the encrypted file
    encrypted_file_path = os.path.join(ENCRYPTED_FOLDER, filename)
    decrypted_file_path = os.path.join(ENCRYPTED_FOLDER, f"decrypted_{filename}")

    with open(encrypted_file_path, "rb") as encrypted_file:
        ciphertext = encrypted_file.read()

    # Decrypt the PDF content using the AES key
    pdf_data = aes_cipher.decrypt(ciphertext)
    try:
        # Unpad the decrypted data
        pdf_data = unpad(pdf_data, 16)

        # Save the decrypted PDF
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(pdf_data)

        return send_file(decrypted_file_path, as_attachment=True)

    except Exception as e:
        return jsonify({'error': 'Decryption failed. Incorrect decryption or data integrity issue.'})


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']

    # Create a payload with your API key
    payload = {
        'apikey': API_KEY,
    }

    files = {
        'image': (image.filename, image.read())
    }

    response = requests.post(OCR_SPACE_ENDPOINT, files=files, data=payload)

    if response.status_code == 200:
        result = response.json()
        if 'ParsedResults' in result:
            text = result['ParsedResults'][0]['ParsedText']

            ## Use this text to generate
            return jsonify({"text": text})
        else:
            return jsonify({"error": "OCR failed"}), 500
    else:
        return jsonify({"error": "OCR API request failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)
