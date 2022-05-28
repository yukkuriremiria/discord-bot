import discord
from discord.ext import commands

client = commands.Bot(command_prefix="pi!")

@client.event
async def on_ready():
   print('''
正常に起動できますん
 ''')
   await client.change_presence(activity=discord.Game(name="Windowsサーバーからてすと"))

@client.event
async def on_message(message):
    if message.content.startswith("偽警告"):
        if client.user != message.author:
            m = "https://pi-mannokanzumee.ml/%E3%82%A8%E3%83%A9%E3%83%BC%E3%83%8A%E3%83%B3%E3%83%90%E3%83%BC%EF%BC%9ABW6VE36.mp4"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("おやすみ"):
        if client.user != message.author:
            m = "おやすみなさい" + message.author.name + "さん♡"
            await message.channel.send(m)


async def on_message(message):
    if message.content.startswith("おはよ"):
        if client.user != message.author:
            m = "おはよございます！" + message.author.name + "さん♡"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("あーしこしこ"):
        if client.user != message.author:
            m = "TADA=あーしこしこBOT"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("ぴぃまんぼっと"):
        if client.user != message.author:
            m = "呼んだ？" + message.author.name + "すん"
            await message.channel.send(m)
@client.event
async def on_message(message):
    if message.content.startswith("pi!m"):
        if client.user != message.author:
            m = + message.author.name + "さんが、ご飯を食べに行くそです"
            await message.channel.send(m)
@client.event
async def on_message(message):
    if message.content.startswith("pi!f"):
        if client.user != message.author:
            m = message.author.name + "さんが、お風呂に入るらしいです"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("飯"):
        if client.user != message.author:
            m = "行ってらっしゃい！" + message.author.name + "さん♡"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith(":kusa:"):
        if client.user != message.author:
            m = "www"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("www"):
        if client.user != message.author:
            m = "www"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("TADA"):
        if client.user != message.author:
            m = "TADA=あーしこしこBOT"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("🤣"):
        if client.user != message.author:
            m = "www"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("死ね"):
        if client.user != message.author:
            m = "(´・ω・`)"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("ぴぃまん"):
        if client.user != message.author:
            m = "https://www.youtube.com/channel/UCQDr6KWgEHNnKvhTzaUuYjQ"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("ホームページ"):
        if client.user != message.author:
            m = "https://pi-mannokanzumee.ml"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("草"):
        if client.user != message.author:
            m = "wwww"
            await message.channel.send(m)
@client.event
async def on_message(message):
    if message.content.startswith("TADA"):
        if client.user != message.author:
            m = "TADA=あーしこしこBOT"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("TADA"):
        if client.user != message.author:
            m = "声出ししろ"
            await message.channel.send(m)
@client.event
async def on_message(message):
    if message.content.startswith("k"):
        if client.user != message.author:
            m = "声出ししろ"
            await message.channel.send(m)
@client.event
async def on_message(message):
    if message.content.startswith("koe"):
        if client.user != message.author:
            m = "声出ししろ"
            await message.channel.send(m)
@client.event
async def on_message(message):
    if message.content.startswith("azure神"):
        if client.user != message.author:
            m = "死ねや" + message.author.name
            await message.channel.send(m)



client.run('OTY4MTg2MjQyMDQwNzMzNzE2.YmbLtA.HKe9sAClmMYP682q-PuJXKXh_ys')
