import pytest


@pytest.fixture()
def prepare_data():
    return "test_name"


def some_decorator(function):
    def wrapper():
        print('Before function')
        function()
        print('After function')

    return wrapper


@some_decorator
def test_prepare(prepare_data):
    assert prepare_data == "test_name"
