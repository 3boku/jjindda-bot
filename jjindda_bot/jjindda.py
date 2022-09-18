import discord, random
from discord import Client

token = "토근값"
intents = discord.Intents.default()
client: Client = discord.Client(intents=intents)

#시작코드
@client.event
async def on_ready():
    print(client.user.id)
    print("작동준비완료!")
    print("NANONANDFLASH#1066")
    game = discord.Game("$명령어치면 명령어 볼수있음")
    await client.change_presence(status=discord.Status.online, activity=game)

#텍스트 코드
@client.event
async def on_message(message):
    if message.content.startswith("찐따야 안녕"):
        await message.channel.send("어...어... 안.. 안녕..")
    if message.content.startswith("찐따야 ㅎㅇ"):
        await message.channel.send("어...어... 안.. 안녕..")
    if message.content.startswith("찐따야 안녕하세요"):
        await message.channel.send("반갑군 자네는 뭐하는 새끼인가")
    if message.content.startswith("찐따야 반가워"):
        await message.channel.send("어...어... 안.. 안녕..")
    if message.content.startswith("찐따야 뭐하고있어"):
        await message.channel.send("나.. 애니.. 보고.. 있..있었...어...")
    if message.content.startswith("찐따야 뭐해"):
        await message.channel.send("나.. 애니.. 보고.. 있..있었...어...")
    if message.content.startswith("$명령어"):
        await message.channel.send("'찐따야 급식표', '찐따야 n반시간표', '찐따야 (심심해, 빵사와, 안녕 등등)', '애니추천해줘'")
    if message.content.startswith("찐따야 나 심심해"):
        await message.channel.send("우..우리개발자랑 놀아... insta: p_q.d_23 디스코드: NANONANDFLASH#1066")
    if message.content.startswith("찐따야 빵사와"):
        await message.channel.send("맨.. 맨..날먹던... 크림...빵 맞..지..?")
    elif message.content.startswith("이거 아니잖아"):
        await message.channel.send("잘못했어 떄리지마ㅜㅜㅜ")
    if message.content.startswith("찐따야 너 모델이 누구야"):
        await message.channel.send("이민국입니다. 고죠#1592")
    if message.content.startswith("찐따야 고마워"):
        await message.channel.send("으..응..(날 좋아하나?)")
    if message.content.startswith("찐따야 대화시작"):
        await message.channel.send("준혁아 나랑 사귀자 ")
    if message.content.startswith("ㄲㅈ ㅂㅅㅇ"):
        await message.channel.send("좆까고 있네")
    if message.content.startswith("어? 씨빨이?"):
        await message.channel.send("ㅇ ㅇㅉ")


#사진나오게
    if message.content.startswith("찐따야 급식표"):
        await message.channel.send(file=discord.File("급식표.png"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 1반시간표"):
        await message.channel.send(file=discord.File("1반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 2반시간표"):
        await message.channel.send(file=discord.File("2반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 3반시간표"):
        await message.channel.send(file=discord.File("3반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 4반시간표"):
        await message.channel.send(file=discord.File("4반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 5반시간표"):
        await message.channel.send(file=discord.File("5반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 6반시간표"):
        await message.channel.send(file=discord.File("6반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 7반시간표"):
        await message.channel.send(file=discord.File("7반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 8반시간표"):
        await message.channel.send(file=discord.File("8반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")
    if message.content.startswith("찐따야 9반시간표"):
        await message.channel.send(file=discord.File("9반시간표.jpg"))
        await message.channel.send("여..여기..있..어...")

#랜덤
    if message.content == "애니추천해줘" :
        await message.channel.send(random.choice(['블렌드s', '귀멸의 칼날', '던전에서의 만남을 추구하면 안 되는 걸까', '5등분의 신부', '건어물 여동생 우마루짱', 'Re : 제로부터 시작하는 이세계 생활']))
        await message.channel.send("이.. 이거엄..엄청 재밌어...헤헤")



client.run(token)
