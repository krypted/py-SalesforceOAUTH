import requests
import json
import sys

print("Script Starting...")
print("")

access_token_url = 'https://login.salesforce.com/services/oauth2/token'

data = {
    'grant_type': 'password',
    'client_id': 'INSERTYOURCLIENTIDHERE',
    'client_secret': 'INSERTYOURSECRETHERE',
    'username': sys.argv[1],
    'password': sys.argv[2]
}

headers = {
    'content-type': 'application/x-www-form-urlencoded'
}

req = requests.post(access_token_url, data=data, headers=headers)
response = req.json()

print("Completed Response ==> ")
print(json.dumps(response, indent=4,))

print("")
print("Access Token ==> " + response['access_token'])

print("")
print("Script Completed...")
