 # pytest全局配置，用于统一管理 fixture，比如浏览器初始化、环境准备，实现用例之间的资源复用
import pytest
from playwright.sync_api import sync_playwright
from common.logger import setup_logger

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

#token管理
@pytest.fixture(scope="session")
def token():
    return "xxx_token"


def pytest_configure():
    setup_logger()