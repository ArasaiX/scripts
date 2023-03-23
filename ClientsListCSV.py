import csv
import requests
import json


vtexAPIKey = ""
vtexAPIToken = ""

headers= {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-VTEX-API-AppKey": vtexAPIKey,
    "X-VTEX-API-AppToken": vtexAPIToken
}

url=""

response_API = requests.get(url, headers=headers)
data = response_API.text
json_data = json.loads(data)
fieldnames=[] #put here the fieldnames for a csv output file

token = response_API.headers['x-vtex-md-token']

nameFile = ''

with open(nameFile, 'w') as csvfile:
    Writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='', extrasaction='raise')
    Writer.writeheader()
    Writer.writerows(json_data)

# cacheTimeControl = response_API.headers['x-vtex-cache-time']

while True:
    url ="" + token 
    response_API = requests.get(url, headers=headers)
    data = response_API.text
    json_data = json.loads(data)
    try:
        # cacheTimeControl = response_API.headers['x-vtex-cache-time']
        with open(nameFile, 'a') as csvfile:
            Writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='', extrasaction='raise')
            Writer.writerows(json_data)
    except Exception:
        print("Tarea finalizada!")
        break