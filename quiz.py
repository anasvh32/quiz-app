# Quiz app - khandan soalat az JSON, gereftan javab, mohasebe nomre
import json
import time 
from question import load_questions
from grading import is_correct
from storage import save_result
import logging

logging.basicConfig(filename="quiz.log", level=logging.INFO)

try:
    questions = load_questions()
except ValueError as e:
    print(f"Khata: {e}")
    exit()
print(f"Khosh amadid! {len(questions)} soal dar peysh ast.")
score = 0
wrong_answers = []
start_time = time.time()
time_limit = 120

for q in questions:
    if time.time() - start_time > time_limit:
        print("Zaman tamoom shod!")
        break

    print(q.text)
    user_answer = input("javabe shoma: ")

    if is_correct(q, user_answer):
        print("Dorost!")
        score = score + 1
    else:
        wrong_answers.append(q)

print(f"Nomre-ye nahaei: {score} az {len(questions)}")

if wrong_answers:
    print("Soalhaye ghalat:")
    for wa in wrong_answers:
        print(f"- {wa.text} (Javabe dorost: {wa.answer})")

duration = time.time() - start_time
save_result({
    "score": score,
    "total": len(questions),
    "duration_seconds": round(duration, 1),
})

print("Natije zakhire shod.")