################################
# Election_Commands.py
################################

import discord
from discord.ext import commands

class Election_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def electme(self, ctx):

        print(f'{ctx.author.mention} used electme')
        f = open('Candidates.txt', 'r')

        for line in f.readlines():
            if line.strip() == str(ctx.author.id):
                await ctx.send("You are already running in the election!")
                return
        f.close()

        f = open('Candidates.txt', 'a')
        f.write(f'{ctx.author.id}\n')
        await ctx.send(f"{ctx.author.mention} is now running in the election!")
        f.close()


    @commands.command()
    async def unelectme(self, ctx):

        print(f'{ctx.author.mention} used unelectme')
        elected = False
        people = []
        f = open('Candidates.txt', 'r+')

        for line in f.readlines():
            if line.strip() == str(ctx.author.id):
                elected = True
            else:
                people.append(line.strip())

        print(people)

        if elected:
            f.truncate(0)

            for person in people:
                f.write(person + '\n')

            await ctx.send(f"{ctx.author.mention} is no longer running in the election!")

        else:
            await ctx.send("You are not running in the election.")

        f.close()







def setup(client):
    client.add_cog(Election_Commands(client))
