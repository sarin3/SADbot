from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should...")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    lang = ['C', 'Python', 'Java', 'Binary (LUL IMAGINE)']

    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)} in {random.choice(lang)}! :slight_smile:'
    await ctx.send(idea)

@bot.command(name="calc")
async def calc(ctx, x, fn, y):
    x = float(x)
    y = float(y)
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '**':
        await ctx.send(pow(x,y))
    else:
        await ctx.send("We only support 5 function operations")

@bot.command(name="idea", help="Get a side project idea")
@bot.command(name="calc", help="Perform a calculation where fn is either +,-,*,**, or /")

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
