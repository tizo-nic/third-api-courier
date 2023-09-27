import requests
import json

url = "https://staging-api.tizo.co/api/v1/delivery/update-steps/?idDelivery=3884"

payload = json.dumps({
  "stepsCode": "ANNULLED",
  "name": "Orden anulada",
  "description": "Envio de ejemplo, anular"
})
headers = {
  'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoibWFuYWdlciIsInR5cGUiOiJhY2Nlc3MiLCJ1c2VybmFtZSI6Im1fcGVyZXppdG8yIiwiaWF0IjoxNjk1ODMzMDQ2LCJleHAiOjE2OTU4MzY2NDZ9.Lt7n5GDh6gb7Usg9Ek8BNnQnYLzX5FtPinmMMUUup53NUkluUCpqjTdcZpRFmDfzU56aeDidSdN4WsKYaVVqDg',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
