import pygame
import images
import constants


class Projectile(object):

	def __init__(self, sprite, speed, damage, x, y, dirn):

		self.sprite = sprite
		self.speed = speed
		self.damage = damage
		self.x = x
		self.y = y
		self.dirn = dirn


class WizardShot(Projectile):

	def __init__(self, x, y, dirn):

		sprite = images.wizard_shot
		if dirn == constants.LEFT:
			sprite = images.wizard_shot_left
		elif dirn == constants.UP:
			sprite = images.wizard_shot_up
		elif dirn == constants.DOWN:
			sprite = images.wizard_shot_down

		super().__init__(sprite, constants.WIZARD_SHOT_SPEED, constants.WIZARD_SHOT_DAMAGE, x, y, dirn)

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

	def update(self):
		
		dirn = self.getDirn()
		if dirn == constants.LEFT:
			self.x -= self.speed
		if dirn == constants.RIGHT:
			self.x += self.speed
		if dirn == constants.UP:
			self.y -= self.speed
		if dirn == constants.DOWN:
			self.y += self.speed


class TurretShot(Projectile):
	def __init__(self, x, y):

		sprite = images.turret_shot

		super().__init__(sprite, 4, 1, x, y, None)

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

	def update(self):
