# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    # for server in client.guilds:
    #     if server.name == SERVER:
    #         break
    # server = discord.utils.find(lambda g: g.name == SERVER, client.guilds)
    server = discord.utils.get(client.guilds, name=SERVER)
    print(f'{client.user} has connected to ' f'{server.name}')
    members = '\n - '.join([member.name for member in server.members])
    print(f'Guild Members:\n - {members}')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if 'happy birthday' in message.content.lower():
#         await message.channel.send('Happy Birthday! 🎈🎉')

client.run(TOKEN)