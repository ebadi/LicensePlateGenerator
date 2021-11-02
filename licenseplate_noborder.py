from PIL import Image, ImageDraw, ImageFont
import string
import random

import pymeanshift as pms
import os
import sys

random.seed(4141)
def rnd_str(l):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=l))

# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Czech_Republic


font = ImageFont.truetype('resources/din1451alt.ttf', size=310)
color = 'rgb(0, 0, 0)' # black

for i in range(1,5):
	part1 = rnd_str(3)
	part2 = rnd_str(4)


	##########################################################
	image = Image.open('resources/CZ-number-plate-2004.png')
	draw = ImageDraw.Draw(image)

	draw.text((250, 0), part1, fill=color, font=font)
	draw.text((950, 0), part2, fill=color, font=font)
	image.save('output/' + str(i) + '_' + part1 + '_' + part2 + '.png')


