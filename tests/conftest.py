import pytest
import requests
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


@pytest.fixture
def auth_user_method():
    data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
    }
    response = MyRequests.post("/user/login", data=data)

    auth_sid = response.cookies["auth_sid"]
    token = response.headers["x-csrf-token"]
    user_id_from_auth_method = response.json()["user_id"]
    return {"user_id": user_id_from_auth_method,
            "x-csrf-token": token,
            "auth_sid": auth_sid}


@pytest.fixture
def create_and_auth_user_method():
    data = BaseCase().prepare_registration_data()
    response = MyRequests.post("/user/", data=data)

    data1 = {
        'email': data['email'],
        'password': data['password']
    }

    response1 = MyRequests.post("/user/login", data=data1)
    auth_sid = response1.cookies["auth_sid"]
    token = response1.headers["x-csrf-token"]
    user_id_from_auth_method = response1.json()["user_id"]
    return {"user_id": user_id_from_auth_method,
            "x-csrf-token": token,
            "auth_sid": auth_sid}
