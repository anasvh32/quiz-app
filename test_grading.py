# test_grading.py
import pytest
from models import Question
from grading import is_correct


@pytest.fixture
def tehran_question():
    """fixture: ye soal-e Tehran ro yebar misaze va be hame test-ha mide"""
    return Question(text="Paytakht Iran kojast?", answer="Tehran")


def test_is_correct_normal(tehran_question):
    """halat-e adi: javab dorost"""
    assert is_correct(tehran_question, "Tehran") is True


def test_is_correct_wrong(tehran_question):
    """javab ghalat"""
    assert is_correct(tehran_question, "Shiraz") is False


def test_is_correct_with_spaces_and_case(tehran_question):
    """fasele ezafe va harf-e bozorg/kuchak nabayad mohem bashe"""
    assert is_correct(tehran_question, "  tehran  ") is True
    assert is_correct(tehran_question, "TEHRAN") is True


def test_is_correct_empty_answer(tehran_question):
    """javab khali bayad ghalat hesab she"""
    assert is_correct(tehran_question, "") is False


def test_is_correct_only_spaces(tehran_question):
    """faghat fasele bayad ghalat hesab she"""
    assert is_correct(tehran_question, "   ") is False


def test_is_correct_non_string_raises(tehran_question):
    """agar vorodi matn nabashe bayad TypeError bede"""
    with pytest.raises(TypeError, match="matn"):
        is_correct(tehran_question, 123)


def test_is_correct_none_raises(tehran_question):
    """agar None bedim bayad TypeError bede"""
    with pytest.raises(TypeError, match="matn"):
        is_correct(tehran_question, None)