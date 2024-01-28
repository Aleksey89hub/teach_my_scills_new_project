import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from dotenv import load_dotenv

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
