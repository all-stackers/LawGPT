from dotenv import load_dotenv
load_dotenv()

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

if __name__ == "__main__":
    app.run(debug=True)
