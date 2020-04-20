################################
# Math_Commands.py
################################

import discord
from discord.ext import commands
import wolframalpha
import os

# Load WolframAlpha AppID
f = open(os.path.join('D:/Documents/Programming/WolframAppID.txt'))  # BotToken.txt contains the private token
ID = f.readline().strip()
f.close()

wolfram_client = wolframalpha.Client(ID)


class Math_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def query(self, ctx, *, q):
        global wolfram_client
        res = wolfram_client.query(q)
        print(f"Queried {q}")
        await ctx.send(next(res.results).text)


def setup(client):
    client.add_cog(Math_Commands(client))
