from selenium.webdriver.common.by import By


def test_name_tag(driver):
    """Поиск одного слова в тексте"""
    driver.get("https://the-internet.herokuapp.com/login")
    h_text = driver.find_element(By.TAG_NAME, "h4")
    assert "tomsmith" in h_text.text