import random
import images
import constants
import animation
import pygame


def draw_board(width, height, game_display, player, enemies, projectiles):
	grid = generate_grid(width, height)

	place_tiles(game_display, grid)
	draw_projectiles(projectiles, game_display)
	place_objects(width, height, game_display, player, enemies)
	add_shadows(width, height, game_display, grid)

	# Place player
	game_display.blit(player.sprite, (player.x + constants.TILE_SIZE, player.y - constants.TILE_SIZE))


def generate_grid(width, height):
	new_list = []
	for x in range(0, width, constants.TILE_SIZE):
		for y in range(0, height, constants.TILE_SIZE):
			new_list.append((x, y))
	return new_list


def draw_projectiles(projectiles, game_display):
	for projectile in projectiles:
		game_display.blit(projectile.sprite, (projectile.getX(), projectile.getY()))


def place_tiles(game_display, grid):
	for tup in grid:
		game_display.blit(images.tile, tup)


def add_shadows(width, height, game_display, grid):
	flicker = random.randint(0, 15)
	if flicker != 1:
		flicker = 0
	for tup in grid:
		s = pygame.Surface((32, 32))
		s.set_alpha(
			((width / 2 - tup[0]) ** 2 + (height / 2 - tup[1]) ** 2) ** 0.5 * (0.9 + 0.15 * flicker)
		)
		game_display.blit(s, tup)


def place_objects(width, height, game_display, player, enemies):
	"""
	This function places objects on the board
	"""

	for badguy in enemies:
		game_display.blit(badguy.sprite, (badguy.x + constants.TILE_SIZE, badguy.y - constants.TILE_SIZE))

	# campfire image
	game_display.blit(animation.campfire_flicker(constants.FLICKER_I), (width / 2, height / 2))
	constants.FLICKER_I += 1
	if constants.FLICKER_I == 20:
		constants.FLICKER_I = 1
