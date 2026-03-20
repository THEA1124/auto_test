from api.login_api import LoginAPI

def test_login_success():
    api = LoginAPI()

    res = api.login("eve.holt@reqres.in", "cityslicka")

    assert res.status_code == 200
    assert "token" in res.json()