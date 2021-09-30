myList = [
    'https://media.discordapp.net/attachments/862860280963137576/891526893587791913/184911044_4455473174474787_5674831452980533442_n.jpg?width=436&height=571',
    'https://media.discordapp.net/attachments/862860280963137576/891526891050258472/184621690_1140732606432585_6930265095334697536_n.jpg',
    'https://media.discordapp.net/attachments/862860280963137576/891526889208971375/183282012_4662519483765418_1747658833760399911_n.jpg?width=770&height=571',
    'https://media.discordapp.net/attachments/862860280963137576/891526888428818582/179382885_4632675603416473_7950293887183965846_n.jpg?width=518&height=571']
chat_bot = 891569931777368064
# Libs
import sr_api
from aiohttp import request
from discord import Embed
import aiohttp
from datetime import datetime
import secrets
import discord
from pathlib import Path  # For paths
import logging
import randomstuff
from discord.ext import commands  # For discord
import requests
from prsaw import RandomStuff
import datetime
from better_profanity import profanity

# initiate the object with async mode
client = randomstuff.Client(api_key="8gFgqMTpz0nD")
async_client = randomstuff.AsyncClient(api_key="8gFgqMTpz0nD")
# Get current working directory
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")
client_1 = sr_api.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# Defining a few things
DEFAULTPREFIX = '.'
# secret_file = json.load(open(cwd + '/bot_config/secrets.json'))
bot = commands.Bot(command_prefix=('ignt ', 'Ignt ', 'IGNT'))  # , owner_id=756308319622397972)
# bot.config_token = secret_file['token']
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: ignt\n-----")


