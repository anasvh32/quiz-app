# Khandan va check-e soalat. Hich input/print inja nist.
import json

from models import Question


def load_questions(path: str = "questions.json") -> list[Question]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise ValueError("file questions.json peyda nashod.")
    except json.JSONDecodeError:
        raise ValueError("file questions.json kharabe (JSON moatabar nist).")

    if not isinstance(data, list):
        raise ValueError("questions.json bayad yek list az soalat bashe.")

    questions = []
    for number, item in enumerate(data, 1):
        if not isinstance(item, dict) or "question" not in item or "answer" not in item:
            raise ValueError(f"soal-e shomare {number} 'question' ya 'answer' nadare.")
        questions.append(Question(text=item["question"], answer=item["answer"]))
    return questions