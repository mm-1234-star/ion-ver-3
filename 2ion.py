import discord
import random
import io
from PIL import Image, ImageDraw, ImageFont
import requests
import json
import asyncio

bot=discord.Bot()

url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(url)
data = json.loads(response.text)
pokemon_list = [pokemon['name'] for pokemon in data['results']]

@bot.command()
async def 포켓몬퀴즈(ctx):
    pokemon_name = random.choice(pokemon_list)

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(pokemon_url)
    data = json.loads(response.text)
    image_url = data['sprites']['front_default']

    species_url = data['species']['url']
    species_response = requests.get(species_url)
    species_data = json.loads(species_response.text)
    for name in species_data['names']:
        if name['language']['name'] == 'ko':
            pokemon_kor_name = name['name'].lower()
            break

    embed = discord.Embed(title="오늘의 포켓몬은 뭘까아~~~요??", description=f"- 오박사", color=0x00FFFF)
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    try:
        answer = await bot.wait_for('message', timeout=30.0, check=check)
        await ctx.send(f'정답은 {pokemon_kor_name}!')
    except asyncio.TimeoutError:
        await ctx.send("저런, 시간초과란다")

@bot.slash_command(description="뉴-리뉴얼 자판기")
async def 자판기(ctx):
    drinks = ['물', '커피', '오렌지주스', '사이다', '콜라', '쏠에눈', '대자와', '바나나우유', '딸기우유', '초코우유', '이온음료', '복숭아음료', '딸기라떼', '초코라떼', '민트초코프라페', '네온시티소다', '핑크소다', '크림소다', '메론소다', '체리콕', '뚜껑따인웰치어스', '알수없는 무언가', '도둑']
    weights = [22, 16, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 3, 3, 3, 2, 3, 3, 2, 1, 1, 1]
    result = random.choices(drinks, weights=weights, k=1)[0]
    prob = weights[drinks.index(result)]
    image_file = f"{result}.png"
    image_path = rf"C:\Users\jgs14\OneDrive\바탕 화면\gotcha\drinks\{image_file}"
    await ctx.respond(content=f"뽑힌 것은 {result}! 확률{prob}%!", file=discord.File(image_path))

@bot.slash_command(description="1부터 6까지의 숫자중 하나를 랜덤뽀끼이")
async def 주사위(ctx):
    randnum = random.randint(1, 6)
    embed = discord.Embed(
        title=f'주사위 결과는 {randnum}입니다!',
        color=0x00FFFF
    )
    await ctx.respond(embed=embed)

class MyView(discord.ui.View):
    @discord.ui.button(label="(지구 멸망 버튼)", style=discord.ButtonStyle.primary, emoji="🛑")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("지구는 멸망했습니다!")

@bot.slash_command()
async def 지구멸망(ctx):
    await ctx.respond("이것은 지구멸망 버튼입니다...누르시겠습니까?", view=MyView())

@bot.command()
async def 숫자맞추기(ctx, 정답: discord.Option(int)):
    num = random.randint(1, 10)
    if 정답 == num:
        await ctx.respond('맞추셨습니다! 궁예질에 소질이 있으신것같은데 대머리신가요?')
    else:
        await ctx.respond(f'정답은 {num}이였습니다. 멍청한 인간이시군요!')

@bot.slash_command()
async def 보노보노피피티(ctx, text: discord.Option(str)):
    bg_image = Image.open('보노보노.png')

    font_path = '궁서체.ttf'
    font_size = 100
    font = ImageFont.truetype(font_path, font_size)

    color = (255, 255, 255)

    draw = ImageDraw.Draw(bg_image)
    text_content = text
    text_width, text_height = draw.textsize(text_content, font=font)
    x = (bg_image.width - text_width) / 2
    y = (bg_image.height - text_height) / 2

    draw.text((x, y), text_content, fill=color, font=font)

    new_image_path = 'new_image.png'
    bg_image.save(new_image_path)

    await ctx.respond(file=discord.File(new_image_path))

@bot.slash_command()
async def 뭔가메스가키(ctx, message: discord.Option(str)):
    converted = message.replace("거냐", "야?♡")
    converted = converted.replace("다", "다라구~허접♡")
    converted = converted.replace("당신", "너같은 허접")
    converted = converted.replace("너", "너같은 바보")
    converted = converted.replace("정말", "완~전")
    converted = converted.replace("네", "네~♡")
    converted = converted.replace("?", "~?♡")
    converted = converted.replace("!", "~!!♡")
    converted = converted.replace("ㅋ", "w")
    converted = converted.replace("요", "~")
    
    embed = discord.Embed(title=f"허접♡{converted}~~www 완전 최저♡", color=0x00FFFF)
    await ctx.respond(embed=embed)

bot.run('ODc2OTY5MDQ3MTcyOTg5MDI5.GkIHCn.kZYOHsdSG97Nv8xI31JwAxGvagbymJaSbkq3uM')
