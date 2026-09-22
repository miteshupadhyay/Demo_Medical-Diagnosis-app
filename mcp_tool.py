from mcp.server.mcpserver import MCPServer
from functions.symptom_extractor import extract_symptoms_from_user_query
from functions.diagnosis_symptom import get_diagnosis
from functions.pubmed_articles import fetch_pubmed_articles_with_metadata
from functions.summarized_pubmed_urls import summarize_text

mcp = MCPServer("Clinisight AI")

@mcp.tool()
async def ClinisightAI(sympton_text):
     symptom = extract_symptoms_from_user_query(sympton_text)
     diagnosis_result = get_diagnosis(symptom)
     pubmed_article = fetch_pubmed_articles_with_metadata(" ".join(symptom))
     summary = summarize_text(pubmed_article[:3000])
    
     return {
            "symptom":symptom,
            "diagnosis":diagnosis_result,
            "pubmed_summary" :summary
        }

# To run it locally
if __name__=="__main__":
     mcp.run(transport = "stdio")