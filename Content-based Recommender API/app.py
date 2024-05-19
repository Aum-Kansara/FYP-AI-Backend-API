from fastapi import FastAPI
from typing import List
import pandas as pd
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv
import ast
import os

app = FastAPI()
load_dotenv()

def convert_to_array(x):
    return np.array(ast.literal_eval(x))

API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
final_videos_df=pd.read_csv("df_with_embeddings.csv")
final_videos_df['Embeddings']=final_videos_df['Embeddings'].apply(lambda x: convert_to_array(x))

def recommend_videos(query, dataframe,number_of_videos=5):
  """
  Compute the distances between the query and each document in the dataframe
  using the dot product.
  """
  query_embedding = genai.embed_content(model='models/embedding-001',
                                        content=query,
                                        task_type="SEMANTIC_SIMILARITY")
  dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])
  top_indices = dot_products.argsort()[-number_of_videos:][::-1]
  # idx = np.argmax(dot_products)
  # print(idx)
  return dataframe.iloc[top_indices]['Video ID'].to_list() # Return text from index with max value

@app.get("/")
def index():
    return {"Title": "Content-based Recommender API","Docs":"Visit /docs for more info"}

@app.post("/context")
def addContext(query: str):
    """
    To get Quiz and Other Metadata info to recommend Video
    """
    return {"video_ids":recommend_videos(query,final_videos_df)}