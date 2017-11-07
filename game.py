import pygame
import baseCharacter
from board import *
pygame.init()

# Game Dimensions
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 704

# initialisation of components
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Fire and Shadow')
clock = pygame.time.Clock()

player_dead = False

projectiles_array = []

# movement related mechanics
player_x = DISPLAY_WIDTH/2
player_y = DISPLAY_HEIGHT/2

dx = 0
dy = 0

# Making player
player = baseCharacter.Wizard(player_x, player_y, 100, 100, 100, 100, 100, 100, 100)

while not player_dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_dead = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                dx = -constants.CHAR_SPEED
                player.flipScript("a")
            elif event.key == pygame.K_d:
                dx = constants.CHAR_SPEED
                player.flipScript("d")
            if event.key == pygame.K_w:
                dy = -constants.CHAR_SPEED
                player.flipScript("w")
            elif event.key == pygame.K_s:
                dy = constants.CHAR_SPEED
                player.flipScript("s")

            if event.key == pygame.K_SPACE:
                #Change image to attack image, fire shot, both based on direction
                #this function will return a projectile
                projectiles_array.append(player.attack())
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                dx = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                dy = 0

    player_x += dx
    player_y += dy	
    if player_x >= DISPLAY_WIDTH - constants.TILE_SIZE:
        player_x = DISPLAY_WIDTH - 2 * constants.TILE_SIZE
    if player_x <= -2 * constants.TILE_SIZE:
        player_x = -1 * constants.TILE_SIZE
    if player_y >= DISPLAY_HEIGHT + constants.TILE_SIZE:
        player_y = DISPLAY_HEIGHT
    if player_y <= constants.TILE_SIZE:
        player_y = constants.TILE_SIZE

    player.setX(player_x)
    player.setY(player_y)

    place_tiles(DISPLAY_WIDTH, DISPLAY_HEIGHT, game_display, pygame)
    place_object(player_x, player_y, DISPLAY_WIDTH, DISPLAY_HEIGHT, game_display, player)

    pygame.display.update()
    clock.tick(24)

pygame.quit()
quit()
