import time

import requests
import requests_mock

with requests_mock.Mocker() as mock:  # контекстный менеджер with нужен, чтобы изолировать наш мок от других тестов
    mock.get(
        url='https://api.ezample.com/user/123',
        json={  # подменяем ответ сервеса
            'id': 123,
            'name': 'Sergey'
        },
        status_code=101,
        headers={"Sergey": "MOCk"}
    )
    response = requests.get('https://api.ezample.com/user/123')  # делаем запрос к этому эндпойту
    print(response.json())
    print(response.status_code)
    print(response.headers, '\n')

with requests_mock.Mocker() as mock:  # контекстный менеджер with нужен, чтобы изолировать наш мок от других тестов
    mock.post(
        url='https://api.ezample.com/user/123',
        json={  # подменяем ответ сервеса
            'id': 123,
            'name': 'Peter Parker'
        },
        status_code=200
    )
    response = requests.post('https://api.ezample.com/user/123',
                             json={"name": "Parker"}
                             )  # делаем запрос к этому эндпойту
    print(response.json())
    print(response.status_code, '\n')

with requests_mock.Mocker() as mock:  # создаем задержку от сервиса
    mock.get(url='https://api.ezample.com/user/123', json={"key": "value"})
    start_time = time.time()
    time.sleep(2.5)
    response = requests.get('https://api.ezample.com/user/123')
    end_time = time.time()

    print(end_time - start_time)
    print(response.json(), '\n')

"web_hook уведомления - это способ с помощью котого сторонний сервер отправляет в ваше предложение данные в ответ на какое либо событие"


def payment_webhook(data):
    """Обрабатыевает хук уведомления"""
    if data["type"] == 'payment_intent.succeeded':
        return f'Payment succeeded for ID: {data['data']['object']['id']}'
    elif data['type'] == 'payment_intent.payment_failed':
        return f'Payment failed for ID: {data['data']['object']['id']}'


with requests_mock.Mocker() as mock:
    mock.post(
        url='https://myapp.com/webhook',
        json={
            'type': 'payment_intent.succeeded',
            'data': {'object': {'id': 'pi_12345'}}
        }
    )

    webhook_response = requests.post(
        url='https://myapp.com/webhook',
        json={
            'type': 'payment_intent.succeeded',
            'data': {'object': {'id': 'pi_12345'}}
        }
    )

print(payment_webhook(webhook_response.json()))