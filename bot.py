"""
    Bot docstring for pylint's sake.
"""

from discord.ext import commands
from discord.utils import get
import discord

bot = commands.Bot(command_prefix='!')

curses = ['yeo']

# @bot.command(name="idea", help="Get an idea for a Side Project!")
# async def idea(ctx):
#     await ctx.send("Ideas are hard")
#     await ctx.send("Worry not, I think you should...")

#     topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
#     areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
#     lang = ['C', 'Python', 'Java', 'Binary (LUL IMAGINE)']

#     idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)} in {random.choice(lang)}! :slight_smile:'
#     await ctx.send(idea)

# @bot.command(name="calc", help="Perform a calculation where fn is either +,-,*,**, or /")
# async def calc(ctx, x, fn, y):
#     x = float(x)
#     y = float(y)
#     if fn == '+':
#         await ctx.send(x + y)
#     elif fn == '-':
#         await ctx.send(x - y)
#     elif fn == '*':
#         await ctx.send(x * y)
#     elif fn == '/':
#         await ctx.send(x / y)
#     elif fn == '**':
#         await ctx.send(pow(x,y))
#     else:
#         await ctx.send("We only support 5 function operations")

# @bot.command(name="dog", help="Return information about certain breeds of dogs")
# async def dog(ctx, fn = None):
#     if fn == None:
#         await ctx.send("No input. Try again with an input")

#     breeds = {
#         "kohaku": "The Creator's dog; the best doggo in existence. 9999/10",
#         "labrador": "Medium doggo, very fun and cute. 9/10",
#         "daschund": "Small, long doggo, sausage doggo is good doggo. 8/10",
#         "chihuahua": "Tiny animal, loud and annoying. 0/10",
#     }

#     fnS = fn.lower()

#     if breeds.get(fnS) == None:
#         await ctx.send("This doggo does not exist or is not yet supported. Recheck spelling or try other doggo")
#     else:
#         await ctx.send(breeds.get(fnS))

@bot.command(name="curse")
async def curse(ctx, com = None, cword = None):
    """
        Functions relating to curse words

        Add, remove or display curseword(s)
    """
    if com.lower() == "add":
        curses.append(cword.lower())
        await ctx.send(cword + " added to curse list")
    elif com.lower() == "delete":
        curses.remove(cword)
    elif com.lower() == "display":
        # await ctx.send("There are " + curses.count() + "curses")
        for word in curses:
            await ctx.send(word)
    elif com is None and cword is None:
        await ctx.send("Invalid curse command")

@bot.command()
@commands.has_role("Admin")
async def giverole(ctx, member : discord.Member, role : discord.Role):
    """
         Give specified role to specified member if Admin
    """
    await member.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, {member.name} has been giving a role called: {role.name}")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def addrole(ctx, role: str):
    """
        Create specified role if Admin
    """
    guild = ctx.guild
    await guild.create_role(name=role)
    await ctx.send(f"hey @{ctx.author.name}, {role} has been created")

@bot.command()
@commands.has_permissions(ban_members = True)
@commands.has_role("Admin")
async def ban(ctx, member :  discord.Member, *,reason=None):
    """
        Ban specified member if Admin
    """
    if member is None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason is None:
        reason = "For being a jerk! (Reason not provided)"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await member.ban(reason=reason)
    await ctx.send(f"{member} is banned!")

@bot.command()
@commands.has_permissions(ban_members = True)
@commands.has_role("Admin")
async def kick(ctx, member :  discord.Member = None, *,reason=None):
    """
        Kick specified member if Admin
    """
    if member is None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick yourself")
        return
    if reason is None:
        reason = "For being a jerk! (Reason not provided)"
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await member.kick(reason=reason)
    await ctx.send(f"{member} is kicked!")

@bot.command()
@commands.has_permissions(ban_members = True)
@commands.has_role("Admin")
async def warn(ctx, member :  discord.Member, *,reason=None):
    """
        Warn specified member if Admin
    """
    if member is None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason is None:
        reason = "For being a jerk! (Reason not provided)"
    message = f"You have been warned for {reason} for {ctx.guild.name}"
    await member.send(message)
    await ctx.send(f"{member} has been warned")


@bot.listen()
async def on_message(message):
    """
        Run checks on any sent message
    """
    if message.author.id == bot.user.id:
        return
    if message.content.startswith("!"):
        return
    msg_content = message.content.lower()

    curse_word = curses

    # delete curse word if match with the list
    if any(word in msg_content for word in curse_word):
        await message.delete()

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
