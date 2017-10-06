#!/usr/bin/env python3

"""Contains a cog for various weeb reaction commands."""

import random

import discord
from discord.ext import commands

systemrandom = random.SystemRandom()

BASE_URL_API = "https://api.weeb.sh/images/random?type={0}"
BASE_URL_IMAGE = "{0[url]}"

EMOJIS_KILL = (":gun:", ":knife:", ":eggplant:", ":bear:", ":fox:", ":wolf:", ":snake:",
               ":broken_heart:", ":crossed_swords:", ":fire:")


async def _generate_message(ctx, kind: str=None, user: str=discord.Member):
    """Generate a message based on the user."""
    if not kind:
        message = ""
    elif user.id == ctx.bot.user.id:
        message = f"Aw, thank you. Here, have one back. :3"
    elif user.id == ctx.author.id:
        message = systemrandom.choice(("Okay. :3",
                                       f"Sorry to see you're alone, have a {kind} anyway. :<",
                                       f"I'll {kind} your face alright. :3",
                                       ":<"))
    else:
        message = f"**{user.display_name}**, you got a {kind} from **{ctx.author.display_name}!**"
    return message


async def _weeb(ctx, kind: str, message: str=""):
    """A helper function that grabs an image and posts it in response to a user.

    * kind - The type of image to retrieve.
    * user - The member to mention in the command.
    """
    token = ctx.bot.config.get("wolken")
    url = BASE_URL_API.format(kind)
    headers = {"Authorization": "Wolke " + token}
    async with ctx.bot.session.request("GET", url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            c = random.randint(0, 16777215)
            url = BASE_URL_IMAGE.format(data)
            embed = discord.Embed(title=message, color=c)
            embed.set_image(url=url)
            embed.set_footer(text="Powered by weeb.sh")
            await ctx.send(embed=embed)
        else:
            message = "Could not retrieve image. :("
            await ctx.send(message)


async def _send_image(ctx, url_image, message: str=""):
    """A helper function that creates an embed with an image and sends it off."""
    if isinstance(url_image, (tuple, list)):
        url_image = systemrandom.choice(url_image)
    embed = discord.Embed(title=message)
    embed.set_image(url=url_image)
    await ctx.send(embed=embed)


class weeb:
    """Weeb reaction commands."""

    @commands.command(aliases=["cuddles", "snuggle", "snuggles"])
    @commands.cooldown(6, 12)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddle a user!

        * user - The user to be cuddled.
        """
        message = await _generate_message(ctx, "cuddle", user)
        await _weeb(ctx, "cuddle", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def hug(self, ctx, *, user: discord.Member):
        """Hug a user!

        * user - The user to be hugged.
        """
        message = await _generate_message(ctx, "hug", user)
        await _weeb(ctx, "hug", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss a user!

        * user - The user to be kissed.
        """
        message = await _generate_message(ctx, "kiss", user)
        await _weeb(ctx, "kiss", message)

    @commands.command(aliases=["2lewd", "2lewd4me"])
    @commands.cooldown(6, 12)
    async def lewd(self, ctx):
        """Lewd!"""
        await _weeb(ctx, "lewd")

    @commands.command()
    @commands.cooldown(6, 12)
    async def lick(self, ctx, *, user: discord.Member):
        """Lick a user!

        * user - The user to be licked.
        """
        message = await _generate_message(ctx, "lick", user)
        await _weeb(ctx, "lick", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def nom(self, ctx):
        """Nom!"""
        await _weeb(ctx, "nom")

    @commands.command(aliases=['nya', 'meow', 'nyan'])
    @commands.cooldown(6, 12)
    async def _neko(self, ctx):
        """Nyan!"""
        await _weeb(ctx, "neko", f"{ctx.invoked_with.capitalize()}~")

    @commands.command()
    @commands.cooldown(6, 12)
    async def owo(self, ctx):
        """owo"""
        await _weeb(ctx, "owo")

    @commands.command()
    @commands.cooldown(6, 12)
    async def awoo(self, ctx):
        """awoo"""
        await _weeb(ctx, "awoo")

    @commands.command(aliases=["headpat", "pet"])
    @commands.cooldown(6, 12)
    async def pat(self, ctx, *, user: discord.Member):
        """Pat a user!

        * user - The user to be patted.
        """
        message = await _generate_message(ctx, "pat", user)
        await _weeb(ctx, "pat", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def pout(self, ctx):
        """Pout!"""
        await _weeb(ctx, "pout")

    @commands.command()
    @commands.cooldown(6, 12)
    async def slap(self, ctx, *, user: discord.Member):
        """Slap a user!

        * user - The user to be slapped.
        """
        message = await _generate_message(ctx, "slap", user)
        await _weeb(ctx, "slap", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def smug(self, ctx):
        """Smug!"""
        await _weeb(ctx, "smug")

    @commands.command()
    @commands.cooldown(6, 12)
    async def stare(self, ctx, *, user: discord.Member):
        """Stare at a user!

        * user - The user to be stared at.
        """
        message = await _generate_message(ctx, "stare", user)
        await _weeb(ctx, "stare", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickle a user!

        * user - The user to be tickled.
        """
        message = await _generate_message(ctx, "tickle", user)
        await _weeb(ctx, "tickle", message)

    @commands.command()
    @commands.cooldown(6, 12)
    async def triggered(self, ctx):
        """Triggered!"""
        await _weeb(ctx, "triggered")

    @commands.command()
    @commands.cooldown(6, 12)
    async def blush(self, ctx):
        """blush"""
        await _weeb(ctx, "blush")

    @commands.command()
    @commands.cooldown(6, 12)
    async def bang(self, ctx):
        """bang!"""
        await _weeb(ctx, "bang")

    @commands.command()
    @commands.cooldown(6, 12)
    async def jojo(self, ctx):
        """jojo!"""
        await _weeb(ctx, "jojo")

    @commands.command(aliases=["megu", "Megu"])
    @commands.cooldown(6, 12)
    async def megumin(self, ctx):
        """Triggered!"""
        await _weeb(ctx, "megumin")

    @commands.command(aliases=["Rem"])
    @commands.cooldown(6, 12)
    async def rem(self, ctx):
        """rem!"""
        await _weeb(ctx, "rem")

    @commands.command()
    @commands.cooldown(6, 12)
    async def wag(self, ctx):
        """wag"""
        await _weeb(ctx, "wag")

    @commands.command(aliases=["waifuinsult", 'waifuin'])
    @commands.cooldown(6, 12)
    async def waifu_insult(self, ctx):
        """insult waifuuuu!"""
        await _weeb(ctx, "waifu_insult")

    @commands.command()
    @commands.cooldown(6, 12)
    async def wasted(self, ctx):
        """wasted!"""
        await _weeb(ctx, "wasted")

    @commands.command()
    @commands.cooldown(6, 12)
    async def sumfuk(self, ctx):
        """owowow!"""
        await _weeb(ctx, "sumfuk")

    @commands.command()
    @commands.cooldown(6, 12)
    async def dab(self, ctx):
        """dab!"""
        await _weeb(ctx, "dab")

    @commands.command(aliases=["dmemes", "dismemes"])
    @commands.cooldown(6, 12)
    async def discord_memes(self, ctx):
        """memes!"""
        await _weeb(ctx, "discord_memes")

    @commands.command(aliases=["delet"])
    @commands.cooldown(6, 12)
    async def delet_this(self, ctx):
        """jojo!"""
        await _weeb(ctx, "delet_this")

    @commands.command()
    @commands.cooldown(6, 12)
    async def nani(self, ctx):
        """nani?!"""
        await _weeb(ctx, "nani")


def setup(bot):
    """Setup function for reaction images."""
    bot.add_cog(weeb())
