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

    def is_main_page_opened(self):
        """
        Opens the main page and checks if the main page title is shown
        """
        title_name = "Onliner logo"
        self.open("")
        self.assertion.check_presence(self.MAIN_PAGE_TITLE,
                                      AssertMessage.TITLE_SHOULD_BE_SHOWN.value.format(title_name))

    def click_on_search_field(self) -> None:
        """
        Clicks on the fast search field.
        """
        self.click(self.FAST_SEARCH_FIELD)

    def input_text_to_search_field(self, text: str) -> None:
        """
        Inputs text into the fast search field.
        """
        self.input(self.FAST_SEARCH_FIELD, text)

    def is_text_entered_to_search_field(self, text: str) -> None:
        """
        Clicks on the search field, inputs text, and verifies if the entered text is displayed.
        """
        self.click_on_search_field()
        self.input_text_to_search_field(text)
        actual = self.switch_to_iframe_and_get_text(self.NEW_FRAME, self.SEARCH_INPUT_TEXT)
        self.assertion.check_equals(actual, text,
                                    AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(text))

    def scroll_to_footer_and_verify_loggo_presence(self) -> None:
        """
        Scrolls to the footer and verifies the presence of the footer logo.
        """
        self.scroll_to_element(self.FOOTER_LOGGO)

    def close_new_frame_window(self) -> None:
        """
        Closes the new frame window.
        """
        self.click(self.SEARCH_CLOSE)

    def is_footer_loggo_shown(self) -> None:
        """
        Verifies if the footer logo is shown.
        """
        footer_logo = "Footer logo"
        self.switch_to_iframe_and_click(self.NEW_FRAME, self.SEARCH_CLOSE)
        self.scroll_to_element(self.FOOTER_LOGGO)
        self.assertion.check_presence(self.FOOTER_LOGGO,
                                      AssertMessage.TITLE_SHOULD_BE_SHOWN.value.format(footer_logo))

    def move_to_basket_page(self):
        """
        Clicks on the basket icon/button to move to the basket page.
        """
        from pages.basket_page import Basket
        self.open("")
        self.click(self.BASKET)
        return Basket
