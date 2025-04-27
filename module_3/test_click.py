from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClick:
    def test_click(self, driver):
        """Кликаем по кнопке, она открывает кнопку delete и кликаем по кнопке delete и она закрывается"""
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        driver.find_element(By.XPATH, '//button').click()
        driver.find_element(By.XPATH, '//button[@class="added-manually"]').click()

    def test_failed_click(self, driver):
        """по перекрытым элементам нелья кликать"""
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        driver.find_element(By.XPATH, '//button').click()

    def test_double_click(self, driver):
        """Кликаем по кнопке двойным нажатием"""
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(driver.find_element(By.XPATH, '//button[@class="added-manually"]')).perform()
        #для двойного нажатия кнопки используем double_click(помещаем в него нужный атрибут)

    def test_checkbox(self, driver):
        """"Функция кликает по checkbox"""
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        driver.find_element(By.XPATH, '//input'[0]).click()

    def test_drop_down(self, driver):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        driver.find_element(By.XPATH, "//*[@id='dropdown']").click()
        pass

    def test_calendar(self, driver):
        driver.get("https://practice-automation.com/calendars/")
        driver.find_element(By.XPATH, "//*/input[@id='g1065-2-1-selectorenteradate']").click()
        pass

