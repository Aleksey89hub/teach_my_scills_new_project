from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def have_text(self, locator, text: str, msg) -> None:
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text), msg

    def check_presence(self, locator, msg) -> None:
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000), msg

    def check_absence(self, locator, msg) -> None:
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700), msg

    def check_equals(self, actual, expected, msg) -> None:
        assert actual == expected, msg

    def to_be_empty(self, locator, msg) -> None:
        loc = self.page.locator(locator)
        expect(loc).to_be_empty(), msg

    def contain_text(self, locator, text: str, msg) -> None:
        loc = self.page.locator(locator)
        expect(loc).to_contain_text(text), msg
