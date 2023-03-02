import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('你媽')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "?test" or message.content == "?Test":
        await message.channel.send('早上好中國 現在我有冰淇淋')
    if message.content == "?臭甲":
        await message.channel.send("你是臭甲")

client.run("OTUyMDU3NTMyNjI3NjkzNjM5.GZWwNo.Q3uk0-JoBZUYuoxVK7fZpCIe_UlCf8K6jSYs9I")