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


class WizardShot(Projectile):

	def __init__(self, sprite, speed, damage, x, y, dirn):

		super().__init__(self, images.wizard_shot, constants.WIZARD_SHOT_SPEED, constants.WIZARD_SHOT_DAMAGE, x, y, dirn)

	def getX(self):
		return self.x

	def setX(self, arg):
		self.x = arg

	def getY(self):
		return self.y

	def setY(self, arg):
		self.y = arg

	def getDirn(self):
		return self.dirn

	def setDirn(self, arg):
		self.dirn = arg

	def update(self, x, y, dirn):

		if dirn == constants.LEFT:
			self.x -= self.speed
		if dirn == constants.RIGHT:
			self.x += self.speed
		if dirn == constants.UP:
			self.y -= self.speed
		if dirn == constants.DOWN:
			self.y += self.speed

