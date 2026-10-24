# test_sources.py
import pytest

from fake_service import FakeResponse, fake_get_timeout
from models import Question
from service import ServerError, ServiceTimeout
from sources import get_questions


def test_service_source_returns_questions():
    """manba-e service: list-e Question bar migarde"""
    questions = get_questions("service")

    assert len(questions) == 2
    assert all(isinstance(q, Question) for q in questions)


def test_file_source_reads_json(tmp_path, monkeypatch):
    """manba-e file: az questions.json mikhoone"""
    content = '[{"question": "a?", "answer": "b"}]'
    (tmp_path / "questions.json").write_text(content, encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    assert len(get_questions("file")) == 1


def test_service_source_does_not_use_network(monkeypatch):
    """ba service, hich ettesali be shabake sakhte nemishe"""
    import socket

    def blocked(*args, **kwargs):
        raise AssertionError("shabake estefade shod")

    monkeypatch.setattr(socket, "socket", blocked)

    assert len(get_questions("service")) == 2


def test_service_errors_are_passed_on():
    """khata-haye service jelo-ye barname gom nemishan"""
    with pytest.raises(ServiceTimeout):
        get_questions("service", get=fake_get_timeout)

    with pytest.raises(ServerError):
        get_questions("service", get=lambda url, timeout=None: FakeResponse(500, {}))


def test_unknown_source():
    """manba-e nashnakhte bayad khata bede"""
    with pytest.raises(ValueError, match="nashnakhte"):
        get_questions("internet")