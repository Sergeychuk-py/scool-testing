import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestInput:
    def test_send_keys(self, driver):
        """Функция вводит указанное значение в input"""
        driver.get("")
        driver.find_element(By.ID, "username_1").send_keys("basic text")

    def test_clear_keys(self, driver):
        """Функция удаляет указанное значение в input"""
        driver.get("")
        el = driver.find_element(By.ID, "username_1")
        el.send_keys("basic text")
        el.clear()

    def test_copy_past(self, driver):
        """Функция выделяет нужный текст и копирует его в поле ввода, затем удаляет его,
         и вставляет заново в input"""
        driver.get("")
        el = driver.find_element(By.ID, "username_1")
        el.send_keys("basic text")

        action_shains = webdriver.ActionChains(driver)

        action_shains.key_down(Keys.COMMAND).send_keys("a").perform() #выделяем этой строкой текст в поле ввода который нужно скопировать
        action_shains.key_down(Keys.COMMAND).send_keys("c").perform() # копируем
        el.clear() #очищаем поле от символов
        el.click() #кликаем по полю ввода
        action_shains.key_down(Keys.COMMAND).send_keys("v").perform() #вставляем скопируемый текс в поле ввода

    def test_input_mask(self, driver):
        """Функция работает с input-маской, вставляет в поле ввода цифры"""
        driver.get("")
        el = driver.find_element(By.ID, "basic")
        value = "12345678"
        for c in value:
            el.send_keys(c)
            time.sleep(0.2)

    def test_input_filter(self, driver):
        driver.get("")
        driver.find_element(By.ID, "alpa").send_keys("asd123twe321")

    def test_input_tag(self, driver):
        """Функция вставляет слова в поле ввода"""
        driver.get("")
        driver.find_element(By.XPATH, "//input(3)").send_keys("skillbox" + Keys.ENTER)
        driver.find_element(By.XPATH, "//input(3)").send_keys("python" + Keys.ENTER)
        driver.find_element(By.XPATH, "//input(3)").send_keys("pytest" + Keys.ENTER)
