################################
# Message_Commands.py
################################

import discord
from discord.ext import commands
import time

class Message_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
        print(f'Ping: {self.client.letency * 1000}ms')


    @commands.command()
    async def dinner(self, ctx):
        await ctx.send('<@&631594442771660801> the table is set.')
        print('Dinner has been called')


    @commands.command()
    async def nuke(self, ctx):
        await ctx.send('<:nuke:535289100761038869> TACTICAL NUKE INCOMING <:nuke:535289100761038869>')
        print('A nuke was dropped')


    @commands.command()
    async def tsar_bomba(self, ctx):
        await ctx.send(("The Tsar Bomba was the biggest bomb ever created. \nTested"
                        "on 30 October 1961 as an experimental verification of "
                        "calculation principles and multi-stage thermonuclear weapon "
                        "designs, it also remains the most powerful human-made "
                        "explosive ever detonated.\nIt's frequently dropped by "
                        "Cameron 'fucking' Neethling"))
        print('The tsar bomba was the BIGGEST BOMB')


    @commands.command()
    async def jason(self, ctx, num = ''):
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

        print('The Kwan was called')


    @commands.command()
    async def echo(self, ctx, message: str):
        await ctx.send(message)
        print(f'Echoed {message}')


    @commands.command()
    async def source(self, ctx):
        await ctx.send(f'Asi4nBot was made by Asi4n#4243\nSource: github.com/Asi4n-Inv4sion/Asi4nBot')


    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, num=0):
        await ctx.channel.purge(limit = num)
        time.sleep(2)
        await ctx.send(f"Deleted {num} messages!")
        print(f'Deleted {num} messages from {ctx.channel.name}')
        temp = ctx.channel.last_message_id
        async for message in ctx.channel.history(limit=5):
            if message.id == temp:
                await message.delete(delay = 3)


def setup(client):
    client.add_cog(Message_Commands(client))
