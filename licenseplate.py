from PIL import Image, ImageDraw, ImageFont
import string
import random
random.seed(4141)
def rnd_str(l):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=l))

# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Czech_Republic


font = ImageFont.truetype('resources/din1451alt.ttf', size=310)
color = 'rgb(0, 0, 0)' # black

for i in range(1,10):
	part1 = rnd_str(3)
	part2 = rnd_str(4)
	
	#part1 = "5A6"
	#part2 = "3240"

	##########################################################
	image = Image.open('resources/CZ-number-plate-2004-square-2048x2048.png')
	draw = ImageDraw.Draw(image)

	pos1= (400, 850)
	draw.text(pos1, part1, fill=color, font=font)
	pos2= (1180, 850)
	draw.text(pos2, part2, fill=color, font=font)
	image.save('output/' + str(i) + '_' + part1 + '_' + part2 + '.png')

	##########################################################
	#image = Image.open('resources/CZ-number-plate-2004-US.png')
	#draw = ImageDraw.Draw(image)

	#draw.text((300, 0), part1, fill=color, font=font)
	#draw.text((250, 350), part2, fill=color, font=font)
	#image.save('licenseplate_us_' + str(i) + '_' + part1 + '_' + part2 + '.png')
