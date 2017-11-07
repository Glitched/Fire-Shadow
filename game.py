import pygame
import random
import animation
import baseCharacter

pygame.init()

#Game Dimensions
display_width= 1280
display_height= 704

#Colours
black= (0,0,0)
white= (255,255,255)
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)

#Game constants
FLICKER_I= 1
TILE_SIZE= 32
CHAR_SPEED= 6

#initialisation of components

game_display= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bitch ass')
clock= pygame.time.Clock()

player_dead= False

#Loading image files
wizard_image= pygame.image.load('images/wizard.png')
tile_image= pygame.image.load('images/tile.png')
campfire_image= pygame.image.load('images/campfire.png')
campfire_image_2= pygame.image.load('images/campfire2.png')

def place_object(x,y):
	"""
	This function places objects (to be called in the loop)
	"""
	#Insert the character image
	global FLICKER_I

	game_display.blit(player.sprite,(x+TILE_SIZE,y-TILE_SIZE))

	#campfire image
	game_display.blit(animation.campfire_flicker(FLICKER_I), (display_width/2,display_height/2))
	FLICKER_I+= 1
	if(FLICKER_I== 20):
		FLICKER_I= 1
	

def generate_grid():
	newList= []
	for x in range(0,display_width,TILE_SIZE):
		for y in range(0,display_height,TILE_SIZE):
			newList.append((x,y))
	return newList

def place_tiles():
	cordList= generate_grid()
	flicker = random.randint(0,15)
	if flicker != 1:
		flicker = 0
	for tup in cordList:
		game_display.blit(tile_image,tup)
		# Darken
		s = pygame.Surface((32,32))
		s.set_alpha(((display_width/2 - tup[0]) ** 2 + (display_height/2 - tup[1]) ** 2 ) ** 0.5 * (0.9 + 0.15 * flicker))
		game_display.blit(s, tup) 

#movement related mechanics
player_x= display_width/2
player_y= display_height/2

dx=0
dy=0

#Making player
player= baseCharacter.Wizard(player_x,player_y,100,100,100,100,100,100,100)

while not player_dead:

	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			player_dead= True

		if event.type== pygame.KEYDOWN:
			
			if event.key== pygame.K_a:
				dx= -CHAR_SPEED
			elif event.key== pygame.K_d:
				dx= CHAR_SPEED
			if event.key== pygame.K_w:
				dy= -CHAR_SPEED
			elif event.key== pygame.K_s:
				dy= CHAR_SPEED

		if event.type== pygame.KEYUP:
			if event.key== pygame.K_a or event.key== pygame.K_d:
				dx=0
			elif event.key== pygame.K_w or event.key== pygame.K_s:
				dy=0

	player_x+= dx
	player_y+= dy	
	if(player_x>=display_width-TILE_SIZE):
		player_x= display_width-2*TILE_SIZE
	if(player_x<= -2*TILE_SIZE):
		player_x= -1*TILE_SIZE
	if(player_y>=display_height+TILE_SIZE):
		player_y= display_height
	if(player_y<= TILE_SIZE):
		player_y= TILE_SIZE

	place_tiles()
	place_object(player_x,player_y)

	pygame.display.update()
	clock.tick(25)

pygame.quit()
quit()