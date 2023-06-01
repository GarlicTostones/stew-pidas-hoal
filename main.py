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
    
    greeting = ['hello', 'hi', 'hey', 'howdy']
    for x in greeting:
        if message.content.startswith(x) and len(x) <= 3:
            async with message.channel.typing():
                await channel.send('SHUT UP')
        elif message.content.startswith(x) and len(x) > 3:
            async with message.channel.typing():
                await channel.send('LEAVE ME ALONE')
     
                                  
    basic_question = ['?', 'what']
        for x in basic_question:
         if message.content.startswith(x) and x == basic_question[0]:
          async with message.channel.typing():
           await channel.send('question marks go at the end, you moron')
         elif x in message.content and len(x) > 1:
           async with message.channel.typing():
            await channel.send('do you ever stop talking')
          
    speculative_question = ['imagine', 'consider', 'think']
    for x in speculative_question:
      if x in message.content:
        if x == speculative_question[0]:
          async with message.channel.typing():
            await channel.send('imagine if you stopped talking')
        elif x == speculative_question[1]:
          async with message.channel.typing():
            await channel.send('have you considered picking up a hobby or two')
        elif x == speculative_question[2]:
          async with message.channel.typing():
            await channel.send('have you thought about being quiet')
     
    firstPerson = ['thats cool but i dont care', 'nobody is listening to you',
                   'bro you jus love to talk huh <:skull:1113634475218325635>']
    firstPersonResponse = random.choice(firstPerson)
    if message.content.startswith('i '):
        await channel.send(firstPersonResponse)

@client.event
async def on_ready():
    print('AAAAA')


client.run(#the token)
