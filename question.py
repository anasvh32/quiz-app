# Khandan va check-e soalat. Hich input/print inja nist.
import json
import logging

from models import Question

logger = logging.getLogger(__name__)


def load_questions(path: str = "questions.json") -> list[Question]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.error("file %s peyda nashod", path)
        raise ValueError("file questions.json peyda nashod.")
    except json.JSONDecodeError:
        logger.error("file %s kharabe", path)
        raise ValueError("file questions.json kharabe (JSON moatabar nist).")

    if not isinstance(data, list):
        raise ValueError("questions.json bayad yek list az soalat bashe.")

    questions = []
    seen = {}
    for number, item in enumerate(data, 1):
        if not isinstance(item, dict) or "question" not in item or "answer" not in item:
            raise ValueError(f"soal-e shomare {number} 'question' ya 'answer' nadare.")
        key = item["question"].strip().lower()
        if key in seen:
            raise ValueError(f"soal-e shomare {number} tekrari-ye soal-e shomare {seen[key]} ast.")
        seen[key] = number
        kind = item.get("kind", "text")
        choices = tuple(item.get("choices", ()))
        text = item["question"]
        if kind == "choice":
            if len(choices) < 2:
                raise ValueError(f"soal-e shomare {number} chandgozine-ie ama gozine-ash kame.")
            for i, choice in enumerate(choices, 1):
                text += f"\n  {i}) {choice}"

        questions.append(Question(text=text, answer=str(item["answer"]), kind=kind, choices=choices))
    logger.info("%d soal khande shod", len(questions))
    return questions