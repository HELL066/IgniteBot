import asyncio
import datetime
import pickle
import random

import disnake
from disnake import ButtonStyle
from disnake.ext import commands

leave = {}
name_queue = {}
love_stats = {}
user_pet = {}
pet_check = {}
buying = {}
uid = {}
food_stats = {}
wash_stats = {}
pet_name = {}
list = []
bar1_full = "<a:bar1_full:913686597088710706>"
bar1_half = "<a:bar1_half:917698621510664203>"
bar1_empty = "<:bar1_empty:917205649694277652>"
bar2_full = "<a:bar2_full:913686585428566056>"
bar2_half = "<a:bar2_half:917698621766516736>"
bar2_empty = "<:bar2_empty:917697677406392361>"
bar3_full = "<a:bar3_full:917698622030761984>"
bar3_half = "<a:bar3_half:917698621179330560>"
bar3_empty = "<:bar3_empty:917697757890895872>"
bar2_high = "<a:bar2_high:925547411676491788>"


async def get_odds(uid: int):
    user_pet = await pickle_get("pet")
    pet = user_pet.get(uid)
    if pet == "Rock":
        return .01 / 100
    elif pet == "Dog":
        return .1 / 100
    elif pet == "Cat":
        return .5 / 100
    elif pet == "Duck":
        return 1 / 100
    elif pet == "Fish":
        return 3 / 100
    elif pet == "Koala":
        return 5 / 100


async def odds(percent):
    perc = float(percent)
    num = float(random.randint(0, 100))
    if num <= perc:
        return True
    else:
        return False


async def check_negative(s):
    try:
        f = float(s)
        if (f < 0):
            return True
        # Otherwise return false
        return False
    except ValueError:
        return False


async def convert(time: int):
    time = int(0 if time is None else time)
    if await check_negative(time) is True:
        time = 0
    else:
        time = time
    if time > 100:
        time = 100 * 15
        new = 100
        time = time
        woah = time * 60
        d = datetime.datetime.now()
        a = datetime.timezone(datetime.timedelta(hours=8))
        time = d.astimezone(a)
        b = time + datetime.timedelta(seconds=woah)
        format = disnake.utils.format_dt(b, style="R")
        if await check_negative(new) is False:
            return f"{new}% full\nEmpty {format}"
        else:
            new = 0
            return f"{new}% full\nWas empty {format}"
    else:
        new = time
        time = time * 15
        woah = time * 60
        d = datetime.datetime.now()
        a = datetime.timezone(datetime.timedelta(hours=8))
        time = d.astimezone(a)
        b = time + datetime.timedelta(seconds=woah)
        format = disnake.utils.format_dt(b, style="R")
        if await check_negative(new) is False:
            return f"{new}% full\nEmpty {format}"
        else:
            new = 0
            return f"{new}% full\nWas empty {format}"


async def emoji(percentage: int):
    percentage = int(0 if percentage is None else percentage)
    if await check_negative(percentage) is True:
        percentage = 0
    else:
        percentage = percentage
    if percentage >= 95:
        return f"{bar1_full}{bar2_full}{bar2_full}{bar3_full}"
    elif 95 > percentage >= 85:
        return f"{bar1_full}{bar2_full}{bar2_full}{bar3_half}"
    elif 85 > percentage >= 75:
        return f"{bar1_full}{bar2_full}{bar2_full}{bar3_empty}"
    elif 75 > percentage >= 65:
        return f"{bar1_full}{bar2_full}{bar2_high}{bar3_empty}"
    elif 65 > percentage >= 55:
        return f"{bar1_full}{bar2_full}{bar2_half}{bar3_empty}"
    elif 55 > percentage >= 45:
        return f"{bar1_full}{bar2_full}{bar2_empty}{bar3_empty}"
    elif 45 > percentage >= 35:
        return f"{bar1_full}{bar2_high}{bar2_empty}{bar3_empty}"
    elif 35 > percentage >= 25:
        return f"{bar1_full}{bar2_half}{bar2_empty}{bar3_empty}"
    elif 25 > percentage >= 15:
        return f"{bar1_half}{bar2_empty}{bar2_empty}{bar3_empty}"
    elif 15 > percentage >= 5:
        return f"{bar1_empty}{bar2_empty}{bar2_empty}{bar3_empty}"
    else:
        return f"{bar1_empty}{bar2_empty}{bar2_empty}{bar3_empty}"


