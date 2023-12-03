import time
from pages.elements_page import TextBoxPage
from conftest import driver
class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            print(text_box_page.check_filled_form())

            time.sleep(10)