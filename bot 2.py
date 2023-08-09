import discord
from discord.ext import commands
from googletrans import Translator
import random
import os
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

pollMessage = [] 
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command(pass_context = True)
async def poll(ctx, txt):
    global pollMessage
    await delete_messages(ctx.message)
    await ctx.send(txt)
    pollMessage = ["True",ctx.message]
    await ctx.add_reaction(":thumbsup:")
    await ctx.add_reaction(":thumbsdown:")
bot.run("TOKEN")
