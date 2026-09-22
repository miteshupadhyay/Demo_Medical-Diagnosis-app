import re

# This function would extract the symptoms from user query , example
# If user has asked "I am having headache and pain", then this function would return
# ['pain','headache'].
# We could use cheaper LLM as well here for more accurately detection

def extract_symptoms_from_user_query(text:str) -> list[str]:
    symptoms = re.findall(
    r"\b(headache|fever|nausea|fatigue|pain)\b",
    text.lower()
)
    return list(set(symptoms))



# Please Uncomment , if you want this function to be tested independently
# user_query = "I have fever and also feeling headache"
# print(extract_symptoms_from_user_query(user_query))