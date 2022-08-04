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
async def 이온(ctx):
    await ctx.reply('왜')


@bot.command()
async def 이온찬양(ctx):
    await ctx.reply('차냥해')


@bot.command()
async def 배고파(ctx):
    await ctx.reply('밥먹어')


@bot.command()
async def 자기소개(ctx):
    await ctx.reply('세상을 정복할 우주최강 봇!!')


@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.reply(text)


@bot.command()
async def 가위바위보(ctx, user: str):  
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot) 
    if result == 0:
        await ctx.reply(f'{user} vs {bot}  비겼다!!')
    elif result == 1 or result == -2:
        await ctx.reply(f'{user} vs {bot}  오류임.암튼그럼.')
    else:
        await ctx.reply(f'{user} vs {bot}  내가 이김 숫고')


@bot.command()
async def 울프님(ctx):
    await ctx.reply('비코님보다 이상함')


@bot.command()
async def 비코님(ctx):
    await ctx.reply('울프님보다 이상함')


@bot.command()
async def 뀨(ctx):
    await ctx.reply('뀨')


@bot.command()
async def 깡통(ctx):
    await ctx.reply('아니거든!!')


@bot.command()
async def 샌즈(ctx):
    await ctx.reply('wa sans!')

@bot.command()
async def 슈슉(ctx):
    await ctx.reply('슉.슈슉.슈.슈슉.슉')

@bot.command()
async def 입시덕후(ctx):
    await ctx.reply('후!')

@bot.command()
async def 안녕(ctx):
    await ctx.reply('안녕!')


@bot.command()
async def 네로리님(ctx):
    await ctx.reply('>.<!!')


@bot.command()
async def 에메랄드님(ctx):
    await ctx.reply('돌맹이')


@bot.command()
async def 쿠마린님(ctx):
    await ctx.reply('여신!!')


@bot.command()
async def 피코님(ctx):
    await ctx.reply('찬양!!')


@bot.command()
async def 한숨님(ctx):
    await ctx.reply('존잘님!!')


@bot.command()
async def 모딘님(ctx):
    await ctx.reply('귤!!')


@bot.command()
async def 카툰윤아님(ctx):
    await ctx.reply('유니콘!!')


@bot.command()
async def 페니님(ctx):
    await ctx.reply('만세!!')


@bot.command()
async def 똥꾸님(ctx):
    await ctx.reply(':rainbow:')


@bot.command()
async def 귤희님(ctx):
    await ctx.reply('>: ) !!')


@bot.command()
async def 세디님(ctx):
    await ctx.reply('퇴물!')


@bot.command()
async def 호야님(ctx):
    await ctx.reply('거부기!!')


@bot.command()
async def 코디님(ctx):
    await ctx.reply('주황색!!')


@bot.command()
async def 안득님(ctx):
    await ctx.reply('메뚜기!!')


@bot.command()
async def 사랑해(ctx):
    await ctx.reply('우리..헤어지자...')


@bot.command()
async def 야옹(ctx):
    await ctx.reply('냐아악아앍엉아아아악')


@bot.command()
async def 돈(ctx):
    await ctx.reply('돈 없어')


@bot.command()
async def 잘가(ctx):
    await ctx.reply('짭이온님이 서버를 떠나셨습니다.')


@bot.command()
async def 배워(ctx):
    await ctx.reply('싫어')


@bot.command()
async def 저리가(ctx):
    await ctx.reply('안녕히 계세요 여러분!전 이 세상의 모든 굴레와 속박을 벗어 던지고 제 행복을 찾아 떠납니다!여러분도 행복하세요~~!')



@bot.command()
async def 둣교(ctx):
    await ctx.reply('둣교봇 귀여워!!')


@bot.command()
async def 소맥거핀님(ctx):
    await ctx.reply('OwO')


@bot.command()
async def 고누리님(ctx):
    await ctx.reply('형형~브로콜리 가지 오이 당근 토마트샐러드에 굴소스뿌려서 건포도빵 먹어줘~')


@bot.command()
async def 테미(ctx):
    await ctx.reply('안뇽! 테미 샵에 온 걸... 화녕행!!!!')


@bot.command()
async def 가우르구라(ctx):
    await ctx.reply('상어!!')


@bot.command()
async def 크시(ctx):
    await ctx.reply('자꾸 말바꾼다.')

@bot.command()
async def 배추(ctx):
    await ctx.reply('김치!!')


@bot.command()
async def 미육(ctx):
    await ctx.reply('미역!!')


@bot.command()
async def 이드님(ctx):
    await ctx.reply('이드탕!!')

