# This file is mainly to diagnosis the symptoms we've identified as previous step.
import os
from dotenv import load_dotenv
from openai import OpenAI
from config.settings import DIAGNOSIS_LLM

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_diagnosis(symptoms: list[str]) -> str:
    prompt = f"Patien has symptoms: {', '.join(symptoms)}. Suggest possible medical diagnoses. Suggest me a possible cure for the same"

    response = client.chat.completions.create(
        model = DIAGNOSIS_LLM,
        messages=[
            {"role":"system","content": "You are a helpful assistant"},
            {"role":"user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


# Please Uncomment , if you want this function to be tested independently
# print(get_diagnosis(["pain","headache"]))
# python -m functions.diagnosis_symptom