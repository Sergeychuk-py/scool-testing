import pytest
import logging.config

from os import path
from selenium import webdriver

lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(lof_file_path)


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
