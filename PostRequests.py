import requests
url = "https://jsonplaceholder.typicode.com/posts"

newdata ={
    
  "userId": 1,
  "id": 200,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

}


response = requests.post(url, json=newdata)

print("Status Code: ",response.status_code)
print("Response Data: " , response.json())