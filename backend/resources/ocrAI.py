from flask_restful import Resource, reqparse
from flask import jsonify, request, send_file
import os
import cloudinary
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding, ServiceContext, VectorStoreIndex, set_global_service_context, SimpleDirectoryReader
import os
import random
from llama_index import (
    LangchainEmbedding,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
    set_global_service_context,
)
from llama_index.memory import ChatMemoryBuffer

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))
# llm=HuggingFaceHub(repo_id="distilbert-base-uncased-distilled-squad", task="summarization", huggingfacehub_api_token="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")
service_context = ServiceContext.from_defaults(embed_model=embed_model)
set_global_service_context(service_context)

class OCR(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, required=True)
        args = parser.parse_args()

        # create a txt file with the text

        with open("temp/ocr.txt", "w") as f:
            f.write(args["text"])

        documents = SimpleDirectoryReader("./temp/").load_data()

        # delete the temp folder


        # Create an index using the service context
        index = VectorStoreIndex.from_documents(
            documents,
            service_context=service_context,
        )

        random_number = random.randint(1000, 9999)
        index.storage_context.persist(f"indexes/{random_number}/")

        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

        return jsonify({"error": False, "data": random_number})
