from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_attribute_to_include


class TestLog:
    def test_log(self, driver):
        driver.get('https://letcode.in/button')
        assert element_attribute_to_include(
            locator=(By.XPATH, '//button[@class="button is-info"]'),
            attribute_='Disabled'
        )(driver) is True
        pass
