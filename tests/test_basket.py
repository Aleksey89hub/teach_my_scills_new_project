import pytest

from pages.basket_page import Basket
from pages.main_page import Main


@pytest.mark.smoke
@pytest.mark.usefixtures("browser")
class TestBasketPage:
    @pytest.mark.run(order=1)
    def test_verify_empty_basket_label_is_shown(self, browser):
        main_page = Main(browser)
        basket_page = Basket(browser)

        main_page.move_to_basket_page()
        basket_page.is_label_empty_basket_shown()
