from PIL import Image, ImageDraw, ImageFont
import string
import random
def rnd_str(l):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=l))

# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Czech_Republic


font = ImageFont.truetype('resources/din1451alt.ttf', size=310)
color = 'rgb(0, 0, 0)' # black
part1 = rnd_str(3)
part2 = rnd_str(4)

#part1 = "5A6"
#part2 = "3240"

##########################################################
image = Image.open('resources/CZ-number-plate-2004.png')
draw = ImageDraw.Draw(image)

draw.text((210, 0), part1, fill=color, font=font)
draw.text((950, 0), part2, fill=color, font=font)
image.save('result.png')

##########################################################
image = Image.open('resources/CZ-number-plate-2004-US.png')
draw = ImageDraw.Draw(image)

draw.text((300, 0), part1, fill=color, font=font)
draw.text((250, 350), part2, fill=color, font=font)
image.save('resultUS.png')
