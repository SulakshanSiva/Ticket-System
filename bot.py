import discord
from discord.ext import commands
from discord.utils import get

import os
from dotenv import load_dotenv 

load_dotenv('.env')
token = os.getenv('TUTORIAL_BOT_TOKEN')
channel_id = os.getenv('CHANNEL_ID')
channel_id2 = os.getenv('CHANNEL_ID2')

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event
async def on_ready(self, guild):
    print("Bot is online")

@bot.event
async def on_reaction_add(reaction, user):
    
    channel = bot.get_channel(int(channel_id2))
    if reaction.message.channel.id != channel.id:
        return
    if reaction.emoji == "🟦":
      Role = discord.utils.get(user.guild.roles, name="Python")
      await user.add_roles(Role)
    elif reaction.emoji == "🟥":
      Role = discord.utils.get(user.guild.roles, name="Java")
      await user.add_roles(Role)
    elif reaction.emoji == "🟨":
      Role = discord.utils.get(user.guild.roles, name="C")
      await user.add_roles(Role)

@bot.event
async def on_reaction_remove(reaction, user):
    print("TODO")
    
@bot.command()
async def roles(ctx: commands.context, member:discord.Member = None):

    lineOne =  """Welcome to the server!

Which of these languages do you use:

* Python (🟦)
* Java (🟥)
* C (🟨)

React to this message with the corresponding emoji to get assigned the role!"""

    embed = discord.Embed(title="Roles", colour=discord.Colour.random())
    embed.add_field(name="", value=f"{lineOne}", inline=False)

    emoji = await ctx.send(embed=embed)
    await emoji.add_reaction('🟦')
    await emoji.add_reaction('🟥')
    await emoji.add_reaction('🟨')

@bot.command()
async def ticket(ctx: commands.context, *note, member:discord.Member = None):
    if member == None:  
        member = ctx.author

    channel = bot.get_channel(int(channel_id))

    embed = discord.Embed(title="Ticket", colour=discord.Colour.random())

    embed.add_field(name="Discord Username", value=f"{member}", inline=False)
    embed.add_field(name="Question", value=" ".join(note), inline=False)

    await channel.send(embed=embed)


@bot.command()
async def profile(ctx, member:discord.Member = None):
    if member == None:  
        member = ctx.author

    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title=f"{name}", colour=discord.Colour.random())
    embed.set_author(name="Profile")
    embed.set_thumbnail(url=f"{pfp}")
    roles = f"{' '.join([role.mention for role in member.roles if role.name != '@everyone'])}"
    embed.add_field(name="Roles:", value=f"{roles}", inline=False)

    await ctx.send(embed=embed)


bot.run(token)