@bot.command()
async def 마티나(ctx):
    await ctx.reply('안녕하십니까? 이온이라고합니다?')


@bot.command()
async def 스페이드(ctx):
    await ctx.reply('걔 이름 스페이드 아니야!!')


@bot.command()
async def 워터리(ctx):
    await ctx.reply('물')


@bot.command()
async def 이프(ctx):
    await ctx.reply('ㅇㄴㅅ')


@bot.command()
async def 심심해(ctx):
    await ctx.reply('나도..')

@bot.command()
async def 링딩동(ctx):
    await ctx.reply('링딩동링딩동링기리리링링딩딩')


@bot.command()
async def 밖득님(ctx):
    await ctx.reply('메뚜기!!!')


@bot.command()
async def 티라미수님(ctx):
    await ctx.reply('존경!!!')


@bot.command()
async def 리오님(ctx):
    await ctx.reply(':dog:')


@bot.command()
async def 생강님(ctx):
    await ctx.reply(':초생강!!:')


@bot.command()
async def 콜라(ctx):
    await ctx.reply('이온음료가 최고!!(사실 이봇의 주인은 콜라를 더 좋아합니다)')



@bot.command()
async def 사이다(ctx):
    await ctx.reply('이온음료가 최고!!(사실 이봇의 주인은 사이다를 더 좋아합니다)')



@bot.command()
async def 환타(ctx):
    await ctx.reply('이온음료가 최고!!(사실 이봇의 주인은 환타를 더 좋아합니다)')



@bot.command()
async def 이온음료(ctx):
    await ctx.reply('최고!!(사실 이봇의 주인은 이온음료를 안좋아합니다)')



@bot.command()
async def 주사위(ctx):
    randnum = random.randint(1, 6)
    await ctx.reply(f'주사위 결과는 {randnum} !!')


@bot.command()
async def 인형뽑기(ctx):
    minerals = ['**스페이드 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944761695421730857/1382_20220220093642.png?width=694&height=572 ', '**이온 인형을 뽑았다!...으응?**ㅣ*확률 0.1%*  https://media.discordapp.net/attachments/768375730773164046/944761695086182431/1382_20220220093202.png?width=694&height=572 ', '**돌리 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944761695904088094/1382_20220220095025.png?width=694&height=572 ', '**이바 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944761696155762728/1382_20220220095809.png?width=694&height=572 ', '**디유 인형을 뽑았다!**ㅣ*확률 1%* https://media.discordapp.net/attachments/768375730773164046/944761696365453343/1382_20220220100446.png?width=694&height=572 ', '**프레즈 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944764341150945300/1382_20220220101600.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750994175176734/1382_20220220091803.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750994477178920/1382_20220220091905.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995051802714/1382_20220220091945.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995357958164/1382_20220220092024.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995576074270/1382_20220220092037.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995823558747/1382_20220220092116.png?width=694&height=572 ', '**토끼 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750996091977728/1382_20220220092226.png?width=694&height=572 ', '**토끼 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944749170328207380/1382_20220220091540.png?width=694&height=572 ', '**강아지 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944749169078304798/1382_20220220084131.png?width=694&height=572 ', '**귀여운 인형을 뽑았다!*ㅣ*확률 8%*  https://media.discordapp.net/attachments/768375730773164046/944749169992683530/1382_20220220091245.png?width=694&height=572 ', '**먼지를 뽑았다..**ㅣ*확률 50%*  https://media.discordapp.net/attachments/768375730773164046/944749169690701834/1382_20220220090536.png?width=694&height=572 ']
    weights = [1, 0.1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 50]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.reply(results[0])

    
