import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

### Main Bot Functions ###

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

### Game Commands ###

# Flip a coin
@bot.command(pass_context=True, help='Flips a coin')
async def coinflip(ctx):
    coin = random.randint(1, 2)
    if coin == 1:
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')

# Rock, Paper, Scissors
@bot.command(pass_context=True, help='Play a game of Rock, Paper, Scissors')
async def rps(ctx, choice):
    user_choice = choice.lower()
    bot_choice = random.choice(['rock', 'paper', 'scissors'])
    if user_choice == bot_choice:
        await ctx.send(f'We both chose {user_choice}! It\'s a tie!')
    elif user_choice == 'rock':
        if bot_choice == 'paper':
            await ctx.send(f'I chose {bot_choice}! You lose!')
        else:
            await ctx.send(f'I chose {bot_choice}! You win!')
    elif user_choice == 'paper':
        if bot_choice == 'scissors':
            await ctx.send(f'I chose {bot_choice}! You lose!')
        else:
            await ctx.send(f'I chose {bot_choice}! You win!')
    elif user_choice == 'scissors':
        if bot_choice == 'rock':
            await ctx.send(f'I chose {bot_choice}! You lose!')
        else:
            await ctx.send(f'I chose {bot_choice}! You win!')
    else:
        await ctx.send(f'Invalid input! Please choose rock, paper, or scissors.')

# Error Resolving Function
@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

keep_alive()
bot.run(os.getenv("TOKEN"))

