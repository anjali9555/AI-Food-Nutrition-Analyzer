# AI-Based Food Nutrition Analyzer

An AI-powered web application that provides nutritional analysis of food items and answers nutrition-related questions using the **Groq API**, **LlamaIndex**, and a local nutrition knowledge base.

The application uses **FastAPI** as the backend and **Streamlit** as the frontend.

## Key Features

* **Detailed Food Analysis**: Generates nutritional information for food items using an AI model.
* **Macro-Nutrient Analysis**: Provides protein, fat, carbohydrates, and fiber values.
* **Health Scoring**: Generates a health score from 1 to 10.
* **Suggested Pairings**: Provides a suggested food pairing for the analyzed food.
* **Nutrition Explanation**: Generates a detailed explanation of the nutritional analysis.
* **RAG-Based Knowledge Retrieval**: Retrieves information from a local nutrition knowledge base using LlamaIndex.
* **Natural Language Nutrition Queries**: Allows users to ask questions about nutrition and retrieve information from the local knowledge base.
* **JSON-Based AI Response**: The food analysis API returns structured nutritional data in JSON format.

## Tech Stack

* **Frontend**: Streamlit
* **Backend**: FastAPI
* **Programming Language**: Python
* **LLM Provider**: Groq API
* **LLM Model**: `qwen/qwen3.8-27b`
* **RAG Framework**: LlamaIndex
* **Embedding Model**: `BAAI/bge-small-en-v1.5`
* **Vector Index**: LlamaIndex `VectorStoreIndex`
* **Document Loader**: LlamaIndex `SimpleDirectoryReader`
* **API Server**: Uvicorn
* **Logging**: Loguru

## Project Architecture

```text
                         User
                          │
                          ▼
                 Streamlit Frontend
                    /           \
                   /             \
                  ▼               ▼
        Food Analysis        Nutrition Question
              │                     │
              ▼                     ▼
        FastAPI Backend       FastAPI Backend
              │                     │
              ▼                     ▼
        Groq API             LlamaIndex RAG
              │                     │
              ▼                     ▼
    qwen/qwen3.8-27b          Local Knowledge Base
              │                     │
              ▼                     ▼
     Structured JSON          Retrieved Context
              │                     │
              └──────────┬──────────┘
                         ▼
                  Streamlit UI
```

## How the Application Works

### 1. Food Nutrition Analysis

When a user requests nutrition information for a food item:

```text
User
 ↓
Streamlit
 ↓
FastAPI /analyze/{food_item}
 ↓
get_nutrition_info()
 ↓
Groq API
 ↓
qwen/qwen3.8-27b
 ↓
JSON Response
 ↓
Streamlit
```

The model is instructed to return the following information:

* Protein
* Fat
* Carbohydrates
* Fiber
* Health Score
* Suggested Pairing
* Detailed Explanation

The response is returned as structured JSON.

## 2. RAG-Based Nutrition Question Answering

The application also provides a separate knowledge-retrieval pipeline for nutrition-related questions.

```text
User Question
      ↓
FastAPI /ask/{question}
      ↓
query_nutrition_knowledge()
      ↓
SimpleDirectoryReader
      ↓
Local data/ directory
      ↓
LlamaIndex VectorStoreIndex
      ↓
Query Engine
      ↓
Relevant Knowledge
      ↓
Answer
```

The local documents are loaded from the `data/` directory and converted into a searchable LlamaIndex vector index.

## RAG Components

### Document Loader

The project uses LlamaIndex `SimpleDirectoryReader` to load documents from the local `data/` directory.

### Embedding Model

The project configures:

```text
BAAI/bge-small-en-v1.5
```

as the embedding model through HuggingFace.

Embeddings convert text into numerical vector representations that can be used for semantic retrieval.

### Vector Store Index

The project uses:

```text
VectorStoreIndex
```

from LlamaIndex to create a searchable index from the nutrition documents.

### Query Engine

When a user asks a nutrition question, the application creates a query engine from the index and retrieves relevant information to generate the response.

## API Endpoints

### Root Endpoint

```http
GET /
```

Returns a basic API status message.

Example response:

```json
{
  "status": "success",
  "message": "API is running securely!"
}
```

### Food Analysis Endpoint

```http
GET /analyze/{food_item}
```

Analyzes a food item using the Groq API and returns structured nutritional information.

Example:

```text
/analyze/apple
```

### Nutrition Knowledge Endpoint

```http
GET /ask/{question}
```

Searches the local nutrition knowledge base using the LlamaIndex retrieval pipeline.

Example:

```text
/ask/What are the benefits of protein?
```

## AI Model Configuration

The project uses the Groq API with:

```text
qwen/qwen3.8-27b
```

The food analysis model is instructed to return a JSON object containing:

```text
protein
fat
carbohydrates
fiber
health_score
suggested_pairing
explanation
```

## Embedding Configuration

The project uses:

```text
BAAI/bge-small-en-v1.5
```

through:

```text
HuggingFaceEmbedding
```

This embedding model is used by LlamaIndex for the document retrieval pipeline.

## Project Structure

```text
AI-Food-Nutrition-Analyzer/
│
├── src/
│   ├── main.py
│   └── ai_model.py
│
├── data/
│   └── nutrition knowledge files
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── logs/
└── README.md
```

## Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anjali9555/AI-Food-Nutrition-Analyzer.git
cd AI-Food-Nutrition-Analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

**Important:** Never commit your `.env` file or API key to GitHub.

### 4. Start the Backend

Run:

```bash
uvicorn src.main:app --reload
```

The FastAPI backend will start locally.

### 5. Start the Frontend

Open another terminal and run:

```bash
streamlit run app.py
```

The Streamlit frontend will start locally.

## Logging

The application uses **Loguru** for application logging.

Logs are stored in:

```text
logs/app.log
```

The log file is configured with a rotation size of 10 MB.

## Error Handling

The backend handles errors using FastAPI's `HTTPException`, while the AI module logs errors using Loguru.

If the AI nutrition request fails, the API returns an appropriate error response.

The RAG pipeline also handles missing knowledge-base directories and internal retrieval errors.

## Future Improvements

* Improve the accuracy of nutrition information using a verified nutrition dataset.
* Connect the food-analysis pipeline with the nutrition knowledge base.
* Add image-based food recognition.
* Add user-specific dietary preferences.
* Add meal planning and daily nutrition tracking.
* Improve the visualization dashboard.
* Add authentication and user profiles.
* Deploy the application to a cloud platform.

## Author

**Anjali**
Computer Science & Engineering Student
IET Lucknow

## Repository

[AI-Food-Nutrition-Analyzer](https://github.com/anjali9555/AI-Food-Nutrition-Analyzer)
