import discord, os, asyncio
import aiohttp
import urllib.parse, urllib.request, re
from discord import user
from discord.ext import commands
from discord.flags import PublicUserFlags

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #command hug
    @commands.command(aliases=['peluk', 'ba polo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, *, member:discord.Member=None):
        member = ctx.author if not member else member
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/animu/hug') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = f'{ctx.message.author.name} memeluk {member.display_name} >w<',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.reply(embed=embed)
                    await ses.close()

    @commands.command()
    async def remind(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            
            return val * time_dict[unit]

        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send("you didn't answer the time correctly.")
            return

        if converted_time == -2:
            await ctx.send("the time must integer")
            return

        await ctx.send(f'Noted! **{task}** akan di ingatkan pada waktu hitung mundur **{time}**.')

        await asyncio.sleep(converted_time)
        await ctx.send(f'{ctx.author.mention},  **{task}** has finished!')


def setup(client): client.add_cog(Fun(client))