import requests
import os
import json
import easier
from datetime import datetime

mainURL = os.getenv("MAIN_CHANNEL_EDIT")

headers = {
    "Authorization": os.getenv("TOKEN_BOT")
}

# envia mensagem de atualização

def sendData():

    # declaração de booleanos com valor esperado

    verifyRelevant = False
    isNew = True
    isUpdated = False

    # leitura de diretório com arquivos de cena

    files = os.listdir('./infoData')

    # loop de verificação

    for file in files:

        # coleta de id de cena

        pageRaw = file.split(".")
        page = pageRaw[0]

        # abertura para coleta de id de jogador

        with open (f'./infoData/{page}.json', "r", encoding='utf8') as archive:
            infoFinder = json.load(archive)

            # dados da mensagem de informações

            userFinded = infoFinder["properties"]["Jogador ID"]["rich_text"][0]["text"]["content"]
            infoStatus = infoFinder["properties"]["Status"]["select"]["name"]
            infoScene = infoFinder["properties"]["Cena"]["rich_text"][0]["text"]["content"]
            infoChar = infoFinder["properties"]["Personagem"]["title"][0]["text"]["content"]
            infoComp = infoFinder["properties"]["Companhia"]["rich_text"][0]["text"]["content"]
            infoLoc = infoFinder["properties"]["Local"]["select"]["name"]
            infoDate = infoFinder["properties"]["Dia e Hora"]["date"]["start"]

            # horário da cena: correção de formato

            infoDate = easier.DataCorreted(infoDate)
            infoDate = infoDate.split("/")
            infoDate_Data = infoDate[0]
            infoDate_Time = infoDate[1]

            # dados para filtragem de tipo de atualização

            # criação: correção de formato

            createdTime = infoFinder["created_time"]
            createdTime = easier.DataCorreted(createdTime)
            createdTimeEdit = createdTime.split("/")
            createdTime_Data = createdTimeEdit[0]
            createdTime_Time = createdTimeEdit[1]

            # edição: correção de formato

            lastTime = infoFinder["last_edited_time"]
            lastTime = easier.DataCorreted(lastTime)
            lastTimeEdit = lastTime.split("/")
            lastTime_Data = lastTimeEdit[0]
            lastTime_Time = lastTimeEdit[1]

            if (createdTime_Data == lastTime_Data):
                verifyRelevant = easier.isTimeDifferentRelevant(lastTime_Time, createdTime_Time)
            else:
                verifyRelevant = True

            manager= {
                "page": f"{page}",
                "detalhes": {
                    "edição": f"{lastTime}"
                }
            }

            if os.path.isfile(f'./Manager/fileManager-{page}.json') is True:
                isNew = False

                with open (f'./Manager/fileManager-{page}.json', "r", encoding='utf8') as previousCheck:
                    prevCheck = json.load(previousCheck)

                isUpdated = (lastTime != (prevCheck["detalhes"]["edição"]))

                if (isUpdated == True):
                    os.remove(f'./Manager/fileManager-{page}.json')

                    with open (f'./Manager/fileManager-{page}.json', "w", encoding='utf8') as infoManager:
                        json.dump(manager, infoManager, ensure_ascii= False, indent= 4)

                else:
                    pass
            else:
                with open (f'./Manager/fileManager-{page}.json', "w", encoding='utf8') as infoManager:
                    json.dump(manager, infoManager, ensure_ascii= False, indent= 4)

        # caso precisar avisar, abertura para coleta de jogadores registrados
        if (isUpdated == True or isNew == True):
            with open('infoUsers.json', "r", encoding='utf8') as userFile:
                rawUserData = json.load(userFile)

                userData = rawUserData["userInfo"]

                # loop de coleta de id do banco

                for i in userData:
                    name = i["info"]["name"]
                    userID = i["info"]["id"]
                    userChannel = i["info"]["channel"]
                    newStruct = i["info"]["struct"]["new_scene"]
                    updateStruct = i["info"]["struct"]["update_scene"]
                    endStruct = i["info"]["struct"]["end_scene"]

            # caso tenha encontrado o usuário no banco, enviar mensagem

            if (userFinded == userID) is True: 
                specURL = mainURL + userChannel

                # cena encerrada + deletar arquivo de cena encerrada

                if (infoStatus == "encerrada"):
                    print("delete!")
                    sceneType = endStruct

                    os.remove(f'./infoData/{page}.json')
                    os.remove(f'./Manager/fileManager-{page}.json')

                    message_text = f"{sceneType} `{infoChar} encerrou uma cena com {infoComp} em {infoLoc} no dia {infoDate_Data} às {infoDate_Time}.`"

                # cena nova adicionada

                elif (verifyRelevant == False):
                    print("new!")
                    sceneType = newStruct

                    message_text = f"{sceneType} `{infoChar} iniciou uma cena com {infoComp} em {infoLoc} no dia {infoDate_Data} às {infoDate_Time}. Essa é a cena {infoScene} de {infoChar}.`"

                # cena foi atualizada

                elif (verifyRelevant == True):
                    print("update!")
                    sceneType = updateStruct

                    message_text = f"{sceneType} `{infoChar} está com {infoComp} em {infoLoc} no dia {infoDate_Data} às {infoDate_Time}. Essa é a cena {infoScene} de {infoChar}.`"

                else:
                    print("algo deu errado :(")

                message = {
                    "content": f"{message_text}"
                }

                req = requests.post(specURL, message, headers=headers)
                
            # caso não encontrar usuário no banco

            else:
                pass