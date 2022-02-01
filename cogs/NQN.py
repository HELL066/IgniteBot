import datetime
from typing import List

import disnake
from disnake import utils
from disnake.ext import commands

guilds = []
dict = {}
embeds = []


class Menu(disnake.ui.View):
    def __init__(self, embeds: List[disnake.Embed], ctx: commands.Context):
        super().__init__(timeout=None)

        # Sets the embed list variable.
        self.embeds = embeds
        self.ctx = ctx
        # Current embed number.
        self.embed_count = 0

    @disnake.ui.button(label=None, emoji="<:left:915425233215827968>", style=disnake.ButtonStyle.blurple)
    async def next_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.embed_count == 0:  # If current embed is the first embed then, do not do anything.
            pass
        else:  # If current embed is not the first embed then, sends the preview embed.
            self.embed_count -= 1

            # Gets the embed object.
            embed = self.embeds[self.embed_count]

            # Sets the footer of the embed with current page and then sends it.
            embed.set_footer(text=f"Page {self.embed_count + 1} of {len(self.embeds)}")
            await interaction.response.edit_message(embed=embed)

    @disnake.ui.button(label=None, emoji="<:right:915425310592356382>", style=disnake.ButtonStyle.blurple)
    async def last_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.embed_count == (
                len(self.embeds) - 1
        ):  # If current embed is the last embed then, do not   do anything.
            pass
        else:  # If current embed is not the last embed then, sends the next embed.
            self.embed_count += 1

            # Gets the embed object.
            embed = self.embeds[self.embed_count]

            # Sets the footer of the embed with current page and then sends it.
            embed.set_footer(text=f"Page {self.embed_count + 1} of {len(self.embeds)}")
            await interaction.response.edit_message(embed=embed)

    async def interaction_check(self, i):
        if i.user != self.ctx.author:
            await i.response.send_message(f'You can\'t do that', ephemeral=True)
            return False
        else:
            return True


class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def getemote(self, arg):
        emoji = utils.get(self.bot.emojis, name=arg.strip(":"))

        if emoji is not None:
            if emoji.animated:
                add = "a"
            else:
                add = ""
            return f"<{add}:{emoji.name}:{emoji.id}>"
        else:
            return None

    async def getinstr(self, content):
        ret = []

        spc = content.split(" ")
        cnt = content.split(":")

        if len(cnt) > 1:
            for item in spc:
                if item.count(":") > 1:
                    wr = ""
                    if item.startswith("<") and item.endswith(">"):
                        ret.append(item)
                    else:
                        cnt = 0
                        for i in item:
                            if cnt == 2:
                                aaa = wr.replace(" ", "")
                                ret.append(aaa)
                                wr = ""
                                cnt = 0

                            if i != ":":
                                wr += i
                            else:
                                if wr == "" or cnt == 1:
                                    wr += " : "
                                    cnt += 1
                                else:
                                    aaa = wr.replace(" ", "")
                                    ret.append(aaa)
                                    wr = ":"
                                    cnt = 1

                        aaa = wr.replace(" ", "")
                        ret.append(aaa)
                else:
                    ret.append(item)
        else:
            return content

        return ret

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:  # check is author bot
            return
        if ":" in message.content:
            msg = await self.getinstr(message.content)
            ret = ""
            em = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
                        emoji = await self.getemote(word)
                        if emoji is not None:
                            em = True
                            ret += f" {emoji}"
                        else:
                            ret += f" {word}"
                    else:
                        ret += f" {word}"

            else:
                ret += msg

            if em:
                webhooks = await message.channel.webhooks()
                webhook = utils.get(webhooks, name="Imposter NQN")
                if webhook is None:
                    webhook = await message.channel.create_webhook(name="Imposter NQN")
                await webhook.send(ret, username=message.author.display_name, avatar_url=message.author.avatar.url)
                await message.delete()

    @commands.command(aliases=["emote", "emoji", "emojilist", "emoji_list"])
    async def emotes(self, ctx):
        embeds = [

        ]
        index = 0
        for guild in self.bot.guilds:
            embeds.append(disnake.Embed(
                title=f"{guild.name}'s Emojis",
                colour=disnake.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            ))
            dict[str(guild.name)] = int(index)
            index = index + 1
            for emoji in guild.emojis:
                emojir = await self.getemote(emoji.name)
                embeds[index - 1].add_field(name=f"{emojir}", value=f"`:{emoji.name}:`", inline=True)
        try:
            numb = dict.get("Diamond Team")
            embeds.pop(numb)
            bumb = dict.get("Fear Street 2021")
            embeds.pop(bumb)
            rumb = dict.get("JAMES's server")
            embeds.pop(rumb)

            embeds[0].set_footer(text=f"Page 1 of {len(embeds)}")
            await ctx.send(embed=embeds[0], view=Menu(embeds, ctx))

        except TypeError:
            embeds[0].set_footer(text=f"Page 1 of {len(embeds)}")
            await ctx.send(embed=embeds[0], view=Menu(embeds, ctx))


def setup(bot):
    bot.add_cog(Emoji(bot))
