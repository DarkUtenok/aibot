import discord
from discord.ext import commands
from config import *
import requests
from PIL import Image
import os
from ai_logic import classificate_image

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Успешно запущен бот", bot.user.name)


@bot.command(aliases=["img"])
async def i(ctx):
    if len(ctx.message.attachments) > 0:
        img = Image.open(requests.get(ctx.message.attachments[0].url, stream=True).raw).convert("RGB")
        result = classificate_image(img)
        await ctx.send('Я думаю на картинке ' + result)
        
    else:
        await ctx.send('добавьте изображение, пожалуйста.')

bot.run(TOKEN)