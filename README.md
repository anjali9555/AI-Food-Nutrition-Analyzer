# AI-Based Food Nutrition Analyzer

Ek advanced web application jo AI ka use karke food items ka detailed nutritional analysis karti hai. Ismein **RAG (Retrieval-Augmented Generation)** aur **Groq API** ka use kiya gaya hai.

## Key Features
* **Detailed Food Analysis**: Food items ke macro-nutrients ka breakdown.
* **Macro Visualization**: Bar charts ke zariye nutrients ka representation.
* **Health Scoring**: AI-driven health rating (1-10).
* **Suggested Pairings**: Behtar diet ke liye food pairing suggestions.
* **Knowledge Base (RAG)**: Local files se sawal poochne ki suvidha.

## Tech Stack
* **Frontend**: Streamlit
* **Backend**: FastAPI (Python)
* **AI Engine**: OpenAI API (Llama 3.1)
* **Framework**: LlamaIndex

## Setup Instructions
1. Clone the repo: `git clone https://github.com/anjali9555/AI-Food-Nutrition-Analyzer.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your API Key in `.env` file.
4. Run Backend: `uvicorn src.main:app --reload`
5. Run Frontend: `streamlit run app.py`

## Author
* **Anjali** - Computer Science & Engineering student at IET Lucknow.
