import time
import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
response_dict = response.json()
payload = {"token": response_dict["token"]}
sleep_secs = response_dict["seconds"]

response = requests.get(url, params=payload)
time.sleep(sleep_secs)

response = requests.get(url, params=payload)
result_json = response.json()

if "result" in result_json and result_json["status"] == "Job is ready":
    print("Job is ready!")
