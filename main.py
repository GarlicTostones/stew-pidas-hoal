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


@client.event
async def on_ready():
    print('AAAAA')


client.run(#the token)
