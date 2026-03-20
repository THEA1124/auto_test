import pytest

#用例标签，方便执行用例
@pytest.mark.smoke
def test_shop_flow(page):
    # 1. 打开网站
    page.goto("https://www.saucedemo.com/")

    # 2. 登录
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 3. 添加商品
    page.click("text=Add to cart")

    # 4. 进入购物车
    page.click(".shopping_cart_link")

    # 5. 结账
    page.click("text=Checkout")

    # 6. 填信息
    page.fill("#first-name", "test")
    page.fill("#last-name", "user")
    page.fill("#postal-code", "12345")

    page.click("text=Continue")

    # 7. 完成订单
    page.click("text=Finish")

    # 8. 断言
    assert "Thank you" in page.inner_text(".complete-header")