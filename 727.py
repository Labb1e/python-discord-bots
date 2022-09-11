import discord
import aiocron

client = discord.Client()

@client.event
async def on_ready():
    print("Ready!")
    print(f'Logged in as {client.user} on {len(client.guilds)} servers')

@aiocron.crontab('27 0 * * *')
async def cronjob1():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Idaho!')

@aiocron.crontab('27 1 * * *')
async def cronjob2():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Texas!')

@aiocron.crontab('27 2 * * *')
async def cronjob3():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in New York!')

@aiocron.crontab('27 3 * * *')
async def cronjob4():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Barbados!')

@aiocron.crontab('27 4 * * *')
async def cronjob5():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Guyana!')

@aiocron.crontab('27 5 * * *')
async def cronjob6():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Brazil!')

@aiocron.crontab('27 6 * * *')
async def cronjob7():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Cape Verde!')

@aiocron.crontab('27 7 * * *')
async def cronjob8():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in the UK!')

@aiocron.crontab('27 8 * * *')
async def cronjob9():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in France!')

@aiocron.crontab('27 9 * * *')
async def cronjob10():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Greece!')

@aiocron.crontab('27 10 * * *')
async def cronjob11():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Qatar!')

@aiocron.crontab('27 11 * * *')
async def cronjob12():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in the UAE!')

@aiocron.crontab('27 12 * * *')
async def cronjob13():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Pakistan!')

@aiocron.crontab('27 13 * * *')
async def cronjob14():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Bangladesh!')

@aiocron.crontab('27 14 * * *')
async def cronjob15():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Singapore!')

@aiocron.crontab('27 15 * * *')
async def cronjob16():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Malaysia!')

@aiocron.crontab('27 16 * * *')
async def cronjob17():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Western Australia!')

@aiocron.crontab('27 17 * * *')
async def cronjob18():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Eastern Australia!')

@aiocron.crontab('27 18 * * *')
async def cronjob19():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Samoa!')

@aiocron.crontab('27 19 * * *')
async def cronjob20():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in New Zealand!')

@aiocron.crontab('27 20 * * *')
async def cronjob21():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Tonga!')

@aiocron.crontab('27 21 * * *')
async def cronjob22():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in Kiribati!')

@aiocron.crontab('27 22 * * *')
async def cronjob23():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 nowhere but i still added this time!')

@aiocron.crontab('27 23 * * *')
async def cronjob24():
    channel = client.get_channel(998609893877616683)
    await channel.send('It is 7:27 in also nowhere but i also still added this!')


client.run()