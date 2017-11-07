import constants
import random
import game
import images


def place_tiles():
	cord_list = game.generate_grid()
	flicker = random.randint(0, 15)
	if flicker != 1:
		flicker = 0
	for tup in cord_list:
		game.game_display.blit(images.tile, tup)

		# Add shadow to tiles
		s = game.pygame.Surface((32, 32))
		s.set_alpha(
			((constants.display_width / 2 - tup[0]) ** 2 + (constants.display_height / 2 - tup[1]) ** 2) ** 0.5 * (0.9 + 0.15 * flicker)
		)
		game.game_display.blit(s, tup)
