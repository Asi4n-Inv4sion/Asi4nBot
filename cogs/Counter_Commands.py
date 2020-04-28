################################
# Counter_Commands.py
################################

import discord
from discord.ext import commands


class Counter_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def forbid(self, ctx, message: str):
        words = open('Forbidden_Words.txt', 'r+')
        word_list = []
        for line in words.readlines():
            l = line.strip()
            word_list.append(l)

        if message in word_list:
            await ctx.send(f"{message} is already forbidden!")
        else:
            words.write(f"{message}\n")
            await ctx.send(f'"{message}" has been forbidden!')


    @commands.command()
    async def unforbid(self, ctx, message: str): # REMEMBER TO REMOVE THE WORD FROM THE Word_Counters.txt
        words = open('Forbidden_Words.txt', 'r')

        word_list = []
        for line in words.readlines():
            l = line.strip()
            word_list.append(l)

        if (message in word_list):
            word_list.remove(message)
            await ctx.send(f"{message} has been unforbidden!")
        else:
            await ctx.send(f"{message} is not currently forbidden.")

        words = open('Forbidden_Words.txt', 'w')
        for word in word_list:
            words.write(f"{word}\n")


    @commands.command(aliases = ['swearjar'])
    async def check(self, ctx, member: str):
        print(f"Checking swear jar of {member}")
        f = open('Word_Counter.txt', 'r')
        lines = f.readlines()
        if member.startswith("<@") and len(member) >= 21:
            for line in lines:
                if member[3:-1] in line or member[2:-1] in line:
                    await ctx.send(f"{member} has said the following")
                    l = line.strip().split(':')
                    index = lines.index(line)
                    for i in range(1, int(l[1])+1):
                        await ctx.send(f'"{lines[index+i].strip().split(":")[0]}" - {lines[index+i].strip().split(":")[1]} times')
                        lines.close()
                        return

        guild_members = [member.mention for member in ctx.guild.members]
        print(member)
        print(guild_members)
        if member not in guild_members:
            await ctx.send(f'"{member}" does not exist')
        else:
            await ctx.send(f"{member} hasn't said any forbidden words")

        lines.close()


def setup(client):
    client.add_cog(Counter_Commands(client))
