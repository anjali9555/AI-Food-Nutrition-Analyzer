from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.ai_model import get_nutrition_info, query_nutrition_knowledge

app = FastAPI(title="Nutrition Analyzer API", version="1.0.0")

@app.get("/")
async def root():
    return {"status": "success", "message": "API is running securely!"}

@app.get("/analyze/{food_item}")
async def analyze_food(food_item: str):
    result = get_nutrition_info(food_item)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to fetch nutrition data from AI.")
    
    return JSONResponse(content={"food": food_item, "data": result}, status_code=200)

@app.get("/ask/{question}")
async def ask_nutrition_question(question: str):
    result = query_nutrition_knowledge(question)
    return {"question": question, "answer": result}