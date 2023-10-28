from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
from typing import Annotated

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PDFResponse(BaseModel):
    filename: str

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
  print("request received")
  print(file.filename)
  with open(file.filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
  return {"filename": file.filename}

  # return JSONResponse(content=PDFResponse(filename=file.filename), status_code=200)

@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

@app.get("/test/")
async def test():
  print("Test working")
  return {"error": False, "data": "XYZ"}

# import nest_asyncio
# from pyngrok import ngrok
# import uvicorn

# port = 8000

# # Set the Ngrok auth token
# ngrok.set_auth_token(Ngrok_token)

# # Open a Ngrok tunnel with the specified domain
# tunnel = ngrok.connect(port, hostname=Ngrok_domain)

# print('Public URL:', tunnel.public_url)
# nest_asyncio.apply()
# uvicorn.run(app, port=8000)
