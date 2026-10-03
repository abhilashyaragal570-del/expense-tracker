import os
import json
import time
import sys
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

from main import ExpenseTracker

load_dotenv(Path(__file__).parent.parent / "llm-practice" / ".env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found. Check your .env file.")
    raise SystemExit

MODEL = "models/gemini-3.6-flash"

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=60000)
)

tracker = ExpenseTracker()

while True:
    text = input("Describe an expense (or type quit): ")
    if text.lower() == "quit":
        break

    prompt = f"""Extract the expense from the text below.
Reply with ONLY valid JSON, no extra words, in this format:
{{"name": "...", "amount": 0, "category": "..."}}

Text: {text}"""

    response = None
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {type(e).__name__}: {e}")
            time.sleep(5)

    if response and response.text:
        raw = response.text.strip().replace("```json", "").replace("```", "").strip()
        print("Raw reply from Gemini:")
        print(raw)
        try:
            data = json.loads(raw)
            print("Name:", data["name"])
            print("Amount:", data["amount"])
            print("Category:", data["category"])

            tracker.add(data["name"], data["amount"], data["category"])
            print("Saved to expenses.json")
            total = sum(e["amount"] for e in tracker.expenses)
            print("Total so far:", total)
        except json.JSONDecodeError:
            print("Could not read the reply as JSON.")

        except KeyError:
            print("The reply was missing a field.") 

        else:
            print("No answer. Try again later.")       