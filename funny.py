import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Ready!")
    print(f'Logged in as {client.user} on {len(client.guilds)} servers')
    await client.change_presence(activity=discord.Game(name="wobwox"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "owo ping":
        await message.channel.send(f"Pong! {round(client.latency * 1000)}ms")
    if message.content == "owo":
        await message.channel.send(f"uwu you furry cunt")
    if message.content == "uwu":
        await message.channel.send(f"owo you furry cunt")
    if message.content == "fuck":
        await message.channel.send(f"no swweromv this is a Christian Minecraft server")
    if message.content == "shit":
        await message.channel.send(f"no swweromv this is a Christian Minecraft server")
    if message.content == "owo coinflip":
        coin = random.randint(0, 1)
        if coin == 0:
            await message.channel.send(f"Heads")
        if coin == 1:
            await message.channel.send(f"Tails")
    if message.content == "owo gay":
        if message.author.id == 690898639656321026:
            await message.channel.send(f"{message.author.name} is 100% gay")
        else:
            if message.author.id == 385834274550448128:
                await message.channel.send(f"{message.author.name} is 100% gay")
            else:
                if message.author.id == 383966262155280386:
                    await message.channel.send(f"{message.author.name} is 100% gay")
                else:
                    if message.author.id == 722346181430345778:
                        await message.channel.send(f"{message.author.name} is 100% gay")
                    else:
                        gay = random.randint(0, 100)
                        await message.channel.send(f"{message.author.name} is {gay}% gay")
    if message.content == "owo virgin":
        coin = random.randint(0, 1)
        if coin == 0:
            await message.channel.send(f"{message.author.name} is a virgin")
        if coin == 1:
            await message.channel.send(f"{message.author.name} is not a Virgin")
    if message.content == "owo pp":
        pp = random.randint(0, 19)
        if pp == 0:
            await message.channel.send(f"{message.author.name}'s pp size: 8=D")
        if pp == 1:
            await message.channel.send(f"{message.author.name}'s pp size: 8==D")
        if pp == 2:
            await message.channel.send(f"{message.author.name}'s pp size: 8===D")
        if pp == 3:
            await message.channel.send(f"{message.author.name}'s pp size: 8====D")
        if pp == 4:
            await message.channel.send(f"{message.author.name}'s pp size: 8=====D")
        if pp == 5:
            await message.channel.send(f"{message.author.name}'s pp size: 8======D")
        if pp == 6:
            await message.channel.send(f"{message.author.name}'s pp size: 8=======D")
        if pp == 7:
            await message.channel.send(f"{message.author.name}'s pp size: 8========D")
        if pp == 8:
            await message.channel.send(f"{message.author.name}'s pp size: 8=========D")
        if pp == 9:
            await message.channel.send(f"{message.author.name}'s pp size: 8==========D")
        if pp == 10:
            await message.channel.send(f"{message.author.name}'s pp size: 8===========D")
        if pp == 11:
            await message.channel.send(f"{message.author.name}'s pp size: 8============D")
        if pp == 12:
            await message.channel.send(f"{message.author.name}'s pp size: 8=============D")
        if pp == 13:
            await message.channel.send(f"{message.author.name}'s pp size: 8==============D")
        if pp == 14:
            await message.channel.send(f"{message.author.name}'s pp size: 8===============D")
        if pp == 15:
            await message.channel.send(f"{message.author.name}'s pp size: 8================D")
        if pp == 16:
            await message.channel.send(f"{message.author.name}'s pp size: 8=================D")
        if pp == 17:
            await message.channel.send(f"{message.author.name}'s pp size: 8==================D")
        if pp == 18:
            await message.channel.send(f"{message.author.name}'s pp size: 8===================D")
        if pp == 19:
            await message.channel.send(f"{message.author.name}'s pp size: 8====================D")
    if message.content == "owo cbt":
        cbt = random.randint(0, 100)
        await message.channel.send(f"{message.author.name} is {cbt}% reliant on cognitive behavioural therapy")
    if message.content == "owo waifu":
        waifu = random.randint(0, 100)
        await message.channel.send(f"{message.author.name} is {waifu}% a waifu")
    if message.content == "owo 8ball":
        ball = random.randint(0, 19)
        if ball == 0:
            await message.channel.send(f"It is certain")
        if ball == 1:
            await message.channel.send(f"It is decidedly so")
        if ball == 2:
            await message.channel.send(f"Without a doubt")
        if ball == 3:
            await message.channel.send(f"Yes definitely")
        if ball == 4:
            await message.channel.send(f"You may rely on it")
        if ball == 5:
            await message.channel.send(f"As I see it, yes")
        if ball == 6:
            await message.channel.send(f"Most likely")
        if ball == 7:
            await message.channel.send(f"Outlook good")
        if ball == 8:
            await message.channel.send(f"Yes")
        if ball == 9:
            await message.channel.send(f"Signs point to yes")
        if ball == 10:
            await message.channel.send(f"Reply hazy, try again")
        if ball == 11:
            await message.channel.send(f"Ask again later")
        if ball == 12:
            await message.channel.send(f"Cannot predict now")
        if ball == 13:
            await message.channel.send(f"Concentrate and ask again")
        if ball == 14:
            await message.channel.send(f"Don't count on it")
        if ball == 15:
            await message.channel.send(f"My reply is no")
        if ball == 16:
            await message.channel.send(f"My sources say no")
        if ball == 17:
            await message.channel.send(f"Outlook not so good")
        if ball == 18:
            await message.channel.send(f"Very doubtful")
        if ball == 19:
            await message.channel.send(f"Cannot predict now")
    if message.content == "pog":
        await message.channel.send(f"That word is as dead as ur sense of humor, motherfucker")
    if message.content == "owo cringe":
        cringe = random.randint(0, 100)
        await message.channel.send(f"{message.author.name} is {cringe}% cringe")
    if message.content == "@everyone":
        await message.channel.send(f"{message.author.mention} Shut the fuck up")
    if message.content == "owo braincell":
        braincell = random.randint(0, 100000000000)
        await message.channel.send(f"{message.author.name} has {braincell} braincells")
    if message.content == "owo haircell":
        haircell = random.randint(0, 20000)
        await message.channel.send(f"{message.author.name} has {haircell} haircells")
    if message.content == "owo bald":
        bald = random.randint(0, 4)
        if bald == 0:
            await message.channel.send(f"Congrats! You have hair!")
        if bald == 1:
            await message.channel.send(f"LLL U have a receding hairline!")
        if bald == 2:
            await message.channel.send(f"You have a fucking bald patch cunt.")
        if bald == 3:
            await message.channel.send(f"Istg u have only got like 3 haircells.")
        if bald == 4:
            await message.channel.send(f"Where the fuck did all of your hair go.")
    if message.content == "owo help":
        embed = discord.Embed(title="Gay_Bot Help", description="Commands:", color=0xffb9e7)
        embed.add_field(
            name="owo gay, owo ping, owo, uwu, fuck, shit, owo coinflip, "
                 "owo virgin, owo pp, owo cbt, owo waifu, owo 8ball, pog, owo cringe, "
                 "@everyone, owo braincell, owo haircell, owo bald, owo invite, owo iq",
            value="made by labrador", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "owo invite":
        await message.channel.send(
            f"https://discord.com/api/oauth2/authorize?client_id=100"
            f"4450562881900544&permissions=296062774592&scope=bot%20applications.commands")
    if message.content == "owo iq":
        if message.author.id == 690898639656321026:
            await message.channel.send(f"{message.author.name} has an iq of 200")
        else:
            iq = random.randint(0, 200)
            await message.channel.send(f"{message.author.name} has an iq of {iq}")
    if message.content == "hi":
        await message.channel.send(f"Go away!")
    if message.content == "hello":
        await message.channel.send(f"GO THE FUCK AWAY CUNT")

client.run('')
