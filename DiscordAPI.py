import requests
import os
import json

headers = {
    "Authorization": os.getenv("TOKEN_BOT")
}

payload = {
    "content": ""
}

# envia mensagem de atualização

def sendData(): 

    # leitura de diretório com arquivos de cena

    files = os.listdir('./infoData')


    # loop de verificação

    for file in files:

        # coleta de id de cena

        pageRaw = file.split(".")
        page = pageRaw[0]

        # abertura para coleta de id de jogador

        with open (f'./infoData/{page}.json', "r", encoding='utf8') as archive:
            userFinder = json.load(archive)

            userFinded = userFinder["properties"]["Jogador ID"]["number"]

        # abertura para coleta de jogadores registrados

        with open('infoUsers.json', "r", encoding='utf8') as userFile:
            rawUserData = json.load(userFile)

            userData = rawUserData["userInfo"]

            # loop de coleta de id do banco

            for i in userData:
                name = i["info"]["name"]
                userID = i["info"]["id"]
                userChannel = i["info"]["channel"]

        # caso tenha encontrado o usuário no banco, enviar mensagem

        if userFinded == userID is True: # isso está funcionando, mas o notion por algum motivo está alterando o valor que eu coloco
            print("User Finded!")
            print(name)

        # caso não encontrar usuário no banco

        else:
            print(userFinded)
            print(userID)

sendData()