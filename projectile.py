import pygame
import images
import math
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

	def __init__(self, x, y, dirn, atk):

		sprite = images.wizard_shot
		if dirn == constants.LEFT:
			sprite = images.wizard_shot_left
		elif dirn == constants.UP:
			sprite = images.wizard_shot_up
		elif dirn == constants.DOWN:
			sprite = images.wizard_shot_down

		super().__init__(sprite, constants.WIZARD_SHOT_SPEED, atk, x, y, dirn)

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
	def __init__(self, x, y, dirn, posy, posx):

		sprite = rot_center(images.turret_shot, -round(math.degrees(dirn)))
		self.dirn = dirn
		self.posy = posy
		self.posx = posx

		super().__init__(sprite, 16, 1, x, y, dirn)

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

	def update(self):
		if self.posx:
			self.x += self.speed * abs(math.cos(self.dirn))
		else:
			self.x -= self.speed * abs(math.cos(self.dirn))
		if self.posy:
			self.y += self.speed * abs(math.sin(self.dirn))
		else:
			self.y -= self.speed * abs(math.sin(self.dirn))


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image