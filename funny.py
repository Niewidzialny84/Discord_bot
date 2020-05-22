import asyncio
import discord
import pickle
import re
from bot import bot

#help
@bot.command()
async def todo(ctx):
    embed = discord.Embed(title="Help",description="this displays the help commands",color=0x00ff00)
    embed.add_field(name="Ayaya",value="narazie nicz nie ma",inline=False)
    await ctx.message.channel.send(embed=embed)

@bot.event
async def on_message(message):
    #:OOF: reaction to and OOF message
    emoji = discord.utils.get(message.guild.emojis, name='OOF')
    msg = message.content.lower()
    x = re.search("^[^a-zA-Z0-9]*[o]+of[^a-zA-Z0-9]*$",msg)
    if x != None:
        await message.add_reaction(emoji)

    #Hello and goodbye
    if bot.user.mentioned_in(message):
        if re.search('dzień dobry .*', msg) != None:
            await message.channel.send('Dzień dobry! '+message.author.mention)
        elif re.search('dobranoc .*', msg) != None:
            await message.channel.send('Dobranoc! '+message.author.mention)
    await bot.process_commands(message)

    #Check if the send attachment is an image
    try:
        for attachments in message.attachments:
            att = attachments.url
            for ext in ['.jpg','.png','.jpeg','.PNG','.JPEG','.JPG']:
                if att.endswith(ext):
                    for x in ['🇦', '🇧' , '🇨', '🇩', '🇪', '🇫']:
                        emoji = bot.get_emoji(x)
                        await message.add_reaction(x)
    except IndexError:
        pass

#Bot reaction to an image -> leaving one reaction
#@bot.event
#async def on_reaction_add(reaction,user):
#    for react in reaction.message.reactions:
#        async for users in react.users (limit=None,after=None):
#            if react != reaction and users == user and user != bot.user:
#                await reaction.remove(user)        