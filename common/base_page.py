import logging

class BasePage:

    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def open(self, url):
        self.logger.info(f"打开页面: {url}")
        self.page.goto(url)

    def click(self, locator):
        self.logger.info(f"点击元素: {locator}")
        self.page.click(locator)

    def fill(self, locator, text):
        self.logger.info(f"输入内容: {locator} -> {text}")
        self.page.fill(locator, text)

    def get_url(self):
        return self.page.url