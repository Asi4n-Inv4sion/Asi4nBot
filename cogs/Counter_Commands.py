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
            await ctx.send(f"{message.lower()} is already forbidden!")
        else:
            words.write(f"{message.lower()}\n")
            await ctx.send(f'"{message.lower()}" has been forbidden!')


    @commands.command()
    async def unforbid(self, ctx, message: str): # REMEMBER TO REMOVE THE WORD FROM THE Word_Counters.txt
        words = open('Forbidden_Words.txt', 'r')

        word_list = []
        for line in words.readlines():
            l = line.strip()
            word_list.append(l)

        if message.lower() in word_list:
            word_list.remove(message.lower())
            await ctx.send(f"{message.lower()} has been unforbidden!")

            # reused code from message_events cog
            counter = open("Word_Counter.txt", 'r')
            first = counter.readline().strip()
            total_counter = {}
            if first != '':
                for i in range(int(first)):
                    id_counter = {}
                    id = counter.readline().strip().split(':')
                    for j in range(int(id[1])):
                        word = counter.readline().strip().split(':')
                        if word[0] != message.lower(): # this removes the unforbidden word
                            id_counter[word[0]] = word[1]
                    if (len(id_counter) > 0): # removes members who have no words stored
                        total_counter[id[0]] = id_counter

            counter = open("Word_Counter.txt", 'w')
            counter.write(f"{len(total_counter)}\n")
            for member in total_counter:
                counter.write(f"{member}:{len(total_counter[member])}\n")
                for w in total_counter[member]:
                    counter.write(f"{w}:{total_counter[member][w]}\n")

            counter.close()

        else:
            await ctx.send(f"{message.lower()} is not currently forbidden.")

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
                    await ctx.send(f"{member} has said the following:")
                    l = line.strip().split(':')
                    index = lines.index(line)
                    for i in range(1, int(l[1])+1):
                        await ctx.send(f'"{lines[index+i].strip().split(":")[0]}" - {lines[index+i].strip().split(":")[1]} times')
                        lines.close()
                        return

        guild_members = [member.mention for member in ctx.guild.members]
        if member not in guild_members:
            await ctx.send(f'"{member}" does not exist')
        else:
            await ctx.send(f"{member} hasn't said any forbidden words")

        lines.close()


def setup(client):
    client.add_cog(Counter_Commands(client))
