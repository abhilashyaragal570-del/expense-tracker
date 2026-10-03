# AI-Powered Expense Tracker (Python CLI + Gemini API)

A command-line expense tracker in Python. Add expenses manually from a menu,
or type a plain sentence like "bought a pen for 20" and the Gemini API turns it
into structured JSON (name, amount, category) that is saved to a JSON file.

## Features
- Add, view, and delete expenses
- Total spending per category
- AI-powered entry: describe an expense in plain English
- Input validation and error handling
- Retry logic for API failures
- API key kept out of the code with a .env file

## Tech
Python, Gemini API, JSON, python-dotenv, Git/GitHub

## How to run
1. pip install google-genai python-dotenv
2. Create llm-practice/.env with: GEMINI_API_KEY=your_key
3. Manual menu: python expense-tracker/main.py
4. AI entry: python expense-tracker/ai_add.py

## What I learned
I built a menu-driven expense tracker with a class that loads and saves data in JSON.
I then connected the Gemini API so a plain sentence becomes structured JSON that my
tracker can store. I learned to keep API keys in a .env file, and to add retries
because the API sometimes fails with 503 errors.