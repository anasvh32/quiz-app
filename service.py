# Adapter-e service-e soal. Hich input/print inja nist.
import logging

from fake_service import fake_get
from question import parse_questions

logger = logging.getLogger(__name__)

# fe'lan service-e sakhtegi, bedune internet (badan mishe get ro avaz kard)
SERVICE_URL = "http://example.test/questions"


def fetch_questions(get=fake_get, url=SERVICE_URL):
    """soalat ro az service migire va list-e Question barmigardoone"""
    response = get(url, timeout=3)

    try:
        data = response.json()
    except ValueError:
        logger.error("javab-e service JSON-e moatabar nabud")
        raise ValueError("javab-e service kharabe (JSON moatabar nist).")

    if not isinstance(data, dict) or "questions" not in data:
        logger.error("javab-e service kelid-e 'questions' nadasht")
        raise ValueError("javab-e service shekl-e dorost nadare (kelid-e 'questions' nist).")

    try:
        questions = parse_questions(data["questions"])
    except (AttributeError, TypeError):
        logger.error("shekl-e soalat-e service ghalate")
        raise ValueError("shekl-e soalat-e service ghalate.")

    logger.info("%d soal az service gerefte shod", len(questions))
    return questions