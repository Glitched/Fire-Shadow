import pygame
import images
import constants
import game

class Projectile(object):

	def __init__(self, sprite, speed, damage, x, y, dirn):

		self.sprite = sprite
		self.speed = speed
		self.damage = damage
		self.x = x
		self.y = y
		self.dirn = dirn

	def update(self, x, y, dirn):

		pass


class WizardShot(Projectile):

	def __init__(self, sprite, speed, damage, x, y, dirn):

		super().__init__(self, images.wizard_shot, constants.WIZARD_SHOT_SPEED, constants.WIZARD_SHOT_DAMAGE, x, y, dirn)

	def update(self, x, y, dirn):

		if self.x >= game.DISPLAY_WIDTH:
			