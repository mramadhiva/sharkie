import discord
from discord.ext import commands

class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):
        embed = discord.Embed(
            title = "Pesan Dihapus",
            description = f"Pesan yang dikirim oleh {message.author.mention} pada channel {message.channel.mention} dihapus.",
            color = 0xff0000
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)

        embed.add_field(name="Isi Pesan", value=message.content)

        embed.set_footer(text=f"ID Pesan: {message.id} | ID Pengirim: {message.author.id}")

        await self.client.get_channel(858708843646550056).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before:discord.Message, after:discord.Message):
        embed = discord.Embed(
            title = "Pesan Diedit",
            description = f"Pesan diedit pada channel {before.channel.mention}",
            color = before.author.color
        )
        embed.set_author(name=before.author, icon_url=before.author.avatar_url)

        embed.add_field(name="Sebelum", value=before.content)
        embed.add_field(name="Setelah", value=after.content)

        embed.set_footer(text=f"ID Pesan: {after.id} | ID Pengirim: {before.author.id}")

        await self.client.get_channel(858708843646550056).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel:discord.abc.GuildChannel):
        embed = discord.Embed(
            title = "Channel Dibuat",
            description = f"Channel {channel.mention} (`{channel.name}`) dibuat.",
            color = channel.guild.me.color
        )
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
        embed.set_footer(text=f"ID Server: {channel.guild.id}")
        
        await self.client.get_channel(858708843646550056).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel:discord.abc.GuildChannel):
        embed = discord.Embed(
            title = "Channel Dihapus",
            description = f"Channel **#{channel.name}** dihapus.",
            color = 0xff0000
        )
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
        embed.set_footer(text=f"ID Server: {channel.guild.id}")
        
        await self.client.get_channel(858708843646550056).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before:discord.abc.GuildChannel, after:discord.abc.GuildChannel):
        if before.name != after.name:
            embed = discord.Embed(
                title = "Channel Berganti Nama",
                description = f"Channel **#{before.name}** berubah nama menjadi **#{after.name}**",
                color = after.guild.me.color
            )
            embed.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
            embed.set_footer(text=f"ID Server: {after.guild.id}")
            
            await self.client.get_channel(858708843646550056).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role:discord.Role):
        embed = discord.Embed(
            title = "Role Dibuat",
            description = f"Ada Role yang baru saja dibuat, yaitu {role.mention} (`{role.name}`).",
            color = role.color
        )
        embed.set_author(name=role.guild.name, icon_url=role.guild.icon_url)
        embed.set_footer(text=f"ID Role: {role.id} | ID Server: {role.guild.id}")
        
        await self.client.get_channel(858708843646550056).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role:discord.Role):
        embed = discord.Embed(
            title = "Role Dihapus",
            description = f"Ada Role yang baru saja dihapus, yaitu **@{role.name}**.",
            color = 0xff0000
        )
        embed.set_author(name=role.guild.name, icon_url=role.guild.icon_url)
        embed.set_footer(text=f"ID Role: {role.id} | ID Server: {role.guild.id}")
        
        await self.client.get_channel(858708843646550056).send(embed=embed)

def setup(client):
    client.add_cog(Log(client))