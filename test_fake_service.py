# test_fake_service.py
from fake_service import fake_get


def test_fake_response_status_is_200():
    """javab-e sakhtegi bayad status_code 200 dashte bashe"""
    response = fake_get("http://example.test/questions", timeout=3)
    assert response.status_code == 200


def test_fake_response_has_questions_list():
    """JSON bayad yek list az soalat dashte bashe"""
    data = fake_get("http://example.test/questions").json()
    assert isinstance(data["questions"], list)
    assert len(data["questions"]) == 2