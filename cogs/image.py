from datetime import datetime

import disnake
from disnake.ext import commands  # For disnake


class image(commands.Cog, name="Image"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wasted(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Wasted",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def glass(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Glass",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/glass?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def passed(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Passed",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/passed?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def jail(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Jail",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/jail?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def communist(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="*Ours",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/comrade?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def pixel(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Pixels",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/pixelate?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def youtube(self, ctx, *, tweet=None):
        if tweet == None:
            await ctx.send("Please put a text behind ignt **youtube**")
        else:
            user = ctx.message.author
            userAvatar = user.avatar.url
            userName = user.name

            embed = disnake.Embed(
                title="Hmmmm, Interesting....",
                timestamp=datetime.utcnow()
            )
            New = tweet.replace(" ", "%20")
            Sup = userName.replace(" ", "+")
            embed.set_image(
                url=f"https://some-random-api.ml/canvas/youtube-comment?username={Sup}&comment={New}&avatar={userAvatar}")
            msg = await ctx.send(embed=embed)

    @commands.command()
    async def tweet(self, ctx, *, tweet=None):
        if tweet == None:
            await ctx.send("Please put a text behind ignt **tweet**")
        else:
            user = ctx.message.author
            userAvatar = user.avatar.url
            userName = user.name

            embed = disnake.Embed(
                title="Look who it is",
                timestamp=datetime.utcnow()
            )

            New = tweet.replace(" ", "%20")
            Sup = userName.replace(" ", "+")
            embed.set_image(
                url=f"https://some-random-api.ml/canvas/tweet?username={Sup}&displayname={Sup}&comment={New}&avatar={userAvatar}")
            msg = await ctx.send(embed=embed)

    @commands.command()
    async def adios(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Adios",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://vacefron.nl/api/adios?user={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def first(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="First Time?",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def rip(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="☠",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://api.cool-img-api.ml/rip?image={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def supreme(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Our Supreme Chief:",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://vacefron.nl/api/drip?user={userAvatar}")
        msg = await ctx.send(embed=embed)

    @commands.command()
    async def invert(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.message.author
        userAvatar = user.avatar.url
        embed = disnake.Embed(
            title="Something seems wrong",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/invert?avatar={userAvatar}")
        msg = await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(image(bot))
