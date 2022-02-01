import io
import json
import random
import textwrap
import traceback
from contextlib import redirect_stdout
from datetime import datetime

import aiohttp
import disnake
import randomstuff
import wikipedia
from disnake import ButtonStyle
from disnake.ext import commands  # For disnake
from disnake.ext.commands import Context

import utils.buttons

messagething = {}

async def api_fetch(base_url, *args):
    """Fetch JSON from the URL."""

    async with aiohttp.ClientSession() as session:
        url = base_url

        for e in args:
            url += str(e)

        async with session.get(url) as new_data:
            data = await new_data.read()
            json_data = json.loads(data)

            return json_data

client = randomstuff.Client(api_key="8gFgqMTpz0nD")

lyrics_channel = [891568732810408007, 892205334721101844, 870116673980616785]

class RowButtons(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx
    @disnake.ui.button(label="Next", style=ButtonStyle.blurple)
    async def first_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()

        comic_no = random.randint(1, 1900)
        url = f"http://xkcd.com/{comic_no}/info.0.json"

        data = await api_fetch(url)

        img = data.get("img")
        title = data.get("title")
        id = messagething.get(interaction.user.id)
        response = disnake.Embed(
            title=title,
            color=disnake.Color.random(),
            timestamp=datetime.utcnow())
        response.set_footer(text="Comics from XKCD")
        response.set_image(url=img)
        await interaction.followup.edit_message(id, embed=response, view=self)


    @disnake.ui.button(label="Delete", style=ButtonStyle.red)
    async def second_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        await interaction.delete_original_message()

    async def interaction_check(self, i):
        if i.user != self.ctx.author:
            await i.response.send_message(f'You can\'t do that', ephemeral=True)
            return False
        else:
            return True

class other(commands.Cog, name="other"):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.command()
    async def ping(self, ctx):
        """
        Gets the ping of the bot.
        """
        await ctx.send(f'Server Ignite:\nPing: {round(self.bot.latency * 1000)}ms <a:loading:870870083285712896>')

    enabled_channel = [891569196427804672, 798339782949863425, 798331789294043208, 870116673980616785]

    @commands.command()
    async def weather(self, ctx, *, Weather=None):
        if Weather == None:
            await ctx.send("Please enter a location after ignt **weather**.")
        else:
            msg = await ctx.send(
                embed=disnake.Embed(
                    color=disnake.Color.blurple(),
                    description=f"Loading data <a:loading:870870083285712896>")
            )
            try:
                weather = client.get_weather(Weather)
            except Exception:
                await ctx.send("Please give me a valid location. Thanks.")
            Location = weather.location.name
            New = Weather.replace(" ", "%20")
            embed = disnake.Embed(
                title=f"Weather for {Location}",
                color=disnake.Color.blurple(),
                timestamp=datetime.utcnow()
            )
            embed.set_image(
                url=f"https://api.cool-img-api.ml/weather-card?location={New}&background=https://cdn.discordapp.com/attachments/908245191213850694/909275112371531786/abstract-banner-background-with-red-shapes_1361-3348.png")
            await msg.edit(embed=embed)

    @commands.command(name='calculator', aliases=['cal'])
    async def cal(self, ctx):
        mbed = disnake.Embed(
            title='Calculator',
            description=f'Use the buttons below to calculate. Click on the `Quit` Button to close the caluclator when you are done. And also please don\'t try to break the calculator\n``` 0```',
            color=disnake.Color.random()
        )
        mbed.set_footer(icon_url=ctx.author.display_avatar.url, text=f'Requested by {ctx.author.name}')
        msg = await ctx.send(embed=mbed)
        await msg.edit(view=utils.buttons.Calculator(msg, ctx))

    @commands.command(name="nitro")
    async def n_(self, ctx):
        em = disnake.Embed(
            title=f'You\'ve been gifted a subscription!',
            description=f'You\'ve been gifted Nitro for 1 month!',
            color=disnake.Color.greyple()
        )

        em.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/sVYV81qlzJcVdaE0xE7wdxeNkS2PzfKCpQvB2sqNG7k/https/i.imgur.com/w9aiD6F.png')

        msg = await ctx.send(embed=em)
        await msg.edit(view=utils.buttons.NitroFun(msg))

    @commands.command()
    @commands.is_owner()
    async def peval(self, ctx, *, body: str):
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

    @commands.command(pass_context=True)
    async def wiki(self, ctx: Context, *, args=None):
        if args is None:
            await ctx.reply("Please put your query after **ignt wiki**")
        '''Display result from wikipedia'''
        async with ctx.typing():
            msg = await ctx.send(embed=disnake.Embed(
                description=f"Loading... <a:loading:870870083285712896>"
            ))
            searchResults = wikipedia.search(args)
            if not searchResults:
                embed = disnake.Embed(
                    title=f"**{args}**",
                    description='It appears that there is no instance of this in Wikipedia index...',
                    colour=disnake.Color.red())
                embed.set_footer(text='Powered by Wikipedia...')
            else:
                try:
                    page = wikipedia.page(searchResults[0], auto_suggest=False)
                    pg = 0
                except wikipedia.DisambiguationError as err:
                    page = wikipedia.page(err.options[0], auto_suggest=False)
                    pg = err.options
                wikiTitle = str(page.title.encode('utf-8'))
                wikiSummary = page.summary
                embed = disnake.Embed(title=f'**{wikiTitle[1:]}**', description=str(
                    wikiSummary[0:900]) + '...', color=disnake.Color.blurple(), url=page.url)
                embed.set_footer(text='Powered by Wikipedia...')
                if pg != 0:
                    s = pg[1:10] + ['...']
                    s = ','.join(s)
                    embed.add_field(name='Did you mean?:', value=s)
                embed.set_image(url=page.images[0])

            await msg.edit(embed=embed)

    @commands.command(aliases=['comfort'])
    async def comfortme(self, ctx):
        randomcomf = random.choice(
            ["You've always been able to always figure out how to pick yourself up. You can do it again.",
             "It's so great to see you're doing your best.",
             'You can get through this.',
             "If you're going through something, remember: this too shall pass.",
             "If today was bad, remember that you won't have to repeat this day ever again.",
             "Even if you feel like you're getting nowhere you're still one step ahead of yesterday - and that's still progress.",
             "You're growing so much, and if you can't see it now, you certainly will in a few months.",
             "You're strong for going on even when it's so hard.",
             "If you are having really awful thoughts right now or feeling very insecure, remember that what you think does not always reflect the reality of things.",
             "I know they can be hard to deal with, but even a bot like me knows your emotions are valid and important!",
             "(source: softangelita)\nhttps://78.media.tumblr.com/757d6f9eceacd22e585f5763aed3b6b7/tumblr_pbs2drA9yX1wzarogo1_1280.gif",
             "You are going to be okay. Things are going to be okay. You will see.",
             "(source: princess-of-positivity)\nhttps://78.media.tumblr.com/209ac4a784925d71d3d3c7293b7d75f4/tumblr_o883p7C7e21vwxwino1_1280.jpg",
             "Sit down, take a breath. There’s still time. Your past isn’t going anywhere, the present is right here and the future will wait.",
             "It is never too late to make a positive change in your life.",
             "https://78.media.tumblr.com/14a19b1f5c785c0af5966175c0c87c8f/tumblr_owob0dUAzy1ww31y6o1_500.jpg",
             "Don't be upset if you aren't always doing your absolute best every waking moment. Flowers cannot always bloom.",
             "(source: jessabella-hime)\nhttps://78.media.tumblr.com/b1e54721f7520a6f425c112a67170e63/tumblr_ozi5gdM4de1trvty1o1_500.png",
             "There are good people in this world who do or will help you, care about you, and love you.",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/37778dd51384fbdba835349e6f0081d5/tumblr_oz8v11c9CC1wssyrbo1_500.jpg",
             "https://78.media.tumblr.com/ed8e14743dac29bbc606fc099ab77ec3/tumblr_nphyqvqGvi1qzz08do1_500.jpg",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/980109437f848b501d9ac96ed5a9ead0/tumblr_p285yaPKk31wssyrbo2_r2_250.jpg",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/63a7933dfe6ed98dd00682533d249efe/tumblr_pc558poobr1wssyrbo1_250.jpg",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/5827e477fff5b22c693c00d94eb19b2a/tumblr_p40de4xrrC1wssyrbo1_250.jpg",
             "It is perfectly okay to rest and take a break from things If you are taking yourself to exhaustion, at that point it isn't your best anymore.",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/50f06d2360aae36c815b1757326d878d/tumblr_p40de4xrrC1wssyrbo5_r1_250.jpg",
             "Sometimes it's okay if the only thing you did today was breathe.",
             "(source: recovering-and-healing)\nhttps://78.media.tumblr.com/e7b47e53ba372425728f384685748435/tumblr_oc93tmtPBj1ue8qxbo3_r1_250.jpg",
             "(source: positivedoodles)\nhttps://78.media.tumblr.com/c04f396bfd2501b4876c239a329c035b/tumblr_pcutj6i57Z1rpu8e5o1_1280.png",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/6602114029258f4097fffc33a2ae5887/tumblr_otfj86Xgq91wssyrbo1_r4_250.jpg"])

        await ctx.send(randomcomf)

    @commands.command(description="Send a random XKCD comic.")
    async def comics(self, ctx):
        comic_no = random.randint(1, 1900)
        url = f"http://xkcd.com/{comic_no}/info.0.json"

        data = await api_fetch(url)

        img = data.get("img")
        title = data.get("title")
        alt = data.get("alt")

        response = disnake.Embed(
            title=title,
            color=disnake.Color.random(),
            timestamp=datetime.utcnow())
        response.set_footer(text="Comics from XKCD")
        response.set_image(url=img)
        msg = await ctx.send(embed=response, view=RowButtons(ctx))
        messagething[ctx.author.id] = msg.id

def setup(bot):
    bot.add_cog(other(bot))
