from fastapi import FastAPI
from pydantic import BaseModel
from functions.symptom_extractor import extract_symptoms_from_user_query
from functions.diagnosis_symptom import get_diagnosis
from functions.pubmed_articles import fetch_pubmed_articles_with_metadata
from functions.summarized_pubmed_urls import summarize_text


app = FastAPI()


class SymptomInput(BaseModel):
    description:str

@app.post("/diagnosis")
def diagnosis(data:SymptomInput):
    symptom = extract_symptoms_from_user_query(data.description)
    diagnosis_result = get_diagnosis(symptom)
    pubmed_article = fetch_pubmed_articles_with_metadata(" ".join(symptom))
    summary = summarize_text(pubmed_article[:3000])

    return {
        "symptom":symptom,
        "diagnosis":diagnosis_result,
        "pubmed_summary" :summary
    }
