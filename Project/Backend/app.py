from fastapi import FastAPI
from extractor import extract_quantity
import uvicorn

app = FastAPI()

@app.post("/analyze/")
async def analyze_transaction(transaction: dict):
    text = transaction.get("description", "")
    quantities = extract_quantity(text)
    return {"quantities": quantities}