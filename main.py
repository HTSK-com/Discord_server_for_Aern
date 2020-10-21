import discord
from discord.ext import commands
import sqlite3
from discord import utils


conn = sqlite3.connect('aern.db')

TOKEN = 'NzY2NDA2MDIxNDU5MjE0Mzc3.X4i5Og.FT8ySMXk9Gp7eXnOXbMclvnm-A0'
bot = commands.Bot(command_prefix='/')


@bot.command(pass_context=True)
# разрешаем передавать агрументы


async def poll(ctx, *, text):
    message = await ctx.send(text)
    for emoji in ('🤡', '💩'):
        await message.add_reaction(emoji)



if __name__ == '__main__':
    bot.run(TOKEN)