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
    async def jason(self, ctx, num=''):
        if num.isnumeric() is False:
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
        embed = discord.Embed(
            title='Asi4n Discord Bot',
            description='Discord bot for general use',
            colour=discord.Colour.gold(),
            url='https://github.com/Leo-Wang-Toronto/Asi4nBot'
        )

        embed.set_image(url='https://cdn.discordapp.com/attachments/452559141458935808/766789463337730118/face.png')
        embed.add_field(name='Made by Asi4n#4243', value='github.com/Leo-Wang-Toronto')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, num=0):
        await ctx.channel.purge(limit=num)
        time.sleep(2)
        await ctx.send(f"Deleted {num} messages!")
        print(f'Deleted {num} messages from {ctx.channel.name}')
        temp = ctx.channel.last_message_id
        async for message in ctx.channel.history(limit=5):
            if message.id == temp:
                await message.delete(delay=3)


def setup(client):
    client.add_cog(Message_Commands(client))
