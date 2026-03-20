from pages.login_page import LoginPage

def test_login_fail(page):
    login = LoginPage(page)
    login.goto()
    login.login("wrong", "123456")
    assert "错误" in login.get_error()