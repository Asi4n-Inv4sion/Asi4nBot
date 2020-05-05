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
        f = open('Candidates.txt', 'r')

        for line in f.readlines():
            if line.strip().split(':')[0] == str(ctx.author.id):
                elected = True
            else:
                people.append(line.strip())

        if elected:
            f = open('Candidates.txt', 'w')
            for person in people:
                f.write(person + '\n')

            await ctx.send(f"{ctx.author.mention} is no longer running in the election!")
        else:
            await ctx.send("You are not running in the election.")

        f.close()

        f = open('Voters.txt', 'r')
        voters_to_candidates = {}
        for line in f.readlines():
            l = line.strip().split(':')
            if l[1] != str(ctx.author.id):
                voters_to_candidates[l[0]] = l[1]

        f = open('Voters.txt', 'w')
        for voter in voters_to_candidates:
            f.write(f"{voter}:{voters_to_candidates[voter]}\n")


    @commands.command()
    async def candidates(self, ctx):

        f = open('Candidates.txt', 'r')

        candidates = f.readlines()
        if candidates == []:
            await ctx.send("There are no current candidates.")
        else:
            await ctx.send("Current candidates:")
            for line in candidates:
                await ctx.send(f'<@!{line.strip().split(":")[0]}>')

        f.close()


    @commands.command()
    async def vote(self, ctx, candidate: str):
        print(f"{ctx.author} voted for {candidate}")
        # Fixes mentions sometimes having an exclaimation mark for whatever reason
        cand = ''
        for c in candidate:
            if c.isdigit():
                cand += c

        candidates = open("Candidates.txt", 'r')
        voters = open("Voters.txt", 'r')
        candidates_to_votes = {}
        voters_to_candidates = {}
        for line in voters.readlines():
            l = line.strip().split(':')
            voters_to_candidates[l[0]] = l[1]

        for line in candidates.readlines():
            l = line.strip().split(':')
            candidates_to_votes[l[0]] = int(l[1])

        if cand in candidates_to_votes:
            if str(ctx.author.id) == cand:
                await ctx.send("You can't vote for yourself, dummy")
                return
            elif str(ctx.author.id) in voters_to_candidates:
                if cand == voters_to_candidates[str(ctx.author.id)]:
                    await ctx.send(f"You are already voting for {candidate}")
                else:
                    candidates_to_votes[cand] += 1
                    candidates_to_votes[voters_to_candidates[str(ctx.author.id)]] -= 1
                    await ctx.send(f"You changed your vote to {candidate}")
                    voters_to_candidates[str(ctx.author.id)] = cand
            else:
                candidates_to_votes[cand] += 1
                await ctx.send(f"You voted for {candidate}")
                voters_to_candidates[str(ctx.author.id)] = cand

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


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def results(self, ctx):
        print("Displaying results of the election")
        results = open("Candidates.txt", "r")

        most_votes = 0
        winner = []
        for line in results.readlines():
            cand = line.strip().split(':')
            await ctx.send(f'<@{cand[0]}> has {cand[1]} votes')
            if int(cand[1]) > most_votes:
                winner = [cand[0]]
                most_votes = int(cand[1])
            elif int(cand[1]) == most_votes:
                winner.append(cand[0])

        if len(winner) > 1:
            await ctx.send("It's a tie between:")
            for person in winner:
                await ctx.send(f'<@{person}>')
        else:
            await ctx.send(f'The new president is <@{winner[0]}>!!!')

        results.close()


def setup(client):
    client.add_cog(Election_Commands(client))
