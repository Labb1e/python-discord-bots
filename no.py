import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Ready!")
    print(f'Logged in as {client.user} on {len(client.guilds)} servers')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = discord.utils.get(message.guild.channels, name="no")
    if not message.content == no:
        await message.delete()
        await channel.send(f"no")


client.run('')
