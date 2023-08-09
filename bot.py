import discord
from discord.ext import commands
from googletrans import Translator
import random
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.event
async def on_member_join(member):
    await member.send(f"{member} sunucuya hoş geldin.")
@bot.event
async def on_message_delete(message):
    print(f"{message.author} : {message.content} : {message.created_at}")
@bot.command()
async def cevir(ctx, text):
    translator = Translator()
    ceviri = translator.translate(text)
    await ctx.send(ceviri.text)
@bot.command()
async def ban(member):
    await ban(member)
@bot.event
async def on_member_ban(guild,member):
    await member.send(f"{guild} sunucusundan banlandınız. Bütün eğlenceyi kaçıracaksınız.")
@bot.command()
async def unban(member):
    await unban(member)
@bot.event
async def on_member_unban(guild,member):
    await member.send(f"{guild} sunucusuna olan banınız kaldırılmıştır. Aramıza tekrar hoşgeldiniz")
@bot.command()
async def sendMeme(ctx):
    liste = os.listdir("meme")
    randomMeme = random.choice(liste)
    fullPlace = "meme/" + randomMeme
    f = open(fullPlace,"rb")
    meme = discord.File(f)
    await ctx.send(file=meme)
@bot.command()
async def sendSong(ctx):
    liste = os.listdir("song")
    randomSong = random.choice(liste)
    fullDest = "song/" + randomSong
    f = open(fullDest,"rb")
    song = discord.File(f)
    await ctx.send(file=song)
bot.run("TOKEN")


