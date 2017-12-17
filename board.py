import images
import constants
import animation
import pygame


def draw_board(width, height, screen, player, enemies, projectiles, towers, lights, light_map, fx, debug_mode):

	screen.blit(images.board_background, (0, 0))
	place_towers(towers, screen)
	draw_fx(fx, screen)
	draw_projectiles(projectiles, screen)
	place_objects(width, height, screen, enemies, lights)

	# Draw lighting
	if not debug_mode:
		screen.blit(light_map, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

	# Place player
	screen.blit(player.sprite, (player.x, player.y))


def draw_projectiles(projectiles, screen):
	for projectile in projectiles:
		screen.blit(projectile.sprite, (projectile.getX(), projectile.getY()))


def draw_fx(fx, screen):
	for effect in fx:
		screen.blit(images.frost, effect, special_flags=pygame.BLEND_ADD)


def place_towers(towers, screen):
	for tower in towers:
		screen.blit(tower.sprite, (tower.x, tower.y))


def place_objects(width, height, screen, enemies, lights):
	"""
	This function places objects on the board
	"""

	for badguy in enemies:
		screen.blit(badguy.sprite, (badguy.x, badguy.y))

	# campfire image
	current_image = animation.campfire_flicker(constants.FLICKER_I)
	screen.blit(current_image, (width / 2, height / 2))
	constants.FLICKER_I += 1
	if constants.FLICKER_I == 20:
		constants.FLICKER_I = 1

	for light in lights:
		screen.blit(current_image, light)


def generate_light_surface(width, height, lights):
	fx = pygame.surface.Surface((width, height))
	fx.fill(pygame.color.Color('White'))
	for light in lights:
		fx.blit(images.light, (light[0] - 352 + 16, light[1] - 352 + 16))
	return fx


def add_light(light_map, light):
	light_map.blit(images.light, (light[0] - 352 + 16, light[1] - 352 + 16))
	return light_map
