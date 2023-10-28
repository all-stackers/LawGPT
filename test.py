from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import os
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import (
    LangchainEmbedding,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
    set_global_service_context,
)
from llama_index.memory import ChatMemoryBuffer
import openai
from langchain import HuggingFaceHub

os.environ["TOKENIZERS_PARALLELISM"] = "False"
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = "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"

model = LangchainEmbedding(HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))
llm=HuggingFaceHub(repo_id="TheBloke/Llama-2-7B-Chat-GGML", huggingfacehub_api_token="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")
# llm=HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", huggingfacehub_api_token="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")
# llm=HuggingFaceHub(repo_id="google/pegasus-cnn_dailymail", huggingfacehub_api_token="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")
service_context = ServiceContext.from_defaults(embed_model=model, llm=llm)
set_global_service_context(service_context)

storage_context = StorageContext.from_defaults(persist_dir="./backend/indexes/001")
medical_index = load_index_from_storage(storage_context)

memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

balance_dosha_engine = medical_index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt="""
        Summarize the given the whole document in english.
    """ ,
)

print(balance_dosha_engine.chat("Summarize the complete document in english."))