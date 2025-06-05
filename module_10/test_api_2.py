import requests

""" CRUD-API-тесты"""


def create_autor():
    """Тест на чтение post запрос"""
    request_body = {  # тело
        'age': 0,
        'name': 'test',
        'genre': 'some',
        'dateOfBirth': '',
        'dateOfDeath': '',
        'dead': False
    }
    response = requests.post('https://127.0.0.1:8080/api/authors/create',
                             json=request_body)  # указываем адрес созданного нами json-файла
    return response.json()


def test_get_autor():
    """Вызываем метод и проверяем, что данные одинаковые"""
    created_autor = create_autor()

    request_header = {
        'Accept': 'application/json'
    }

    response = requests.get(f'https://127.0.0.1:8080/api/authors/create{created_autor['id']}', headers=request_header)
    assert response.status_code == 200
    assert response.json() == created_autor
