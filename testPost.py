import requests

# url = "http://192.168.0.167:8000/add_row"
url = "http://192.168.0.167:8000/add_row?name=John&age=30"
data = {"name": "John", "age": "30"}

response = requests.post(url, data=data)
print(response.json())