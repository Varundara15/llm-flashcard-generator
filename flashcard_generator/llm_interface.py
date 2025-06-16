from langchain_openai import ChatOpenAI
from typing import List, Dict
from dotenv import load_dotenv
from utils.prompt_template import FLASH_CARD_PROMPT_TEMPLATE
from langchain.schema import HumanMessage
import json

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini",temperature=0.8)

def generate_flashcard_from_chunks(chunk : str, num_cards : int) -> List[Dict[str,str]]:

    prompt = FLASH_CARD_PROMPT_TEMPLATE.format(text = chunk,num_cards = num_cards)

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return parse_flashcards(response.content)
    except Exception as e:
        print(f"An Error Occured {e}")

        return []

def parse_flashcards(raw_output: str) -> List[Dict[str, str]]:

    try:
        flashcards = json.loads(raw_output)

        cleaned_flashcards = []
        for card in flashcards:
            if all(k in card for k in ["question", "answer", "difficulty"]):
                cleaned_flashcards.append({
                    "question": card["question"].strip(),
                    "answer": card["answer"].strip(),
                    "difficulty": card["difficulty"].strip().lower()
                })
        return cleaned_flashcards

    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        print("LLM output was:\n", raw_output)
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
# def parse_flashcards(raw_output:str) -> List[Dict[str,str]]:
#     lines = raw_output.strip().split("\n")
#     flashcards = []
#     question = answer = difficulty = ""

#     for line in lines:
#         if not line or ":" not in line:
#             continue
#         line = line.strip()
#         if line.lower().startswith('q'):
#             if question and answer:
#                 flashcards.append({
#                     "question":question,
#                     "answer":answer,
#                     "difficulty":difficulty
#                 })
#                 answer = difficulty = ""
#             question = line.split(":",1)[1].strip()
#         elif line.lower().startswith("a"):
#             answer = line.split(":",1)[1].strip()
#         elif "difficulty" in line.lower():
#             difficulty = line.split(":",1)[1].strip()

#     if question and answer:
#         flashcards.append({
#             "question":question,
#             "answer":answer,
#             "difficulty":difficulty
#         })

#     return flashcards



