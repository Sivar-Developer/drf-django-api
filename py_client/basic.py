import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.jsno())
print(get_response.status_code)
