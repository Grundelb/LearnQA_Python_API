import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
count_of_redirects = len(response.history)
final_url = response.url
print(f"Count of redirects is {count_of_redirects}, final url is {final_url}")
