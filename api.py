# importações

import discord
import json
import os
import requests

# especificações de importação

from notion_client import Client
from pprint import pprint
from datetime import datetime
from dotenv import load_dotenv

# carregar informações protegidas

load_dotenv()

# token

notionToken = os.getenv('API_TOKEN_NOTION')

# API notion, solicitador de dados do Database

asst_module = Client(auth= notionToken)
database_url = os.getenv('DATABASE_URL_NOTION')

# etiquetas de URL

queryDB_Url = f"https://api.notion.com/v1/databases/{database_url}/query"
updateDB_Url = f"https://api.notion.com/v1/databases/{database_url}"
createDB_Url = "https://api.notion.com/v1/databases"

# define headers

headers = {
    "Authorization": ("Bearer" + "notionToken"),
    "Notion-Version": "2024-09-11",
    "Content-Type": "application/json",
}

# listagem de informações do DataBase

def getData():

    res = asst_module.databases.query(
        **{
            "database_id": f"{database_url}",
            "filter": {
                "property": "Status",
                "select": {
                    "equals": "respondida",
                },
            },
        }
    )

    with open("./infoData/res.json", "w", encoding='utf8') as file:
        json.dump(res, file, ensure_ascii=False, indent=4)

    results = res["results"]
    return results

info = getData()
for i in info:
    props = i["properties"]
    charName = props["Personagem"]["title"][0]["text"]["content"]
    player = props["Jogador ID"]["number"]
    sceneStatus = props["Status"]["select"]["name"]
    withWho = props["Companhia"]["rich_text"][0]["text"]["content"]
    where = props["Local"]["select"]["name"]
    scene = props["Cena"]["rich_text"][0]["text"]["content"]
    dateAndTime = props["Dia e Hora"]["date"]["start"]
    dateAndTime = datetime.fromisoformat(dateAndTime)


print(charName, player, sceneStatus, withWho, where, scene, dateAndTime)




