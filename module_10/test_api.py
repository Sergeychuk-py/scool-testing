import requests


def test_create_autor():
    """Тест на создание post запрос"""
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
    deserialized_response = response.json()  # десериализуем

    print(response.text)
    assert response.status_code == 200  # проверяем кода ответа
    assert deserialized_response['age'] == request_body['age']  # проверяем ли равны данные


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
    response = requests.get(f'https://127.0.0.1:8080/api/authors/create{created_autor['id']}')
    assert response.status_code == 200
    assert response.json() == created_autor


def test_update():
    """"Тест на обновление"""
    created_autor = create_autor()
    update_request_body = {  # тело
        'age': 555,
        'name': 'tests',
        'genre': 'we',
        'dateOfBirth': '05.06.2025',
        'dateOfDeath': '22.33.44.',
        'dead': True
    }
    response = requests.put(f'https://127.0.0.1:8080/api/authors/create{created_autor['id']}', json=update_request_body)
    parsed_response = response.json()

    assert response.status_code == 200
    assert parsed_response['id']
    del parsed_response['id']
    assert parsed_response == update_request_body


def test_delete():
    """"Тест на удаление"""
    created_autor = create_autor()
    delete_response = requests.delete(f'https://127.0.0.1:8080/api/authors/create{created_autor['id']}')
    assert delete_response.status_code == 200

    get_autor_response = requests.get(f'https://127.0.0.1:8080/api/authors/create{created_autor['id']}')
    assert get_autor_response == 500

    