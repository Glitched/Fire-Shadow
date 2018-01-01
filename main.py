import pygame

pygame.init()
import game
import baseCharacter
import enemy
import tower
import images
import sounds
import projectile
import math
import wave
from board import *
from HUD import *

"""
TODO LIST:

- Branding work: Logo and other shit
- Towers that shoot/ different ideas/ power up towers (beacons)
- GUI rework
- Actual pathfinding algorithms
- Upgrade systems
- Hearts instead of health number (Ten hearts, divisible in half)
- Per Tower Upgrades
- Sprites for character upgrades
- Better path detection
- Cache Tower surface, like lighting
- Upgrade the wave system, i.e. tweaking numbers and spawning algorithms
- NOTES FROM GAMEPLAY: Need to cap the "Upgrade speed". If you keep going like twice or thrice the game becomes unplayable. Also need to figure out HP + DMG scaling.

IDEAS LIST:

- The game is currently too easy: perhaps more enemy variety/ boss waves (i.e. every 5 or so)
- On the same vein, probably need to weaken towers a decent bit, playing this game I had no difficulty getting to wave 14 just sitting in towers, 
and it got boring quickly.

DONE LIST: 
- Better Anti-Tower Stacking 17-Dec-17
- Character Upgrades 17-Dec-17
- Implement a debug mode DONE 01-Dec-17
- Implement a start screen (nothing fancy yet necessarily, but something functional) DONE 01-Dec-17
- Implement a dying screen
- Find a new font (Check google fonts) DONE 01-Dec-17
- Play Again option DONE 23-Dec-17
- Wave System DONE 25-Dec-17

"""

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
		location = enemy.random_spawn_location(constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT)
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
			player.health = 0
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_t:
				if buy(player, instance, 40) and not tower_is_overlapping(player, instance):
					instance.towers.append(tower.Trap(player.x, player.y))

			if event.key == pygame.K_g:
				if buy(player, instance, 100) and not tower_is_overlapping(player, instance):
					instance.lights.append((player.x, player.y))
					instance.light_map = add_light(instance.light_map, (player.x, player.y))

			if event.key == pygame.K_f:
				if buy(player, instance, 250) and not tower_is_overlapping(player, instance):
					instance.towers.append(tower.Freeze(player.x, player.y))

			if event.key == pygame.K_r:
				if buy(player, instance, 250) and not tower_is_overlapping(player, instance):
					instance.towers.append(tower.Turret(player.x, player.y))

			if event.key == pygame.K_d:
				if buy(player, instance, 400):
					player.atk = 1.5 * player.atk

			if event.key == pygame.K_c:
				if buy(player, instance, 400):
					player.speed_upgrades += 1
					player.speed = (1 + (0.4/player.speed_upgrades)) * player.speed

			if event.key == pygame.K_x:
				buy(player, instance, 600)

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


def init_new_wave(currWave):
	num_fast_per_wave = 2
	num_big_per_wave = 2  # THESE ARE TEMPORARY NUMBERS, WE CAN COME UP WITH A GOOD AMOUNT AND SCALING LATER, AS WELL AS AN ASSIGNMENT

	enem = []
	level = currWave.getLevel() + 1

	for n in range(int(currWave.getNumEnemies()*constants.WAVE_SCALING)):
		location = enemy.random_spawn_location(constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT)
		if n == 0 or n == 1:
			enem.append(enemy.SpeedZombie(location[0], location[1]))
		elif n == 2 or n == 3:
			enem.append(enemy.StrongZombie(location[0], location[1]))
		else:
			enem.append(enemy.Zombie(location[0], location[1]))

	for badguy in enem:
		badguy.setDamage(badguy.getDamage()*level/3)

	newWave = wave.Wave(level, enem)
	
	return newWave


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
					player.health = 0
					return True
				handle_movement(event, player, instance)

			instance.tick()
			spawn_enemies(instance)
			player.move()
			process_projectiles(instance, player)
			process_enemies(instance, player)
			fx = process_towers(instance)

			draw_board(game_display, player, instance, fx)
			draw_hud(game_display, basicfont, player, instance)
			draw_wave_number(game_display, basicfont, instance.current_wave.getLevel())

			if len(instance.enemies) == 0:
				draw_incoming_wave(game_display, basicfont, instance.current_wave.getLevel())

			if instance.debug_mode:
				player.gold = 31337

			pygame.display.update()
			clock.tick(24)

			if player.getHealth() <= 0:
				player.setHealth(0)
			elif player.health <= player.max_health:
				player.health += constants.PLAYER_HEALTH_INCREMENT
		else:
			player.dx = player.dy = 0
			draw_board(game_display, player, instance, None)
			draw_hud(game_display, basicfont, player, instance)
			if instance.current_tower is not None:
				draw_build_hud(game_display, basicfont, instance.current_tower)
			game_display.blit(images.build_overlay, (0, 0))
			pygame.display.flip()
			handle_build_keys(player, instance)
	return False


