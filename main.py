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
        
@bot.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')        



if __name__ == '__main__':
    bot.run(TOKEN)
