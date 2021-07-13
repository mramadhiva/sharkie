import discord
import random
from discord.ext import commands

class Ask(commands.Cog):
    def __init__(self, client): self.client = client

    @commands.command(aliases=['ask','benarkah'])
    async def _ask(self, ctx, *, question):
        response = ['A',
                    'B',
                    'C']

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

def setup(client): client.add_cog(Ask(client))