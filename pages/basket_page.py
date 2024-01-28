import allure
from playwright.sync_api import Page

from data_helper.assertions import Assertions
from enumeration.assert_message import AssertMessage
from pages.base import Base


class Basket(Base):
    BASKET_IS_EMPTY_TITLE = "//div[normalize-space(text()) = 'Ваша корзина пуста']"
    CATALOG = "//a[text() ='каталог']"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the Basket class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Is the label empty basket shown")
    def is_label_empty_basket_shown(self) -> None:
        """
        Verifies if the label empty basket is shown.
        """

        expected_result = 'Ваша корзина пуста'
        actual_result = self.get_text(self.BASKET_IS_EMPTY_TITLE, 0).strip()
        self.assertion.check_equals(actual_result, expected_result,
                                    AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(expected_result))

    @allure.step("Click on the catalog field")
    def click_on_catalog_field(self) -> None:
        """
        Clicks on the catalog button.
        """
        self.click(self.CATALOG)
