# Tashih-e javab. Hich input/print inja nist.
from models import Question


def is_correct(question: Question, user_answer: str) -> bool:
    user_answer = user_answer.strip().lower()
    correct = question.answer.strip().lower()

    if question.kind == "choice":
        # karbar shomare-ye gozine ro mizane, ma tabdilesh mikonim be matn-e gozine
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question.choices):
            user_answer = question.choices[int(user_answer) - 1].strip().lower()
        return user_answer == correct

    return user_answer == correct