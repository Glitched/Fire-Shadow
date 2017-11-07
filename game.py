import pygame
import random
import animation
import baseCharacter
import constants

pygame.init()

#Game Dimensions
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 704

#initialisation of components
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

player_dead = False

#Loading image files
wizard_image = pygame.image.load('images/wizard.png')
tile_image = pygame.image.load('images/tile.png')
campfire_image = pygame.image.load('images/campfire.png')
campfire_image_2 = pygame.image.load('images/campfire2.png')

def place_object(x, y):
    """
    This function places objects (to be called in the loop)
    """
    #Insert the character image
    game_display.blit(player.sprite, (x+constants.TILE_SIZE, y-constants.TILE_SIZE))

    #campfire image
    game_display.blit(animation.campfire_flicker(constants.FLICKER_I), (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2))
    constants.FLICKER_I += 1
    if constants.FLICKER_I == 20:
        constants.FLICKER_I = 1

def generate_grid():
    newList = []
    for x in range(0, DISPLAY_WIDTH, constants.TILE_SIZE):
        for y in range(0, DISPLAY_HEIGHT, constants.TILE_SIZE):
            newList.append((x, y))
    return newList

def place_tiles():
    cordList = generate_grid()
    flicker = random.randint(0, 15)
    if flicker != 1:
        flicker = 0
    for tup in cordList:
        game_display.blit(tile_image, tup)
        # Darken
        s = pygame.Surface((32, 32))
        s.set_alpha(((DISPLAY_WIDTH/2 - tup[0]) ** 2 + (DISPLAY_HEIGHT/2 - tup[1]) ** 2 ) ** 0.5 * (0.9 + 0.15 * flicker))
        game_display.blit(s, tup) 

#movement related mechanics
player_x = DISPLAY_WIDTH/2
player_y = DISPLAY_HEIGHT/2

dx = 0
dy = 0

#Making player
player = baseCharacter.Wizard(player_x, player_y, 100, 100, 100, 100, 100, 100, 100)

while not player_dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_dead = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                dx = -constants.CHAR_SPEED
                player.flipScript()
            elif event.key == pygame.K_d:
                dx = constants.CHAR_SPEED
                player.flipScript()
            if event.key == pygame.K_w:
                dy = -constants.CHAR_SPEED
                player.flipScript()
            elif event.key == pygame.K_s:
                dy = constants.CHAR_SPEED
                player.flipScript()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                dx=0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                dy=0

    player_x += dx
    player_y += dy	
    if(player_x >= DISPLAY_WIDTH-constants.TILE_SIZE):
        player_x = DISPLAY_WIDTH-2*constants.TILE_SIZE
    if(player_x <= -2*constants.TILE_SIZE):
        player_x = -1*constants.TILE_SIZE
    if(player_y >= DISPLAY_HEIGHT+constants.TILE_SIZE):
        player_y= DISPLAY_HEIGHT
    if(player_y <= constants.TILE_SIZE):
        player_y = constants.TILE_SIZE

    place_tiles()
    place_object(player_x, player_y)

    pygame.display.update()
    clock.tick(25)

pygame.quit()
quit()
