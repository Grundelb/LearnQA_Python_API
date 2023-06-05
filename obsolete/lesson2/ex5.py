import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
            '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)

key = "messages"
nested_key= "message"

if nested_key in obj[key][1]:
    print(obj[key][1][nested_key])
else:
    print(f"Key '{key}' doesn't exist")
