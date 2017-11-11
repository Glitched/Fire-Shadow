import images
import random


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


class Enemy(object):

	def __init__(self, sprite, speed, damage, health, x, y):

		self.sprite = sprite
		self.speed = speed
		self.damage = damage
		self.health = health
		self.x = x
		self.y = y

	def update(self, playerX, playerY):
		for i in range(0, self.speed):
			if playerX > self.x:
				self.x += 1
			elif playerX < self.x:
				self.x -= 1

			if playerY > self.y:
				self.y += 1
			elif playerY < self.y:
				self.y -= 1


class Zombie(Enemy):

	def __init__(self, x, y):
		super().__init__(images.zombie, 2, 1, 5, x, y)
