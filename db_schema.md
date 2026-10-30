# Tarahi-ye database (hefte 5)

users: id (kelid-e asli), name
questions: id, text, answer, kind, choices, topic
attempts: id, user_id -> users.id, question_id -> questions.id,
          given_answer, is_correct, created_at

Ertebat: yek karbar chand talash dare, yek soal chand bar pasokh dade mishe.