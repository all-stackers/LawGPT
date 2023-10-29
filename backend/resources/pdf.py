import requests
from flask import jsonify
from flask import jsonify, request, send_file
from flask_restful import Resource, reqparse
from models.pdf import PDF as PDFModel


class Pdf(Resource):
    def get(self):
        try:
            response = PDFModel.get_all()
            if response["error"]:
                return response, 400
            
            pdfs = response['data']

            return jsonify({"error": False, "data": pdfs})
        
        except Exception as e:
            print(e)
            return {"error": True, "message": "Error while getting the PDF"}, 500
        

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pdf_name', type=str, required=True)
        parser.add_argument('original_file_cid', type=str, required=True)
        parser.add_argument('original_file_url', type=str, required=True)
        parser.add_argument('translated_file_cid', type=str, required=True)
        parser.add_argument('translated_file_url', type=str, required=True)
        parser.add_argument('chat_id', type=int, required=False)
        args = parser.parse_args()

        try:
            response = PDFModel.add(args["pdf_name"], args["original_file_cid"], args["original_file_url"],
                                    args["translated_file_cid"], args["translated_file_url"], args["chat_id"])

            if response["error"]:
                return response, 400

            return jsonify({"error": False,  "data": response})
            # pdf = PDF(**data).save()
            # return {"error": False, "data": pdf}, 201  # 201 Created status code

        except Exception as e:
            print(e)
            return {"error": True, "message": "Error while creating the PDF"}, 500
