import pygame

FLICKER_I = 1
TILE_SIZE = 32
CHAR_SPEED = 6

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

WIZARD_SHOT_SPEED = 16
WIZARD_SHOT_DAMAGE = 2

# Player Constants
WIZARD_BASE_HEALTH = 100
PLAYER_HEALTH_INCREMENT = 0.06

# Wave constants
BASE_WAVE_AMOUNT = 10
WAVE_GAP = 1  # This number is in seconds
WAVE_SCALING = 1.5

# Enemy constants
ZOMBIE_SPEED = 3
ZOMBIE_DAMAGE = 1
ZOMBIE_HEALTH = 5
ZOMBIE_VALUE = 5

STRONG_ZOMBIE_SPEED = 2
STRONG_ZOMBIE_DAMAGE = 3
STRONG_ZOMBIE_HEALTH = 12
STRONG_ZOMBIE_VALUE = 10

SPEED_ZOMBIE_SPEED = 5
SPEED_ZOMBIE_DAMAGE = 1
SPEED_ZOMBIE_HEALTH = 5
SPEED_ZOMBIE_VALUE = 10

# Game Dimensions
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 704

# Tower Prices
PRICE = {
	"trap": 40,
	"trap2": 60,
	"campfire": 100,
	"freeze": 150,
	"freeze2": 100,
	"freeze3": 150,
	"turret": 250,
	"turret2": 150,
	"turret3": 200,
	"attack": 400,
	"speed": 400,
	"intelligence": 600,
}

# Build HUD
FONT_HEADER = pygame.font.Font('ArsleGothic.ttf', 32)
FONT_ITEM = pygame.font.Font('ArsleGothic.ttf', 18)
ITEM_COLOR = (255, 188, 144)
BUILD_PAD_LEFT = 120