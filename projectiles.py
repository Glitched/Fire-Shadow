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

		super().__init__(images.wizard_shot, constants.WIZARD_SHOT_SPEED, constants.WIZARD_SHOT_DAMAGE, x, y, dirn)

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

	def update(self, game_display):
		
		# TODO: Get sprites for different directions and use them to update
		dirn = self.getDirn()
		if dirn == constants.LEFT:
			self.x -= self.speed
			self.sprite = images.wizard_shot_left
		if dirn == constants.RIGHT:
			self.x += self.speed
			self.sprite = images.wizard_shot
		if dirn == constants.UP:
			self.y -= self.speed
			self.sprite = images.wizard_shot_up
		if dirn == constants.DOWN:
			self.y += self.speed
			self.sprite = images.wizard_shot_down
		game_display.blit(self.sprite, (self.getX(),self.getY()))
		pygame.display.flip()

