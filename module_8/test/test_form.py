from module_8.pages.form_page import FormPage
from module_8.conftest import driver


class TestFormPage:
    def test_form(self, driver):
        fom_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        fom_page.open()
        first_name, last_name, email = fom_page.fill_fields_and_submit()
        result = fom_page.form_result()
        assert f'{first_name} {last_name}' == result[0]
        assert email == result[1]

