import allure
import pytest

from enumeration.assert_message import AssertMessage
from pages.file_downloader_page import FileDownLoader
from pages.inputs_page import InputPage
from pages.java_script_alerts_page import JavaScriptAlertPage
from pages.internet_site_main_page import NewTheInternetMainPage
from pages.opening_new_window_page import OpenNewWindowPage


@pytest.mark.smoke
class TestHomeWorkSeven:
    @pytest.mark.run(order=1)
    @allure.title("Verify click and input text")
    def test_click_and_input_text(self, browser):
        hero_kuapp = NewTheInternetMainPage(browser)
        input_page = InputPage(browser)
        random_number = str(input_page.fake.random_number(digits=5))
        hero_kuapp.open_main_page() \
            .scroll_to_input_section() \
            .click_on_input_section()
        input_page.enter_text_into_input_field(random_number)

        assert input_page.get_text_from_input_field() == random_number, \
            AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(random_number)

    @pytest.mark.run(order=2)
    @allure.title("Verify the text is removed")
    def test_clean_text(self, browser):
        input_page = InputPage(browser)
        input_page.clear_input_text_field()

        assert not input_page.get_text_from_input_field(), \
            AssertMessage.FIELD_SHOULD_BE_CLEANED.value

    @allure.title("Verify the alert is dismissed")
    def test_verify_alert_dismissal(self, browser):
        js_alert_page = JavaScriptAlertPage(browser)
        js_alert_page.open_js_alert_page()

        assert js_alert_page.is_alert_dismissed(), \
            AssertMessage.ALERT_SHOULD_BE_DISMISSED.value

    @allure.title("Verify a new tab is opened")
    def test_new_window_tab(self, browser):
        open_new_window = OpenNewWindowPage(browser)
        new_window_title_text = "New Window"
        open_new_window.open_new_window_page()

        assert open_new_window.switch_to_new_tab_and_get_text() == new_window_title_text, \
            AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(new_window_title_text)

    @allure.title("Verify the file is downloaded")
    def test_that_file_is_downloaded(self, browser, remove_data):
        file_downloader = FileDownLoader(browser)
        file_downloader.open_input_page()

        assert file_downloader.is_file_downloaded(), AssertMessage.FILE_SHOULD_BE_DOWNLOADED.value
