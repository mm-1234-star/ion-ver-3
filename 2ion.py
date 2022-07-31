import discord
from discord.ext.commands import Bot
import random

intents=discord.Intents.default()
bot = Bot(command_prefix='이온아 ', intents=intents)
client = discord.Client()


@bot.event
async def on_ready() :
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("이온아 도움"))
    print("이온작동!!")


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


@bot.command()
async def hello(ctx):
    await ctx.reply('hello world')

bot.run('MTAwMzI3NDE0Mjg2ODU3NDI0OQ.Gm02AT.gFNePefYJCmpm5DaMZmA179zYRta3Qjm34dVNo')
