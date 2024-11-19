import discord
import config
from datetime import datetime
import storytelling

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
                        icon_url=(config.BOT_ICON))
        self.embed.set_footer(text= storytelling.footer)
    
    def to_dict(self):
        return self.embed.to_dict()