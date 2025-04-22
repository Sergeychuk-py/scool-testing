

class TestExample:
    def test_open(self, driver):
        driver.get("https://skillbox.ru")
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title

    def test_open_1(self, driver):
        driver.get("https://skillbox.ru")
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title

    def test_open_2(self, driver):
        driver.get("https://skillbox.ru")
        assert 'Skilbox – образовательная платформа с онлайн-курсами.' == driver.title
