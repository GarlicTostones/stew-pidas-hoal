import discord

intents = discord.Intents.default()
intents.message_content = True # make sure to go to developer portal and turn on the respective intents
client = discord.Client(intents=intents)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    channel = message.channel

        trigger1 = ['hello', 'hi', 'hey', 'howdy', 'whats up']
    for x in trigger1:
        if x in message.content and len(x) <= 3:
            async with message.channel.typing():
                await channel.send('SHUT UP')
        elif x in message.content and len(x) > 3:
            async with message.channel.typing():
                await channel.send('LEAVE ME ALONE
     
                                  
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

@client.event
async def on_ready():
    print('AAAAA')


client.run(#the token)
