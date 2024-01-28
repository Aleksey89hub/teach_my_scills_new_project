import allure
from playwright.async_api import Page

from data_helper.assertions import Assertions
from enumeration.assert_message import AssertMessage
from pages.base import Base


class Catalog(Base):
    CATALOG_SEARCH = "//input[@class = 'fast-search__input']"
    NEW_FRAME = "//iframe[@class = 'modal-iframe']"
    CATALOG_ITEM = "//ul[@class='search__results']//li[1]//a[contains(@class, 'button')]"
    ADD_ITEM_TO_BASKET = "//div[@class='offers-list__group']/div[1]//div[contains(@class, 'helpers_hide_ta')]//a[contains(text(), 'В корзин')]"
    MOVE_TO_BASKET_BUTTON = "//a[contains(text(), 'Перейти в корзину')]"
    BASKET_TITLE = "//div[contains(text(), 'Корзина')]"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the Catalog class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Click to the search field")
    def click_on_search_field(self) -> None:
        """
        Clicks on the search field.
        """
        self.click(self.CATALOG_SEARCH)

    @allure.step("Move to the basket button")
    def move_to_basket_button(self) -> None:
        """
        Move to basket button.
        """
        self.click(self.MOVE_TO_BASKET_BUTTON)

    @allure.step("Add the first item to basket")
    def add_first_item_to_basket(self) -> None:
        """
        Add the first item to basket.
        """
        self.scroll_to_element(self.ADD_ITEM_TO_BASKET)
        self.click(self.ADD_ITEM_TO_BASKET)

    @allure.step("Input the '{1}' text to the search field")
    def input_text_to_search_field(self, text: str) -> None:
        """
        Inputs text into the catalog search field.
        """
        self.input(self.CATALOG_SEARCH, text)

    @allure.step("Switch to a new frame and click on the item")
    def switch_to_new_frame_and_click_on_new_item(self) -> None:
        """
        Switch to the new frame.
        """
        self.switch_to_iframe_and_click(self.NEW_FRAME, self.CATALOG_ITEM)

    @allure.step("Get the '{1}' text from the first item")
    def get_text_from_first_item(self, text: str) -> str:
        """
        Get text from the first item.
        """
        return self.get_text(f"//a[contains(text(), '{text}')]", 0)

    @allure.step("Verify the {1} item is added to the basket")
    def verify_that_item_is_added_to_basker(self, item_name: str) -> None:
        self.click_on_search_field()
        self.input_text_to_search_field(item_name)
        self.switch_to_new_frame_and_click_on_new_item()
        self.add_first_item_to_basket()
        self.move_to_basket_button()
        self.assertion.contain_text(f"//a[contains(text(), '{item_name}')]", item_name,
                                    AssertMessage.TEXT_SHOULD_BE_SHOWN.value.format(item_name))
        self.assertion.check_presence(self.BASKET_TITLE, AssertMessage.TITLE_SHOULD_BE_SHOWN.value.format("Корзина"))
