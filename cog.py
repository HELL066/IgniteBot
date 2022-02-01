import json
import os
import platform
import sys
from datetime import datetime

import disnake
import randomstuff
import requests
from disnake.ext import commands


owners = [755975812909367387, 756308319622397972]

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = disnake.Intents.all()

bot = commands.Bot(
    command_prefix=("ignt ", "Ignt ", "IGNT "),
    owner_ids=owners,
    intents=intents,
    test_guilds=[798325359878864937, 860295266765635584, 843769353040298011, 899477307792695296]
)

client = randomstuff.Client(api_key="8gFgqMTpz0nD")
async_client = randomstuff.AsyncClient(api_key="8gFgqMTpz0nD")


# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"disnake.py API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")


bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself

    await bot.process_commands(message)


# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance (error, disnake.ext.commands.errors.CommandNotFound) is True:
        return
    else:
        raise error


@bot.command()
@commands.is_owner()
async def load(ctx):
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.reload_extension(f"cogs.{extension}")
                embed = disnake.Embed(
                    colour=disnake.Color.blurple(),
                    description=f"```Loaded extension {extension}```"
                )
                await ctx.send(embed=embed)
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                embed = disnake.Embed(
                    colour=disnake.Color.blurple(),
                    description=f"Failed to load extension {extension}`"
                )
                await ctx.send(embed=embed)


@bot.user_command(name="Avatar")  # optional
async def avatar(inter: disnake.ApplicationCommandInteraction, user: disnake.User):
    emb = disnake.Embed(title=f"{user}'s avatar")
    emb.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=emb, ephemeral=True)


Report = {}


@bot.message_command(name="Report")
async def report(inter: disnake.ApplicationCommandInteraction, message: disnake.Message):
    message_channel: disnake.TextChannel = message.channel.id
    msg_id = str(message.id)
    user_name = inter.author.id
    channel = bot.get_channel(911419541442138153)
    await channel.send(f"{message_channel}-{msg_id}-{user_name}")
    await inter.response.send_message("User has been Reported", ephemeral=True)


@bot.command()
@commands.is_owner()
async def endgame(ctx):
    await ctx.send("Shutting Down")
    exit()


something = {}
channel = {
891569931777368064
}




