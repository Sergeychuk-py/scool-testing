import time

from selenium.webdriver import Keys
from module_8.pages.base_page import BasePage
from module_8.locator.form_page_locators import FormPageLocators


class FormPage(BasePage):
    def fill_fields_and_submit(self):
        first_name = 'Sergey'
        last_name = 'Scorov'
        email = 'serg@bk.ru'
        self.remove_footer()
        self.element_is_visible(FormPageLocators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(FormPageLocators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(FormPageLocators.EMAIL).send_keys(email)
        self.element_is_visible(FormPageLocators.GENDER).click()
        self.element_is_visible(FormPageLocators.MOBILE).send_keys('791229207273')
        subject = self.element_is_visible(FormPageLocators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.ENTER)
        self.element_is_visible(FormPageLocators.HOBBIES).click()
        self.element_is_visible(FormPageLocators.FILE_INPUT).send_keys(
            r'C:\Users\serge\PycharmProjects\scool-testing\module_8\test.txt')
        self.element_is_visible(FormPageLocators.CURRENT_ADRESS).send_keys('City, 1234, USA')

        self.element_is_visible(FormPageLocators.SUBMIT).click()
        return first_name, last_name, email

    def form_result(self):
        result_list = self.elements_are_visible(FormPageLocators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        # for i in result_list: метод цикла
        #     result_text.append(i.text)

        return result_text



