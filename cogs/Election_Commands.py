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
            if line.strip().split(':')[0] == str(ctx.author.id):
                await ctx.send("You are already running in the election!")
                return
        f.close()

        f = open('Candidates.txt', 'a')
        f.write(f'{ctx.author.id}:0\n')
        await ctx.send(f"{ctx.author.mention} is now running in the election!")
        f.close()


    @commands.command()
    async def unelectme(self, ctx):

        print(f'{ctx.author.mention} used unelectme')
        elected = False
        people = []
        f = open('Candidates.txt', 'r+')

        for line in f.readlines():
            if line.strip().split(':')[0] == str(ctx.author.id):
                elected = True
            else:
                people.append(line.strip())

        if elected:
            f.truncate(0)

            for person in people:
                f.write(person + '\n')

            await ctx.send(f"{ctx.author.mention} is no longer running in the election!")

        else:
            await ctx.send("You are not running in the election.")

        f.close()


    @commands.command()
    async def candidates(self, ctx):

        f = open('Candidates.txt', 'r')

        candidates = f.readlines()
        if candidates == []:
            await ctx.send("There are no current candidates.")
        else:
            await ctx.send("Current candidates:")
            for line in candidates:
                await ctx.send(f'<@!{line.strip()}>')

        f.close()


    @commands.command()
    async def vote(self, ctx, candidate: str):
        print(f"{ctx.author} voted for {candidate}")
        candidates = open("Candidates.txt", 'r')
        voters = open("Voters.txt", 'r')
        candidates_to_votes = {}
        voters_to_candidates = {}
        for line in voters.readlines():
            l = line.strip().split(':')
            voters_to_candidates[l[0]] = l[1]

        print(voters_to_candidates)

        for line in candidates.readlines():
            l = line.strip().split(':')
            candidates_to_votes[l[0]] = int(l[1])

        if candidate[3:-1] in candidates_to_votes:
            if str(ctx.author.id) == candidate[3:-1]:
                await ctx.send("You can't vote for yourself, dummy")
                return
            elif str(ctx.author.id) in voters_to_candidates:
                if candidate[3:-1] == voters_to_candidates[str(ctx.author.id)]:
                    await ctx.send(f"You are already voting for {candidate}")
                else:
                    candidates_to_votes[candidate[3:-1]] += 1
                    candidates_to_votes[voters_to_candidates[str(ctx.author.id)]] -= 1
                    await ctx.send(f"You changed your vote to {candidate}")
                    voters_to_candidates[str(ctx.author.id)] = candidate[3:-1]
            else:
                candidates_to_votes[candidate[3:-1]] += 1
                await ctx.send(f"You voted for {candidate}")
                voters_to_candidates[str(ctx.author.id)] = candidate[3:-1]


        else:
            await ctx.send("Choose from the folliowing candidates (use /vote {@candidate}):")
            for c in candidates_to_votes:
                await ctx.send(f"<@!{c}>")

        candidates = open("Candidates.txt", 'w')
        voters = open("Voters.txt", 'w')

        for key in candidates_to_votes:
            candidates.write(f"{key}:{candidates_to_votes[key]}\n")

        for key in voters_to_candidates:
            voters.write(f"{key}:{voters_to_candidates[key]}\n")

        candidates.close()
        voters.close()


def setup(client):
    client.add_cog(Election_Commands(client))
