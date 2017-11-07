import random
import images
import constants
import animation


def generate_grid(width, height):
	new_list = []
	for x in range(0, width, constants.TILE_SIZE):
		for y in range(0, height, constants.TILE_SIZE):
			new_list.append((x, y))
	return new_list


def place_tiles(width, height, game_display, pygame):
	cord_list = generate_grid(width, height)
	flicker = random.randint(0, 15)
	if flicker != 1:
		flicker = 0
	for tup in cord_list:
		game_display.blit(images.tile, tup)

		# Add shadow to tiles
		s = pygame.Surface((32, 32))
		s.set_alpha(
			((width / 2 - tup[0]) ** 2 + (height / 2 - tup[1]) ** 2) ** 0.5 * (0.9 + 0.15 * flicker)
		)
		game_display.blit(s, tup)


def place_object(x, y, width, height, game_display, player):
	"""
	This function places objects (to be called in the loop)
	"""
	# Insert the character image
	game_display.blit(player.sprite, (x + constants.TILE_SIZE, y - constants.TILE_SIZE))

	# campfire image
	game_display.blit(animation.campfire_flicker(constants.FLICKER_I), (width / 2, height / 2))
	constants.FLICKER_I += 1
	if constants.FLICKER_I == 20:
		constants.FLICKER_I = 1
