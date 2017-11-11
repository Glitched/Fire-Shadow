import random
import images
import constants
import animation
import pygame


def draw_board(width, height, screen, player, enemies, projectiles, towers, lights, light_map):
	grid = generate_grid(width, height)

	place_tiles(screen, grid)
	place_towers(towers, screen)
	draw_projectiles(projectiles, screen)
	place_objects(width, height, screen, enemies, lights)

	# Draw lighting
	screen.blit(light_map, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

	# Place player
	screen.blit(player.sprite, (player.x + constants.TILE_SIZE, player.y - constants.TILE_SIZE))


def generate_grid(width, height):
	new_list = []
	for x in range(0, width, constants.TILE_SIZE):
		for y in range(0, height, constants.TILE_SIZE):
			new_list.append((x, y))
	return new_list


def draw_projectiles(projectiles, screen):
	for projectile in projectiles:
		screen.blit(projectile.sprite, (projectile.getX(), projectile.getY()))


def place_tiles(screen, grid):
	for tup in grid:
		screen.blit(images.tile, tup)


def place_towers(towers, screen):
	for tower in towers:
		screen.blit(tower.sprite, (tower.x, tower.y))


def place_objects(width, height, screen, enemies, lights):
	"""
	This function places objects on the board
	"""

	for badguy in enemies:
		screen.blit(badguy.sprite, (badguy.x + constants.TILE_SIZE, badguy.y - constants.TILE_SIZE))

	# campfire image
	screen.blit(animation.campfire_flicker(constants.FLICKER_I), (width / 2, height / 2))
	constants.FLICKER_I += 1
	if constants.FLICKER_I == 20:
		constants.FLICKER_I = 1

	for light in lights:
		screen.blit(animation.campfire_flicker(constants.FLICKER_I + random.randint(-2,2)), light)


def generate_light_surface(width, height, lights):
	fx = pygame.surface.Surface((width, height))
	fx.fill(pygame.color.Color('White'))
	for light in lights:
		fx.blit(images.light, (light[0] - 352 + 16, light[1] - 352 + 16))
	return fx


def add_light(light_map, light):
	light_map.blit(images.light, (light[0] - 352 + 16, light[1] - 352 + 16))
	return light_map