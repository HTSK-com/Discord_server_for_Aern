import asyncio
from discord.ext import commands
import sqlite3
import discord
import universal

conn = sqlite3.connect('aern.db')
cursor = conn.cursor()

TOKEN = ''
bot = commands.Bot(command_prefix='/')

a = ""
discord.ext.commands.context.Context
@bot.command(pass_context=True)
# разрешаем передавать агрументы
async def new_order(ctx, *, text):
    print(ctx)
    message = await ctx.send(
        "1 - Siege of Boralus \n2 - Freehold \n3 - Shrine of the Storm \n4 - Tol Dagor \n5 - Waycrest Manor \n6 - Atal'Dazar \n7-The MOTHERLODE \n8 - Temple of Sethrallis \n9 - The Underrot \n10 - King's Rest \n# - Junkyard \n* - Workshop")
    print(message.channel.id)
    # universal.add("", "WoW")
    for emoji in ('1️⃣', '🏴󠁧󠁢󠁳󠁣󠁴󠁿'):
        await message.add_reaction(emoji)


@bot.event  # выдавливает совытия
async def on_raw_reaction_add(payload):  # конкретное соббытие связанное с нажатием на реакцию
    print("payload.user_id", payload)
    c = bot.get_channel(760454915000369176)
    print(c)
    user_id = payload.user_id
    emoji = payload.emoji.name
    if discord.RawReactionActionEvent == type(
            payload) and user_id != 766406021459214377:  # мы проверили что реакцию оставил не бот, а пользователь
        print("Польователь: {user_id} нажал на emoji: {emoji}".format(user_id=user_id,
                                                                      emoji=emoji))  # полученную реакцию надо записать в БД в зависиммости от того какие данные вводятся
        if emoji != ':x:' and emoji != ':white_check_mark:':
            i = universal.find_inf("question", "WoW", user_id)
            if i == 1:
                m = await c.send("1 - Horde\n2 - Alliance\n:x:-Cancel")
                for emoji in (':1:', ':2:', ':x:'):
                    await m.add_reaction(emoji)
            if i == 2:
                m = await c.send(":white_check_mark: - Horde\n2 - Alliance\n:x:-Cancel")
                for emoji in (':1:', ':2:', ':x:'):
                    await m.add_reaction(emoji)
            universal.upd("question", i + 1, table="WoW", user_id=payload.user_id)

        else:
            pass


bot.run(TOKEN)
