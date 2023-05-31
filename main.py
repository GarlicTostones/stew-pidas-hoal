import discord

intents = discord.Intents.default()
intents.message_content = True # make sure to go to developer portal and turn on the respective intents
client = discord.Client(intents=intents)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    channel = message.channel

    if 'a' in message.content:
        await channel.send('no')


@client.event
async def on_ready():
    print('AAAAA')


client.run(#the token)
