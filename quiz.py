# Quiz app - khandan soalat az JSON, gereftan javab, mohasebe nomre
import json
import time

try:
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
except FileNotFoundError:
    print("Khata: file questions.json peyda nashod.")
    exit()
except json.JSONDecodeError:
    print("Khata: file questions.json kharabe (JSON moatabar nist).")
    exit()

score = 0
wrong_answers = []
start_time = time.time()
time_limit = 120

for q in questions:
    if time.time() - start_time > time_limit:
        print("Zaman tamoom shod!")
        break

    print(q["question"])
    user_answer = input("javabe shoma: ")
    correct_answer = q["answer"]

    if user_answer.strip().lower() == correct_answer.strip().lower():
        print("Dorost!")
        score = score + 1
    else:
        wrong_answers.append({"question": q["question"], "correct_answer": q["answer"]})

print(f"Nomre-ye nahaei: {score} az {len(questions)}")

if wrong_answers:
    print("Soalhaye ghalat:")
    for wa in wrong_answers:
        print(f"- {wa['question']} (Javabe dorost: {wa['correct_answer']})")

end_time = time.time()
duration = end_time - start_time

result = {
    "score": score,
    "total": len(questions),
    "duration_seconds": round(duration, 1)
}

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Natije zakhire shod.")