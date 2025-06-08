import requests
from pretenders.client.http import HTTPMock

mock = HTTPMock("localhost", 8000)


def setup_ok():
    """Метод отвечает на get-запрос по пути онлайн"""
    mock.reset()  # сбрасываем мок
    mock.when('GET /admins_online').reply('{"Result":"OK"}', status=200)  # передаем метод запроса


def setup_error():
    mock.reset()
    mock.when('GET /admins_online').reply(status=500)


def test_mock():
    setup_ok()
    mock_url = mock.pretend_access_point + mock.pretend_access_path

    response = requests.get(f'http://{mock_url}/admins_online')

    assert response.text == '{"Result": "OK"}'
