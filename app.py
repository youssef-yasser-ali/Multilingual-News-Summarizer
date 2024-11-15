from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

summarizer = pipeline("text2text-generation", model="YoussefAnwar/mt5-summarize-ar-en")

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(request: TextRequest):
    text = request.text    

    summary = summarizer(text)
    
    return {"summary": summary[0]['generated_text']}
