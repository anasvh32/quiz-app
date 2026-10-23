# Service-e sakhtegi-ye soal (baraye test, bedune internet)
from requests.exceptions import Timeout


class FakeResponse:
    """shabih-e javab-e yek service: yek status_code va yek JSON"""

    def __init__(self, status_code, data):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data


SAMPLE_QUESTIONS = {
    "questions": [
        {"question": "Paytakht Iran kojast?", "answer": "Tehran"},
        {
            "question": "Paytakht Fransa kodoom ast?",
            "kind": "choice",
            "choices": ["Landan", "Paris", "Roum"],
            "answer": "Paris",
        },
    ]
}


def fake_get(url, timeout=None):
    """jaye requests.get: be jaye internet, hamishe yek javab-e sakhtegi mide"""
    return FakeResponse(200, SAMPLE_QUESTIONS)


def fake_get_timeout(url, timeout=None):
    """service be moal pasokh nemide, mesle requests ye Timeout mikhore"""
    raise Timeout("service pasokh nadad")