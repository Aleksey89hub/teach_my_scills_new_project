import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from dotenv import load_dotenv
import hashlib
import os
from slugify import slugify
import allure

from pages.authorization_page import AuthorizationWindow
from pages.basket_page import Basket
from pages.catalog_page import Catalog
from pages.main_page import Main

load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--bn', action='store', default="chrome", help="Choose browser: chrome, remote_chrome or firefox")
    parser.addoption('--h', action='store', default=False, help='Choose headless: True or False')
    parser.addoption('--s', action='store', default={'width': 1920, 'height': 1080}, help='Size window: width,height')
    parser.addoption('--slow', action='store', default=200, help='Choose slow_mo for robot action')
    parser.addoption('--t', action='store', default=60000, help='Choose timeout')
    parser.addoption('--l', action='store', default='en-US', help='Choose locale')


@pytest.fixture(scope='class', autouse=True)
def browser(request) -> Page:
    playwright = sync_playwright().start()
    if request.config.getoption("bn") == 'remote_chrome':
        browser = get_remote_chrome(playwright, request)
        context = get_context(browser, request, 'remote')
        page_data = context.new_page()
    elif request.config.getoption("bn") == 'firefox':
        browser = get_firefox_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    elif request.config.getoption("bn") == 'chrome':
        browser = get_chrome_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


@pytest.fixture(scope='class')
def setup_main(browser) -> Main:
    return Main(browser)


@pytest.fixture(scope='class')
def setup_basket(browser) -> Basket:
    return Basket(browser)


@pytest.fixture(scope='class')
def setup_catalog(browser) -> Catalog:
    return Catalog(browser)


@pytest.fixture(scope='class')
def setup_authorization_window(browser) -> AuthorizationWindow:
    return AuthorizationWindow(browser)


def get_firefox_browser(playwright, request) -> Browser:
    return playwright.firefox.launch(
        headless=request.config.getoption("h"),
        slow_mo=request.config.getoption("slow"),
    )


def get_chrome_browser(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=request.config.getoption("h"),
        slow_mo=request.config.getoption("slow"),
        args=['--start-maximized']
    )


def get_remote_chrome(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=True,
        slow_mo=request.config.getoption("slow")
    )


def get_context(browser, request, start) -> BrowserContext:
    if start == 'local':
        context = browser.new_context(
            no_viewport=True,
            locale=request.config.getoption('l')
        )
        context.set_default_timeout(
            timeout=request.config.getoption('t')
        )
        return context

    elif start == 'remote':
        context = browser.new_context(
            viewport=request.config.getoption('s'),
            locale=request.config.getoption('l')
        )
        context.set_default_timeout(
            timeout=request.config.getoption('t')
        )
        return context


@pytest.fixture(scope="function")
def return_back(browser):
    browser.go_back()


@pytest.fixture(scope='function', autouse=True)
def add_artifacts_to_allure_teardown(request):
    """
    Make after step fixture for attach screenshot, video and trace.\n
    Use flags: --screenshot=only-on-failure --video=retain-on-failure --tracing=retain-on-failure --full-page-screenshot
    :param request:
    :return:
    """
    yield

    output_path = os.path.join(request.config.rootdir, "allure-results",
                               truncate_file_name(slugify(request.node.nodeid)))

    ext = ("png", "webm", "zip")
    if not os.path.exists(output_path):
        return
    for file in os.listdir(output_path):
        if file.endswith(ext):
            allure.attach(
                open(os.path.join(output_path, file), 'rb').read(),
                name=f"{file}",
                extension=file.split('.')[-1]
            )


def truncate_file_name(file_name: str) -> str:
    if len(file_name) < 256:
        return file_name
    return f"{file_name[:100]}-{hashlib.sha256(file_name.encode()).hexdigest()[:7]}-{file_name[-100:]}"
