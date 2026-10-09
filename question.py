# Khandan va check-e soalat. Hich input/print inja nist.
import json


def load_questions(path="questions.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise ValueError("file questions.json peyda nashod.")
    except json.JSONDecodeError:
        raise ValueError("file questions.json kharabe (JSON moatabar nist).")

    if not isinstance(data, list):
        raise ValueError("questions.json bayad yek list az soalat bashe.")
    for number, q in enumerate(data, 1):
        if not isinstance(q, dict) or "question" not in q or "answer" not in q:
            raise ValueError(f"soal-e shomare {number} 'question' ya 'answer' nadare.")
    return data