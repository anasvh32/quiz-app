# test_service.py
import pytest

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


class BadJsonResponse:
    """javabi ke json()-esh khata mide, mesle JSON-e kharab"""

    status_code = 200

    def json(self):
        raise ValueError("JSON kharab")


def make_get(response):
    """yek get-e sakhtegi misaze ke hamishe hamin response ro bar migardoone"""

    def my_get(url, timeout=None):
        return response

    return my_get


def test_broken_json_raises_clear_error():
    """JSON kharab bayad ValueError bede"""
    with pytest.raises(ValueError, match="kharabe"):
        fetch_questions(get=make_get(BadJsonResponse()))


def test_response_is_not_a_dict():
    """javab be jaye dictionary yek list bashe"""
    with pytest.raises(ValueError, match="shekl"):
        fetch_questions(get=make_get(FakeResponse(200, [1, 2, 3])))


def test_response_without_questions_key():
    """kelid-e 'questions' nadashte bashe"""
    with pytest.raises(ValueError, match="questions"):
        fetch_questions(get=make_get(FakeResponse(200, {"items": []})))


def test_questions_is_not_a_list():
    """'questions' be jaye list, yek matn bashe"""
    with pytest.raises(ValueError, match="list"):
        fetch_questions(get=make_get(FakeResponse(200, {"questions": "salam"})))


def test_question_without_answer():
    """yek soal bedune 'answer' bashe"""
    data = {"questions": [{"question": "a?"}]}
    with pytest.raises(ValueError, match="answer"):
        fetch_questions(get=make_get(FakeResponse(200, data)))


def test_question_text_has_wrong_type():
    """matn-e soal adad bashe, na string"""
    data = {"questions": [{"question": 5, "answer": "b"}]}
    with pytest.raises(ValueError, match="ghalate"):
        fetch_questions(get=make_get(FakeResponse(200, data)))