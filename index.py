import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

async def hello(ctx):
    await ctx.send('hello!')


bot.run('my-bot-token')
