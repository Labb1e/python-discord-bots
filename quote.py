import discord
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Ready!")
    print(f'Logged in as {client.user} on {len(client.guilds)} servers')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = discord.utils.get(message.guild.channels, name="quotes")
    if not channel:
        await message.guild.create_text_channel("quotes")
        channel = discord.utils.get(message.guild.channels, name="quotes")
    embed = discord.Embed(title=f"{message.author.name}", color=0xffb9e7)
    embed.add_field(name=f"{message.content}", value=f"{datetime.today().strftime('%d/%m/%Y')}", inline=False)
    embed.set_thumbnail(url=message.author.avatar_url)
    await channel.send(embed=embed)


client.run('')
