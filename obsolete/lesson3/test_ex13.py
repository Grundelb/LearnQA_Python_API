import pytest
import requests


@pytest.mark.parametrize("user_agent_value, expected_platform, expected_browser, expected_device",
                         [(
                                 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko)'
                                 ' Version/4.0 Mobile Safari/534.30',
                                 {'platform': 'Mobile'}, {'browser': 'No'}, {'device': 'Android'}),
                             (
                                     'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77'
                                     ' Mobile/15E148 Safari/604.1', {'platform': 'Mobile'}, {'browser': 'Chrome'},
                                     {'device': 'iOS'}),
                             ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                              {'platform': 'Googlebot'}, {'browser': 'Unknown'}, {'device': 'Unknown'}),
                             (
                                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
                                     'Safari/537.36 Edg/91.0.100.0', {'platform': 'Web'}, {'browser': 'Chrome'},
                                     {'device': 'No'}),
                             (
                                     'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                                     'Version/13.0.3 Mobile/15E148 Safari/604.1',
                                     {'platform': 'Mobile'}, {'browser': 'No'}, {'device': 'iPhone'})
                         ])
def test_check_user_agent(user_agent_value, expected_platform, expected_browser, expected_device):
    url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
    payload = {"User-Agent": user_agent_value}

    response = requests.get(url, headers=payload)

    assert expected_platform["platform"] == response.json()[
        "platform"], f"\"User-Agent\": \"{user_agent_value}\"" \
                     f"Platform value \"{response.json()['platform']}\" doesn't equail {expected_platform}"

    assert expected_browser["browser"] in response.json()[
        "browser"], f"\"User-Agent\": \"{user_agent_value}\"" \
                    f"Browser value \"{response.json()['browser']}\" doesn't equail {expected_browser}"

    assert expected_device["device"] in response.json()[
        "device"], f"\"User-Agent\": \"{user_agent_value}\"" \
                   f"Device value \"{response.json()['device']}\" doesn't equail {expected_device}"