@bot.event
async def on_message(message):
    a = message.content
    msg = a.lower()
    if bot.user == message.author:
        return
    if message.channel.id in channel:
        if "what is ignite" in msg:
            await message.reply(
                "Ignite is Grace Christian Church of the Philippines' High School Ministry. Our goal is for every high school student to have ignited hearts for Christ.")
        if "ignite" == msg:
            await message.reply(
                "Ignite is Grace Christian Church of the Philippines' High School Ministry. Our goal is for every high school student to have ignited hearts for Christ.")
        elif "ignite is what" in msg:
            await message.reply(
                "Ignite is Grace Christian Church of the Philippines' High School Ministry. Our goal is for every high school student to have ignited hearts for Christ.")
        elif "coil" in msg:
            await message.reply(
                "COIL is Ignite Ministry's Official Discord Server. COIL was named after a car's ignition coil that ignites power in a car's engine. In COIL, we desire to provide a safe space for all high school students so that they will be encouraged to continue igniting their spiritual lives for God's glory.")
        elif "ministry" in msg:
            await message.reply(
                "Currently, we have two online ministries: Ignite the Night, happens every Friday at 8:00 PM, is a fun-filled gathering of high school students with interactive activities and messages that caters to the needs of their generation. Ignite Sundays, happens every Sunday at 9:00 AM, is a Sunday school for high school students (Grade 7-10 only) that focuses on in-depth Bible studies and fun activities. Ignite Ministries also hosts events such as Ignite Game Night (IGN) wherein Igniters play classic board and table-top games, game show style! We also host CLUEDO nights and Valentines celebrations! ")
        elif "ignite coin" in msg:
            await message.reply(
                "Ignite Coins is Ignite's official digital currency used to purchase in Ignite's online pop-up store every December and July. Igniters can earn Ignite Coins by attending various Ignite gatherings. Igniters can earn 10 coins everytime they come on time for our weekly gatherings, 3 if they're late, 5 if cameras are open and is seen on screen (yep, not just eyes and forehead!), and 8 for every new Igniter invited! ")
        elif "allowed to join ignite" in msg:
            await message.reply(
                "Definitely, yes! As long as you're a high school student, you are more that welcome to join us!")
        elif "i need someone to talk to" in msg:
            await message.reply(
                "Your Ignite Ahyas and Achis are always here for you! We want to journey life with you, whether it be in the highs or even through the lows. Simply send us a message here in Discord or FB Messenger! We will try our best to be of help to you.")
        elif "grace christian church of the philippines" in msg:
            await message.reply(
                "GCCP is our home! To know more about our church, click on this link: ( https://gccp.org.ph/new-here-2/ )")
        elif "gccp" in msg:
            await message.reply(
                "GCCP is our home! To know more about our church, click on this link: ( https://gccp.org.ph/new-here-2/ )")
        elif "is ignite's fb page and fb group different" in msg:
            await message.reply(
                "Yes! Ignite's FB page is public, while our group is only for Igniters (high school studnets) or their parent's FB account in case they don't have one. This is to ensure the safety of our Igniters! To follow our FB page, click on this link: ( https://www.facebook.com/GCCPHighSchool/ ) To join our FB group, click on this link: ( https://www.facebook.com/groups/322843642426914/?ref=share )")
        elif "what if i am not a chistian can i attend ignite" in msg:
            await message.reply(
                "By all means, yes! You are more than welcome! Our hope is that you'll be able to know Jesus, our Lord and Savior, who paid the penalty of our sins on the cross, to give us eternal life. Simply because He loves us so much!")
        elif "ignite believe in" in msg:
            await message.reply(
                "Ignite, same as GCCP, believes in the same thing! Read about our church's Statement of Faith in this link: ( https://gccp.org.ph/our-statement-of-faith/ )")
        elif "ignite believes in" in msg:
            await message.reply(
                "Ignite, same as GCCP, believes in the same thing! Read about our church's Statement of Faith in this link: ( https://gccp.org.ph/our-statement-of-faith/ )")
        elif "senior highschool" in msg:
            await message.reply(
                "We would love for you to mature in your spiritual life as well! GCCP provides weekly worship guide for senior high school students and up! Here's the link to our weekly worship guide: ( https://gccp.org.ph/all-posts/category/sermons/ )")
        elif "coil study hall" in msg:
            await message.reply(
                "Think of it as our online coffee shop where you and your friends can gather and study together! Check out the Study Hall's rules channel for more information!")
        elif "coil's study hall" in msg:
            await message.reply(
                "Think of it as our online coffee shop where you and your friends can gather and study together! Check out the Study Hall's rules channel for more information!")
        elif "ahyas and achis" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "ahya" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "achi" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "ahyas" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "achis" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "ahia" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "ahias" in msg:
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888576932407545876/0001-7791209199_20210914_014317_0000.png")
            await message.reply(
                "https://cdn.discordapp.com/attachments/757130997178302506/888974696371077150/Cyber.png")
        elif "time" in msg and "ignite" in msg:
            await message.reply(
                "Ignite the Night starts at 8:00 PM, every Friday. Ignite Sundays starts at 9:00 AM, every Sunday!")
        elif "difference" in msg and "ignite" in msg:
            await message.reply(
                "Ignite the Night is for all high school students (Grades 7-12), while Ignite Sundays are for Grades 7-10 only. Ignite the Night's messages are directed towards the six grade levels combined while Ignite Sundays' messages are much more grade-level focused.")
        elif "ignite" in msg and "which" in msg:
            await message.reply("Any! It's up to you! 😄 You can choose to attend one, or better yet, attend both!")
        elif "ignite" in msg and "more" in msg and "fun" in msg:
            await message.reply("Absolutely not! The program for both Ignite ministries are made by the same team!")
        elif "series" in msg and "ignite" in msg and "night":
            await message.reply(
                "To know more about our current series, go ahead and click on the link! https://www.facebook.com/GCCPHighSchool")
        elif "series" in msg and "ignite" in msg and "sunday":
            await message.reply(
                "To know more about our current series, go ahead and click on the link! https://www.facebook.com/GCCPHighSchool")
        elif "student" in msg and "leader" in msg:
            await message.reply(
                "Ignite Student Leaders serves as representatives of various grade levels. The Student Leaders help our Ahyas and Achis plan for Ignite's programs! Meet our Student Leaders!")
            await message.reply(
                "https://media.discordapp.net/attachments/886899842100641823/887158790082936903/0001-7818425920_20210914_100910_0000.png")
        elif "student" in msg and "leaders" in msg:
            await message.reply(
                "Ignite Student Leaders serves as representatives of various grade levels. The Student Leaders help our Ahyas and Achis plan for Ignite's programs! Meet our Student Leaders!")
            await message.reply(
                "https://media.discordapp.net/attachments/886899842100641823/887158790082936903/0001-7818425920_20210914_100910_0000.png")
        elif "when" in msg and "ignite" in msg:
            await message.reply(
                "Ignite the Night starts at 8:00 PM, every Friday. Ignite Sundays starts at 9:00 AM, every Sunday!")
        elif "made" in msg and "you" in msg:
            await message.reply("God made me, just like you.")
        elif "ignite" in msg and "link" in msg:
            await message.reply("Go to https://www.facebook.com/GCCPHighSchool and find the zoom link.")
        elif "join" in msg and "ignite" in msg:
            await message.reply("Go to https://www.facebook.com/GCCPHighSchool and find the zoom link.")
        elif "want" in msg and "join" in msg:
            await message.reply("Go to https://www.facebook.com/GCCPHighSchool and find the zoom link.")
        else:
            text = msg.replace(" ", "%20")
            uid = message.author.id
            link = f"http://api.brainshop.ai/get?bid=160405&key=fiw8cHfBB3GXdDW6&uid={uid}&msg={text}"
            response = requests.get(link)
            response = response.text
            decode = json.loads(response)
            response = decode['cnt']
            await message.reply(response)
    await bot.process_commands(message)


