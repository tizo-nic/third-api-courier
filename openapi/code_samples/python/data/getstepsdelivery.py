import requests

url = "https://api.tizo.co/api/v1/system-data/steps-deliveries/36/"

payload={}
headers = {
  'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoic3RvcmVfYXBpIiwidXNlcm5hbWUiOiJzdG9yZV8yIiwiaWF0IjoxNjU4MTU0Mjc3LCJleHAiOjE2NTg3NTkwNzd9.u6b7ap-7vYikiIBwJ8ugj7rTM_0nVkuMXVlI-Mz7ayXmPT661F9--p-QfbcOcPtewQliHWqktS5P8YYNgPH3uA'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
