# test_service_errors.py
import pytest

from fake_service import FakeResponse, fake_get_timeout
from service import ServerError, ServiceError, ServiceTimeout, fetch_questions


def get_returning(response):
    """yek get-e sakhtegi misaze ke hamishe hamin response ro bar migardoone"""

    def my_get(url, timeout=None):
        return response

    return my_get


def test_timeout_raises_service_timeout():
    """vaghti service be moal pasokh nade, bayad ServiceTimeout bede"""
    with pytest.raises(ServiceTimeout):
        fetch_questions(get=fake_get_timeout)


def test_status_500_raises_server_error():
    """status 500 yaani khata az taraf-e server, bayad ServerError bede"""
    with pytest.raises(ServerError, match="500"):
        fetch_questions(get=get_returning(FakeResponse(500, {})))


def test_status_404_is_not_a_server_error():
    """status 404 yaani darkhast-e khode ma ghalat bood, na server"""
    with pytest.raises(ServiceError) as error:
        fetch_questions(get=get_returning(FakeResponse(404, {})))

    assert not isinstance(error.value, ServerError)