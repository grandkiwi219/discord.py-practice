import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>>')

bot.run('my-bot-token')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send('hello!')

@bot.command()
async def owo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
