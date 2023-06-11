import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):

    def test_user_with_existing_email(self):
        url = "/user/"
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post(url, data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpexted response content {response.content}"

    def test_create_user_successufully(self):
        url = "/user/"
        data = self.prepare_registration_data()

        response = MyRequests.post(url, data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(
            response,
            "id"
        )
