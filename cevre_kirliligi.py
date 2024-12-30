import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program get_duck_image_url fonksiyonunu çağırır'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

@bot.command()
async def cevre_kirliligi(ctx):
    await ctx.send("Çevre kirliliği, insanların çevreye zarar veren atıklarını doğaya bırakmaları sonucu oluşan bir sorundur. ")


 
    
bot.run("MTI3NzY3MTkxNTM3MjQxNzA4NA.GhuVoF.k7Mavr27vsyc4Q9rOylMG39NeiT4lPIYfHcVlg")
