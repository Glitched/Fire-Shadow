import pygame

pygame.init()

import baseCharacter
import enemy
import tower
import images
import sounds
import projectile
import math
from board import *
from HUD import *

"""
TODO LIST:

- Branding work: Logo and other shit
- Towers that shoot/ different ideas/ power up towers (beacons)
- GUI rework
- Actual pathfinding algorithms
- Upgrade systems
- Wave systems
- Hearts instead of health number (Ten hearts, divisible in half)
- Per Tower Upgrades
- Sprites for character upgrades
- Better path detection

- Cache Tower surface, like lighting

DONE LIST: 
- Better Anti-Tower Stacking 17-Dec-17
- Character Upgrades 17-Dec-17
- Implement a debug mode DONE 01-Dec-17
- Implement a start screen (nothing fancy yet necessarily, but something functional) DONE 01-Dec-17
- Implement a dying screen
- Find a new font (Check google fonts) DONE 01-Dec-17
- Play Again option DONE 23-Dec-17

"""

pygame.font.init()

# Game Dimensions
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 704

# initialisation of components
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Fire & Shadow')
clock = pygame.time.Clock()

basicfont = pygame.font.SysFont(None, 22)

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)

def initialise():
	global player_dead, start_screen, debug_mode, build_mode, quitting_bool, current_tower, projectiles, enemies, towers, lights, light_map, player_x, player_y, dx, dy
	global player, prevDir, max_health, frame, seconds, score
	player_dead = False
	start_screen = True
	debug_mode = False
	build_mode = False
	quitting_bool = False
	current_tower = None

	projectiles = []
	enemies = []
	towers = []
	lights = [(DISPLAY_WIDTH/2, DISPLAY_HEIGHT /2)]
	light_map = generate_light_surface(DISPLAY_WIDTH, DISPLAY_HEIGHT, lights)

	# movement related mechanics
	player_x = DISPLAY_WIDTH / 2
	player_y = DISPLAY_HEIGHT / 2

	dx = 0
	dy = 0

	# Making player
	player = baseCharacter.Wizard(player_x, player_y, 20, constants.CHAR_SPEED, constants.WIZARD_SHOT_DAMAGE, 100, 100, 0, [])
	prevDir = constants.RIGHT
	max_health = player.getHealth()

	frame = 0
	seconds = 0

	score = 0


def handle_movement(event):
	global dx, prevDir, dy, debug_mode, seconds, build_mode, current_tower

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_a:
			dx = -player.speed
			player.flipScript("a")
			prevDir = constants.LEFT
		elif event.key == pygame.K_d:
			dx = player.speed
			player.flipScript("d")
			prevDir = constants.RIGHT
		if event.key == pygame.K_w:
			dy = -player.speed
			player.flipScript("w")
		elif event.key == pygame.K_s:
			dy = player.speed
			player.flipScript("s")

		if event.key == pygame.K_SPACE:
			projectiles.append(player.attack())

		if event.key == pygame.K_o and debug_mode:
			seconds *= 2

		if event.key == pygame.K_p:
			debug_mode = not debug_mode

		if event.key == pygame.K_e:
			build_mode = True
			current_tower = None
			for item in towers:
				if abs(item.x - player.x) < 20 and abs(item.y - player.y) < 20:
					current_tower = item
					break

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_a or event.key == pygame.K_d:
			dx = 0
		elif event.key == pygame.K_w or event.key == pygame.K_s:
			dy = 0

		if event.key == pygame.K_SPACE:
			player.attack_flip(prevDir)


def handle_build_keys():
	global build_mode, light_map, player_dead

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			player_dead = True
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_t:
				if buy(40) and not tower_is_overlapping():
					towers.append(tower.Trap(player_x, player_y))

			if event.key == pygame.K_g:
				if buy(100) and not tower_is_overlapping():
					lights.append((player_x, player_y))
					light_map = add_light(light_map, (player_x, player_y))

			if event.key == pygame.K_f:
				if buy(250) and not tower_is_overlapping():
					towers.append(tower.Freeze(player_x, player_y))

			if event.key == pygame.K_r:
				if buy(250) and not tower_is_overlapping():
					towers.append(tower.Turret(player_x, player_y))

			if event.key == pygame.K_d:
				if buy(400):
					player.atk = 1.5 * player.atk

			if event.key == pygame.K_c:
				if buy(400):
					player.speed = 1.5 * player.speed

			if event.key == pygame.K_x:
				buy(600)

			if event.key == pygame.K_e:
				build_mode = False


def tower_is_overlapping():
	global build_mode
	for item in towers:
		if abs(item.x - player.x) < 20 and abs(item.y - player.y) < 20:
			build_mode = True
			sounds.fail.play()
			return True
	sounds.success.play()
	return False


def buy(price):
	global build_mode
	if player.gold >= price:
		player.setGold(player.gold - price)
		build_mode = False
		return True
	sounds.fail.play()
	return False


def debug_mode_script():
	if debug_mode:
		player.setGold(100000)
	

def update_player_location():
	global player_x, player_y
	player_x += dx
	player_y += dy

	if player_x >= DISPLAY_WIDTH - constants.TILE_SIZE:
		player_x = DISPLAY_WIDTH - constants.TILE_SIZE
	if player_x <= 0:
		player_x = 0
	if player_y >= DISPLAY_HEIGHT - constants.TILE_SIZE:
		player_y = DISPLAY_HEIGHT- constants.TILE_SIZE
	if player_y <= 0:
		player_y = 0

	player.setX(player_x)
	player.setY(player_y)



