import asyncio
import discord
import random

intents = discord.Intents.default()
intents.message_content = True # make sure to go to developer portal and turn on the respective intents
client = discord.Client(intents=intents)

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    channel = message.channel

    async def delay():
        await asyncio.sleep(0.7)

    greeting = ['hello', 'hi', 'hey', 'gm', 'gn']
    for x in greeting:
        if message.content.startswith(x) and len(x) <= 3:
            await delay()
            async with message.channel.typing():
                await channel.send('SHUT UP')
        elif message.content.startswith(x) and len(x) > 3:
            await delay()
            async with message.channel.typing():
                await channel.send('LEAVE ME ALONE')

    basic_question = ['?', 'what']
    for x in basic_question:
        if message.content.startswith(x) and x == basic_question[0]:
            await delay()
            async with message.channel.typing():
                await channel.send('question marks go at the end, you moron')
        elif x in message.content and len(x) > 1:
            await delay()
            async with message.channel.typing():
                await channel.send('do you ever stop talking')

    speculative_question = ['imagine', 'consider', 'think']
    for x in speculative_question:
        if x in message.content:
           if x == speculative_question[0]:
                await delay()
                async with message.channel.typing():
                   await channel.send('imagine if you didnt speak')
           elif x == speculative_question[1]:
                await delay()
                async with message.channel.typing():
                   await channel.send('have you considered picking up a hobby or two <:sob:1113665958939205632>')
           elif x == speculative_question[2]:
                await delay()
                async with message.channel.typing():
                   await channel.send('have you thought not breathing? you know, to save oxygen?')

    firstPerson = ['thats cool but i dont care', 'nobody is listening to you',
                   'bro you jus love to talk huh <:skull:1113634475218325635>']
    firstPersonResponse = random.choice(firstPerson)
    if message.content.startswith('i '):
        await delay()
        async with message.channel.typing():
            await channel.send(firstPersonResponse)

    secondPerson = ['i aint even a real person bruh <:skull_crossbones:1113667775152529490>',
                    'you genuinely need to stop talking to me' ] #add more
    secondPersonResponse = random.choice(secondPerson)
    if message.content.startswith('you '):
        await delay()
        async with message.channel.typing():
            await channel.send(secondPersonResponse)


@client.event
async def on_ready():
    gameList = ['Google Classroom', 'Gmail', 'JupiterEd', 'Runestone Academy', 'practice.it',
                'codingbat.com', 'My AP Classroom']
    game = discord.Game(random.choice(gameList))
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('AAAAA')


client.run(token) #environment file containing token has not been implemented yet
