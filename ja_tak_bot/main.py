import discord
import os
import requests
import urllib
from PIL import Image, ImageFont, ImageDraw
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


#x_1 = 125
#y_1 = 290
#
#x_2 = 625
#y_2 = 290
#
#shadowcolor = "black"
#
#my_image = Image.open("frede.jpg")
#font = ImageFont.truetype('impact.ttf', 50)
#result_image = my_image.convert("RGB")
#
#text1 = input("Hvad får du?")
#text2 = input("Hvad giver du?")
#image_editable = ImageDraw.Draw(result_image)
#
#image_editable.text((x_1-2, y_1-2), text1, font=font, fill=shadowcolor)
#image_editable.text((x_1+2, y_1-2), text1, font=font, fill=shadowcolor)
#image_editable.text((x_1-2, y_1+2), text1, font=font, fill=shadowcolor)
#image_editable.text((x_1+2, y_1+2), text1, font=font, fill=shadowcolor)
#
#image_editable.text((x_2-2, y_2-2), text2, font=font, fill=shadowcolor)
#image_editable.text((x_2+2, y_2-2), text2, font=font, fill=shadowcolor)
#image_editable.text((x_2-2, y_2+2), text2, font=font, fill=shadowcolor)
#image_editable.text((x_2+2, y_2+2), text2, font=font, fill=shadowcolor)
#
#
#image_editable.text((x_1,y_1), text1, (255, 255, 255), font=font)
#image_editable.text((x_2,y_2), text2, (255, 255, 255), font=font)
#
#result_image.save("result.jpg")



client.run(TOKEN)
#bot.run(TOKEN)


