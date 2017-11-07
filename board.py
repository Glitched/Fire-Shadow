import random
import game
import images
import constants


def generate_grid():
	new_list = []
	for x in range(0, game.DISPLAY_WIDTH, constants.TILE_SIZE):
		for y in range(0, game.DISPLAY_HEIGHT, constants.TILE_SIZE):
			new_list.append((x, y))
	return new_list


def place_tiles():
	cord_list = generate_grid()
	flicker = random.randint(0, 15)
	if flicker != 1:
		flicker = 0
	for tup in cord_list:
		game.game_display.blit(images.tile, tup)

		# Add shadow to tiles
		s = game.pygame.Surface((32, 32))
		s.set_alpha(
			((game.DISPLAY_WIDTH / 2 - tup[0]) ** 2 + (game.DISPLAY_HEIGHT / 2 - tup[1]) ** 2) ** 0.5 * (0.9 + 0.15 * flicker)
		)
		game.game_display.blit(s, tup)


def place_object(x, y):
	"""
	This function places objects (to be called in the loop)
	"""
	# Insert the character image
	game.game_display.blit(game.player.sprite, (x + constants.TILE_SIZE, y - constants.TILE_SIZE))

	# campfire image
	game.game_display.blit(game.animation.campfire_flicker(constants.FLICKER_I), (game.DISPLAY_WIDTH / 2, game.DISPLAY_HEIGHT / 2))
	constants.FLICKER_I += 1
	if constants.FLICKER_I == 20:
		constants.FLICKER_I = 1
