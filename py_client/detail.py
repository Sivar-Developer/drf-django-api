import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
# endpoint = "http://localhost:8000/api"
endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(endpoint)
# print(get_response.headers)
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
