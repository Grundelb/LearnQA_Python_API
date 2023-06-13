import requests
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self, create_and_auth_user_method):
        auth_data_dict = create_and_auth_user_method
        # EDIT
        new_name = "NEW NAME"

        response3 = MyRequests.put(f"/user/{auth_data_dict['user_id']}",
                                   headers={"x-csrf-token": auth_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": auth_data_dict["auth_sid"]},
                                   data={"firstName": new_name})

        Assertions.assert_status_code(response3, 200)

        # GET

        response4 = MyRequests.get(f"/user/{auth_data_dict['user_id']}",
                                   headers={"x-csrf-token": auth_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": auth_data_dict["auth_sid"]}
                                   )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of user after edit"
        )

    def test_edit_just_created_user_as_not_auth_user(self, create_and_auth_user_method):
        auth_data_dict = create_and_auth_user_method
        # EDIT
        new_name = "NEW NAME"

        response = MyRequests.put(f"/user/{auth_data_dict['user_id']}",
                                  data={"firstName": new_name})

        Assertions.assert_status_code(response, 400)

        # GET

        response1 = MyRequests.get(f"/user/{auth_data_dict['user_id']}",
                                   headers={"x-csrf-token": auth_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": auth_data_dict["auth_sid"]}
                                   )

        Assertions.assert_json_value_by_name(
            response1,
            "firstName",
            auth_data_dict['firstName'],
            "Wrong name of user after edit. Name shouldn't be able to change."
        )

    def test_edit_just_created_user_auth_as_another_user(self, create_and_auth_user_method, auth_user_method):
        edit_user_data_dict = create_and_auth_user_method
        auth_user_data_dict = auth_user_method
        # EDIT
        new_name = "NEW NAME"

        response = MyRequests.put(f"/user/{edit_user_data_dict['user_id']}",
                                  data={"firstName": new_name},
                                  headers={"x-csrf-token": auth_user_data_dict["x-csrf-token"]},
                                  cookies={"auth_sid": auth_user_data_dict["auth_sid"]})

        Assertions.assert_status_code(response, 400)

        # GET

        response1 = MyRequests.get(f"/user/{edit_user_data_dict['user_id']}",
                                   headers={"x-csrf-token": edit_user_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": edit_user_data_dict["auth_sid"]}
                                   )

        Assertions.assert_json_value_by_name(
            response1,
            "firstName",
            edit_user_data_dict['firstName'],
            "Wrong name of user after edit. Name shouldn't be able to change."
        )

    def test_edit_just_created_user_email_without_at_auth_as_same_user(self, create_and_auth_user_method):
        edit_user_data_dict = create_and_auth_user_method
        # EDIT
        new_email = "".join(edit_user_data_dict['email'].split("@"))

        response = MyRequests.put(f"/user/{edit_user_data_dict['user_id']}",
                                  data={"email": new_email},
                                  headers={"x-csrf-token": edit_user_data_dict["x-csrf-token"]},
                                  cookies={"auth_sid": edit_user_data_dict["auth_sid"]})

        Assertions.assert_status_code(response, 400)
        Assertions.assert_content_has_text(response, "Invalid email format")

        # GET

        response1 = MyRequests.get(f"/user/{edit_user_data_dict['user_id']}",
                                   headers={"x-csrf-token": edit_user_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": edit_user_data_dict["auth_sid"]}
                                   )

        Assertions.assert_json_value_by_name(
            response1,
            "email",
            edit_user_data_dict['email'],
            "Wrong email of user after edit. Email shouldn't be able to change."
        )

    def test_edit_just_created_user_firstname_to_short_value_auth_as_same_user(self, create_and_auth_user_method):
        edit_user_data_dict = create_and_auth_user_method
        # EDIT
        new_name = "X"

        response = MyRequests.put(f"/user/{edit_user_data_dict['user_id']}",
                                  data={"firstName": new_name},
                                  headers={"x-csrf-token": edit_user_data_dict["x-csrf-token"]},
                                  cookies={"auth_sid": edit_user_data_dict["auth_sid"]})

        Assertions.assert_status_code(response, 400)
        Assertions.assert_json_value_by_name(response,
                                             'error',
                                             'Too short value for field firstName',
                                             f"Unexpexted response text {response.text}")

        # GET

        response1 = MyRequests.get(f"/user/{edit_user_data_dict['user_id']}",
                                   headers={"x-csrf-token": edit_user_data_dict["x-csrf-token"]},
                                   cookies={"auth_sid": edit_user_data_dict["auth_sid"]}
                                   )

        Assertions.assert_json_value_by_name(
            response1,
            "firstName",
            edit_user_data_dict['firstName'],
            "Wrong name of user after edit. Name shouldn't be able to change."
        )
