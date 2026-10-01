import os
import json
from groq import Groq
from dotenv import load_dotenv
from loguru import logger
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq as LlamaIndexGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Groq Client for direct calls
client = Groq(api_key=groq_api_key)

# Logging Setup
os.makedirs("logs", exist_ok=True)
logger.add("logs/app.log", rotation="10 MB")

# Professional LlamaIndex Setup
try:
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.llm = LlamaIndexGroq(model="qwen/qwen3.8-27b", api_key=groq_api_key)
except Exception as e:
    logger.error(f"Error initializing models: {e}")

def build_food_index(data_path: str = "data") -> VectorStoreIndex:
    try:
        if not os.path.exists(data_path): 
            return None
        documents = SimpleDirectoryReader(data_path).load_data()
        return VectorStoreIndex.from_documents(documents)
    except Exception as e:
        logger.error(f"Index Error: {str(e)}")
        return None

def query_nutrition_knowledge(question: str) -> str:
    try:
        index = build_food_index()
        if index:
            query_engine = index.as_query_engine()
            response = query_engine.query(question)
            res_str = str(response).strip()
            return res_str if res_str else "Sorry, mujhe iski jankari nahi mili."
        return "Knowledge database missing."
    except Exception as e: 
        logger.error(f"Query Error: {str(e)}")
        return "Internal server error while searching."

def get_nutrition_info(food_item: str) -> dict:
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": """You are a nutrition expert. 
                    You MUST respond ONLY in valid JSON format with the following keys:
                    'protein' (float, in grams), 'fat' (float, in grams), 'carbohydrates' (float, in grams), 
                    'fiber' (float, in grams), 'health_score' (integer 1-10), 
                    'suggested_pairing' (string, max 4 words), 'explanation' (string, detailed)."""
                },
                {"role": "user", "content": f"Give me detailed nutrition info for: {food_item}"}
            ],
         model="qwen/qwen3.8-27b",
            response_format={"type": "json_object"} 
        )
        return json.loads(chat_completion.choices[0].message.content)
    except Exception as e:
        logger.error(f"Groq API Error: {str(e)}")
        return {}