import pygame
import constants
import enemy
import random


def init_new_wave(curr_wave):
	num_fast_per_wave = 2
	num_big_per_wave = 2  # THESE ARE TEMPORARY NUMBERS, WE CAN COME UP WITH A GOOD AMOUNT AND SCALING LATER, AS WELL AS AN ASSIGNMENT

	enem = []
	level = curr_wave.getLevel() + 1

	for n in range(int(curr_wave.getNumEnemies() * constants.WAVE_SCALING)):
		location = random_spawn_location(constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT)
		if n == 0 or n == 1:
			enem.append(enemy.SpeedZombie(location[0], location[1]))
		elif n == 2 or n == 3:
			enem.append(enemy.StrongZombie(location[0], location[1]))
		else:
			enem.append(enemy.Zombie(location[0], location[1]))

	for badguy in enem:
		badguy.setDamage(badguy.getDamage() * level / 3)

	return Wave(level, enem)


def random_spawn_location(width, height):
	y = 0
	x = 0
	edge = random.randint(0, 4)
	if edge == 1:
		x = random.randint(0, width)
	elif edge == 2:
		x = random.randint(0, width)
		y = height
	elif edge == 3:
		y = random.randint(0, height)
	else:
		y = random.randint(0, height)
		x = width
	return x, y


class Wave(object):
	"""
	This class defines a "wave" of enemies - a certain amount of enemies appearing at a time.

	Attributes:

	- level: the 'wave number', or the level of the wave. self explanatory. (int)
	- total_length: Keeps track of the original number of enemies. (int)
	- enemies: A list of the active enemies in the wave, yet to be spawned.
	- gap: The time between the waves/cooldown of each wave (float, seconds)
	- damage_multiplier: Work in progress. A number which the damage of the last wave is multiplied by to get this one. (float)
	"""

	def __init__(self, level, enemies):

		self.level = level
		self.total_length = len(enemies)
		self.enemies = enemies
		self.gap = constants.WAVE_GAP
		self.damage_multiplier = level/3 #temporary, can fiddle with this one

	def getLevel(self):
		return self.level

	def setLevel(self, val):
		self.level = val

	def getEnemies(self):
		return self.enemies

	def getNumEnemies(self):
		return self.total_length

	def setEnemies(self, val):
		self.enemies = val

	def getDamageMult(self):
		return self.damage_multiplier

	def getGap(self):
		return self.gap

	def setGap(self, val):
		self.gap = val