@bot.event
async def on_command_error(ctx, error):
    # Ignore these errors
    ignored = (commands.CommandNotFound, commands.UserInputError)
    if isinstance(error, ignored):
        return

    # Begin error handling
    if isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if int(h) is 0 and int(m) is 0:
            await ctx.send(f' You must wait {int(s)} seconds to use this command!')
        elif int(h) is 0 and int(m) is not 0:
            await ctx.send(f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
        else:
            await ctx.send(f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("You lack permission to use this command.")
    raise error


@bot.event
async def on_message(message):
    a = message.content
    msg = a.lower()
    if bot.user == message.author:
        return
    if message.channel.id == 891569931777368064:
        if "ignite" == msg:
            await message.reply(
                "Ignite is Grace Christian Church of the Philippines' High School Ministry. Our goal is for every high school student to have ignited hearts for Christ."
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
        elif "i need someone to talk" in msg:
            await message.reply(
                "Your Ignite Ahyas and Achis are always here for you! We want to journey life with you, whether it be in the highs or even through the lows. Simply send us a message here in Discord or FB Messenger! We will try our best to be of help to you.")
        elif "grace christian church" in msg:
            await message.reply(
                "GCCP is our home! To know more about our church, click on this link: ( https://gccp.org.ph/new-here-2/ )")
        elif "gccp" in msg:
            await message.reply(
                "GCCP is our home! To know more about our church, click on this link: ( https://gccp.org.ph/new-here-2/ )")
        elif "is ignite's fb" in msg:
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
            response = None
            response = await async_client.get_ai_response(message.content)
            messageai = response.message
            await message.reply(messageai)
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    """
    Gets the ping of the bot.
    """
    await ctx.send(f'Server Ignite:\nPing: {round(bot.latency * 1000)}ms <a:loading:870870083285712896>')


@bot.command()
@commands.has_permissions(manage_channels=True)
async def addmeme(ctx, *, meme=None):
    try:
        response = requests.get(meme)
        myList.append(meme)
        print(await ctx.send("Meme has been added <a:user:862895295239028756>"))
        channel = bot.get_channel(891513495982600223)
        await channel.send(f"```\n{myList}\n```")
    except Exception:
        await ctx.send("Please put a link after the addmeme message\nFor example: ignt addmeme https://discord.com")


meme_channel = [891568495098200084, 870116673980616785]


@bot.command()
async def meme(ctx):
    try:
        if ctx.channel.id in meme_channel:
            embed = discord.Embed(
                color=discord.Color.blurple(),
                description=f"",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_image(url=secrets.choice(myList))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=discord.Color.blurple(),
                description=f"<a:cancel:863204248657461298> Incorrect text channel.\nGo to <#891568495098200084> and send ```ignt meme```")
            await ctx.send(embed=embed)
    except Exception:
        await ctx.send("There are no memes yet :/")


fact_channel = [892205334721101844, 870116673980616785]


@bot.command()
async def fact(ctx, animal=None):
    if ctx.channel.id in fact_channel:
        if (animal := animal) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"
            embed = discord.Embed(
                color=discord.Color.blurple(),
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
            animal = ["dog", "cat", "panda", "fox", "bird", "koala"]
            rand_animal = secrets.choice(animal)
            fact_url = f"https://some-random-api.ml/facts/{rand_animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if rand_animal == 'bird' else rand_animal}"
            embed = discord.Embed(
                color=discord.Color.blurple(),
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

                    embed = Embed(title=f"{rand_animal.title()} fact",
                                  description=data["fact"],
                                  colour=ctx.author.colour)
                    if image_link is not None:
                        embed.set_image(url=image_link)
                    await message.edit(embed=embed)
        else:
            await ctx.send("No facts are available for that animal.")
    else:
        embed = discord.Embed(
            color=discord.Color.blurple(),
            description=f"<a:cancel:863204248657461298> Incorrect text channel.\nGo to <#892205334721101844> and send ```ignt facts {animal}```")
        await ctx.send(embed=embed)


import textwrap
import urllib

lyrics_channel = [891568732810408007, 892205334721101844, 870116673980616785]


@bot.command(
    aliases=['l', 'lyrc', 'lyric'])  # adding aliases to the command so they they can be triggered with other names
async def lyrics(ctx, *, search=None):
    channel_id = ctx.channel.id
    if channel_id in lyrics_channel:
        if not search:  # if user hasnt given an argument, throw a error and come out of the command
            embed = discord.Embed(
                title="No search argument!",
                description="You havent entered anything, so i couldn't find lyrics!"
            )
            return await ctx.reply(embed=embed)
            # ctx.reply is available only on discord.py version 1.6.0, if you have a version lower than that use ctx.send

        song = urllib.parse.quote(search)  # url-encode the song provided so it can be passed on to the API

        embed = discord.Embed(
            description="Searching for the lyrics of the song. <a:loading:870870083285712896>",
            color=discord.Color.blurple(),
            timestamp=datetime.datetime.utcnow())
        message = await ctx.send(embed=embed)
        async with aiohttp.ClientSession() as lyricsSession:
            async with lyricsSession.get(
                    f'https://some-random-api.ml/lyrics?title={song}') as jsondata:  # define jsondata and fetch from API
                if not 300 > jsondata.status >= 200:  # if an unexpected HTTP status code is recieved from the website, throw an error and come out of the command
                    return await ctx.send(f'Please try the command again.')

                lyricsData = await jsondata.json()  # load the json data into its json form

        error = lyricsData.get('error')
        if error:  # checking if there is an error recieved by the API, and if there is then throwing an error message and returning out of the command
            return await ctx.send(
                f'<a:cancel:863204248657461298> Received unexpected error: {error} <@756308319622397972>')

        songLyrics = lyricsData['lyrics']  # the lyrics
        songArtist = lyricsData['author']  # the author's name
        songTitle = lyricsData['title']  # the song's title
        songThumbnail = lyricsData['thumbnail']['genius']  # the song's picture/thumbnail

        # sometimes the song's lyrics can be above 4096 characters, and if it is then we will not be able to send it in one single message on Discord due to the character limit
        # this is why we split the song into chunks of 4096 characters and send each part individually
        for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace=False):
            chunked = profanity.contains_profanity(chunk)
            if chunked == True:
                embed = Embed(
                    description=f"```{songTitle} contains some profanity.\nIf the bot got the wrong title try to include the author.```",
                    colour=ctx.author.colour)
                await message.edit(embed=embed)
            else:
                embed = discord.Embed(
                    title=songTitle,
                    description=chunk,
                    color=discord.Color.blurple(),
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_thumbnail(url=songThumbnail)
                await message.edit(embed=embed)
    else:
        if search == None:
            embed = discord.Embed(
                color=discord.Color.blurple(),
                description=f"<a:cancel:863204248657461298> Incorrect text channel.\nGo to <#891568732810408007> or <#892205334721101844> and send ```ignt lyrics *song title```")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=discord.Color.blurple(),
                description=f"<a:cancel:863204248657461298> Incorrect text channel.\nGo to <#891568732810408007> or <#892205334721101844> and send ```ignt lyrics {search}```")
            await ctx.send(embed=embed)


weather_channels = [870116673980616785, 892205334721101844]


@bot.command()
async def weather(ctx, *, Weather=None):
    if ctx.channel.id in weather_channels:
        embed = discord.Embed(
            description=f"Collecting weather of {Weather}. <a:loading:870870083285712896>",
            color=discord.Color.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        msg = await ctx.send(embed=embed)
        weather = client.get_weather(Weather)
        Location = weather.location.name
        temp = weather.current.temperature
        embed = Embed(title=f"Weather for {Location}",
                      description=f"{Location}: {temp} degrees Celsius",
                      colour=ctx.author.colour,
                      timestamp=datetime.datetime.utcnow()
                      )

        await msg.edit(embed=embed)
    else:
        embed = discord.Embed(
            color=discord.Color.blurple(),
            description=f"<a:cancel:863204248657461298> Incorrect text channel.\nGo to <#892205334721101844> and send ```ignt weather {Weather}```")
        await ctx.send(embed=embed)


bot.run("")  # Runs our bot
