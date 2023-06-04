import requests

def test_check_homework_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    cookie_dict = {}

    response = requests.get(url)
    headers_dict = response.headers

    assert "Set-Cookie" in headers_dict, "Key \"Set-Cookie\" doesn't exsist"

    cookies_list = headers_dict["Set-Cookie"].split(";")
    homework_cookie_list = cookies_list[0].split("=")
    cookie_dict[homework_cookie_list[0]] = homework_cookie_list[1]

    assert "HomeWork" in cookie_dict, "Key \"HomeWork\" doesn't exsist"
    assert "hw_value" == cookie_dict["HomeWork"], "Cookie value doesn't equeil \"hw_value\""