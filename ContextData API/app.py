from fastapi import FastAPI,UploadFile
from typing import Union

app = FastAPI()

@app.get("/")
def index():
    return {"Title": "Chatbot Context API","Docs":"Visit /docs for more info"}

@app.post("/context")
def addContext(video_title: str,description: str,files: Union[list[UploadFile],None]):
    """
    To get Context for Chatbot from which it should answer
    """
    return "Uploaded Successfully"