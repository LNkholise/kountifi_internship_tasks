from fastapi import FastAPI
from app.models.query_model import Query
from app.services.query_handler import process_query

app = FastAPI()

@app.post("/chat")
def handle_query(query: Query):
    return process_query(query.query)
