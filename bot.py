################################
# bot.py
################################

import discord
import os
from discord.ext import commands

# INITIALIZATION

client = commands.Bot(command_prefix = '/')
f = open(os.path.join('D:/Documents/Programming/BotToken.txt'))  # BotToken.txt contains the private token
TOKEN = f.readline()
f.close()

# EVENTS

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game('with my code'))


# COMMANDS

@client.command()
@commands.has_permissions(administrator = True)
async def load_cog(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'Loaded cog: {extension}')


@client.command()
@commands.has_permissions(administrator = True)
async def unload_cog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'Unloaded cog: {extension}')


# LOAD COGS

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
