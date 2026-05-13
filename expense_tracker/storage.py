import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "expenses.json")

def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_expenses(expenses):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)
        