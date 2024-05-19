from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Title": "Video Clicks Store API","Docs":"Visit /docs for more info"}

@app.post("/clicked")
async def updateWatchData(user_id: str,video_id : str):
    return {"status":"Successfully updated watch data"}