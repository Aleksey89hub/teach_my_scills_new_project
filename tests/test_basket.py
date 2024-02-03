import allure
import pytest


@pytest.mark.skip
@pytest.mark.usefixtures("setup_main", "setup_basket", "setup_catalog")
class TestBasketPage:
    @pytest.mark.run(order=1)
    @allure.title("Verify that the label 'empty basket' is shown")
    def test_verify_empty_basket_label_is_shown(self, setup_main, setup_basket):
        setup_main.move_to_basket_page()
        setup_basket.is_label_empty_basket_shown()

    @pytest.mark.run(order=2)
    @allure.title("Verify that a item is added to basket")
    def test_verify_item_is_added_to_basket(self, setup_basket, setup_catalog):
        setup_basket.click_on_catalog_field()
        setup_catalog.verify_that_item_is_added_to_basker("iPhone 15")
