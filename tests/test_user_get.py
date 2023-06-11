import requests
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

class TestUserGet(BaseCase):
    def test_get_user_details_no_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self, auth_user_method):
        auth_data_dict = auth_user_method
        response = MyRequests.get(
            f"/user/{auth_user_method['user_id']}",
            headers={"x-csrf-token": auth_data_dict["x-csrf-token"]},
            cookies={"auth_sid": auth_data_dict["auth_sid"]}
        )
        expected_values =["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response, expected_values)