import requests

def test_check_headers():
    url = "https://playground.learnqa.ru/api/homework_header"

    response = requests.get(url)
    headers_dict = response.headers
    assert response.status_code == 200, "The status code is not equal 200"

    assert "x-secret-homework-header" in headers_dict, "Key \"x-secret-homework-header\" doesn't exsist"
    assert headers_dict["x-secret-homework-header"] == "Some secret value", "Cookie value doesn't equeil \"Some secret value\""