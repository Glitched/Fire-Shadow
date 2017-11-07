import pygame

def campfire_flicker(flicker_i):
	"""
	Returns the image of the campfire to go.
	"""
	campfire_image= pygame.image.load('images/campfire.png')
	campfire_image_2= pygame.image.load('images/campfire2.png')
	campfire_image_3= pygame.image.load('images/campfire3.png')

	if flicker_i<= 5:
		return campfire_image
	elif flicker_i<= 10:
		return campfire_image_2
	elif flicker_i<= 15:
		return campfire_image_3
	else:
		return campfire_image_2