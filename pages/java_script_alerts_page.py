import allure
from playwright.async_api import Page

from data_helper.assertions import Assertions
from pages.base import Base


class JavaScriptAlertPage(Base):
    CLICK_ALERT = "//button[contains(text(), 'Click for JS Alert')]"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the JavaScriptAlertPage class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Open js alert page")
    def open_js_alert_page(self):
        self.open(uri="javascript_alerts")
        return self

    @allure.step("Click on the alert page")
    def click_on_alert(self):
        self.click(self.CLICK_ALERT)
        return self

    @allure.step("Click on the alert page")
    def is_alert_dismissed(self):
        return self.is_alert_accepted()
