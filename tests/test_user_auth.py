import pytest
import requests
from lib.base_case import BaseCase


class TestUserAuth(BaseCase):
    url = "https://playground.learnqa.ru/api/user/login"

    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post(self.url, data = data)

        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    def test_auth_user(self):
        pass
