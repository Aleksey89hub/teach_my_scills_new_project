import allure
import pytest


@pytest.mark.skip
@pytest.mark.usefixtures("setup_main", )
class TestMainPage:
    @pytest.mark.run(order=1)
    @allure.title("Verify that the logo is present")
    def test_verify_logo_is_present(self, setup_main):
        setup_main.is_main_page_opened()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("tab", ["Ноутбуки", "Телевизоры", "Видеокарты"])
    @allure.title("Verify that tabs are displayed")
    def test_verify_tabs_are_displayed(self, setup_main, tab):
        setup_main.is_tab_displayed(tab)

    @pytest.mark.run(order=3)
    @allure.title("Verify that text is saved after being entered")
    def test_enter_text_in_search_field(self, setup_main):
        setup_main.is_text_entered_to_search_field("Phone")

    @pytest.mark.run(order=4)
    @allure.title("Verify that the loggo in the footer section is displayed")
    def test_scroll_to_footer_loggo(self, setup_main):
        setup_main.is_footer_logo_shown()
