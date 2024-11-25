import requests
import os
import json

headers = {
    "Authorization": os.getenv("TOKEN_BOT")
}

payload = {
    "content": ""
}

with open('infoUsers.json', "r", encoding='utf8') as userFile:
    rawUserData = json.load(userFile)

    userData = rawUserData["userInfo"]

    print(userData["infoNat"])

