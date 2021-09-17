from PIL import Image, ImageDraw, ImageFont
import string
import random
def rnd_str(l):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=l))

# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Czech_Republic
image = Image.open('resources/CZ-number-plate-2004.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('resources/din1451alt.ttf', size=310)
color = 'rgb(0, 0, 0)' # black

(x, y) = (210, 0)
message = rnd_str(3)
#message = "5A6"
draw.text((x, y), message, fill=color, font=font)


(x, y) = (950, 0)
message = rnd_str(4)
#message = "3240"
draw.text((x, y), message, fill=color, font=font)

image.save('result.png')
