# test_grading_choice.py
from models import Question
from grading import is_correct

# soal-e chandgozine-i: karbar shomare-ye gozine ro mizane
paris_question = Question(
    text="Paytakht Fransa kodoom ast?",
    answer="Paris",
    kind="choice",
    choices=("Landan", "Paris", "Roum"),
)


def test_choice_correct_number():
    """shomare-ye gozine-ye dorost (2 = Paris)"""
    assert is_correct(paris_question, "2") is True


def test_choice_wrong_number():
    """shomare-ye gozine-ye ghalat"""
    assert is_correct(paris_question, "1") is False


def test_choice_correct_text():
    """be jaye shomare, khode matn-e gozine ro benevise"""
    assert is_correct(paris_question, " PARIS ") is True


def test_choice_number_out_of_range():
    """shomare-i ke tu gozine-ha nist bayad ghalat hesab she"""
    assert is_correct(paris_question, "7") is False
    assert is_correct(paris_question, "0") is False