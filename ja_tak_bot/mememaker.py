from PIL import Image, ImageFont, ImageDraw

x_1 = 125
y_1 = 290

x_2 = 625
y_2 = 290

shadowcolor = "black"

my_image = Image.open("frede.jpg")
font = ImageFont.truetype('impact.ttf', 50)
result_image = my_image.convert("RGB")

text1 = input("Hvad får du?")
text2 = input("Hvad giver du?")
image_editable = ImageDraw.Draw(result_image)

image_editable.text((x_1-2, y_1-2), text1, font=font, fill=shadowcolor)
image_editable.text((x_1+2, y_1-2), text1, font=font, fill=shadowcolor)
image_editable.text((x_1-2, y_1+2), text1, font=font, fill=shadowcolor)
image_editable.text((x_1+2, y_1+2), text1, font=font, fill=shadowcolor)

image_editable.text((x_2-2, y_2-2), text2, font=font, fill=shadowcolor)
image_editable.text((x_2+2, y_2-2), text2, font=font, fill=shadowcolor)
image_editable.text((x_2-2, y_2+2), text2, font=font, fill=shadowcolor)
image_editable.text((x_2+2, y_2+2), text2, font=font, fill=shadowcolor)


image_editable.text((x_1,y_1), text1, (255, 255, 255), font=font)
image_editable.text((x_2,y_2), text2, (255, 255, 255), font=font)

result_image.save("result.jpg")
