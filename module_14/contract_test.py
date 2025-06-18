import requests
from pactman import Consumer, Provider

pact = Consumer('FitnessMobileApp').has_pact_with(Provider('FitnessApi'))

head_count_uri = "/meta/head-count"


def test_club_has_people():
    pact \
        .given('there are 5 people in sports club') \
        .upon_receiving('request to get people heead-count') \
        .with_request('get', head_count_uri) \
        .will_respond_width(200, body='5')

    pact \
        .given('sports club is closed') \
        .upon_receiving('request to get people heead-count') \
        .with_request('get', head_count_uri) \
        .will_respond_width(200, body='closed')

    with pact:
        requests.get(pact.uri + head_count_uri)
        requests.get(pact.uri + head_count_uri)

# 11 строка - условие контракта, которое должно быть выполненно
# 12 строка запрос который выполняем
# 13 строка, каким методом и адресом выполняется запрос
# 14 строка, что мы хотим получить, какой код(первый параметр) и какое тело(body)

