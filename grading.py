# Tashih-e javab. Hich input/print inja nist.
from models import Question


def is_correct(question: Question, user_answer: str) -> bool:
    return user_answer.strip().lower() == question.answer.strip().lower()