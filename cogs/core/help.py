#!/usr/bin/env python3

import discord
from discord.ext import commands


class Help:
    """Help command."""

    @commands.command(aliases=["commands"])
    @commands.cooldown(1, 2)
    async def help(self, ctx, *args: str):
        """Help command."""
        try:
            await ctx.bot.all_commands["old_help"].callback(ctx, *args)
            if isinstance(ctx.channel, discord.TextChannel):
                await ctx.send("Sent help to your DMs!")
        except discord.Forbidden:
            await ctx.send("Help failed. Make sure you're allowing me to send you DMs. :<")


def setup(bot):
    """Set up the extension."""
    if not "old_help" in bot.all_commands:
        help_command = bot.all_commands["help"]
        help_command.hidden = True
        help_command.name = "old_help"
        bot.remove_command("help")
        bot.add_command(help_command)
    bot.add_cog(Help())
