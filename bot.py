import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os
import asyncio
from discord import Game

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():

    print ("Bot ist bereit")
    yield from client.change_presence(game=Game(name="#RevealedRepublic"))
    



client.run(str(os.environ.get('BOT_TOKEN')))
