import discord
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Ready!")
    print(f'Logged in as {client.user} on {len(client.guilds)} servers')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="chat for !quote"))

client.run('')