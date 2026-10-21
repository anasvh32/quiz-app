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
    data = response.json()
    questions = parse_questions(data["questions"])
    logger.info("%d soal az service gerefte shod", len(questions))
    return questions