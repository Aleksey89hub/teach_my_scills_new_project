from playwright.async_api import FrameLocator
from playwright.sync_api import Page, TimeoutError, Response
from data_helper.environment import host


class Base:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    def click(self, locator: str) -> None:
        self.page.click(locator)

    def input(self, locator: str, data: str) -> None:
        self.page.locator(locator).fill(data)

    def scroll_to_element(self, locator: str) -> None:
        loc = self.page.locator(locator)
        loc.scroll_into_view_if_needed(timeout=12000)

    def switch_to_frame(self, iframe_locator: str) -> "FrameLocator":
        return self.page.frame_locator(iframe_locator)

    def switch_to_iframe_and_get_text(self, iframe_locator,
                                      locator: str, ) -> str:
        frame = self.switch_to_frame(iframe_locator)
        if frame is not None:
            return frame.locator(locator).text_content()
        else:
            print("Iframe not found with the specified locator:", iframe_locator)

    def switch_to_iframe_and_click(self, iframe_locator,
                                   locator: str, ) -> None:
        frame = self.switch_to_frame(iframe_locator)
        if frame is not None:
            frame.locator(locator).click()
        else:
            print("Iframe not found with the specified locator:", iframe_locator)

    def get_text(self, locator: str,
                 index: int) -> str:
        return self.page.locator(locator).nth(index).text_content()

    def wait_for_element(self, locator, timeout=12000) -> None:
        self.page.wait_for_selector(locator, timeout=timeout)

    def current_url(self) -> str:
        return self.page.url

    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, timeout=10000)
        except TimeoutError as e:
            return False
        return True

    def is_element_NOT_presence(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, timeout=5000)
        except TimeoutError as e:
            return True
        return False

    def selector(self, locator: str, value: str) -> None:
        self.page.select_option(locator, value)

    def drag_and_drop(self, source, target) -> None:
        self.page.drag_and_drop(source, target)

    def alert_accept(self, locator: str) -> None:
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.click(locator)

    def refresh(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')

    def switch_to_iframe_and_input(self, iframe_locator,
                                   locator_for_input,
                                   data: str) -> None:
        frame = self.page.frame_locator(iframe_locator)
        if frame is not None:
            frame.locator(locator_for_input).fill(data)
        else:
            print("Iframe not found with the specified locator:", iframe_locator)
