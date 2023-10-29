from dotenv import load_dotenv
load_dotenv()

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
from resources.pdf import Pdf
from resources.askai import AskAI
from resources.ocrAI import OCR as OCRAI

app = Flask(__name__)
api = Api(app)
CORS(app)

DB_URI = os.getenv("MONGODB_URI")

app.config["MONGODB_HOST"] = DB_URI

db.init_app(app)

api.add_resource(Translation, "/translation")

api.add_resource(Chat, "/chat")
api.add_resource(AskAI, "/askai")
api.add_resource(OCRAI, "/ai/ocr")


api.add_resource(Pdf, "/pdf")

API_KEY = os.environ.get('OCR_API_KEY')
OCR_SPACE_ENDPOINT = 'https://api.ocr.space/parse/image'

@app.route('/ocr', methods=['POST'])
def ocrOmkar():
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
