import pygame

pygame.init()
import game
import baseCharacter
import enemy
import tower
import images
import sounds
import projectile
import wave
from board import *
from HUD import *


pygame.font.init()

# initialisation of components
game_display = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Fire & Shadow')
clock = pygame.time.Clock()

basicfont = pygame.font.Font('ArsleGothic.ttf', 16)

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)


def initialise():
	curr_enemies = []
	for n in range(constants.BASE_WAVE_AMOUNT):
		location = wave.random_spawn_location(constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT)
		curr_enemies.append(enemy.Zombie(location[0], location[1]))

	instance = game.Game()
	instance.light_map = generate_light_surface(instance.lights)
	instance.current_wave = wave.Wave(1, curr_enemies)

	player = baseCharacter.Wizard(
		constants.DISPLAY_WIDTH / 2,
		constants.DISPLAY_HEIGHT / 2,
		constants.WIZARD_BASE_HEALTH,
		constants.CHAR_SPEED,
		constants.WIZARD_SHOT_DAMAGE,
		100,
		100,
		0,
		[]
	)

	return player, instance


def handle_movement(event, player, instance):
	if event.type == pygame.KEYDOWN:
		player.set_momentum(event.key)

		if event.key == pygame.K_SPACE:
			instance.projectiles.append(player.attack())

		if event.key == pygame.K_o and instance.debug_mode:
			instance.seconds *= 2

		if event.key == pygame.K_p:
			instance.debug_mode = not instance.debug_mode

		if event.key == pygame.K_e:
			instance.build_mode = True
			instance.current_tower = None
			for item in instance.towers:
				if abs(item.x - player.x) < 20 and abs(item.y - player.y) < 20:
					instance.current_tower = item
					break

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_a or event.key == pygame.K_d:
			player.dx = 0
		elif event.key == pygame.K_w or event.key == pygame.K_s:
			player.dy = 0

		if event.key == pygame.K_SPACE:
			player.attack_flip()


def handle_build_keys(player, instance):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			player.setHealth(0)
		if event.type == pygame.KEYDOWN:

			if not tower_is_overlapping(player, instance):
				if event.key == pygame.K_t:
					if buy(player, instance, constants.PRICE["trap"]):
						instance.towers.append(tower.Trap1(player.x, player.y))
				if event.key == pygame.K_g:
					if buy(player, instance, constants.PRICE["campfire"]):
						instance.lights.append((player.x, player.y))
						instance.light_map = add_light(instance.light_map, (player.x, player.y))
				if event.key == pygame.K_f:
					if buy(player, instance, constants.PRICE["freeze"]):
						instance.towers.append(tower.Freeze(player.x, player.y))
				if event.key == pygame.K_r:
					if buy(player, instance, constants.PRICE["turret"]):
						instance.towers.append(tower.Turret(player.x, player.y))

			if event.key == pygame.K_d:
				if buy(player, instance, constants.PRICE["attack"]):
					player.atk = 1.5 * player.atk

			if event.key == pygame.K_c:
				if buy(player, instance, constants.PRICE["speed"]):
					player.speed_upgrades += 1
					player.speed = (1 + (0.2/player.speed_upgrades)) * player.speed

			if event.key == pygame.K_x:
				buy(player, instance, constants.PRICE["intelligence"])

			if event.key == pygame.K_v:
				if isinstance(instance.current_tower, tower.Trap1) and buy(player, instance, constants.PRICE["trap2"]):
					instance.towers.remove(instance.current_tower)
					instance.towers.append(tower.Trap2(instance.current_tower.x, instance.current_tower.y))

			if event.key == pygame.K_e:
				instance.build_mode = False


def tower_is_overlapping(player, instance):
	for item in instance.towers:
		if abs(item.x - player.x) < 20 and abs(item.y - player.y) < 20:
			instance.build_mode = True
			sounds.fail.play()
			return True
	sounds.success.play()
	return False


def buy(player, instance, price):
	if player.gold >= price:
		player.setGold(player.gold - price)
		instance.build_mode = False
		return True
	sounds.fail.play()
	return False


# Start screen loop
def start_loop():
	game_display.blit(images.title_screen, (0, 0))
	pygame.display.flip()
	start_screen = True
	while start_screen:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				start_screen = False


# Main game loop
def main_game_loop(player, instance):
	while player.health > 0:
		if not instance.build_mode:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					player.setHealth(0)
					return True
				handle_movement(event, player, instance)

			player.setHealth(player.getHealth() + constants.PLAYER_HEALTH_INCREMENT)

			instance.tick()
			enemy.spawn_enemies(instance)
			player.move()
			projectile.process_projectiles(instance, player)
			enemy.process_enemies(instance, player)
			fx = tower.process_towers(instance)

			draw_board(game_display, player, instance, fx)
			draw_hud(game_display, basicfont, player, instance)
			draw_wave_number(game_display, basicfont, instance.current_wave.getLevel())

			if len(instance.enemies) == 0:
				draw_incoming_wave(game_display, basicfont, instance.current_wave.getLevel())

			if instance.debug_mode:
				player.gold = 31337

			pygame.display.update()
			clock.tick(24)
		else:
			player.dx = player.dy = 0

			draw_board(game_display, player, instance, [])
			draw_hud(game_display, basicfont, player, instance)
			game_display.blit(images.build_overlay, (0, 0))

			if instance.current_tower is not None:
				draw_build_hud(game_display, basicfont, instance.current_tower)

			pygame.display.flip()
			handle_build_keys(player, instance)
	return False


def quit_loop():
	game_display.blit(images.death_overlay, (0, 0))
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					break
				if event.key == pygame.K_a:
					play_game()
			if event.type == pygame.QUIT:
				break


def play_game():
	player, instance = initialise()
	start_loop()
	didClose = main_game_loop(player, instance)
	if not didClose:
		quit_loop()


play_game()
pygame.quit()
quit()
