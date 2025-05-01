from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def test_wait(self, driver):
        driver.get("https://github.com")
        driver.find_element(By.XPATH,
                            '//*[contains(text(), "Join the world’s most widely adopted AI-powered developer platform.")]')

    def test_wait_types(self, driver):
        driver.get("https://github.com")
        # driver.find_element(By.PARTIAL_LINK_TEXT, '//*[contains(text(), "Join the world’s most widely adopted AI-powered developer platform.")]')
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(
            By.XPATH, '//*[contains(text(), "Join the world’s most widely adopted AI-powered developer platform.")]'
        ))  # явное ожидание загрузки на странице определеного элемента

    def test_wait_forms(self, driver):
        driver.get('https://practice-automation.com/form-fields/')
        driver.find_element(By.XPATH, "//*[@id='name-input']").send_keys('Sergey')
        driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys('skillbox')
        driver.find_element(By.NAME, 'fav_drink').click()
        WebDriverWait(driver, timeout=5).until(
            lambda d: d.find_element(By.XPATH, "//*[@id='color4']")
        )
        driver.find_element(By.XPATH, "//*[@id='color4']").click()
        pass
