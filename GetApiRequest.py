
import requests
url = "http://api.example.com/data"

response = requests.get(url)

print(response.status_code)
print(response.text)