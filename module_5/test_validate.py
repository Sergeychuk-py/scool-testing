from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_attribute_to_include


class TestValidate:
    def test_validate(self, driver):
        driver.get("https://letcode.in/frame")
        test_name = driver.find_element(By.NAME, 'name="fname"')
        test_name.send_keys('Sergey')
        assert test_name.get_attribute(
            'value') == 'Sergey'  # get+attribute метод который может вытащить значение атрибута

    def test_checkbox(self, driver):
        driver.get('https://letcode.in/forms')
        checkbox = driver.find_element(By.XPATH, '//label[@class="checkbox"]')

        checkbox.click()
        assert checkbox.is_selected() is True # метод is_selected в данном случае проверяет поставлен ли флажок

    def test_disabled(self, driver):
        driver.get('https://letcode.in/button')
        assert element_attribute_to_include(
            locator=(By.XPATH, '//button[@class="button is-info"]'),
            attribute_='Disabled'
        )(driver) is True
        pass




















