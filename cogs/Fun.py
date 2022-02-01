import json

some_channel = [891568495098200084, 798339782949863425, 798331789294043208, 870116673980616785]
from aiohttp import request
from disnake.ext import commands  # For disnake
import requests

dictionary = {
    "Keene": 14
}
import disnake
from disnake import Embed
from datetime import datetime
import disnake as discord


class fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx, animal=None):
        if (animal := animal) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"
            embed = disnake.Embed(
                color=disnake.Color.blurple(),
                description=f"Loading data <a:loading:870870083285712896>")
            message = await ctx.send(embed=embed)
            async with request("GET", image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]

                else:
                    image_link = None

            async with request("GET", fact_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    embed = Embed(title=f"{animal.title()} fact",
                                  description=data["fact"],
                                  colour=ctx.author.colour)
                    if image_link is not None:
                        embed.set_image(url=image_link)
                    await message.edit(content="Loaded successfully!")
                    await message.edit(embed=embed)

                else:
                    await ctx.send(f"API returned a {response.status} status.")
        elif animal == None:
            embed1 = disnake.Embed(
                description=f"Loading data <a:loading:870870083285712896>"
            )
            msg = await ctx.send(embed=embed1)
            r = requests.get("https://api.vslpro.repl.co/api/fact")
            response = r.text
            decode = json.loads(response)
            fact = decode["fact"]
            embed = disnake.Embed(
                title=f"Fact",
                description=f"```{fact}```",
                timestamp=datetime.utcnow()
            )
            await msg.edit(embed=embed)

    weather_channels = [870116673980616785, 892205334721101844, 891569196427804672]

    @commands.command()
    async def quote(self, ctx):
        r = requests.get("https://api.popcat.xyz/quote")
        response = r.text
        decode = json.loads(response)
        upvotes = decode['upvotes']
        something = decode['quote']
        embed = disnake.Embed(
            title="Quote",
            color=disnake.Color.blurple(),
            description=f"```{something}```",
            timestamp=datetime.utcnow()
        )
        embed.set_footer(text=f"👍 {upvotes}")
        await ctx.send(embed=embed)

    @commands.command()
    async def ani(self, ctx):
        link = f"https://meme-api.herokuapp.com/gimme/eyebleach"
        r = requests.get(link)
        response = r.text
        decode = json.loads(response)
        img_url = decode['url']
        something = decode['title']
        upvote = decode['ups']
        author = decode['author']
        embed = discord.Embed(description="", title=something, timestamp=datetime.utcnow())
        embed.set_image(url=img_url)
        embed.set_footer(text=f"👍 {upvote}")
        msg = await ctx.send(embed=embed, view=None)


def setup(bot):
    bot.add_cog(fun(bot))
