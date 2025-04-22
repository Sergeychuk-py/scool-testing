from selenium.webdriver.common.by import By


class TestExample_1:
    def test_find_elements(self, driver):
        driver.get("https://the-internet.herokuapp.com/login")
        elem_id = driver.find_elements(By.ID, "username")
        elem_name = driver.find_elements(By.NAME, "username")
        elem_class = driver.find_element(By.CLASS_NAME, "subheader")
        elem_xpath = driver.find_element(By.XPATH, "//form/descendant::input[@id='password']")
        elem_css = driver.find_elements(By.CSS_SELECTOR, "form input#password")
        """"Три способа найти определённый нужный элемент"""
        elem_input_1 = driver.find_element(By.XPATH, "//input")
        elem_input_2 = driver.find_element(By.CSS_SELECTOR, "input")
        elem_input_3 = driver.find_element(By.TAG_NAME, "input")
        """Поиск элемента с текстом"""
        driver.get("https://the-internet.herokuapp.com")
        elem_link_text = driver.find_element(By.LINK_TEXT, "Checkboxes")
        """Поиск элемента одного определенного слова в тексте"""
        elem_link_text_1 = driver.find_elements(By.PARTIAL_LINK_TEXT, "Auth")
        pass

