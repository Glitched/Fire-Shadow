import pygame
import constants

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
