# importações

import discord
import os
import requests

# especificações de importação

from datetime import datetime
from dotenv import load_dotenv

# carregar informações protegidas

load_dotenv()

# gerador de mensagens embed

class Embed:
    def __init__(self, title= str, description= str):
        self.embed_title = title
        self.embed_description = description
        self.embed = discord.Embed(title= self.embed_title,
                             description= self.embed_description,
                             colour=0x2c5e42,
                             timestamp= datetime.now())
    def create(self):
        self.embed.set_author(name="Oráculo",
                        icon_url=(os.getenv('BOT_ICON')))
        self.embed.set_footer(text= os.getenv('footer'))
    
    def to_dict(self):
        return self.embed.to_dict()
    
# API notion, solicitador de dados do Database

# define headers

headers = {
    "Authorization": "Bearer" + (os.getenv('API_TOKEN_NOTION')),
    "Notion-Version": "2024-09-11",
    "Content-Type": "application/json",
}

# solicita os dados

# def getData():
#    url = f"https://api.notion.com/v1/databases/{(os.getenv('DATABASE_ID_NOTION'))}/query"

#    payload = {"page_size": 100}
#    response = requests.post(url, json= payload, headers= headers)

#    data = response.json()

    # sessão de teste
#    import json
#    with open('database_test.json', 'w', encoding='utf8') as f:
#              json.dump(data, f, ensure_ascii=False, indent=4)

#    results = data["results"]
#    return results

# database_info = getData()
# for page in database_info:
#    page_id = page["id"]
#    props = page["properties"]
#    personagem = props["Personagem"]["title"][0]["text"]["content"]
#    title = props["Title"]["rich_text"][0]["text"]["content"]
#    published = props["Published"]["date"]["start"]
#    published = datetime.fromisoformat(published)
#    print(url, title, published)
