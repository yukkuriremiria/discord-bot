import discord
from discord.ext import commands
import requests, bs4

res = requests.get('https://test4343434.harumaki.repl.co/');
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('#list h2')
for elem in elems:
    token = "OTY4MTg2MjQyMDQwNzMzNzE2.YmbLtA.HKe9sAClmMYP682q-PuJXKXh_ys"

client = commands.Bot(command_prefix="pi!")


@client.event
async def on_ready():
   print(''' 
正常に起動しました！
 ''')
   await client.change_presence(activity=discord.Game(name="てすとです"))


@client.command()
async def helpmenu(ctx):
    print ("helpmenu : ヘルプを表示しましす")



@client.event
   await client.change_presence(activity=discord.Game(name="てすと"))
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await message.channel.send(m)

client.run(token, bot=True)
