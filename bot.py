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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message) # THIS MAKES SURE THE COMMANDS EXTENSION WORKS


@client.event
async def on_message_delete(message):
    if (message.author.bot):
        return
    else:
        print(f'Deleted "{message.content}" by {message.author.mention}')
        await message.channel.send(f"{message.author.mention}'s message got deleted: {message.content}")


# LOAD COGS

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
