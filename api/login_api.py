import requests

class LoginAPI:

    def __init__(self):
        self.base_url = "https://reqres.in/api"

    def login(self, email, password):
        url = f"{self.base_url}/login"

        data = {
            "email": email,
            "password": password
        }

        response = requests.post(url, json=data)
        return response