@bot.command()
async def 인(ctx):
    minerals = ['**스페이드 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944761695421730857/1382_20220220093642.png?width=694&height=572 ', '**이온 인형을 뽑았다!...으응?**ㅣ*확률 0.1%*  https://media.discordapp.net/attachments/768375730773164046/944761695086182431/1382_20220220093202.png?width=694&height=572 ', '**돌리 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944761695904088094/1382_20220220095025.png?width=694&height=572 ', '**이바 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944761696155762728/1382_20220220095809.png?width=694&height=572 ', '**디유 인형을 뽑았다!**ㅣ*확률 1%* https://media.discordapp.net/attachments/768375730773164046/944761696365453343/1382_20220220100446.png?width=694&height=572 ', '**프레즈 인형을 뽑았다!**ㅣ*확률 1%*  https://media.discordapp.net/attachments/768375730773164046/944764341150945300/1382_20220220101600.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750994175176734/1382_20220220091803.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750994477178920/1382_20220220091905.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995051802714/1382_20220220091945.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995357958164/1382_20220220092024.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995576074270/1382_20220220092037.png?width=694&height=572 ', '**고양이 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750995823558747/1382_20220220092116.png?width=694&height=572 ', '**토끼 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944750996091977728/1382_20220220092226.png?width=694&height=572 ', '**토끼 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944749170328207380/1382_20220220091540.png?width=694&height=572 ', '**강아지 인형을 뽑았다!**ㅣ*확률 4%*  https://media.discordapp.net/attachments/768375730773164046/944749169078304798/1382_20220220084131.png?width=694&height=572 ', '**귀여운 인형을 뽑았다!**ㅣ*확률 8%*  https://media.discordapp.net/attachments/768375730773164046/944749169992683530/1382_20220220091245.png?width=694&height=572 ', '**먼지를 뽑았다..**ㅣ*확률 50%*  https://media.discordapp.net/attachments/768375730773164046/944749169690701834/1382_20220220090536.png?width=694&height=572 ']
    weights = [1, 0.1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 50]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.reply(results[0])



@bot.command()
async def 자판기(ctx):
    minerals = ['**님 음료수 저분이 가져가셨는데요..**ㅣ*확률 0.3%*  https://media.discordapp.net/attachments/927793158576832525/929197984862830622/1267_20220108083857.png?width=694&height=572 ', '**무지갯빛 총공격이다!!!** :rainbow: ㅣ*확률 0.7%* https://media.discordapp.net/attachments/927793158576832525/929197985341014036/1267_20220107201343.png?width=694&height=572 ', '**에엥..고양이?**ㅣ*확률 0.5%* https://media.discordapp.net/attachments/927793158576832525/929679660906864640/1267_20220109185040.png?width=694&height=572 ', '**체력을 회복하셨습니다!...그런건없다.**ㅣ확률 0.5%  https://media.discordapp.net/attachments/824152751184674826/944747041312083978/1331_20220201193656.png?width=694&height=572 ', '와! 저퀄레모네이드를 뽑았...다? 죄송합니다 그리다가 졸렸어요ㅣ확률 1.5% https://media.discordapp.net/attachments/927793158576832525/929679660541952010/1267_20220109191154.png?width=694&height=572 ',  '**와! 초코라떼를 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929679661284347935/1267_20220109183756.png?width=694&height=572 ', '**와! 민초가 세상을 지배한다!!!ㅣ확률 2%** https://media.discordapp.net/attachments/927793158576832525/929679662202880040/1267_20220109173622.png?width=694&height=572 ', '**와! 달고나라떼를 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929679661527609354/1267_20220109165056.png?width=694&height=572 ', '**와! 딸기요거트를 뽑았다!!!**ㅣ*확률2%* https://media.discordapp.net/attachments/927793158576832525/929679661913501756/1267_20220109162824.png?width=694&height=572 ', '**와! 메론소다를 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929197985768804392/1267_20220108111651.png?width=694&height=572 ', '**와! 체리콕을 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929197986058231878/1267_20220108091206.png?width=694&height=572 ', '**와! 복숭아맛 탄산음료를 뽑았다!!**ㅣ확률 3% https://media.discordapp.net/attachments/927793158576832525/929197989052973126/1267_20220107195830.png?width=739&height=609 ', '**와! 초코우유를 뽑았다!!**ㅣ확률 3% https://media.discordapp.net/attachments/927793158576832525/929197988352512020/1267_20220107193805.png?width=739&height=609 ', '**와! 딸기우유를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197988608372826/1267_20220107190025.png?width=739&height=609 ', '**와! 바나나우유를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197986452504586/1267_20220107184715.png?width=739&height=609 ', '**와! 이온음료를 뽑았다!!...내 연료ㅣ*확률 4%* https://media.discordapp.net/attachments/927793158576832525/929609957849071637/FIfNFoiakAQCA02.png?width=739&height=609 ', '**와! 콜라를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197945474150478/1267_20220107181126.png?width=739&height=609 ', '**와! 사이다를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197945839034368/1267_20220107174817.png?width=739&height=609 ', '**와! 오렌지주스를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197946153599076/1267_20220107173330.png?width=739&height=609 ', '**요구르트를 뽑았다!ㅣ*확률3%*  https://media.discordapp.net/attachments/824152751184674826/944747041827999744/1331_20220205100049.png?width=694&height=572 ', '**커피를 뽑았다!**ㅣ*확률15%* https://media.discordapp.net/attachments/927793158576832525/929197946526912542/1267_20220107160822.png?width=739&height=609 ', '**물을 뽑았다!**ㅣ*확률41.5%* https://media.discordapp.net/attachments/927793158576832525/929197946900209694/1267_20220107155501.png?width=694&height=572 ']
    weights = [0.3, 0.7, 0.5, 0.5, 1.5, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 3, 3, 3, 3, 15, 41.5]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.reply(results[0])




