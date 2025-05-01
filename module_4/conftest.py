import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    options = Options()
    options.page_load_strategy = 'normal'  # выбераем тип ожидания по умолчанию "normal"
    # driver.implicitly_wait(5) # явное ожидание
    yield driver
