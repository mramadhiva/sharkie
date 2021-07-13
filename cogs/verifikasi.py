import discord
from discord.ext import commands

class Verifikasi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.channel.id == 863100446343430164:
            if message.content.lower() == "join":
                await message.author.remove_roles(message.guild.get_role(860097471781535765))
                await message.author.add_roles(message.guild.get_role(853975075690119199))
                await message.add_reaction("✅")
            elif message.content.lower() == "verify":
                await message.add_reaction("✅")
                await message.author.add_roles(message.guild.get_role(860097471781535765))

def setup(client):
    client.add_cog(Verifikasi(client))