# Start screen loop
def start_loop():
	global start_screen
	while start_screen:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				start_screen = False
		game_display.blit(images.title_screen, (0, 0))
		pygame.display.update()

# Main game loop
def main_game_loop():
	
	global player_dead, start_screen, debug_mode, build_mode, quitting_bool, current_tower, projectiles, enemies, towers, lights, light_map, player_x, player_y, dx, dy
	global player, prevDir, max_health, frame, seconds, score, fx
	while not player_dead:
		if not build_mode:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					player_dead = True
				handle_movement(event)

			# Spawn two bad guys per second
			frame += 1
			if frame >= 24:
				seconds += 1
				frame = 0
			if frame == 0 or frame == 12:
				location = enemy.random_spawn_location(DISPLAY_WIDTH, DISPLAY_HEIGHT)
				enemies.append(enemy.Zombie(location[0], location[1]))

			if seconds > 0 and frame == 12 and seconds % 12 == 0:
				for _ in range(0, int(seconds / 12)):
					location = enemy.random_spawn_location(DISPLAY_WIDTH, DISPLAY_HEIGHT)
					enemies.append(enemy.StrongZombie(location[0], location[1]))

			if seconds > 0 and frame == 12 and ((seconds - 6) % 12 == 0):
				for _ in range(0, int((seconds - 6) / 12)):
					location = enemy.random_spawn_location(DISPLAY_WIDTH, DISPLAY_HEIGHT)
					enemies.append(enemy.SpeedZombie(location[0], location[1]))

			update_player_location()

			# Deal damage to bad guys
			for proj in projectiles:
				if proj.getX() >= DISPLAY_WIDTH or proj.getX() <= 0 \
					or proj.getY() >= DISPLAY_HEIGHT or proj.getY() <= 0:
					projectiles.remove(proj)
				else:
					proj.update()
					for badguy in enemies:
						if abs((proj.getX()) - badguy.x ) < 20 and abs((proj.getY()) - badguy.y) < 20:
							badguy.health -= proj.damage
							projectiles.remove(proj)
							if badguy.health <= 0:
								enemies.remove(badguy)
								score += 1
								player.setGold(player.getGold() + 5)
							break

			# Move bad guys and deal damage to good guy
			for badguy in enemies:
				badguy.update(player_x, player_y)
				if abs(badguy.x - player.x) < 20 and abs(badguy.y - player.y) < 20 and not debug_mode:
					player.health -= badguy.damage

			fx = []
			for item in towers:
				if item.cooldown <= 0:
					item.cooldown = item.max_cooldown
					if isinstance(item, tower.Trap):
						item.sprite = images.trap
						for badguy in enemies:
							if abs(badguy.x - item.x) < 20 and abs(badguy.y - item.y) < 20:
								enemies.remove(badguy)
								item.sprite = images.trap_disabled
								break
					elif isinstance(item, tower.Freeze):
						for badguy in enemies:
							if abs(badguy.x - item.x) < 64 and abs(badguy.y - item.y) < 64 and badguy.speed != 0:
								fx.append((item.x - 48, item.y - 48))
								badguy.speed = 0
								break
					elif isinstance(item, tower.Turret):
						for badguy in enemies:
							if abs(badguy.x - item.x) < 92 and abs(badguy.y - item.y) < 92:
								proj = projectile.TurretShot(
									item.x, item.y,
									math.atan((badguy.y - item.y)/(0.0001 + badguy.x - item.x)),
									(item.y < badguy.y), (item.x < badguy.x)
								)
								projectiles.append(proj)
								break
				else:
					item.cooldown -= 1

			draw_board(DISPLAY_WIDTH, DISPLAY_HEIGHT, game_display, player, enemies, projectiles, towers, lights, light_map, fx, debug_mode)
			draw_hud(game_display, basicfont, DISPLAY_HEIGHT, player.getGold(), player.getHealth(), score, frame, seconds, debug_mode)

			debug_mode_script()
			pygame.display.update()
			clock.tick(24)

			if player.getHealth() <= 0:
				player.setHealth(0)
				player_dead = True
				quitting_bool = True
			elif player.health <= max_health:
				player.health += constants.PLAYER_HEALTH_INCREMENT
		else:
			dx = 0
			dy = 0
			draw_board(DISPLAY_WIDTH, DISPLAY_HEIGHT, game_display, player, enemies, projectiles, towers, lights, light_map, fx, debug_mode)
			draw_hud(game_display, basicfont, DISPLAY_HEIGHT, player.getGold(), player.getHealth(), score, frame, seconds, debug_mode)
			if current_tower is not None:
				draw_build_hud(game_display, basicfont, current_tower)
			game_display.blit(images.build_overlay, (0, 0))
			pygame.display.flip()
			handle_build_keys()

def quit_loop():
	global quitting_bool, fx
	while quitting_bool:
		draw_board(DISPLAY_WIDTH, DISPLAY_HEIGHT, game_display, player, enemies, projectiles, towers, lights, light_map, fx, debug_mode)
		draw_hud(game_display, basicfont, DISPLAY_HEIGHT, player.getGold(), player.getHealth(), score, frame, seconds, debug_mode)
		game_display.blit(images.death_overlay, (0, 0))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					quitting_bool = False
				if event.key == pygame.K_a:
					play_game()

def play_game():

	initialise()
	start_loop()
	main_game_loop()
	quit_loop()

play_game()
print(score)
pygame.quit()
quit()
