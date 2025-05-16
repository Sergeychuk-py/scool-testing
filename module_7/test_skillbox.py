from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestSkillBox:
    def test_default_count(self, driver):
        """"Первый кейс тест(описание в readme.md)"""
        expected_text = 'Ещё 10 профессий из 152'
        driver.get('https://skillbox.ru')
        catalog = driver.find_element(By.XPATH, '//span[contains(text(), "Каталог")]')
        catalog.click()
        courses = driver.find_element(By.CSS_SELECTOR, 'a[href="/courses/"]')
        courses.click()
        actual_element = WebDriverWait(driver, timeout=60).until(
            lambda driver: driver.find_element(By.XPATH,
                                               '//button[@class="ui-load-more courses-block__load ui-button ui-button--stroke-main ui-button--big ui-button--icon ui-button--icon-left ui-button--stretch-sm-max"]'
                                               ))

        assert expected_text in actual_element.text

    def test_default_count_2(self, driver):
        """"Второй кейс тест(описание в readme.md)"""
        expected_text = 'Ещё 10 профессий из 142'
        driver.get('https://skillbox.ru')
        catalog = driver.find_element(By.XPATH, '//span[contains(text(), "Каталог")]')
        catalog.click()
        courses = driver.find_element(By.CSS_SELECTOR, 'a[href="/courses/"]')
        courses.click()
        WebDriverWait(driver, timeout=60).until(
            lambda driver: driver.find_element(By.XPATH,
                                               '//button[@class="ui-load-more courses-block__load ui-button ui-button--stroke-main ui-button--big ui-button--icon ui-button--icon-left ui-button--stretch-sm-max"]'
                                               )).click()
        actual_element = WebDriverWait(driver, timeout=60).until(
            lambda driver: driver.find_element(By.XPATH,
                                               '//button[@class="ui-load-more courses-block__load ui-button ui-button--stroke-main ui-button--big ui-button--icon ui-button--icon-left ui-button--stretch-sm-max"]'
                                               ))

        assert expected_text in actual_element.text
