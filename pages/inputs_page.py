import allure
from faker import Faker
from playwright.async_api import Page

from data_helper.assertions import Assertions
from pages.base import Base


class InputPage(Base):
    INPUT_TEXT_FIELD = "//input[@type='number']"
    TITLE = "//h3[contains(text(), 'Inputs')]"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the InputPage class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)
        self.fake = Faker()

    @allure.step("Open the Input Page")
    def open_input_page(self):
        self.open(uri="inputs")
        return self

    @allure.step("Click on the Input Text Field")
    def click_on_input_text_field(self):
        self.click(self.INPUT_TEXT_FIELD)
        return self

    @allure.step("Enter '{text}' into the Input Text Field")
    def enter_text_into_input_field(self, text: str):
        self.input(self.INPUT_TEXT_FIELD, text)
        return self

    @allure.step("Retrieve text from the Input Text Field")
    def get_text_from_input_field(self):
        return self.get_text(self.INPUT_TEXT_FIELD, 0)

    @allure.step("Clear the Input Text Field")
    def clear_input_text_field(self):
        self.clear(self.INPUT_TEXT_FIELD)
        return self
