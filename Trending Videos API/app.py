from typing import Union
from fastapi import FastAPI
from random import choices
import pandas as pd
import json

app = FastAPI()
df=pd.read_csv("videos.csv")
total_videos_df=df[['Video ID', 'Keywords', 'Description', 'Super Title',
       'Comments', 'Likes', 'Views', 'Category']].head(100)

def get_trending_video_ids(no_of_videos):
    rec_videos_index=choices(range(total_videos_df.shape[0]),k=no_of_videos)
    rec_videos_df=total_videos_df.iloc[rec_videos_index]
    return rec_videos_df.to_json(orient='records')

@app.get("/")
def read_root():
    return {"Title": "Trending Videos API","Docs":"Visit /docs for more info"}

@app.get("/videos")
async def get_trending_videos(no_of_videos : Union[int,None]=20):
    rec_videos=get_trending_video_ids(no_of_videos)
    return json.loads(rec_videos)