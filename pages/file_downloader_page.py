import os

import allure
from playwright.async_api import Page
from data_helper.assertions import Assertions
from pages.base import Base


class FileDownLoader(Base):
    FILE_TO_DOWNLOAD = "//a[contains(text(), '5mb script.xml')]"

    def __init__(self, page: Page) -> None:
        """
        Constructor for the FileDownLoader class.
        """
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Open the file downloader pager")
    def open_input_page(self):
        self.open(uri="download")
        return self

    @allure.step("Download file to the down_file directory")
    def download_file_from_downloader_page(self) -> str:
        return self.download_file(self.FILE_TO_DOWNLOAD)

    @allure.step("Is file downloaded")
    def is_file_downloaded(self) -> bool:
        file_name = self.download_file_from_downloader_page()
        target_directory = os.path.join(os.getcwd(), f"../download_file/{file_name}")
        return os.path.isfile(target_directory)