@bot.slash_command(description="Adds wasted to profile picture.")
async def wasted(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Wasted",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Adds glass to profile picture.")
async def glass(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Glass",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/glass?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Adds passed to profile picture.")
async def passed(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Passed",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/passed?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Adds jail walls to profile picture.")
async def jail(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Jail",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/jail?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Posts a youtube comment (fake)")
async def youtube(inter: disnake.ApplicationCommandInteraction, youtube):
    user = inter.author
    userAvatar = user.avatar.url
    userName = user.name

    embed = disnake.Embed(
        title="Hmmmm, Interesting....",
        timestamp=datetime.utcnow()
    )
    New = youtube.replace(" ", "%20")
    Sup = userName.replace(" ", "+")
    embed.set_image(
        url=f"https://some-random-api.ml/canvas/youtube-comment?username={Sup}&comment={New}&avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Posts a tweet (fake)")
async def tweet(inter: disnake.ApplicationCommandInteraction, tweet):
    user = inter.author
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
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Goes to adios portal")
async def adios(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Adios",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://vacefron.nl/api/adios?user={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Adds profile picture to first time meme")
async def first(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="First Time?",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="rip")
async def rip(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="☠",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://api.cool-img-api.ml/rip?image={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="drip")
async def drip(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Nice",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://vacefron.nl/api/drip?user={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Inverts the color scheme")
async def invert(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Something seems wrong",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/invert?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Communist")
async def communist(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="*Ours",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/comrade?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


@bot.slash_command(description="Pixelizes the profile picture")
async def pixel(inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
    if not user:
        user = inter.author
    userAvatar = user.avatar.url
    embed = disnake.Embed(
        title="Pixels",
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"https://some-random-api.ml/canvas/pixelate?avatar={userAvatar}")
    await inter.response.send_message(embed=embed)


from disnake import Spotify


@bot.command()
async def spotify(ctx, user: disnake.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = disnake.Embed(
                    title=f"{user.name}'s Spotify",
                    description="Listening to {}".format(activity.title),
                    color=0xC902FF)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                await ctx.send(embed=embed)





bot.run(config["token"])
