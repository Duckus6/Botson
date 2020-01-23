# bot.py
import os
import random as rand
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="roll", help="random number between 1 and user input")
async def roll(ctx, num=6, freq=1):
    rolls = [
        str(rand.choice(range(1,num+1)))
        for _ in range(freq)
    ]
    await ctx.send (", ".join(rolls))


@bot.command(name="odds", help="Odds on")
async def odds(ctx, name, *args):
    print (name)
    for member in ctx.guild.members:
        members = member.name.lower()
        id = member.id
        if (members == name.lower()) or (name[3:-1]==member.id):
            print("test")


    #first arg = person, 2nd onwards = string


@bot.command(name="user", help="Check if a user is present")
async def user(ctx, name):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    members = [member.name.lower() for member in guild.members]
    print(members)


@bot.command(name="shutdown", help="Off switch")
async def shutdown(ctx):
    if ctx.message.author.server_permissions.administrator:
        await ctx.bot.logout()
    else:
        await ctx.send("User does not have permission")

bot.run(TOKEN)