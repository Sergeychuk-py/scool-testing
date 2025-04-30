from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSlider:
    def test_slider(self, driver):
        """Функция проверяет перетягивания ползунка, аналогично работает со splitter"""
        driver.get('https://practice-automation.com/slider/')
        el = driver.find_element(By.XPATH, "//*[@class='slider']")
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(el) \
            .move_by_offset(xoffset=50, yoffset=0).perform()  # зажимает левой кнопкой мыши ползунок click_and_hold,
        # чтобы сдвинуть xofset влево нужно указать минус перед int
        action_chains.release().perform()  # отпускает левую кнопки мышки
