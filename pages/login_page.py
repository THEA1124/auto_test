from common.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://example.com/login"

    def login(self, username, password):
        self.open(self.url)
        self.fill("#username", username)
        self.fill("#password", password)
        self.click("#login-btn")