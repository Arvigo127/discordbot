# bot.py

import constants
from discord.ext import commands
import discord
from discord.abc import User


TOKEN = constants.TOKEN
GUILD = constants.GUILD

bot = commands.Bot(command_prefix='/')


@bot.command(name="italiantime", help="summons fredo")
async def on_message(ctx):
  
    allowed_mentions = discord.AllowedMentions(users=True)
    await ctx.send(content = "@oldyeller", allowed_mentions = allowed_mentions)

bot.run(TOKEN)