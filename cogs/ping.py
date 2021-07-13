import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client): self.client = client

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.client.latency*1000)

        if ping < 300:
            await ctx.send(f"🟩 Ping: **{ping}ms**")
        elif ping >= 300 and ping < 400:
            await ctx.send(f"🟨 Ping: **{ping}ms**")
        elif ping >= 400:
            await ctx.send(f"🟥 Ping: **{ping}ms**")

def setup(client): client.add_cog(Ping(client))