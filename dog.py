import discord
from discord.ext import commands
import aiohttp
import random

client = commands.Bot(command_prefix="owo ")

@client.event
async def on_ready():
    print("Ready!")
    print(f'Logged in as {client.user} on {len(client.guilds)} servers')
    await client.change_presence(activity=discord.Game(name="wobwox"))

@client.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="Doggo!", color=0xffb9e7) # Create embed
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)

@client.command()
async def gay(ctx):
    gay = random.randint(0, 100)
    await ctx.send(f"{ctx.author.name} is {gay}% gay")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Server Ping: {round(client.latency * 1000)}ms.')

@client.command()
async def coinflip(ctx):
    coin = random.randint(0, 1)
    if coin == 0:
        await ctx.send(f"Heads!")
    if coin == 1:
        await ctx.send(f"Tails!")

@client.command()
async def virgin(ctx):
    virginity = random.randint(0, 1)
    if virginity == 0:
        await ctx.send(f"{ctx.author.name} is a virgin")
    if virginity == 1:
        await ctx.send(f"{ctx.author.name} is not a virgin")

@client.command()
async def pp(ctx):
    pp = random.randint(0, 19)
    if pp == 0:
        await ctx.send(f"{ctx.author.name}'s pp size: 8=D")
    if pp == 1:
        await ctx.send(f"{ctx.author.name}'s pp size: 8==D")
    if pp == 2:
        await ctx.send(f"{ctx.author.name}'s pp size: 8===D")
    if pp == 3:
        await ctx.send(f"{ctx.author.name}'s pp size: 8====D")
    if pp == 4:
        await ctx.send(f"{ctx.author.name}'s pp size: 8=====D")
    if pp == 5:
        await ctx.send(f"{ctx.author.name}'s pp size: 8======D")
    if pp == 6:
        await ctx.send(f"{ctx.author.name}'s pp size: 8=======D")
    if pp == 7:
        await ctx.send(f"{ctx.author.name}'s pp size: 8========D")
    if pp == 8:
        await ctx.send(f"{ctx.author.name}'s pp size: 8=========D")
    if pp == 9:
        await ctx.send(f"{ctx.author.name}'s pp size: 8==========D")
    if pp == 10:
        await ctx.send(f"{ctx.author.name}'s pp size: 8===========D")
    if pp == 11:
        await ctx.send(f"{ctx.author.name}'s pp size: 8============D")
    if pp == 12:
        await ctx.send(f"{ctx.author.name}'s pp size: 8=============D")
    if pp == 13:
        await ctx.send(f"{ctx.author.name}'s pp size: 8==============D")
    if pp == 14:
        await ctx.send(f"{ctx.author.name}'s pp size: 8===============D")
    if pp == 15:
        await ctx.send(f"{ctx.author.name}'s pp size: 8================D")
    if pp == 16:
        await ctx.send(f"{ctx.author.name}'s pp size: 8=================D")
    if pp == 17:
        await ctx.send(f"{ctx.author.name}'s pp size: 8==================D")
    if pp == 18:
        await ctx.send(f"{ctx.author.name}'s pp size: 8===================D")
    if pp == 19:
        await ctx.send(f"{ctx.author.name}'s pp size: 8====================D")
        
@client.command()
async def waifu(ctx):
    waifu = random.randint(0, 100)
    await ctx.send(f"{ctx.author.name} is {waifu}% a waifu")

@client.command()
async def magic8(ctx):
    ball = random.randint(0, 19)
    if ball == 0:
        await ctx.send(f"It is certain")
    if ball == 1:
        await ctx.send(f"It is decidedly so")
    if ball == 2:
        await ctx.send(f"Without a doubt")
    if ball == 3:
        await ctx.send(f"Yes definitely")
    if ball == 4:
        await ctx.send(f"You may rely on it")
    if ball == 5:
        await ctx.send(f"As I see it, yes")
    if ball == 6:
        await ctx.send(f"Most likely")
    if ball == 7:
        await ctx.send(f"Outlook good")
    if ball == 8:
        await ctx.send(f"Yes")
    if ball == 9:
        await ctx.send(f"Signs point to yes")
    if ball == 10:
        await ctx.send(f"Reply hazy, try again")
    if ball == 11:
        await ctx.send(f"Ask again later")
    if ball == 12:
        await ctx.send(f"Cannot predict now")
    if ball == 13:
        await ctx.send(f"Concentrate and ask again")
    if ball == 14:
        await ctx.send(f"Don't count on it")
    if ball == 15:
        await ctx.send(f"My reply is no")
    if ball == 16:
        await ctx.send(f"My sources say no")
    if ball == 17:
        await ctx.send(f"Outlook not so good")
    if ball == 18:
        await ctx.send(f"Very doubtful")
    if ball == 19:
        await ctx.send(f"Cannot predict now")

@client.command()
async def cringe(ctx):
    cringe = random.randint(0, 100)
    await ctx.send(f"{ctx.user.name} is {cringe}% cringe")

@client.command()
async def braincell(ctx):
    braincell = random.randint(0, 100000000000)
    await ctx.send(f"{ctx.user.name} has {braincell} braincells")

@client.command()
async def haircell(ctx):
    haircell = random.randint(0, 30000)
    await ctx.send(f"{ctx.user.name} has {haircell} haircells")

@client.command()
async def iq(ctx):
    iq = random.randint(0, 250)
    await ctx.send(f"{ctx.user.name} has {iq} iq")

@client.command()
async def invite(ctx):
    await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id=100"
        f"4450562881900544&permissions=296062774592&scope=bot%20applications.commands")

client.run('')