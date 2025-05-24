from selenium.webdriver.common.by import By


class FormPageLocators:
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, 'label[for="gender-radio-1"]')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]')
    FILE_INPUT = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADRESS = (By.CSS_SELECTOR, '#currentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
