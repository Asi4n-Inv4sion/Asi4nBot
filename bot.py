# bot.py
import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/nuke'):
        await message.channel.send('<:nuke:535289100761038869> TACTICAL NUKE INCOMING <:nuke:535289100761038869>')

    if message.content.startswith('/tsar bomba'):
        await message.channel.send('The Tsar Bomba was the biggest bomb ever created. \nTested on 30 October 1961 as an experimental verification of calculation principles and multi-stage thermonuclear weapon designs, it also remains the most powerful human-made explosive ever detonated.')
        await message.channel.send("It's frequently dropped by Cameron 'fucking' Neethling")

    if message.content.startswith('/dinner'):
        await message.channel.send('<@&631594442771660801> the table is set.')

    if message.content.startswith('/gay'):
        await message.channel.send('read if gay')

    if message.content.startswith('/zak'):
        await message.channel.send('<@!246036648465399809> say nothing if gay')

    await client.process_commands(message) # THIS MAKES SURE THE COMMANDS EXTENSION WORKS


@client.event
async def on_message_delete(message):
    if (message.author.bot):
        return
    else:
        print(f'Deleted "{message.content}" by {message.author.mention}')
        await message.channel.send(f"{message.author.mention}'s message got deleted: {message.content}")

@client.command()
async def jason(ctx, num = ''):
    if num.isnumeric() == False:
        await ctx.send("Welcome to Jason quotes V1.0, type /jason 1-4 for some famous quotes")
        return
    num = int(num)

    if 1 <= num <= 4:
        if num == 1:
            await ctx.send("The North pole isn't Antarctica?")
        elif num == 2:
            await ctx.send("I'll take a screenshot of my screentearing")
        elif num == 3:
            await ctx.send("What's the capital of France?")
        elif num == 4:
            await ctx.send("Wait we have to download the PTS?")
        else:
            await ctx.send("Welcome to Jason quotes V1.0, type /jason 1-4 for some famous quotes")
    else:
        await ctx.send("Welcome to Jason quotes V1.0, type /jason 1-4 for some famous quotes")


@client.command()
async def echo(ctx, message: str):
    await ctx.send(message)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, num=-1):
    if (type(num) != int or num <= 0):
        await ctx.send('Enter a valid integer (/clear {int>0})')
    else:
        await ctx.channel.purge(limit = num)
        time.sleep(2)
        await ctx.send(f"Deleted {num} messages!")
        time.sleep(2)
        await ctx.channel.purge(limit = 1)


client.run('Njk1Nzc3NDIzNDU4OTU5NDEw.XokeEw.-AhrLA3fF9PW7cY-QGZ4gjLEtz4')
