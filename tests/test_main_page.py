import pytest

from pages.main_page import Main


@pytest.mark.smoke
@pytest.mark.usefixtures("browser")
class TestMainPage:
    @pytest.mark.run(order=1)
    def test_verify_logo_is_present(self, browser):
        self.m = Main(browser)
        self.m.is_main_page_opened()

    @pytest.mark.run(order=2)
    def test_enter_text_in_search_field(self, browser):
        self.m = Main(browser)
        self.m.is_text_entered_to_search_field("Phone")

    @pytest.mark.run(order=3)
    def test_scroll_to_footer_loggo(self, browser):
        self.m = Main(browser)
        self.m.is_footer_loggo_shown()
