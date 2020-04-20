################################
# Math_Commands.py
################################

import discord
from discord.ext import commands
import wolframalpha
import os
import time

# Load WolframAlpha AppID
f = open(os.path.join('D:/Documents/Programming/WolframAppID.txt'))  # BotToken.txt contains the private token
ID = f.readline().strip()
f.close()

wolfram_client = wolframalpha.Client(ID)


class Math_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['wolfram', 'wr', 'q'])
    async def query(self, ctx, *, q):
        # global wolfram_client
        print(f"Queried {q}")
        res = wolfram_client.query(q)
        await ctx.send(next(res.results).text)


def setup(client):
    client.add_cog(Math_Commands(client))
