# bot.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

# Bot connection to the discord server
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Deletes messages from channel
@bot.command(pass_context=True, help='Deletes x amount of messages from channel where x is inputted')
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

# Error Resolving Function
@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


bot.run(TOKEN)