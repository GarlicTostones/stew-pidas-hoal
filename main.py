import asyncio
import os
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

    greeting = ['hello', 'hi', 'hey', 'greetings', 'salutatations'] # list of potential trigger words
    for x in greeting: # iterates through list
        if message.content.startswith(x) and len(x) <= 3: # checks for trigger in message
            async with message.channel.typing():
                await delay() 
                await channel.send('SHUT UP')
        elif message.content.startswith(x) and len(x) > 3:
            reactions = ['\U0001F595', '\U0001F611', '\U0001F922', '\U0001F5FF', '\U0001F921']
            await message.add_reaction(random.choice(reactions))

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
                   await channel.send('<:neutral_face:1114392982486012055>')
                   await delay()
                   async with message.channel.typing():
                       await channel.send('i think you need a life bruh')

    firstPerson = ['thats cool but i dont care ', 'nobody is listening to you',
                   'bro you jus love to talk huh <:skull:1113634475218325635>']
    firstPersonResponse = random.choice(firstPerson)
    if message.content.startswith('i '):
        await delay()
        async with message.channel.typing():
            await channel.send(firstPersonResponse)

    secondPerson = ['i aint even a real person bruh <:skull_crossbones:1113667775152529490>',
                    'i dont wanna hear that from you']
    secondPersonResponse = random.choice(secondPerson)
    if message.content.startswith('you') or message.content.startswith('u'):
        await delay()
        async with message.channel.typing():
            await channel.send(secondPersonResponse)

    badJokes = ['The man who invented the funnel passed away recently... tributes have been pouring in',
                'I fired my personal trainer for making me do too many sit ups... I couldn\'t handle the ab use',
                'My wife told me she was sick of me overusing contractions... I told her \"it\'s what it\'s\"',
                'I like making puns about eyes... the cornea the better',
                'Why are plain pizzas the best kind of pizza? Because nothing tops them',
                'To the person who stole all the bulbs in my house... I am absolutely delighted',
                'I miss when Mt. Rushmore before it got carved... It\'s beauty was unprecedented',
                'Did you hear about the chef with terminal illness? It seems he doesn\'t have much thyme...',
                'A friend told me my thinking was too one-dimensional... I couldn\'t imagine y',
                'When I was young, I was poor. Now after years of struggle... I\'m no longer young',
                'As an immigration officer, I might not agree with you... but I can see where you\'re coming from']
    if message.content.startswith('tell me a joke'):
        async with message.channel.typing():
            await delay()
            await channel.send(random.choice(badJokes))

@client.event
async def on_ready():
    gameList = ['Google Classroom', 'Gmail', 'JupiterEd', 'Runestone Academy', 'practice.it',
                'codingbat.com', 'My AP Classroom']
    game = discord.Game(random.choice(gameList))
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('AAAAA')


client.run()
