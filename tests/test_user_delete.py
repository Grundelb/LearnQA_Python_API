from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):

    def test_delete_super_user(self, auth_user_method):
        auth_user_data_dict = auth_user_method

        response = MyRequests.delete("/user/2",
                                     headers={"x-csrf-token": auth_user_data_dict["x-csrf-token"]},
                                     cookies={"auth_sid": auth_user_data_dict["auth_sid"]}
                                     )

        Assertions.assert_status_code(response, 400)
        Assertions.assert_content_has_text(response,
                                           "Please, do not delete test users with ID 1, 2, 3, 4 or 5.")

    def test_delete_just_created_user_auth_as_same_user(self, create_and_auth_user_method, auth_user_method):
        delete_user_data_dict = create_and_auth_user_method
        auth_user_data_dict = auth_user_method
        # DELETE

        response = MyRequests.delete(f"/user/{delete_user_data_dict['user_id']}",
                                     headers={"x-csrf-token": delete_user_data_dict["x-csrf-token"]},
                                     cookies={"auth_sid": delete_user_data_dict["auth_sid"]})

        Assertions.assert_status_code(response, 200)

        # GET

        response1 = MyRequests.get(f"/user/{delete_user_data_dict['user_id']}",
                                   headers={"x-csrf-token": auth_user_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": auth_user_data_dict["auth_sid"]}
                                   )

        Assertions.assert_status_code(response1, 404)
        Assertions.assert_content_has_text(response1, "User not found")

    def test_delete_just_created_user_auth_as_another_user(self, create_and_auth_user_method):
        delete_user_data_dict = create_and_auth_user_method

        # Create another user to delete the first one
        data = BaseCase().prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

        data1 = {
            'email': data['email'],
            'password': data['password']
        }

        response1 = MyRequests.post("/user/login", data=data1)
        auth_sid = response1.cookies['auth_sid']
        token = response1.headers['x-csrf-token']

        # DELETE

        response2 = MyRequests.delete(f"/user/{delete_user_data_dict['user_id']}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response2, 400)
        Assertions.assert_content_has_text(response2, "You are not allowed to DELETE another user")
