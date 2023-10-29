from flask_restful import Resource, reqparse
from flask import jsonify, request, send_file
import os
import cloudinary
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding, ServiceContext, VectorStoreIndex, set_global_service_context, SimpleDirectoryReader
import os
import random
from llama_index.memory import ChatMemoryBuffer
from langchain.llms import HuggingFaceHub
import json
from models.chat import Chat as ChatModel

import json
import os
from flask_restful import Resource, reqparse
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import (
    LangchainEmbedding,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
    set_global_service_context,
)
from llama_index.memory import ChatMemoryBuffer

# os.environ["TOKENIZERS_PARALLELISM"] = "False"
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))
# llm=HuggingFaceHub(repo_id="distilbert-base-uncased-distilled-squad", task="summarization", huggingfacehub_api_token="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")
service_context = ServiceContext.from_defaults(embed_model=embed_model)
set_global_service_context(service_context)

storage_context = StorageContext.from_defaults(persist_dir="./indian_penal_code_index/")
index = load_index_from_storage(storage_context)

memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt="""
        You are expert lawyer. You are helping junior lawyer. Just respond with what is asked, no need to add anything extra. Respond in english.
    """ ,
)

class AskAI(Resource):
    def post(self):
        print("req received")
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        args = parser.parse_args()
        
        output = engine.chat(args["question"])

        return jsonify({"error": False, "data": output.response})
