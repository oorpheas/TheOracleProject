#///////////////////////////////////////////////////////////////
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# . . . . . . . . . . . . .-#%%#**+.*##*. . . . . . . . . . . . 
#. . . . . . . . . . ##........:--......+. . . . . . . . . . . .
# . . . . . . . . :%:...+%%%#%%%%%%%%%%%=...=#. . . . . . . . .
#. . . . . . . . .#*...#%%*+=:.*#%%%%%%%#--=#=...*-. . . . . . .
# . . . . . . .**..+%#-%**.=-.=%%%%%%+......%##...:+. . . . . . 
#. . . . . . -%..=%-#+.%.:*=--%%%%..+:......%.%.%-...#-. . . . .
# . . . . .#..==#::#..%.:.+..%%%%%%%%..==::#.-.+-.*....:= . . . 
#. . . . #...#-.%.....#.......%%%%%*.::..=:+.....+..:. . . . . .
# . . . ........-*+.....#....-........=....*....+...*.. . . . . 
#. . . . .*%**=....-+...+.......-+-..:=..#..=...:*.... . . . . .
# . . . . . . . .=#.....*+-%:....:......#%*....#-.. . . . . . .
#. . . . . . . . . +%.....................%=.. . . . . . . . . . 
# . . . . . . . . . . . .=#%%*+--=+#%%#+. . . . . . . . . . . . 
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# . . . . . . . . . . . . . . .esse código foi feito por 0RFEUS.
#
#
# //
# esse código tem como objetivo criar um bot para auxiliar  fun-
# ções de moderação e divertimento em um servidor no Discord.
#
# se você está com acesso a esse cógido significa que meus estu-
# dos deram certo  (ou eu sem querer fiz merda publicando  antes
# da hora).
#
# ínicio: 04/04/2024.
#
# //

# aqui importamos a >congif< (onde você  irá colocar o token  do 
# seu bot) e a biblioteca do discord;

from datetime import datetime
import config
import discord
import random
import embed
import requisitions

# especificações da biblioteca importada 

from discord.ext import commands
from discord import Interaction

# definindo um prefix para comandos personalizados

oracle = commands.Bot(command_prefix="oracle$", intents= discord.Intents.all())

# modlog para saber se o bot deu boot

@oracle.event
async def on_ready():
    await oracle.tree.sync()
    await oracle.change_presence(activity=discord.activity.Game(name="aprendendo..."),
                                 status=discord.Status.online)

    print(". . . . . . . .  . . . . . . .  . . . . . .")
    print(f"{oracle.user.name.upper()} está funcionando. ⚡")
    print(". . . . . . . .  . . . . . . .  . . . . . .")

# ping check !
    
@oracle.tree.command(name="ping", description="mostra o tempo de resposta atual.")
async def ping(Oracle: Interaction):
    bot_latency = round(oracle.latency*1000)
    await Oracle.response.send_message(f"pong! {bot_latency}ms")

# comando MODROLE, para editar cargos de usuários

@oracle.tree.command(name="modrole", description="gerencia os cargos de outro usuário.")
@commands.has_role(config.EQUIPE_ROLE)
async def modrole(Oracle: Interaction, member: discord.Member , role: discord.Role, action: str):
    # já possui o cargo e quer adicionar
    if (role in member.roles and action == "add" ):
        embed_modrole = embed.Embed(
            (requisitions.REQ400), 
            "Este usuário já possui este cargo! Tente outro usuário ou outra função.")
        embed_modrole.create()
        await Oracle.response.send_message(embed=embed_modrole, delete_after=20)
    # é possivel adicionar
    elif (role not in member.roles and action == "add"):
        await member.add_roles(role)
        embed_modrole = embed.Embed(
            (requisitions.REQ200), 
            f"🔓 {member.mention} recebeu acesso as depedencias relacionadas a **{role.name.upper()}**.")
        embed_modrole.create()
        await Oracle.response.send_message(embed=embed_modrole)
    # não possui o cargo e quer remover
    elif (role not in member.roles and action == "remove"):
        embed_modrole = embed.Embed(
            (requisitions.REQ400), 
            "Este usuário não possui este cargo! Tente outro usuário ou outra função.")
        embed_modrole.create()
        await Oracle.response.send_message(embed=embed_modrole, delete_after=20)
    # é possivel remover
    elif (role in member.roles and action == "remove"):
        await member.remove_roles(role)
        embed_modrole = embed.Embed(
            (requisitions.REQ200), 
            f"🔓 {member.mention} perdeu acesso as depedencias relacionadas a **{role.name.upper()}**.")
        embed_modrole.create()
        await Oracle.response.send_message(embed=embed_modrole)
    # função não existe
    elif (action != "remove" and action != "add"):
        embed_modrole = embed.Embed(
            (requisitions.REQ400), 
            "Peço desculpas, posso apenas adicionar (add) ou remover (remove). Poderia tentar novamente?")
        embed_modrole.create()
        await Oracle.response.send_message(embed=embed_modrole, delete_after=20)


# iniciador

oracle.run(config.TOKEN)