def spawn_enemies(instance):
	if len(instance.current_wave.getEnemies()) > 0:
		if instance.frame % 12 == 0:
			instance.enemies.append(instance.current_wave.getEnemies().pop())

	elif len(instance.current_wave.getEnemies()) <= 0 and len(instance.enemies) == 0:
		instance.current_wave.setGap(instance.current_wave.getGap() - (1 / 60))

		if instance.current_wave.getGap() <= 0:
			instance.current_wave = init_new_wave(instance.current_wave)


def process_towers(instance):
	fx = []
	for item in instance.towers:
		if item.cooldown <= 0:
			item.cooldown = item.max_cooldown
			if isinstance(item, tower.Trap):
				item.sprite = images.trap
				for badguy in instance.enemies:
					if abs(badguy.x - item.x) < 20 and abs(badguy.y - item.y) < 20:
						instance.enemies.remove(badguy)
						item.sprite = images.trap_disabled
						break
			elif isinstance(item, tower.Freeze):
				for badguy in instance.enemies:
					if abs(badguy.x - item.x) < 64 and abs(badguy.y - item.y) < 64 and badguy.speed != 0:
						fx.append((item.x - 48, item.y - 48))
						badguy.speed = 0
						break
			elif isinstance(item, tower.Turret):
				for badguy in instance.enemies:
					if abs(badguy.x - item.x) < 92 and abs(badguy.y - item.y) < 92:
						proj = projectile.TurretShot(
							item.x, item.y,
							math.atan((badguy.y - item.y) / (0.0001 + badguy.x - item.x)),
							(item.y < badguy.y), (item.x < badguy.x)
						)
						instance.projectiles.append(proj)
						break
		else:
			item.cooldown -= 1
	return fx


def process_enemies(instance, player):
	for badguy in instance.enemies:
		badguy.update(player.x, player.y)
		if abs(badguy.x - player.x) < 20 and abs(badguy.y - player.y) < 20 and not instance.debug_mode:
			player.health -= badguy.damage


def process_projectiles(instance, player):
	for proj in instance.projectiles:
		if proj.getX() >= constants.DISPLAY_WIDTH or proj.getX() <= 0 \
				or proj.getY() >= constants.DISPLAY_HEIGHT or proj.getY() <= 0:
			instance.projectiles.remove(proj)
		else:
			proj.update()
			for badguy in instance.enemies:
				if abs((proj.getX()) - badguy.x) < 20 and abs((proj.getY()) - badguy.y) < 20:
					badguy.health -= proj.damage
					instance.projectiles.remove(proj)
					if badguy.health <= 0:
						instance.enemies.remove(badguy)
						instance.score += 1
						player.setGold(player.getGold() + badguy.getValue())
					break


def quit_loop(quitting):
	game_display.blit(images.death_overlay, (0, 0))
	pygame.display.flip()
	while quitting:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					quitting = False
				if event.key == pygame.K_a:
					play_game()
			if event.type == pygame.QUIT:
				quitting = False


def play_game():
	player, instance = initialise()
	start_loop()
	didClose = main_game_loop(player, instance)
	quit_loop(not didClose)


play_game()
pygame.quit()
quit()
