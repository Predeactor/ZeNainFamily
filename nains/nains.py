import discord

from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Nains(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        nain_channel = self.bot.get_channel(696429569804206120)
        beforenick = before.name if before.nick is None else before.nick
        if after.nick != beforenick:
            if "Nain" in after.nick and "Nain" in beforenick:
                await nain_channel.send(
                    "Tada!! Et d'un coup de baguette magique, {oldnick} devient"
                    " {nick} ! :tada:".format(oldnick=beforenick, nick=after.nick)
                )
            if "Nain" in after.nick and "Nain" not in beforenick:
                await nain_channel.send(
                    "Bienvenue à toi, {nick}, à Erebor ! Nous te souhaitons un bon "
                    "séjour dans nos mines.".format(nick=after.nick)
                )
            elif "Nain" not in after.nick and "Nain" in beforenick:
                await nain_channel.send(
                    "Oh non ! {nick} a quitté Erebor !".format(nick=beforenick)
                )

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        nain_channel = self.bot.get_channel(696429569804206120)
        if "Nain" in member.nick:
            await nain_channel.send(
                "Uhm, je ne détecte plus la présence de {name}, il se peut qu'il ait "
                "quitté les mines d'Erebor...".format(name=member.nick)
            )

    @commands.command()
    async def listenains(self, ctx):
        nains = []
        for member in ctx.guild.members:
            if member.nick is not None and "Nain" in member.nick:
                nains.append(
                    "{nick} ({name}) {bot}".format(
                        nick=member.nick,
                        name=member.name,
                        bot="(BOT)" if member.bot else " ",
                    )
                )

        string = "\n".join(("Membres Nains:\n", *map(str, sorted(nains))))

        for text in pagify(string):
            await ctx.send(text)
