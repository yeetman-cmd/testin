import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event

async def on_ready():
     print('Bot is ready.')

client.run('NzIxMzUxNjg3NzgwMTcxODM2.XuTTDg.X3Vx2lW_Y0-jahinCUXOYw7-2po')
