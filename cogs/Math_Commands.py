################################
# Math_Commands.py
################################

import discord
from discord.ext import commands
import wolframalpha

# Load WolframAlpha AppID
f = open('WolframAppID.txt', 'r')
ID = f.readline().strip()
f.close()

wolfram_client = wolframalpha.Client(ID)


class Math_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['query', 'wr', 'q'])
    async def wolfram(self, ctx, *, q):
        # global wolfram_client
        print(f"Queried {q}")
        res = wolfram_client.query(q)
        print(f"Result: {next(res.results).text}")
        await ctx.send(next(res.results).text)


def setup(client):
    client.add_cog(Math_Commands(client))