@bot.command()
async def 자(ctx):
    minerals = ['**님 음료수 저분이 가져가셨는데요..**ㅣ*확률 0.3%*  https://media.discordapp.net/attachments/927793158576832525/929197984862830622/1267_20220108083857.png?width=694&height=572 ', '**무지갯빛 총공격이다!!!** :rainbow: ㅣ*확률 0.7%* https://media.discordapp.net/attachments/927793158576832525/929197985341014036/1267_20220107201343.png?width=694&height=572 ', '**에엥..고양이?**ㅣ*확률 0.5%* https://media.discordapp.net/attachments/927793158576832525/929679660906864640/1267_20220109185040.png?width=694&height=572 ', '**체력을 회복하셨습니다!...그런건없다.**ㅣ확률 0.5%  https://media.discordapp.net/attachments/824152751184674826/944747041312083978/1331_20220201193656.png?width=694&height=572 ', '와! 저퀄레모네이드를 뽑았...다? 죄송합니다 그리다가 졸렸어요ㅣ확률 1.5% https://media.discordapp.net/attachments/927793158576832525/929679660541952010/1267_20220109191154.png?width=694&height=572 ',  '**와! 초코라떼를 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929679661284347935/1267_20220109183756.png?width=694&height=572 ', '**와! 민초가 세상을 지배한다!!!ㅣ확률 2%** https://media.discordapp.net/attachments/927793158576832525/929679662202880040/1267_20220109173622.png?width=694&height=572 ', '**와! 달고나라떼를 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929679661527609354/1267_20220109165056.png?width=694&height=572 ', '**와! 딸기요거트를 뽑았다!!!**ㅣ*확률2%* https://media.discordapp.net/attachments/927793158576832525/929679661913501756/1267_20220109162824.png?width=694&height=572 ', '**와! 메론소다를 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929197985768804392/1267_20220108111651.png?width=694&height=572 ', '**와! 체리콕을 뽑았다!!!**ㅣ*확률 2%* https://media.discordapp.net/attachments/927793158576832525/929197986058231878/1267_20220108091206.png?width=694&height=572 ', '**와! 복숭아맛 탄산음료를 뽑았다!!**ㅣ확률 3% https://media.discordapp.net/attachments/927793158576832525/929197989052973126/1267_20220107195830.png?width=739&height=609 ', '**와! 초코우유를 뽑았다!!**ㅣ확률 3% https://media.discordapp.net/attachments/927793158576832525/929197988352512020/1267_20220107193805.png?width=739&height=609 ', '**와! 딸기우유를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197988608372826/1267_20220107190025.png?width=739&height=609 ', '**와! 바나나우유를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197986452504586/1267_20220107184715.png?width=739&height=609 ', '**와! 이온음료를 뽑았다!!...내 연료ㅣ*확률 4%* https://media.discordapp.net/attachments/927793158576832525/929609957849071637/FIfNFoiakAQCA02.png?width=739&height=609 ', '**와! 콜라를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197945474150478/1267_20220107181126.png?width=739&height=609 ', '**와! 사이다를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197945839034368/1267_20220107174817.png?width=739&height=609 ', '**와! 오렌지주스를 뽑았다!!**ㅣ*확률 3%* https://media.discordapp.net/attachments/927793158576832525/929197946153599076/1267_20220107173330.png?width=739&height=609 ', '**요구르트를 뽑았다!ㅣ*확률3%*  https://media.discordapp.net/attachments/824152751184674826/944747041827999744/1331_20220205100049.png?width=694&height=572 ', '**커피를 뽑았다!**ㅣ*확률15%* https://media.discordapp.net/attachments/927793158576832525/929197946526912542/1267_20220107160822.png?width=739&height=609 ', '**물을 뽑았다!**ㅣ*확률41.5%* https://media.discordapp.net/attachments/927793158576832525/929197946900209694/1267_20220107155501.png?width=694&height=572 ']
    weights = [0.3, 0.7, 0.5, 0.5, 1.5, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 3, 3, 3, 3, 15, 41.5]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.reply(results[0])

bot.run('MTAwMzI3NDE0Mjg2ODU3NDI0OQ.Gm02AT.gFNePefYJCmpm5DaMZmA179zYRta3Qjm34dVNo')
