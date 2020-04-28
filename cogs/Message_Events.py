################################
# Message_Events.py
################################

import discord
from discord.ext import commands


class Message_Events(commands.Cog):

    def __init__ (self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot or 'clear' in message.content:
            return
        else:
            print(f'Deleted "{message.content}" by {message.author.mention}')
            await message.channel.send(f"{message.author.mention}'s message got deleted: {message.content}")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == client.user:
            return

        if not message.content.startswith('/'):
            words = open('Forbidden_Words.txt', 'r')

            word_list = []
            for line in words.readlines():
                l = line.strip()
                word_list.append(l)

            illegal = False
            for w in word_list:
                if w in message.content.lower():
                    illegal = True

            counter = open("Word_Counter.txt", 'r')
            # run if a forbidden word is found in the message
            if illegal:
                first = counter.readline().strip() # first line gives how many members are in the file
                total_counter = {}
                if first != '': # check if the file is none empty
                    # make a dict of members to a dict of forbidden words to the number which the member sent it
                    for i in range(int(first)):
                        id_counter = {}
                        id = counter.readline().strip().split(':') # the id line is defined (id:number of forbidden words typed at least once)
                        for j in range(int(id[1])):
                            word = counter.readline().strip().split(':') # the word line is defined (word:times typed by the id)
                            id_counter[word[0]] = word[1]
                        total_counter[id[0]] = id_counter

                # update the total counter with the sent message
                if str(message.author.id) in total_counter:
                    for w in word_list:
                        if w in message.content.lower():
                            if w in total_counter[str(message.author.id)]:
                                total_counter[str(message.author.id)][w] = int(total_counter[str(message.author.id)][w])
                                total_counter[str(message.author.id)][w] += 1
                                total_counter[str(message.author.id)][w] = str(total_counter[str(message.author.id)][w])
                            else:
                                total_counter[str(message.author.id)][w] = '1'
                else:
                    new_counter = {}
                    for w in word_list:
                        if w in message.content.lower():
                            new_counter[w] = 1
                    total_counter[str(message.author.id)] = new_counter

                # write updated into back into the txt file
                counter = open("Word_Counter.txt", 'w')
                counter.write(f"{len(total_counter)}\n")
                for member in total_counter:
                    counter.write(f"{member}:{len(total_counter[member])}\n")
                    for w in total_counter[member]:
                        counter.write(f"{w}:{total_counter[member][w]}\n")

                counter.close()

            words.close()

            await self.client.process_commands(message) # THIS MAKES COMMANDS WORK


def setup(client):
    client.add_cog(Message_Events(client))
