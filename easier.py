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

class DataCorreted:
    def __new__(self, date= str):
        self.separator = date.split("T")
        self.dateAndMonth = self.separator[0]
        self.hoursRawAndDirty = self.separator[1]
        self.hoursCleaner = self.hoursRawAndDirty.split(".")
        self.hoursRaw = self.hoursCleaner[0]
        self.hoursOrganizer = self.hoursRaw.split(":")
        self.hoursAndMinuts = f"{self.hoursOrganizer[0]}:{self.hoursOrganizer[1]}"
        self.solidAnswer = f"{self.dateAndMonth}/{self.hoursAndMinuts}"

        return self.solidAnswer
    
class isTimeDifferentRelevant:
    def __new__(self, horaA= str, horaB= str):
        self.minutsA = horaA.split(":")
        self.hoursA = self.minutsA[0]
        self.minutsA = self.minutsA[1]
        self.minutsB = horaB.split(":")
        self.hoursB = self.minutsB[0]
        self.minutsB = self.minutsB[1]

        if (self.hoursA == self.hoursB):
            isRelevant = (int(self.minutsA) - int(self.minutsB) >= 3)
        else:
            isRelevant = True

        return isRelevant