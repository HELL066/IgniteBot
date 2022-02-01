import datetime
import pickle

import disnake
from disnake.ext import commands

main = {}
owner = {}
from typing import List



def create_pickle(filename):
    dbfile = open(f'{filename}.pkl', 'wb')
    a = {}
    pickle.dump(a, dbfile)
    dbfile.close()


def pickle_dump(var, filename):
    try:
        dbfile = open(f'{filename}.pkl', 'wb')
        # source, destination
        pickle.dump(var, dbfile)
        dbfile.close()
        return
    except Exception:
        create_pickle(filename)


def pickle_get(filename):
    try:
        dbfile = open(f'{filename}.pkl', 'rb')
        db = pickle.load(dbfile)
        dbfile.close()
        return db
    except Exception:
        create_pickle(filename)


class tags(commands.Cog, name="tags"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def tag(self, ctx, tag=None):

        main = pickle_get("main")
        if tag == None:
            await ctx.reply("Follow this format ignt tag `tagname`")
        else:
            if main.get(tag) is None:
                await ctx.reply("Tag does not exist.")
            else:
                try:
                    message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
                    await message.reply(main.get(tag))
                except:
                    await ctx.reply(main.get(tag))

    @tag.command()
    async def create(self, ctx, tagname=None, *, content=None):
        main = pickle_get("main")
        if main.get(tagname) != None:
            await ctx.reply(
                "A tag for this has already been created. If you own this tag use `ignt tag edit` to edit it.")
        elif tagname is None:
            await ctx.reply("Missing `tagname`. Follow this format: `ignt tag create tagname content`")
        elif content is None:
            await ctx.reply("Missing `content`. Follow this format: `ignt tag create tagname content`")
        elif tagname and content is None:
            await ctx.reply("Follow this format: `ignt tag create tagname content`")
        else:
            main[tagname] = content
            pickle_dump(main, "main")
            owner[tagname] = ctx.author.id
            pickle_dump(owner, "owner")
            await ctx.reply("Added tag successfully.")

    @tag.command()
    async def edit(self, ctx, tagname=None, new=None):
        owner = pickle_get("owner")
        main = pickle_get("main")
        if main.get(tagname) != None:
            if tagname == None:
                await ctx.reply("Give me a tag to edit.")
            elif new == None:
                await ctx.reply("Follow this format `ignt tag edit tagname tagcontent`")
            elif owner.get(tagname) != ctx.author.id:
                await ctx.reply("This isn't your tag.")
            else:
                main[tagname] = new
                pickle_dump(main, "main")
                owner[tagname] = ctx.author.id
                pickle_dump(owner, "owner")
                await ctx.reply("Edited tag successfully.")
        else:
            await ctx.reply("Tag does not exist.")

    @tag.command()
    async def delete(self, ctx, tagname=None):
        owner = pickle_get("owner")
        main = pickle_get("main")
        if owner.get(tagname) == ctx.author.id or 756308319622397972:
            owner[tagname] = None
            main[tagname] = None
            pickle_dump(owner, "owner")
            pickle_dump(main, "main")
            await ctx.reply("Deleted tag. ")
        else:
            await ctx.reply("Either you don't own this tag or This tag does not exist.")

    @tag.command()
    async def info(self, ctx, tagname=None):
        owner = pickle_get("owner")
        main = pickle_get("main")
        if tagname is None:
            await ctx.reply("Please give me a tagname.")
        elif main.get(tagname) is None:
            await ctx.reply("Tag does not exist.")
        else:
            user = await self.bot.fetch_user(owner.get(tagname))
            embed = disnake.Embed(
                title=tagname,
                timestamp=datetime.datetime.utcnow()
            ).set_author(name=user.name, icon_url=user.avatar.url).add_field(name="Owner", value=user.mention,
                                                                             inline=True).add_field(name="Content",
                                                                                                    value=main.get(
                                                                                                        tagname),
                                                                                                    inline=True)
            await ctx.reply(embed=embed)




def setup(bot):
    bot.add_cog(tags(bot))
