import pygame

class Projectile(object):

	def __init__(self, sprite, speed, damage):

		self.sprite = sprite
		self.speed = speed
		self.damage = damage