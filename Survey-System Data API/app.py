from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
def index():
    return {"Title": "Survey System Data Store API","Docs":"Visit /docs for more info"}

@app.post("/surveyData")
async def updateSurveyData(user_id: str,education_level: List[str],field_of_study: List[str],age: int,sex: str,skills: List[str],interests: List[str],preferred_technologies: List[str],core_subjects: List[str],specialization_subjects: List[str],carrer_roles: List[str]):
    return {"status":"Successfully updated survey data"}