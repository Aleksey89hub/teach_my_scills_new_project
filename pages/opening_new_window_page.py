import allure
from playwright.async_api import Page
from data_helper.assertions import Assertions
from pages.base import Base


class OpenNewWindowPage(Base):
    CLICK_HERE_BUTTON = "//a[contains(text(), 'Click Here')]"
    NEW_WINDOW_TITLE = "//h3[contains(text(), 'New Window')]"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the OpenNewWindowPage class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Open the new window page")
    def open_new_window_page(self):
        self.open(uri="windows")
        return self

    @allure.step("Switch to a new tab and get text")
    def switch_to_new_tab_and_get_text(self) -> str:
        return self.open_new_tab_and_get_text(self.CLICK_HERE_BUTTON, self.NEW_WINDOW_TITLE)
