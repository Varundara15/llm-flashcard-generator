# LLM-Powered Flashcard Generator

This tool lets you generate high-quality Q&A flashcards from educational content (PDF, TXT, or pasted text) using OpenAI's GPT model. Perfect for students, teachers, or anyone preparing for exams.


## Features

- Upload `.pdf` or `.txt` documents
- Paste raw text as input
- Choose number of flashcards to generate
- Auto-generated flashcards with questions, answers, and difficulty level
- Export as `.csv` or `.json`

---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/varundara15/llm-flashcard-generator.git
cd llm-flashcard-generator

2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\

3. Install Dependencies

pip install -r requirements.txt

4. Set Your OpenAI API Key
Create a .env file in the root directory and add your key:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Running the App
streamlit run app.py
The app will open in your browser at http://localhost:8501.

How to Use
Choose input type: File Upload or Pasted Text
Upload a .pdf or .txt file — or paste raw content
Choose how many flashcards you want (e.g., 10)
Click Generate Flashcards
View the Q&A cards
Export as .csv or .json

Sample Output
Input Text:

"The mitochondria is the powerhouse of the cell. Photosynthesis occurs in the chloroplast."

Generated Flashcard:

Q1: What is the powerhouse of the cell?
A1: The mitochondria is the powerhouse of the cell.
Difficulty: Easy

Q2: Where does photosynthesis occur?
A2: In the chloroplast.
Difficulty: Easy

LLM Configuration
Model: gpt-4.1-mini or gpt-3.5-turbo via OpenAI API

Temperature: 0.4-0.8 for consistent, fact-based results

Export Formats
CSV: Easy to open in Excel or Google Sheets

JSON: Developer-friendly structured format


Credits
Built by [Varun Dara]
Powered by LangChain and OpenAI.