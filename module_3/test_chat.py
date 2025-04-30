from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCharts:
    def test_tooltip(self, driver):
        """"проверяет кнопку в которой счетчик, у меня без ссылок, так как нет примера"""
        driver.get("")
        el = driver.find_element(By.XPATH, "")
        actions_chains = webdriver.ActionChains(driver)
        actions_chains.move_to_element(el).perform()
        driver.find_element(By.XPATH, "").click()
        driver.find_element(By.XPATH, "").click()
        driver.find_element(By.XPATH, "").click()
        pass

    def test_canvas_pie(self, driver):
        """"Наводим на нужную часть пирога-графика, у меня без ссылок и локаторов, так как нет примера"""
        driver.get("")
        actions_chains = webdriver.ActionChains(driver)
        actions_chains.move_to_element(driver.find_element(By.CSS_SELECTOR, "")).perform() #movi_to_element направляет мышку на определенный элмент
        pass

    def test_table(self, driver):
        driver.get("https://practice-automation.com/tables/")
        driver.find_element(By.XPATH, "//*[@id='dt-search-0']").send_keys('Россия')
