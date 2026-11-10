import json


data ='{"name": "John Doe","age": 30, "city": "New York"}'

json_data = json.loads(data,)
print(json_data)