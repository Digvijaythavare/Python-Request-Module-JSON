import json


data ={
"name": "John Doe",
"age": 30,  
"city": "New York",
}

Json_data = json.dumps(data,indent=4)

print(Json_data)

