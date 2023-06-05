import requests

payload_list = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}, {"method": "PATCH"},
                {"method": "HEAD"}, {}]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response_one = requests.post(url)
print(f"response = {response_one.text}; method GET; params: {None}")

response_two = requests.head(url, params=payload_list[5])
print(f"response = {response_two.text}; method GET; params: {payload_list[5]}")

response_three = requests.put(url, data=payload_list[2])
print(f"response = {response_three.text}; method GET; params: {payload_list[2]}")
print()

for data in payload_list:
    response_four = requests.get(url, params=data)
    print(f"response = {response_four.text}; method GET; params: {data}")
    response_four = requests.post(url, data=data)
    print(f"response = {response_four.text}; method POST; params: {data}")
    response_four = requests.put(url, data=data)
    print(f"response = {response_four.text}; method PUT; params: {data}")
    response_four = requests.delete(url, data=data)
    print(f"response = {response_four.text}; method DELETE; params: {data}")
    response_four = requests.patch(url, data=data)
    print(f"response = {response_four.text}; method PATCH; params: {data}")
    response_four = requests.head(url, params=data)
    print(f"response = {response_four.text}; method HEAD; params: {data}")
    print()
