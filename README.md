# AI-Based Food Nutrition Analyzer

An advanced AI-powered web application that provides detailed nutritional analysis of food items using **RAG (Retrieval-Augmented Generation)** and the **Groq API** with the `qwen/qwen3.8-27b` model.

## Key Features

* **Detailed Food Analysis**: Provides a comprehensive breakdown of nutritional information and macro-nutrients for food items.
* **Macro Visualization**: Represents nutritional values using interactive charts for easy understanding.
* **Health Scoring**: Generates an AI-based health score on a scale of 1–10.
* **Suggested Pairings**: Provides food pairing suggestions to help create a more balanced diet.
* **Knowledge Base (RAG)**: Retrieves relevant information from a local nutrition knowledge base before generating responses.
* **Custom Nutrition Queries**: Allows users to ask nutrition-related questions based on the available local knowledge base.

## Tech Stack

* **Frontend**: Streamlit
* **Backend**: FastAPI
* **Programming Language**: Python
* **AI / LLM Provider**: Groq API
* **AI Model**: `qwen/qwen3.8-27b`
* **RAG Framework**: LlamaIndex
* **Knowledge Base**: Local nutrition data files
* **API Server**: Uvicorn

## Project Architecture

```text
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
                      ▼
                FastAPI Backend
                      │
                      ▼
                 LlamaIndex
                      │
                      ▼
             Retrieve Relevant Data
                      │
                      ▼
            Local Nutrition Knowledge Base
                      │
                      ▼
                  Groq API
                      │
                      ▼
             qwen/qwen3.8-27b
                      │
                      ▼
             Generated AI Response
                      │
                      ▼
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Nutrition      Health Score    Food Pairings
    Analysis
```

## How It Works

1. The user enters or selects a food item through the Streamlit interface.
2. The request is sent to the FastAPI backend.
3. LlamaIndex processes the request and retrieves relevant information from the local nutrition knowledge base.
4. The retrieved information is provided as context to the language model.
5. The Groq API sends the request to the `qwen/qwen3.8-27b` model.
6. The model generates the nutritional analysis.
7. The backend returns the generated result to the Streamlit frontend.
8. The frontend displays the nutrition information, macro breakdown, health score, and suggested food pairings.

## Project Structure

```text
AI-Food-Nutrition-Analyzer/
│
├── src/
│   ├── main.py
│   └── ...
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── ...
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

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_actual_api_key_here
```

**Important:** Never upload your `.env` file or API key to GitHub.

### 4. Run the Backend

```bash
uvicorn src.main:app --reload
```

The FastAPI backend will start locally.

### 5. Run the Frontend

Open a separate terminal and run:

```bash
streamlit run app.py
```

The Streamlit application will start locally.

## Deployment

The project can be deployed using:

* **Backend**: Render
* **Frontend**: Streamlit Community Cloud

### Backend Deployment

The FastAPI backend can be deployed on Render using the appropriate Python start command:

```bash
uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

### Frontend Deployment

The Streamlit frontend can be deployed using Streamlit Community Cloud.

Make sure the required environment variables, such as the Groq API key and backend URL, are configured in the deployment settings.

## Environment Variables

The application requires the following environment variable:

```env
GROQ_API_KEY=your_actual_api_key_here
```

If the frontend communicates with a deployed backend, configure the backend URL according to the project's implementation.

## RAG Pipeline

The application uses **Retrieval-Augmented Generation (RAG)** to improve the reliability of nutrition-related responses.

The basic pipeline is:

```text
User Query
    ↓
Query Processing
    ↓
LlamaIndex
    ↓
Knowledge Base Retrieval
    ↓
Relevant Nutrition Context
    ↓
Groq API
    ↓
qwen/qwen3.8-27b
    ↓
Final Response
```

Instead of relying only on the model's general knowledge, the application retrieves relevant information from the local nutrition knowledge base and uses it as context while generating the response.

## Benefits of Using RAG

* Uses information from a project-specific knowledge base.
* Reduces dependency on the model's general knowledge.
* Allows the knowledge base to be updated independently.
* Provides relevant context to the language model.
* Makes the application suitable for domain-specific question answering.

## API Architecture

The application follows a simple frontend-backend architecture:

```text
Streamlit
   │
   │ HTTP Request
   ▼
FastAPI
   │
   ▼
LlamaIndex
   │
   ▼
Knowledge Base
   │
   ▼
Groq API
   │
   ▼
qwen/qwen3.8-27b
   │
   ▼
FastAPI Response
   │
   ▼
Streamlit UI
```

## Main Functionalities

### 1. Nutritional Analysis

The application provides nutritional information such as:

* Calories
* Protein
* Carbohydrates
* Fat
* Other available nutritional information

### 2. Macro Visualization

The nutritional values are represented visually through charts, making the results easier to understand.

### 3. Health Score

The application generates a health score between **1 and 10** based on the available nutritional information and AI-generated analysis.

### 4. Food Pairing Suggestions

The application suggests complementary food items that may help create a more balanced meal.

### 5. Knowledge-Based Question Answering

Users can ask nutrition-related questions, and the RAG pipeline retrieves relevant information from the local knowledge base before generating an answer.

## Future Improvements

* Expand the nutrition knowledge base.
* Add more food categories and nutritional parameters.
* Improve nutrition-data retrieval accuracy.
* Add user-specific dietary preferences.
* Add meal planning functionality.
* Add authentication and user profiles.
* Improve visualization and analytics.
* Deploy the complete application with production-grade infrastructure.

## Author

**Anjali**
Computer Science & Engineering Student
IET Lucknow

## Repository

[AI-Food-Nutrition-Analyzer](https://github.com/anjali9555/AI-Food-Nutrition-Analyzer)
