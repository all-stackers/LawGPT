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

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))
# llm=HuggingFaceHub(repo_id="distilbert-base-uncased-distilled-squad", task="summarization", huggingfacehub_api_token="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")
service_context = ServiceContext.from_defaults(embed_model=embed_model)
set_global_service_context(service_context)

config = cloudinary.config(
    secure=True, 
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"), 
    api_key=os.getenv("CLOUDINARY_API_KEY"), 
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_pdf_to_cloudinary(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        response = cloudinary.uploader.upload(f, resource_type="raw")
    return response["secure_url"]


class Chat(Resource):
    def post(self):
        create = request.args.get('create')
        add = request.args.get('add')
        parser = reqparse.RequestParser()

        if create:
            return create_chat()
        
        if add:
            parser.add_argument('index_id', type=str, required=True)
            parser.add_argument('message', type=dict, required=True)
            args = parser.parse_args()

            return add_message(args)
        
    def get(self):
        index_id = request.args.get('index_id')

        if index_id:
            response = ChatModel.get_chat_index_id(index_id)
            if response["error"]:
                return response
            
            chat = response['data']

            return jsonify({"error": False, "data": chat})
        
        response = ChatModel.get_all_chat()
        if response["error"]:
            return response
        
        chats = response['data']

        return jsonify({"error": False, "data": chats})

def create_chat():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    args = request.files

    # Check if a file was included in the request
    if 'file' not in args:
        return jsonify({'error': True, 'message': 'No file part'})

    file = args['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': True, 'message': 'No file selected for uploading'})
    
    # print(file)

    # store this file in temp folder named temp create the folder if it doesn't exist
    if not os.path.exists('temp'):
        os.makedirs('temp')

    file.save(os.path.join('temp', file.filename))

    documents = SimpleDirectoryReader("./temp/").load_data()

    # Create an index using the service context
    index = VectorStoreIndex.from_documents(
        documents,
        service_context=service_context,
    )

    random_number = random.randint(1000, 9999)
    index.storage_context.persist(f"indexes/{random_number}/")

    index.as_chat_engine()

    memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

    engine = index.as_chat_engine(
        chat_mode="context",
        memory=memory,
        system_prompt="""
            You are expert lawyer. You are helping junior lawyer. Just respond with what is asked, no need to add anything extra. Respond in english.
        """ ,
    )

    output = engine.chat("""Give me title, language, summary and tags of the document. respond with just an object and the format of the objects is as follows:
                {
                    "title": "title of the document",
                    "language": "language of the document",
                    "summary": "summary of the document",
                    "tags": "matrial, civil, criminal, etc"
                }
    """)

    print(type(engine.chat_history))

    json_output = json.loads(output.response)

    print(json_output)

    title = json_output["title"]
    language = json_output["language"]
    summary = json_output["summary"]
    tags = json_output["tags"]

    response = ChatModel.add(title, language, summary, tags, str(random_number), engine.chat_history)
    if response["error"]:
        return jsonify(response)
    
    chat = response["data"]
    

    return jsonify({
        "error": False,
        "message": "File uploaded successfully",
        "data": chat
    })

        # return send_file(filename, mimetype='application/pdf')

def add_message(args):
    index_id = args["index_id"]
    message = args["message"]

    response = ChatModel.add_message(index_id, message)
    if response["error"]:
        return jsonify(response)

    chat = response["data"]
    index_path = "indexes/" + chat.index_id + "/"

    storage_context = StorageContext.from_defaults(persist_dir=index_path)
    index = load_index_from_storage(storage_context)

    memory = ChatMemoryBuffer.from_defaults(chat_history=chat.chat_history, token_limit=1500)

    engine = index.as_chat_engine(
        chat_mode="context",
        memory=memory,
        system_prompt="""
            You are expert lawyer. You are helping junior lawyer. Just respond with what is asked, no need to add anything extra. Respond in english.
        """ ,
    )

    output = engine.chat(message["message"])
    message = {
        "message": output.response,
        "sender": "agent"
    }

    response = ChatModel.add_message(index_id, message)
    if response["error"]:
        return jsonify(response)
    
    chat = response["data"]

    return jsonify({
        "error": False,
        "message": "Message added successfully",
        "data": output.response
    })

        
if __name__ == '__main__':
    app.run(debug=True)