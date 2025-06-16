from langchain.prompts import PromptTemplate

FLASH_CARD_PROMPT_TEMPLATE = PromptTemplate(
    template="""
        You are an educational helpful assistant. Based on the text below, generate {num_cards} flashcards.

        Each flashcard must include:
        - A clear, concise question
        - A factually correct and self-contained answer
        - A difficulty level: easy, medium, or hard

        Return the output as a JSON array of objects, where each object has:
        - "question"
        - "answer"
        - "difficulty"

        Example format:
        [
            {{
                "question": "What is AI?",
                "answer": "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
                "difficulty": "easy"
            }},
            ...
        ]

        Text:
        {text}
    """,
    input_variables=['text', 'num_cards']
)
