from flask_restful import Resource, reqparse
from flask import jsonify

class Translation(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text", type=str, required=True, help="Text is required")

        args = parser.parse_args()

        print(args)

        return jsonify({"error": False, "message": "Translation successful", "data": {"text": args["text"]}})