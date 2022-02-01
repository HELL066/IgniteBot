import datetime
import json

import disnake
import requests
from disnake import ButtonStyle
from disnake.ext import commands  # For disnake

link = None
some_channel = [891568495098200084, 798339782949863425, 798331789294043208, 870116673980616785, 908245198964916244, 891568495098200084]
dict = {

}
other = ""
so = {}


class Dropdown(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Wholesome Memes', description='Wholesome memes from reddit.', emoji='💖'),
            disnake.SelectOption(label='Programmer Memes', description='Programmer memes from reddit.', emoji='🧑‍💻')
        ]
        super().__init__(placeholder='Choose your meme type:', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.defer()
        if so.get(interaction.user.id) == interaction.message.id:
            dropdown = self.values[0]

            if dropdown == "Programmer Memes":
                other = "programmerhumour"
            elif dropdown == "Christian Memes":
                other = "christianmemes"
            elif dropdown == "Terrible Facebook Memes":
                other = "terriblefacebookmemes"
            elif dropdown == "Advice Animal Memes":
                other = "AdviceAnimals"
            else:
                new_string = dropdown.replace(" ", "")
                other = new_string.lower()

            link = f"https://meme-api.herokuapp.com/gimme/{other}"
            dict[interaction.user.id] = link
            r = requests.get(link)
            response = r.text
            decode = json.loads(response)
            img_url = decode['url']
            something = decode['title']


            upvote = decode['ups']
            embed = disnake.Embed(title=something, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=img_url)
            embed.set_footer(text=f"👍 {upvote}")
            await interaction.followup.edit_message(so.get(interaction.user.id), embed=embed, view=RowButtons())
        else:
            await interaction.followup.send("This is not your dropdown menu.", ephemeral=True)

class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown())


class RowButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.

    @disnake.ui.button(label="Next", style=ButtonStyle.blurple)
    async def first_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        if interaction.message.id == so.get(interaction.user.id):
            link = dict.get(interaction.user.id)
            r = requests.get(link)
            response = r.text
            decode = json.loads(response)
            img_url = decode['url']
            something = decode['title']
            upvote = decode['ups']
            embed = disnake.Embed(title=something, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=img_url)
            embed.set_footer(text=f"👍 {upvote}")
            msg_id = so.get(interaction.user.id)
            await interaction.followup.edit_message(msg_id, embed=embed, view=self)
        else:
            await interaction.followup.send("This is not your button. ", ephemeral=True)

    @disnake.ui.button(label="Delete", style=ButtonStyle.red)
    async def second_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        if interaction.message.id == so.get(interaction.user.id):
            await interaction.delete_original_message()
        else:
            await interaction.followup.send("This is not your button. ", ephemeral=True)

class Meme(commands.Cog, name="Meme"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        view = DropdownView()
        if ctx.channel.id in some_channel:
            embed = disnake.Embed(
                color=disnake.Color.blurple(),
                title=f"Pick what kind of meme you want:",
                timestamp=datetime.datetime.utcnow()
            )
            msg = await ctx.send(embed=embed, view=view)
            so[ctx.author.id] = msg.id
        else:
            embed = disnake.Embed(
                color=disnake.Color.blurple(),
                description=f"<a:cancel:863204248657461298> Incorrect text channel.\nGo to <#891568495098200084> and send ```ignt memes```")
            msg = await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meme(bot))
