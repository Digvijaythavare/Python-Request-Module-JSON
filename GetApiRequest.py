
import requests
url = "https://jsonplaceholder.typ"

response = requests.get(url)

print(response.status_code)
print(response.text)