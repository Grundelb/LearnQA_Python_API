import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    url = "/user/"

    def test_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post(self.url, data=data)

        Assertions.assert_status_code(response, 400)

        Assertions.assert_content_has_text(
            response, f"Users with email '{email}' already exists"
        )

    def test_create_user_successufully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post(self.url, data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(
            response,
            "id"
        )

    def test_create_user_with_email_without_at_symbol(self):
        data = self.prepare_registration_data(email="emailewithoutatexample.com")

        response = MyRequests.post(self.url, data=data)

        Assertions.assert_status_code(response, 400)
        Assertions.assert_content_has_text(
            response, f"Invalid email format"
        )

    @pytest.mark.parametrize("mail, password, username, firstName, lastName, expected_error_message", [
        ("None", 123, "learnqa", "learnqa", "learnqa", 'The following required params are missed: email'),
        (None, None, "learnqa", "learnqa", "learnqa", 'The following required params are missed: password'),
        (None, 123, None, "learnqa", "learnqa", 'The following required params are missed: username'),
        (None, 123, "learnqa", None, "learnqa", 'The following required params are missed: firstName'),
        (None, 123, "learnqa", "learnqa", None, 'The following required params are missed: lastName')
    ])
    def test_create_user_without_registration_data(self, mail, password, username, firstName, lastName,
                                                   expected_error_message):
        data = self.prepare_registration_data(mail, password, username, firstName, lastName)

        response = MyRequests.post(self.url, data=data)

        Assertions.assert_status_code(response, 400)
        Assertions.assert_content_has_text(
            response, expected_error_message
        )

    def test_create_user_with_short_first_name(self):
        data = self.prepare_registration_data()
        data["firstName"] = "A"

        response = MyRequests.post(self.url, data=data)

        Assertions.assert_status_code(response, 400)
        Assertions.assert_content_has_text(
            response, "The value of 'firstName' field is too short"
        )

    def test_create_user_with_long_first_name(self):
        data = self.prepare_registration_data()
        data[
            "firstName"] = "U5xpK5hOM5kcsgOMr4adsCUTkcjhcE62bwafLjYtGaTkGXOh4sV89uqXZHLTBo1g7o5McKFlYahyM3kuUoG6idWE7omy9qnr" \
                           "BJlEU3eFa1oSdAyJZdvGXlOsnc9Q8ElxlxKzvWnjME5mipatlScBcN8OwWpJkp9DpVb8ykwnFlbk6MbVyu22PoFttnFEhvVcsea" \
                           "0eGBvldF3cNBIi8MmWYOdxHZ6DXdI5orymdOvIbosLUn2xMaE75FN251"

        response = MyRequests.post(self.url, data=data)

        Assertions.assert_status_code(response, 400)
        Assertions.assert_content_has_text(
            response, "The value of 'firstName' field is too long"
        )