async def create_pickle(filename):
    dbfile = open(f'{filename}.pkl', 'wb')
    a = {}
    pickle.dump(a, dbfile)
    dbfile.close()


async def pickle_dump(var, filename):
    try:
        dbfile = open(f'{filename}.pkl', 'wb')

        # source, destination
        pickle.dump(var, dbfile)
        dbfile.close()
        return
    except Exception:
        await create_pickle(filename)


async def pickle_get(filename):
    try:
        dbfile = open(f'{filename}.pkl', 'rb')
        db = pickle.load(dbfile)
        dbfile.close()
        return db
    except Exception:
        await create_pickle(filename)


from disnake.ext import tasks


@tasks.loop(seconds=900)
async def deduct_food():
    food_stats = await pickle_get("food")
    for key in food_stats:
        some = food_stats[key]
        thing = some - 1
        food_stats[key] = thing
        await pickle_dump(food_stats, "food")


@tasks.loop(seconds=900)
async def deduct_love():
    love_stats = await pickle_get("love")
    for key in love_stats:
        some = love_stats[key]
        thing = some - 1
        love_stats[key] = thing
        await pickle_dump(love_stats, "love")


@tasks.loop(seconds=900)
async def deduct_water():
    wash_stats = await pickle_get("wash")
    for key in wash_stats:
        some = wash_stats[key]
        thing = some - 1
        wash_stats[key] = thing
        await pickle_dump(wash_stats, "wash")


deduct_water.start()
deduct_food.start()
deduct_love.start()


class confirm(disnake.ui.View):
    message: disnake.Message

    def __init__(self, bot):
        super().__init__(timeout=30.0)
        self.bot = bot

    @disnake.ui.button(label="Yes", style=ButtonStyle.green)
    async def first_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        for child in self.children:
            if isinstance(child, disnake.ui.Button):
                child.disabled = True

        name = name_queue.get(interaction.user.id)
        pet_name = await pickle_get("name")
        pet_name[interaction.user.id] = name
        await pickle_dump(pet_name, "name")

        await interaction.response.edit_message(view=self)

        # Prevents on_timeout from being triggered after the buttons are disabled
        self.stop()
        await interaction.send(f"Your pet name now has been set to **{name}**")

    @disnake.ui.button(label="No", style=ButtonStyle.red)
    async def lolt_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        for child in self.children:
            if isinstance(child, disnake.ui.Button):
                child.disabled = True
        self.stop()
        await interaction.response.edit_message(content="Ok. Bye....", view=self)


