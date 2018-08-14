# util.py - various utility commands

# discord imports
import discord
from discord.ext import commands

class Util:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, arg):
        for member in ctx.message.mentions:
            embed = discord.Embed(title=f"Avatar for user {member.name}#{member.discriminator}")
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def emoji(self, ctx, *, arg):
        converter = commands.EmojiConverter()
        emoji = await converter.convert(ctx, arg)
        embed = discord.Embed(title=f"Emoji {emoji.name}")
        embed.set_image(url=emoji.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Util(bot))