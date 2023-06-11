import json
from requests import Response

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            json_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in json_as_dict, f"Response JSON doesn't have key '{name}'"
        assert json_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            json_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in json_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            json_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in json_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            json_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in json_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present."

    @staticmethod
    def assert_status_code(response: Response, expected_code):
        assert response.status_code == expected_code, \
            f"Unexpected status code! Expected code: {expected_code}. Actual code: {response.status_code}."

    @staticmethod
    def assert_content_has_text(response: Response, expected_text):
        assert response.content.decode("utf-8") == expected_text, f"Unexpexted response content {response.content}"

