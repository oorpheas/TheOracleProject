# importações

import json
import os

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
    
    # chamada de banco de dados

    res = asst_module.databases.query(
        **{
            "database_id": f"{database_url}",
            "filter": {
                "property": "Status",
                "select": {
                    "is_not_empty": True,
                },
            },
        }
    )

    results = res["results"]

    # loop de verificação de cenas existentes

    for i in results:
            
        # filtragem e seleção de dados

        pageID = i["id"]
        props = i["properties"]
        sceneStatus = props["Status"]["select"]["name"]

        # verificações dos arquivos

        # verifica se arquivo já existe

        if os.path.isfile(f'./infoData/{pageID}.json') is True:
            with open(f'./infoData/{pageID}.json', "r", encoding='utf8') as previousFile:
                verify = json.load(previousFile)

                # verifica se houve alteração no status da cena

                changeRelevant = (sceneStatus != (verify["properties"]["Status"]["select"]["name"]))

                #verifica se a cena foi fechada

                isClosed = (sceneStatus == "encerrada")

            # se não foi fechada, atualiza o arquivo a nova informação

            if changeRelevant is True and isClosed is False:
                os.remove(f'./infoData/{pageID}.json')
                
                with open(f'./infoData/{pageID}.json', "w", encoding='utf8') as file:
                    json.dump(i, file, ensure_ascii= False, indent= 4)

            # se foi fechada, deleta o arquivo. talvez precise alterar essa linha, para enviar mensagem de fechamento

            elif changeRelevant is True and isClosed is True:
                os.remove(f'./infoData/{pageID}.json')

            else:
                pass

        # caso não exista arquivo criado com esse nome

        elif os.path.isfile(f'./infoData/{pageID}.json') is False:

            # verifica se não é uma cena encerrada

            if sceneStatus == "encerrada":
                pass

            # cria nova cena

            else:
                with open(f'./infoData/{pageID}.json', "w", encoding='utf8') as file:
                    json.dump(i, file, ensure_ascii= False, indent= 4)






