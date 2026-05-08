import os
from groq import Groq
from dotenv import load_dotenv
from loguru import logger
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.base import BaseEmbedding

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

if not os.path.exists("logs"):
    os.makedirs("logs")
logger.add("logs/app.log", rotation="10 MB")

class MockEmbedding(BaseEmbedding):
    def _get_query_embedding(self, query: str): return [0.1] * 1536
    def _get_text_embedding(self, text: str): return [0.1] * 1536
    def _get_text_embeddings(self, texts: list[str]): return [[0.1] * 1536 for _ in texts]
    async def _aget_query_embedding(self, query: str): return self._get_query_embedding(query)
    async def _aget_text_embedding(self, text: str): return self._get_text_embedding(text)

def build_food_index(data_path: str = "data") -> VectorStoreIndex:
    try:
        if not os.path.exists(data_path): return None
        documents = SimpleDirectoryReader(data_path).load_data()
        service_context = ServiceContext.from_defaults(llm=None, embed_model=MockEmbedding())
        return VectorStoreIndex.from_documents(documents, service_context=service_context)
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
            return res_str if res_str and "None" not in res_str else "Jankari database mein nahi hai."
        return "Database error."
    except Exception as e: return f"Error: {str(e)}"

def get_nutrition_info(food_item: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": """You are a nutrition expert. 
                Strictly follow this format:
                Protein: [number] g
                Fat: [number] g
                Carbohydrates: [number] g
                Fiber: [number] g
                Health Score: [number]/10
                Suggested Pairing: [Only 2-4 words]
                
                ---
                Detailed Explanation:
                [Your explanation here]"""},
                {"role": "user", "content": f"Give me detailed nutrition info for: {food_item}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Groq Error: {str(e)}")
        return "Unable to fetch info."