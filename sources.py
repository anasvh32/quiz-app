# Entekhab-e manba-e soalat (file ya service). Hich input/print inja nist.
import logging

from fake_service import fake_get
from question import load_questions
from service import fetch_questions

logger = logging.getLogger(__name__)


def get_questions(source="file", get=fake_get):
    """soalat ro az file ya az service migire"""
    if source == "file":
        return load_questions()
    if source == "service":
        logger.info("soalat az service gerefte mishe")
        return fetch_questions(get=get)
    raise ValueError(f"manba-e nashnakhte: {source}")