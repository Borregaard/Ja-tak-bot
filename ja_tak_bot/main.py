import discord
import os
import requests
import urllib
from discord.ext import commands


TOKEN = 'ODUzNjEyMjU5OTYzODMwMjcy.YMX6Xg.NKl_PW1IOaKj9TNyKhUds1Efd2g'

client = discord.Client()
#bot = discord.ext.commands.Bot(command_prefix='$')

command = """
Alle commands lige nu, der kommer flere

$ja tak
$nej tak
$trade offer
"""



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ja tak'):
        await message.channel.send('https://cdn.discordapp.com/attachments/776159549231988781/844521835047419904/unknown.png')

    if message.content.startswith('$nej tak'):
      await message.channel.send('https://cdn.discordapp.com/attachments/819144724651966474/849945886971789322/unknown.png')

    if message.content.startswith('$trade offer'):
      await message.channel.send('https://cdn.discordapp.com/attachments/776159549231988781/844526031847030824/unknown.png')

    if message.content.startswith('$commands'):
      await message.channel.send(command)
#
#@bot.command()
#async def test(ctx, *, arg):
#    await ctx.send(arg)
#




client.run(TOKEN)
#bot.run(TOKEN)


