import disnake
from disnake.ext import commands


class EmojiInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="emojiinfo", aliases=["ei"])
    async def emoji_info(self, ctx, emoji: disnake.Emoji = None):
        try:
            try:
                emoji = await emoji.guild.fetch_emoji(emoji.id)
            except disnake.NotFound:
                return await ctx.send("I could not find this emoji in the given guild.")
            except disnake.ext.commands.errors.EmojiNotFound:
                return await ctx.send("I could not find this emoji in the given guild.")

            is_managed = "Yes" if emoji.managed else "No"
            is_animated = "Yes" if emoji.animated else "No"
            requires_colons = "Yes" if emoji.require_colons else "No"
            creation_time = disnake.utils.format_dt(emoji.created_at.timestamp(), style="d")
            can_use_emoji = (
                "Everyone"
                if not emoji.roles
                else " ".join(role.name for role in emoji.roles)
            )

            description = f"""
            **General:**
            **- Name:** {emoji.name}
            **- Id:** {emoji.id}
            **- URL:** [Link To Emoji]({emoji.url})
            **- Author:** {emoji.user.mention}
            **- Time Created:** {creation_time}
            **- Usable by:** {can_use_emoji}
    
            **Other:**
            **- Animated:** {is_animated}
            **- Managed:** {is_managed}
            **- Requires Colons:** {requires_colons}
            **- Guild Name:** {emoji.guild.name}
            **- Guild Id:** {emoji.guild.id}
            """

            embed = disnake.Embed(
                title=f"**Emoji Information for:** `{emoji.name}`",
                description=description,
                colour=0xADD8E6,
            )
            embed.set_thumbnail(url=emoji.url)
            await ctx.send(embed=embed)
        except Exception:
            await ctx.send("Emoji not found.")


def setup(bot):
    bot.add_cog(EmojiInfo(bot))
