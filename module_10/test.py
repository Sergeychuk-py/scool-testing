import requests


def test_create_autor():
    request_body = {
        'age': '0',
        'name': 'test',
        'genre': 'some',
        'dateOfBirth': '',
        'dateOfDeath': '',
        'dead': False
    }
    response = requests.post('https://127.0.0.1:8080/api/authors/create', json=request_body)
    return response.json()










