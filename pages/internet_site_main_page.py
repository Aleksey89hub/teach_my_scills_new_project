import allure
from playwright.async_api import Page
from data_helper.assertions import Assertions
from pages.base import Base


class NewTheInternetMainPage(Base):
    INPUT_BUTTON = "//a[contains(text(), 'Inputs')]"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the NewTheInternetMainPage class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Open the main page")
    def open_main_page(self):
        self.open()
        return self

    @allure.step("Scroll to the input section")
    def scroll_to_input_section(self):
        self.scroll_to_element(self.INPUT_BUTTON)
        return self

    @allure.step("Click on the input section")
    def click_on_input_section(self):
        self.click(self.INPUT_BUTTON)
        return self
