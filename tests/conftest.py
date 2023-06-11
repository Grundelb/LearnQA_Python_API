import pytest
import requests

@pytest.fixture
def auth_user_method():
    url_login = "https://playground.learnqa.ru/api/user/login"
    data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
    }
    response = requests.post(url_login, data=data)

    auth_sid = response.cookies["auth_sid"]
    token = response.headers["x-csrf-token"]
    user_id_from_auth_method = response.json()["user_id"]
    return {"user_id": user_id_from_auth_method,
            "x-csrf-token": token,
            "auth_sid": auth_sid}