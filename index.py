import discord
from getpass import getpass
from python_aternos import Client
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#log in
user = input('Username: ')
pswd = getpass('Password: ')
aternos = Client.from_credentials(user, pswd)

srvs = aternos.list_servers()
TheTitansMods = srvs[0]



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        await message.channel.send('Encendiendo El servidor...')
        TheTitansMods.start()
    if message.content.startswith('!stop'):
        TheTitansMods.stop()
        await message.channel.send('Server Detenido')
    if message.content.startswith('restart'):
        TheTitansMods.restart()
        await message.channel.send('Reiniciando el servidor...')
            

  

client.run('MTA2NTcwNDkzOTAwNDg4NzA5MQ.G3AGKb.1es79tKJSznPfPNeXCEHlHTS0VbOtwhL9mNy6Q')
