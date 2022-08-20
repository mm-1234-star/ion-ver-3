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
async def 도움(ctx) :
    embed = discord.Embed(title="안기여운 짭이온!!", description="우주최강이라서 곧 세계를 지배함", color=0x36ccf2)
    embed.add_field(name="기본 사용법", value="이온아 (하고싶은말)", inline=False)
    embed.add_field(name="배운말들 별로없음", value="짭이온의 인성이 안좋아서 그렇다", inline=False)
    embed.add_field(name="이온아 주사위", value="짭이온이 1부터 6까지의 숫자를 랜덤으로 준다", inline=False)
    embed.add_field(name="이온아 인형뽑기(또는 인)", value="짭이온이 인형뽑기에서 랜덤으로 인형을 뽑아준다", inline=False)
    embed.add_field(name="이온아 자판기(또는 자)", value="짭이온이 자판기에서 랜덤으로 음료를 뽑아준다", inline=False)
    embed.add_field(name="이온아 따라하기", value="짭이온이 따라하기뒤에 있는 말을 따라한다", inline=False)
    embed.set_footer(text="(망한봇..)")
    await ctx.reply(embed=embed)


@bot.command()
async def 심심해(ctx):
    await ctx.reply('로보토미코퍼레이션 하자 스팀에서 26000원에 판매한다!!')


@bot.command()
async def 뭐하지(ctx):
    await ctx.reply('캐피탈리즘 호! 하는 만화보자!!')

bot.run('MTAwMzI3NDE0Mjg2ODU3NDI0OQ.Gm02AT.gFNePefYJCmpm5DaMZmA179zYRta3Qjm34dVNo')
