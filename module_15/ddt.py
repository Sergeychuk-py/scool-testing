from ddt import data, file_data

import ddt
import pytest
import random
import unittest

values = [1, 2, 3, 4, 5]


@pytest.mark.parametrize('number', values)
def test(number):
    """"Работа со списками"""
    print(number)


values_2 = [
    ('1', '2', '1'),
    ('0', '0', '0'),
    ('13', '23', '13')
]


@pytest.mark.parametrize('one, two, three', values_2)
def test_two(one, two, three):
    """В случаи с несколькими переменными, используем кортежи"""
    print(one, two, three)


@pytest.mark.parametrize('x', [0, 1])
@pytest.mark.parametrize('y', [2, 3])
def test_three(x, y):
    """"Также можно использовать два декоратора, для перебора всех возможных вариатнов"""
    print(x, y)


def get_pozitiv():
    return random.randint(1, 100)


def get_negativ():
    return random.randint(-100, 1)


@pytest.mark.parametrize('number', [get_pozitiv(), get_negativ()])
def test_four(number):
    """"С помощью методотов"""
    print(number)


@ddt
class FooTestCase(unittest.TestCase):

    @data(3, 4, 12, 23)
    def test_langer_than_two(self, value_5):
        self.assertTrue(value_5 > 2)

    @file_data('test_data_dict_dict.json')
    def test_data_dict_dict(self, start, end, value_5):
        self.assertTrue(start, end)
        self.assertTrue(value_5, end)
        self.assertTrue(value_5, start)
