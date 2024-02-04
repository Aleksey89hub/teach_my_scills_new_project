import allure
from faker import Faker
from playwright.async_api import Page

from data_helper.assertions import Assertions
from enumeration.assert_message import AssertMessage
from pages.base import Base


class AuthorizationWindow(Base):
    LOG_IN_BUTTON = "//div[contains(text(), 'Вход')]"
    INPUT_BUTTON = "//input[@placeholder='Ник или e-mail']"
    ENTER_BUTTON = "//button[contains(text(), 'Войти')]"
    WARN_MESSAGE_ENTER_PASSWORD = "//div[contains(text(),'Укажите пароль')]"
    WARN_MESSAGE_ENTER_NAME_OR_EMAIL = "//div[contains(text(),'Укажите ник или e-mail')]"
    PASSWORD_FIELD = "//input[@type = 'password']"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the AuthorizationWindow class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)
        self.fake = Faker()

    @allure.step("Click on the login button")
    def click_on_log_in_button(self) -> None:
        """
        Clicks on the login button field.
        """
        self.open("")
        self.click(self.LOG_IN_BUTTON)

    @allure.step("Click on the submit button")
    def click_on_submit_button(self) -> None:
        """
        Clicks on the submit button field.
        """
        self.click(self.ENTER_BUTTON)

    @allure.step("Enter text to the name field ")
    def enter_text_to_name_field(self, name: str = "") -> None:
        """
         Enter random text to log in field provided that function's parameter is blank  .
        """
        login_name = name
        if not login_name:
            login_name = self.fake.name()
        self.input(self.INPUT_BUTTON, login_name)

    @allure.step("Enter text to the password field")
    def enter_random_password_to_password_field(self) -> None:
        """
         Enter password to the password field.
        """

        random_password = self.fake.pystr(min_chars=8, max_chars=12)
        self.input(self.PASSWORD_FIELD, random_password)

    @allure.step("Clear locator '{1}'")
    def clear_input_fields(self, locator: str) -> None:
        """
         Clear input fields.
        """
        self.clear(locator)

    @allure.step("Is warning message shown")
    def is_warning_message_displayed_for_not_populated_password(self) -> None:
        """
        The warning message should be displayed provided that password is not entered
        """
        specify_value = "Укажите пароль"
        self.click_on_log_in_button()
        self.enter_text_to_name_field()
        self.click_on_submit_button()
        self.assertion.contain_text(self.WARN_MESSAGE_ENTER_PASSWORD, specify_value,
                                    AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(specify_value))

    @allure.step("Is warning message shown")
    def is_warning_message_displayed_for_not_populated_name_field(self) -> None:
        """
        The warning message should be displayed provided that name is not entered
        """
        specify_value = "Укажите ник или e-mail"
        self.clear_input_fields(self.INPUT_BUTTON)
        self.enter_random_password_to_password_field()
        self.click_on_submit_button()
        self.assertion.contain_text(self.WARN_MESSAGE_ENTER_NAME_OR_EMAIL, specify_value,
                                    AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(specify_value))
