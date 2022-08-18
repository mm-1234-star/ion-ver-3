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


@bot.command()
async def 심심해(ctx):
    await ctx.reply('로보토미코퍼레이션 하자 스팀에서 26000원에 판매한다!!')


@bot.command()
async def 뭐하지(ctx):
    await ctx.reply('캐피탈리즘 호! 하는 만화보자!!')

bot.run('MTAwMzI3NDE0Mjg2ODU3NDI0OQ.Gm02AT.gFNePefYJCmpm5DaMZmA179zYRta3Qjm34dVNo')
