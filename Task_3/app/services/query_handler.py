import json
from pathlib import Path

# Loading the knowledge base file before running queries
with open(Path(__file__).resolve().parent.parent.parent / "knowledge_base.json") as f:
    KNOWLEDGE_BASE = json.load(f)
    

# Query function for processing simple rule based,if else 
def process_query(query: str):
    query = query.lower()

    if any(keyword in query for keyword in ["payment", "due", "terms"]):
        found_vendor = None
        for vendor in KNOWLEDGE_BASE["vendors"]:
            if vendor in query:
                found_vendor = vendor
                break

        if found_vendor:
            return {
                "response": f"Payment terms for {found_vendor}: {KNOWLEDGE_BASE['vendors'][found_vendor]['payment_terms']}",
                "details": KNOWLEDGE_BASE["vendors"][found_vendor]
            }

        return {
            "response": "Available vendors: " + ", ".join(KNOWLEDGE_BASE["vendors"].keys())
        }

    return {
        "response": "I can answer questions about vendor payments. Try asking things like:",
        "suggestions": [
            "When is Wayne Enterprises payment due?",
            "What are Stark Industries payment terms?"
        ]
    }

