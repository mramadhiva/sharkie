import discord, os
import urllib.parse, urllib.request, re
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.help import MinimalHelpCommand
from discord.flags import Intents

client = commands.Bot(command_prefix="s!", case_insensitive=True, description="Sharkie UwU")

for namafile in os.listdir("./cogs"):
    if namafile.endswith(".py"):
        client.load_extension(f"cogs.{namafile[:-3]}")
        print(f"{namafile} dimuat.")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('yt.com/c/SharkieGD'))
    print(f"\n{client.user} sudah siap.")

    channel = client.get_channel(858708843646550056)
    await channel.send(f"Bot **{client.user}** telah dinyalakan lagi setelah di- udah woi.. gw jangan dimatiin lagi <:argh:858890967381573653>")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Perintah Tidak ditemukan, ketik s!help untuk melihat semua perintah yang ada <:Worried:863075216972578837>')

@client.command()
async def staff(ctx, user: discord.User,*,reason):
    if ctx.message.channel.id == 863931204348280832:
        await ctx.channel.send("Permintaan anda sedang di-proses, mohon tunggu balasannya")

        await user.send(f'Hi Sharkie, **{ctx.message.author.name}** baru saja mengajukan permintaan untuk menjadi **Staff** di **Sharkie Coffee Shop**')

        embed = discord.Embed(
                    title = "Pengajuan Staff Server di Sharkie Coffee Shop",
                    colour = 0x29FF0F
                )

        embed.add_field(
            name=f'**Nama** : {ctx.message.author.name}',
            value=f'**Alasan** : _{reason}_',
            inline=False
        )
        embed.set_image(url=ctx.author.avatar_url_as(format=None, static_format="png", size=4096))
        embed.set_footer(text=f'Di-Request oleh {ctx.author.name}', icon_url="https://thereisabotforthat-storage.s3.amazonaws.com/1548526271231_security%20bot%20logo.png")
        
        await user.send(embed=embed)
        await ctx.message.add_reaction("✅")
client.run("ODYwMjk4NDA1NTQwMjY1OTk0.YN5NUw.Rx1gMRXU7anYtBRulSCdQi6ZGL8")