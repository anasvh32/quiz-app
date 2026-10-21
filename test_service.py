# test_service.py
from fake_service import FakeResponse
from models import Question
from service import fetch_questions


def test_fetch_questions_success():
    """halat-e movafagh: list-e Question bar migarde"""
    questions = fetch_questions()

    assert len(questions) == 2
    assert all(isinstance(q, Question) for q in questions)
    assert questions[0].text == "Paytakht Iran kojast?"
    assert questions[0].answer == "Tehran"


def test_fetch_questions_converts_choice_question():
    """soal-e chandgozine-i ham mesle file tabdil mishe"""
    paris = fetch_questions()[1]

    assert paris.kind == "choice"
    assert paris.choices == ("Landan", "Paris", "Roum")
    assert "2) Paris" in paris.text


def test_fetch_questions_uses_given_get_and_sets_timeout():
    """get ro az biroon migire va hamishe timeout mide"""
    calls = []

    def my_get(url, timeout=None):
        calls.append((url, timeout))
        return FakeResponse(200, {"questions": [{"question": "a?", "answer": "b"}]})

    questions = fetch_questions(get=my_get, url="http://x.test/q")

    assert len(questions) == 1
    assert calls == [("http://x.test/q", 3)]