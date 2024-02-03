import allure

from enumeration.assert_message import AssertMessage
from pages.base import Base
from data_helper.assertions import Assertions
from playwright.sync_api import Page


class Main(Base):
    """
    The Main class represents the main page of the application.
    It contains methods to interact with elements on the main page.
    """

    MAIN_PAGE_TITLE = "//*[@class='b-top-logo']"
    FAST_SEARCH_FIELD = "//input[@class = 'fast-search__input']"
    SEARCH_INPUT_TEXT = "//span[@class = 'text_match']"
    NEW_FRAME = "//iframe[@class ='modal-iframe']"
    FOOTER_LOGGO = "//div[@class ='footer-style__logo']"
    SEARCH_CLOSE = "//span[@class = 'search__close']"
    BASKET = "//a[@title ='Корзина']"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the Main class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Is main page opened")
    def is_main_page_opened(self):
        """
        Opens the main page and checks if the main page title is shown
        """
        title_name = "Onliner logo"
        self.open("")
        self.assertion.check_presence(self.MAIN_PAGE_TITLE,
                                      AssertMessage.TITLE_SHOULD_BE_SHOWN.value.format(title_name))

    @allure.step("Click on search field button")
    def click_on_search_field(self) -> None:
        """
        Clicks on the fast search field.
        """
        self.click(self.FAST_SEARCH_FIELD)

    @allure.step("Input text '{1}' to the search field")
    def input_text_to_search_field(self, text: str) -> None:
        """
        Inputs text into the fast search field.
        """
        self.input(self.FAST_SEARCH_FIELD, text)

    @allure.step("Is '{1}' text entered to search field")
    def is_text_entered_to_search_field(self, text: str) -> None:
        """
        Clicks on the search field, inputs text, and verifies if the entered text is displayed.
        """
        self.click_on_search_field()
        self.input_text_to_search_field(text)
        actual = self.switch_to_iframe_and_get_text(self.NEW_FRAME, self.SEARCH_INPUT_TEXT)
        self.assertion.check_equals(actual, text,
                                    AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(text))

    @allure.step("Scroll to the footer on the main page")
    def scroll_to_footer(self) -> None:
        """
        Scrolls to the footer.
        """
        self.scroll_to_element(self.FOOTER_LOGGO)

    @allure.step("Close the new frame")
    def close_new_frame_window(self) -> None:
        """
        Closes the new frame window.
        """
        self.click(self.SEARCH_CLOSE)

    @allure.step("Is the footer logo shown")
    def is_footer_logo_shown(self) -> None:
        """
        Verifies if the footer logo is shown.
        """
        footer_logo = "Footer logo"
        self.switch_to_iframe_and_click(self.NEW_FRAME, self.SEARCH_CLOSE)
        self.scroll_to_element(self.FOOTER_LOGGO)
        self.assertion.check_presence(self.FOOTER_LOGGO,
                                      AssertMessage.TITLE_SHOULD_BE_SHOWN.value.format(footer_logo))

    @allure.step("Move to the basket page")
    def move_to_basket_page(self):
        """
        Clicks on the basket icon/button to move to the basket page.
        """
        self.open("")
        self.click(self.BASKET)

    @allure.step("Is a '{1}' displayed")
    def is_tab_displayed(self, tab_name: str) -> None:
        """
        Verifies if the tab is shown.
        """
        self.assertion.is_element_present(f"//span[contains(text(), '{tab_name}')]")
