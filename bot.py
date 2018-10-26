import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os

client = commands.Bot(command_prefix="-")
player_dict = dict()


@client.event
async def on_ready():
    print("Bot ist bereit")
    



client.run(str(os.environ.get('BOT_TOKEN')))
