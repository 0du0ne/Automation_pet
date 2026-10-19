import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_all_fields()
        time.sleep(7)
        print('\n')
        assert full_name == output_full_name, 'Full name does not match'
        assert email == output_email, 'Email does not match'
        assert current_address == output_current_address, 'Current address does not match'
        assert permanent_address == output_permanent_address, 'Permanent address does not match'

class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        input_checkbox = [
            check_box_page.normalize_name(name)
            for name in input_checkbox
        ]

        output_result = [
            check_box_page.normalize_name(name)
            for name in output_result
        ]
        print(input_checkbox)
        print(output_result)
        assert set(input_checkbox) == set(output_result), 'Checkbox does not match'

class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radio_button_page.open()

        radio_button_page.click_on_the_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        assert output_yes == "Yes", "The 'Yes' button is not working"

        radio_button_page.click_on_the_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        assert output_impressive == "Impressive", "The 'Impressive' button is not working"

        radio_button_page.click_on_the_radio_button("no")
        output_no = radio_button_page.get_output_result()
        assert output_no == "No", "The 'No' button is not working"
