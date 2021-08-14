import discord
import discord
from discord.ext import commands
import discord.utils

client = commands.Bot(command_prefix="$")

f = open('key.txt', 'r')
CLIENT_KEY = f.read()


@client.event
async def on_ready():
    print('Bot is Ready')


client.run(CLIENT_KEY)
