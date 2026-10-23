# Adapter-e service-e soal. Hich input/print inja nist.
import logging

from requests.exceptions import Timeout

from fake_service import fake_get
from question import parse_questions

logger = logging.getLogger(__name__)

# fe'lan service-e sakhtegi, bedune internet (badan mishe get ro avaz kard)
SERVICE_URL = "http://example.test/questions"


class ServiceError(Exception):
    """khata-ye service: timeout, khata-ye server ya darkhast-e ghalat"""


class ServiceTimeout(ServiceError):
    """service be moal pasokh nadad"""


class ServerError(ServiceError):
    """khata az taraf-e server (status 5xx)"""


def fetch_questions(get=fake_get, url=SERVICE_URL):
    """soalat ro az service migire va list-e Question barmigardoone"""
    try:
        response = get(url, timeout=3)
    except Timeout:
        logger.error("service be moal pasokh nadad (%s)", url)
        raise ServiceTimeout("service be moal pasokh nadad.")

    status = response.status_code
    if status >= 500:
        logger.error("service khata dad, status %s", status)
        raise ServerError(f"service khata dad (status {status}).")
    if status >= 400:
        logger.error("darkhast ghalat bood, status %s", status)
        raise ServiceError(f"darkhast-e ma ghalat bood (status {status}).")

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