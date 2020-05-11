import discord

from redbot.core import commands, checks

class ZNFHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.comand(name="help")
    async def help(self, ctx: commands.Context, *, command: str = None):
        if not command:
            await ctx.send("La commande {prefix}help est en cours de développement.".format(prefix=ctx.prefix))
        else:
            await ctx.send("La commande {prefix}help est en cours de développement.".format(prefix=ctx.prefix))

def setup(bot):
    cog = ZNFHelp(bot)

    global _help
    _help = bot.get_command('help')
    if _help:
        bot.remove_command('help')

    bot.add_cog(cog)
