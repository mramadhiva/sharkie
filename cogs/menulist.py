import discord
from discord.ext import commands

class MenuList(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def menulist(self, ctx):
        embed = discord.Embed(
            title = "Daftar Menu",
            color = 0x39dbff
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url_as(size=512))
        embed.add_field(
            name = "🍔 Makanan",
            value = "```\n"
                    "| No |             Menu           |   Harga   |\n"
                    "|----|----------------------------|-----------|\n"
                    "| 1. | Pisang Goreng              | Rp6.000   |\n"
                    "| 2. | Roti Bakar                 | Rp10.000  |\n"
                    "| 3. | Siomay                     | Rp10.000  |\n"
                    "| 4. | Nachos                     | Rp10.000  |\n"
                    "| 5. | Onion Ring                 | Rp10.000  |\n"
                    "| 6. | Chicken Fingers            | Rp10.000  |\n"
                    "| 7. | Crispy Chicken             | Rp14.000  |\n"
                    "| 8. | Martabak Mie / Omelet Mie  | Rp18.000  |\n"
                    "| 9. | Burger                     | Rp15.000  |\n"
                    "| 10.| Mac n Cheese               | Rp12.000  |\n"
                    "| 11.| Spaghetti                  | Rp20.000  |\n"
                    "| 12.| Nasi Goreng                | Rp13.000  |\n"
                    "| 13.| Mie Goreng                 | Rp13.000  |\n"
                    "```",
            inline = False
        )

        embed.add_field(
            name = "🍷 Minuman",
            value = "```\n"
                    "| No |        Menu        |   Harga   |\n"
                    "|----|--------------------|-----------|\n"
                    "| 1. | Milkshake          | Rp12.000  |\n"
                    "| 2. | Es Teh             | Rp8.000   |\n"
                    "| 3. | Lemon Tea          | Rp9.000   |\n"
                    "| 4. | Avocado Smoothie   | Rp15.000  |\n"
                    "| 5. | Orange Juice       | Rp12.000  |\n"
                    "| 6. | Mango Smoothie     | Rp15.000  |\n"
                    "| 7. | Melon Smoothie     | Rp15.000  |\n"
                    "| 8. | Pineapple Smoothie | Rp15.000  |\n"
                    "| 9. | Apple Juice        | Rp13.000  |\n"
                    "| 10.| Hot Choco          | Rp14.000  |\n"
                    "```",
            inline = False
        )

        embed.add_field(
            name = "☕ Coffee List",
            value = "```\n"
                    "| No |    Menu    |   Harga   |\n"
                    "|----|------------|-----------|\n"
                    "| 1. | Espresso   | Rp15.000  |\n"
                    "| 2. | Macchiato  | Rp18.000  |\n"
                    "| 3. | Latte      | Rp16.000  |\n"
                    "| 4. | Capuccino  | Rp16.000  |\n"
                    "| 5. | Mocha      | Rp16.000  |\n"
                    "| 6. | Affogato   | Rp18.000  |\n"
                    "| 7. | Americano  | Rp20.000  |\n"
                    "```",
            inline = False
        )

        await ctx.send(embed=embed)

def setup(client): client.add_cog(MenuList(client))