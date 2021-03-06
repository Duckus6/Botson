# bot.py
import os
import random as rand
import discord
import sys
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")
bot = commands.Bot(command_prefix='!')

odds = None
users_odds = None


def cleanup():
    odds = None
    users_odds = None


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
    cleanup()
    print(name)
    if (ctx.author.name.lower() == name.lower()) or (name[3:-1] == str(ctx.author.id)):
        await ctx.send("You can't odds on yourself")
        return
    for member in ctx.guild.members:
        members = member.name.lower()
        id = str(member.id)
        #print(str(name[3:-1])==str(id))
        if (members == name.lower()) or (name[3:-1] == id):
            await ctx.send(str(ctx.author.name) + " odds on'd " + members + " " + ' '.join(args))
            await ctx.send(members + " reply with your odds (1-20), decline otherwise")
            msg = await bot.wait_for("message", check=check(member), timeout=300)
            odd = int(msg.content)
            if int(odds < 0) or (odds > 20):
                await ctx.send("those are not valid odds")
                return
            odds = odd
            users_odds = [member,ctx.author.name]
            await ctx.send(member, "Enter your odds between 1 and {}".format(odds))
            await ctx.send(ctx.author.name, "Enter your odds between 1 and {}".format(odds))
    #first arg = person, 2nd onwards = string


@bot.event
async def on_message(message):
    if not(message.channel == discord.DMChannel):
        if odds and (message.author in users_odds):
            try:
                num = int(message.content)
                if (num < 0) or (num > odds):
                    return
            except TypeError:
                return
            if message.author == users_odds[0]:

                print ("yay")
            elif message.author == users_odds[1]:
                print("yay2")

def check(author):
    print ("asdasdasd"+ str(author)+ "asdfasdasd")
    def inner_check(message):
        print(str(message.author)+"tqasdhiu")
        if message.author != author:
            return False
        try:
            int(message.content)
            return True
        except ValueError:
            return False
    return inner_check


@bot.command(name="user", help="Check if a user is present")
async def user(ctx, name):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    members = [member.name.lower() for member in guild.members]
    print(members)


@bot.command(name="shutdown", help="Off switch")
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    await ctx.send("Logging out")
    print(ctx.author)
    await ctx.bot.logout()
bot.run(TOKEN)