class pet_buttons(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @disnake.ui.button(label="Feed", style=ButtonStyle.blurple)
    async def first_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        message_id = pet_check.get(interaction.user.id)
        if message_id == interaction.message.id:
            try:
                thing = await odds(await get_odds(interaction.user.id))
                if thing is False:
                    food_stats = await pickle_get("food")
                    something = ["You gave your pet a taco.", "You gave your pet milk tea. Hope he doesn't choke.",
                                 "You went to McDonalds and bought your pet a hotdog."]
                    choice = random.choice(something)
                    price = random.randint(3000, 30000)
                    channel = self.bot.get_channel(906732146692079636)
                    user_food = food_stats.get(interaction.user.id)
                    if user_food >= 100:
                        await interaction.response.send_message("Don't feed your pet too much.", ephemeral=True)
                    else:
                        user_food = int(0 if user_food is None else user_food)
                        if await check_negative(user_food) is True:
                            user_food = 0
                        else:
                            user_food = user_food
                        uchoice = random.randint(20, 40)
                        food_stats[interaction.user.id] = user_food + uchoice
                        await pickle_dump(food_stats, "food")
                        await channel.send(f"MINUSCREDIT {interaction.user.id} -{price}")
                        await interaction.response.send_message(
                            f"{interaction.author.mention} {choice} You paid {price} credits.")
                else:
                    channel = self.bot.get_channel(906732146692079636)
                    await channel.send(f"MINUSCREDIT {interaction.user.id} 5000000")
                    await interaction.response.send_message(
                        f"{interaction.author.mention} Your pet found you 5,000,000 credits!"
                    )
            except FileNotFoundError:
                await create_pickle(filename="food")
        else:
            await interaction.response.send_message(f"This isn't your button.", ephemeral=True)

    @disnake.ui.button(label="Wash", style=ButtonStyle.blurple)
    async def second_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        message_id = pet_check.get(interaction.user.id)
        if message_id == interaction.message.id:
            try:
                thing = await odds(await get_odds(interaction.user.id))
                if thing is False:
                    wash_stats = await pickle_get("wash")
                    price = random.randint(20000, 50000)
                    channel = self.bot.get_channel(906732146692079636)
                    user_wash = wash_stats.get(interaction.user.id)
                    if user_wash >= 100:
                        await interaction.response.send_message("Don't feed your pet too much.", ephemeral=True)
                    else:
                        user_wash = int(0 if user_wash is None else user_wash)
                        if await check_negative(user_wash) is True:
                            user_wash = 0
                        else:
                            user_wash = user_wash
                        uchoice = random.randint(20, 40)
                        wash_stats[interaction.user.id] = user_wash + uchoice
                        await pickle_dump(wash_stats, "wash")
                        await channel.send(f"MINUSCREDIT {interaction.user.id} -{price}")
                        await interaction.response.send_message(
                            f"{interaction.author.mention} You washed your pet costing you {price}.")
                else:
                    channel = self.bot.get_channel(906732146692079636)
                    await channel.send(f"MINUSCREDIT {interaction.user.id} 5000000")
                    await interaction.response.send_message(
                        f"{interaction.author.mention} Your pet found you 5,000,000 credits!"
                    )
            except FileNotFoundError:
                await create_pickle(filename="wash")
        else:
            await interaction.response.send_message(f"This isn't your button.", ephemeral=True)

    @disnake.ui.button(label="Pat", style=ButtonStyle.blurple)
    async def lol(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        message_id = pet_check.get(interaction.user.id)
        if message_id == interaction.message.id:
            try:
                thing = await odds(await get_odds(interaction.user.id))
                if thing is True:
                    channel = self.bot.get_channel(906732146692079636)
                    await channel.send(f"MINUSCREDIT {interaction.user.id} {5000000}")
                    await interaction.response.send_message(
                        f"{interaction.author.mention} Your pet found you 5,000,000 credits!"
                    )
                else:
                    love_stats = await pickle_get("love")
                    user_wash = love_stats.get(interaction.user.id)
                    if user_wash >= 100:
                        await interaction.response.send_message("Your pet is sleeping :sleeping:", ephemeral=True)
                    else:
                        user_wash = int(0 if user_wash is None else user_wash)
                        if await check_negative(user_wash) is True:
                            user_wash = 0
                        else:
                            user_wash = user_wash
                        uchoice = random.randint(20, 40)
                        love_stats[interaction.user.id] = user_wash + uchoice
                        await pickle_dump(love_stats, "love")
                        await interaction.response.send_message(
                            content=f"{interaction.author.mention} You pat your pet. :D")
            except FileNotFoundError:
                await create_pickle(filename="love")
            except TypeError:
                await interaction.send(content="Something went wrong. Please try again.")
        else:
            await interaction.response.send_message("This isn't your button.", ephemeral=True)

    @disnake.ui.button(label="Refresh", style=disnake.ButtonStyle.green)
    async def refresh(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        message_id = pet_check.get(interaction.user.id)
        if message_id == interaction.message.id:
            user_pet = await pickle_get("pet")
            pet = user_pet.get(interaction.author.id)
            pet_name = await pickle_get("name")
            name = pet_name.get(interaction.author.id)
            if name is None:
                embed = disnake.Embed(
                    title=f"{interaction.author.name}'s {pet}",
                    color=disnake.Color.random(),
                    timestamp=datetime.datetime.utcnow()
                )
            else:
                embed = disnake.Embed(
                    title=f"{interaction.author.name}'s {pet} ({name})",
                    color=disnake.Color.random(),
                    timestamp=datetime.datetime.utcnow()
                )
            food_stats = await pickle_get("food")
            wash_stats = await pickle_get("wash")
            love_stats = await pickle_get("love")
            a = food_stats.get(interaction.author.id)
            b = wash_stats.get(interaction.author.id)
            c = love_stats.get(interaction.author.id)
            the = 0
            if a <= 0:
                the = the + 1
            if b <= 0:
                the = the + 1
            if c <= 0:
                the = the + 1
            if the == 3:
                uid = interaction.author.id
                user_pet[uid] = None
                await pickle_dump(user_pet, "pet")
                pet_name[uid] = None
                await pickle_dump(pet_name, "name")
            else:
                hunger = await emoji(a)
                hygiene = await emoji(b)
                love = await emoji(c)
                format = await convert(a)
                embed.add_field(name=f"Hunger", value=f"{hunger}\n{format}", inline=True)
                format = await convert(b)
                embed.add_field(name=f"Hygiene", value=f"{hygiene}\n{format}", inline=True)
                format = await convert(c)
                embed.add_field(name=f"Love", value=f"{love}\n{format}")
                message = await interaction.response.edit_message(embed=embed, view=pet_buttons(self.bot))
        else:
            await interaction.send("This is not your button.", ephemeral=True)

    @disnake.ui.button(label="Name", style=disnake.ButtonStyle.grey)
    async def name(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        message_id = pet_check.get(interaction.user.id)
        if message_id == interaction.message.id:
            await interaction.send("What will the name of the pet be?")
            try:
                msg = await self.bot.wait_for(
                    "message",
                    check=lambda m: m.author == interaction.author and m.channel == interaction.channel,
                    timeout=30,
                )
            except asyncio.TimeoutError:
                await interaction.channel.send(
                    f"{interaction.author.mention} You took too long to reply."
                )
            else:
                name_queue[interaction.user.id] = msg.content
                await interaction.send(
                    f"Are you sure you want to name your pet {msg.content}?",
                    ephemeral=True, view=confirm(self.bot)
                )
        else:
            await interaction.send("This is not your button.", ephemeral=True)


class row_buttons(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @disnake.ui.button(label="Buy", style=ButtonStyle.green)
    async def first_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pet = buying.get(interaction.user.id)
        user_pet[interaction.user.id] = pet
        food_stats = await pickle_get(filename="food")
        food_stats[interaction.user.id] = 100
        wash_stats = await pickle_get(filename="wash")
        wash_stats[interaction.user.id] = 100
        love_stats[interaction.user.id] = 100
        await pickle_dump(user_pet, "pet")
        await pickle_dump(food_stats, "food")
        await pickle_dump(wash_stats, "wash")
        await pickle_dump(love_stats, "love")

        channel = self.bot.get_channel(906732146692079636)

        async def check(pet: str):
            if pet == "Rock":
                return 2000000
            elif pet == "Dog":
                return 5000000
            elif pet == "Cat":
                return 10000000
            elif pet == "Duck":
                return 30000000
            elif pet == "Fish":
                return 50000000
            elif pet == "Koala":
                return 100000000

        await channel.send(f"MINUSCREDIT {interaction.user.id} -{await check(pet)}")
        await interaction.response.edit_message(content=f"You bought a pet **{pet}**.", view=None)

    @disnake.ui.button(label="Cancel", style=ButtonStyle.red)
    async def second_button(
            self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message(content=f"Canceled.", view=None)


class Dropdown(disnake.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        # Set the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Rock", description="costs 2,000,000 credits", emoji="<:rock:913613083262476338>"
            ),
            disnake.SelectOption(
                label="Dog", description="costs 5,000,000 credits", emoji="<:doggy:914673871901294622>"
            ),
            disnake.SelectOption(
                label="Cat", description="costs 10,000,000 credits", emoji="😺"
            ),
            disnake.SelectOption(
                label="Duck", description="costs 30,000,000 credits", emoji="🦆"
            ),
            disnake.SelectOption(
                label="Fish", description="costs 50,000,000 credits", emoji="🐠"
            ),
            disnake.SelectOption(label="Koala", description="costs 100,000,000 credits", emoji="🐨")
        ]

        super().__init__(
            placeholder="Choose your pet....",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        buying[interaction.user.id] = self.values[0]
        value = self.values[0]
        credits = None
        if value.lower() == "rock":
            credits = "2,000,000"
        elif value.lower() == "dog":
            credits = "5,000,000"
        elif value.lower() == "cat":
            credits = "10,0000,000"
        elif value.lower() == "duck":
            credits = "30,000,000"
        elif value.lower() == "fish":
            credits = "50,000,000"
        elif value.lower() == "koala":
            credits = "100,000,000"
        await interaction.response.send_message(
            f"Are you sure you want to buy a pet **{self.values[0]}?** for **{credits}** credits",
            view=row_buttons(self.bot), ephemeral=True)


class DropdownView(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown(self.bot))


class pet(commands.Cog, name="pet"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def petshop(self, ctx):
        embed = disnake.Embed(
            title=f"Pet Shop",
            description=f"Feel free to buy a pet here.\n Note: **While you still have a pet, buying a pet replaces that pet.**",
            timestamp=datetime.datetime.utcnow(),
            color=disnake.Color.random()
        )
        embed.set_thumbnail(
            f"https://cdn.discordapp.com/attachments/757130997178302506/914322279566028800/petshop1.png")
        embed.set_footer(text="Use ignt chances to view your chances of getting money!")
        await ctx.send(embed=embed, view=DropdownView(self.bot))

    @commands.command()
    async def pet(self, ctx):
        user_pet = await pickle_get("pet")
        pet = user_pet.get(ctx.author.id)
        pet_name = await pickle_get("name")
        try:
            name = pet_name.get(ctx.author.id)
        except AttributeError:
            name = None
        if pet is None:
            embed = disnake.Embed(
                title=f"Pet Shop",
                description=f"Feel free to buy a pet here.\n Note: **While you still have a pet, buying a pet "
                            f"replaces that pet.**",
                timestamp=datetime.datetime.utcnow(),
                color=disnake.Color.random()
            )
            embed.set_thumbnail(
                f"https://cdn.discordapp.com/attachments/757130997178302506/914322279566028800/petshop1.png")

            await ctx.send(embed=embed, view=DropdownView(self.bot))
        else:
            if name is None:
                embed = disnake.Embed(
                    title=f"{ctx.author.name}'s {pet}",
                    color=disnake.Color.random(),
                    timestamp=datetime.datetime.utcnow()
                )
            else:
                embed = disnake.Embed(
                    title=f"{ctx.author.name}'s {pet} ({name})",
                    color=disnake.Color.random(),
                    timestamp=datetime.datetime.utcnow()
                )
            food_stats = await pickle_get("food")
            wash_stats = await pickle_get("wash")
            love_stats = await pickle_get("love")
            the = 0
            a = food_stats.get(ctx.author.id)
            b = wash_stats.get(ctx.author.id)
            c = love_stats.get(ctx.author.id)
            if a <= 0:
                the = the + 1
            if b <= 0:
                the = the + 1
            if c <= 0:
                the = the + 1
            if the == 3:
                uid = ctx.author.id
                user_pet[uid] = None
                await pickle_dump(user_pet, "pet")
                pet_name[uid] = None
                await pickle_dump(pet_name, "name")
                await ctx.reply("Your pet left you. Take care of your pet better next time.")
                embed = disnake.Embed(
                    title=f"Pet Shop",
                    description=f"Feel free to buy a pet here.\n Note: **While you still have a pet, buying a pet "
                                f"replaces that pet.**",
                    timestamp=datetime.datetime.utcnow(),
                    color=disnake.Color.random()
                )
                embed.set_thumbnail(
                    f"https://cdn.discordapp.com/attachments/757130997178302506/914322279566028800/petshop1.png")

                await ctx.send(embed=embed, view=DropdownView(self.bot))
            else:
                hunger = await emoji(a)
                hygiene = await emoji(b)
                love = await emoji(c)
                format = await convert(a)
                embed.add_field(name=f"Hunger", value=f"{hunger}\n{format}", inline=True)
                format = await convert(b)
                embed.add_field(name=f"Hygiene", value=f"{hygiene}\n{format}", inline=True)
                format = await convert(c)
                embed.add_field(name=f"Love", value=f"{love}\n{format}")
                message = await ctx.send(embed=embed, view=pet_buttons(self.bot))
                pet_check[ctx.author.id] = message.id

    @commands.command()
    async def chances(self, ctx: commands.Context):
        await ctx.send("```\nRock: 0.01%\nDog: 0.1%\nCat: 0.5%\nDuck: 1%\nFish: 3%\nKoala: 5%```")


def setup(bot):
    bot.add_cog(pet(bot))
