################################
# Message Events.py
################################

import discord
from discord.ext import commands


class Message_Events(commands.Cog):

    def __init__ (self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        # await self.client.process_commands(message) # THIS MAKES SURE THE COMMANDS EXTENSION WORKS


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot or 'clear' in message.content:
            return
        else:
            print(f'Deleted "{message.content}" by {message.author.mention}')
            await message.channel.send(f"{message.author.mention}'s message got deleted: {message.content}")


def setup(client):
    client.add_cog(Message_Events(client))
