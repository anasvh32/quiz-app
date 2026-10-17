# test_question.py
import pytest
from question import load_questions
from models import Question


def test_load_questions_normal(tmp_path):
    """file dorost ro bayad betune bekhoone"""
    content = '[{"question": "Paytakht Iran kojast?", "answer": "Tehran"}]'
    file_path = tmp_path / "q.json"
    file_path.write_text(content, encoding="utf-8")

    questions = load_questions(str(file_path))
    assert len(questions) == 1
    assert questions[0].answer == "Tehran"
    assert questions[0].kind == "text"


def test_load_questions_file_not_found():
    """file vojud nadashte bashe bayad ValueError bede"""
    with pytest.raises(ValueError, match="peyda nashod"):
        load_questions("file_ke_vojood_nadare.json")


def test_load_questions_invalid_json(tmp_path):
    """file kharab (JSON namotabar) bayad ValueError bede"""
    file_path = tmp_path / "bad.json"
    file_path.write_text("{ in json nist", encoding="utf-8")

    with pytest.raises(ValueError, match="kharabe"):
        load_questions(str(file_path))


def test_load_questions_missing_answer(tmp_path):
    """soal bedune answer bayad ValueError bede"""
    content = '[{"question": "Paytakht Iran kojast?"}]'
    file_path = tmp_path / "no_answer.json"
    file_path.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match="answer"):
        load_questions(str(file_path))


def test_load_questions_duplicate(tmp_path):
    """soal tekrari bayad ValueError bede"""
    content = '''
    [
        {"question": "Paytakht Iran kojast?", "answer": "Tehran"},
        {"question": "Paytakht Iran kojast?", "answer": "Tehran"}
    ]
    '''
    file_path = tmp_path / "dup.json"
    file_path.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match="tekrari"):
        load_questions(str(file_path))


def test_load_questions_numeric_answer(tmp_path):
    """agar javab adad bashe (mesle 4 be jaye "4") nabayad crash kone"""
    content = '[{"question": "2 + 2 chand mishe?", "answer": 4}]'
    file_path = tmp_path / "num.json"
    file_path.write_text(content, encoding="utf-8")

    questions = load_questions(str(file_path))
    assert questions[0].answer == "4"   # bayad be string tabdil shode bashe