# test_logging.py
import logging
import pytest
from question import load_questions


def test_missing_file_is_logged(caplog):
    """vaghti file nist, bayad yek khata tu log sabt she"""
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            load_questions("file_ke_vojood_nadare.json")

    assert "peyda nashod" in caplog.text


def test_loaded_questions_are_logged(tmp_path, caplog):
    """vaghti soalat dorost khande beshan, tedadeshun tu log sabt she"""
    file_path = tmp_path / "q.json"
    file_path.write_text('[{"question": "2 + 2?", "answer": "4"}]', encoding="utf-8")

    with caplog.at_level(logging.INFO):
        load_questions(str(file_path))

    assert "1 soal" in caplog.text