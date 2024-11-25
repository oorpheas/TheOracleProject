# importações

import discord
import os

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
    