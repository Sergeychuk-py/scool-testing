import json

import requests
import dict2xml



class Autor(object):
    def __init__(self, age, name, genre, dateOfBirth, dateOfDeath, dead, id):
        self.age = age
        self.name = name
        self.genre = genre
        self.dateOfBirth = dateOfBirth
        self.dateOfDeath =dateOfDeath
        self.dead = dead
        self.id =id


def object_create_autor():
    request_body = Autor(age=0, name='someName', genre='SomeGenre', dateOfBirth='', dateOfDeath='', dead=False)

    response = requests.post('https://127.0.0.1:8080/api/authors/create', json=request_body.__dict__)
    return Autor(**json.loads(response.text))


def test_deserialize():
    created_autor = object_create_autor()

    response = requests.get(f'https://127.0.0.1:8080/api/authors/create/{created_autor.id}')
    deserialized_autor = Autor(**json.loads(response.text))

    assert deserialized_autor.dead == created_autor.dead
    assert deserialized_autor.name == created_autor.name
    assert deserialized_autor.dateOfDeath == created_autor.dateOfDeath


def test_xml():
    request_body = Autor(age=0, name='someName', genre='SomeGenre', dateOfBirth='', dateOfDeath='', dead=False)
    serialized_xml = dict2xml.dict2xml(request_body, 'Create Autor')
    print(serialized_xml)























