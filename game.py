import pygame
import baseCharacter
import enemy
import tower
import images
import projectile
import math
from board import *
from HUD import *
"""
TODO LIST:

- Implement a debug mode DONE 01-Dec-17
- Implement a start screen (nothing fancy yet necessarily, but something functional) DONE 01-Dec-17
- Implement a dying screen
- Find a new font (Check google fonts) DONE 01-Dec-17
- Branding work: Logo and other shit
- Towers that shoot/ different ideas/ power up towers (beacons)
- GUI rework
- Actual pathfinding algorithms
- Upgrade systems
- Wave systems
"""

pygame.init()
pygame.font.init()

# Game Dimensions
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 704

# initialisation of components
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Fire & Shadow')
clock = pygame.time.Clock()

player_dead = False
start_screen = True
debug_mode = False
quitting_bool = False

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
player = baseCharacter.Wizard(player_x, player_y, 20, 100, 100, 100, 100, 0, [])
prevDir = constants.RIGHT
max_health = player.health

frame = 0
seconds = 0

score = 0


basicfont = pygame.font.SysFont(None, 22)

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)


def handle_key():
	global dx, prevDir, dy, light_map, debug_mode
	currGold = player.getGold()
	if event.type == pygame.KEYDOWN:

		if event.key == pygame.K_a:
			dx = -constants.CHAR_SPEED
			player.flipScript("a")
			prevDir = constants.LEFT
		elif event.key == pygame.K_d:
			dx = constants.CHAR_SPEED
			player.flipScript("d")
			prevDir = constants.RIGHT
		if event.key == pygame.K_w:
			dy = -constants.CHAR_SPEED
			player.flipScript("w")
		elif event.key == pygame.K_s:
			dy = constants.CHAR_SPEED
			player.flipScript("s")

		if event.key == pygame.K_SPACE:
			projectiles.append(player.attack())

		if event.key == pygame.K_t:
			if currGold >= 40:
				player.setGold(currGold-40)
				towers.append(tower.Trap(player_x, player_y))

		if event.key == pygame.K_e:
			if currGold >= 100:
				player.setGold(currGold - 100)
				lights.append((player_x, player_y))
				light_map = add_light(light_map, (player_x, player_y))

		if event.key == pygame.K_f:
			if currGold >= 250:
				player.setGold(currGold - 250)
				towers.append(tower.Freeze(player_x, player_y))

		if event.key == pygame.K_r:
			if currGold >= 250:
				player.setGold(currGold - 250)
				towers.append(tower.Turret(player_x, player_y))

		if event.key == pygame.K_p:
			print("P pressed")
			if debug_mode == False:
				
				debug_mode = True
			

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_a or event.key == pygame.K_d:
			dx = 0
		elif event.key == pygame.K_w or event.key == pygame.K_s:
			dy = 0

		if event.key == pygame.K_SPACE:
			player.attack_flip(prevDir)


def debug_mode_script():
	if debug_mode == True:
		player.setGold(99999)
		for badguy in enemies:
			badguy.setDamage(0)
		# print("FPS: ", clock.get_fps)
	

def update_player_location():
	global player_x, player_y
	player_x += dx
	player_y += dy

	if player_x >= DISPLAY_WIDTH-constants.TILE_SIZE:
		player_x = DISPLAY_WIDTH- constants.TILE_SIZE
	if player_x <= 0:
		player_x = 0
	if player_y >= DISPLAY_HEIGHT-constants.TILE_SIZE:
		player_y = DISPLAY_HEIGHT- constants.TILE_SIZE
	if player_y <= 0:
		player_y = 0

	player.setX(player_x)
	player.setY(player_y)


# Start screen loop
while start_screen:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			start_screen = False
	game_display.blit(images.title_screen,(0,0))
	pygame.display.update()

# Main game loop
while not player_dead:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			player_dead = True
		handle_key()

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
		if abs(badguy.x - player.x) < 20 and abs(badguy.y - player.y) < 20:
			player.health -= badguy.damage

	fx = []
	for item in towers:
		if item.cooldown <= 0:
			if isinstance(item, tower.Trap):
				item.sprite = images.trap
				for badguy in enemies:
					if abs(badguy.x - item.x) < 20 and abs(badguy.y - item.y) < 20:
						enemies.remove(badguy)
						item.sprite = images.trap_disabled
						item.cooldown = 48
			elif isinstance(item, tower.Freeze):
				for badguy in enemies:
					if abs(badguy.x - item.x) < 64 and abs(badguy.y - item.y) < 64:
						if badguy.speed != 0:
							fx.append((item.x - 48, item.y - 48))
							badguy.speed = 0
							item.cooldown = 24
							break
			elif isinstance(item, tower.Turret):
				for badguy in enemies:
					if abs(badguy.x - item.x) < 92 and abs(badguy.y - item.y) < 92:
						if badguy.speed != 0:
							item.cooldown = 6
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

while quitting_bool:

	
	draw_board(DISPLAY_WIDTH, DISPLAY_HEIGHT, game_display, player, enemies, projectiles, towers, lights, light_map, fx, debug_mode)
	draw_hud(game_display, basicfont, DISPLAY_HEIGHT, player.getGold(), player.getHealth(), score, frame, seconds, debug_mode)
	game_display.blit(images.death_overlay,(0,0))
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				quitting_bool = False


print(score)
pygame.quit()
quit()
