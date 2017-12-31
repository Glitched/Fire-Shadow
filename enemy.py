import images
import random
import constants


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

	def __init__(self, sprite, speed, damage, health, x, y, value):

		self.sprite = sprite
		self.speed = speed
		self.damage = damage
		self.health = health
		self.x = x
		self.y = y
		self.value = value

	def setHealth(self, arg):
		self.health = arg

	def getHealth(self):
		return self.health

	def setDamage(self, arg):
		self.damage = arg

	def getDamage(self):
		return self.damage

	def getValue(self):
		return self.value

	def setValue(self, val):
		self.value = val

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
		super().__init__(images.zombie, constants.ZOMBIE_SPEED, constants.ZOMBIE_DAMAGE, constants.ZOMBIE_HEALTH,
		x, y, constants.ZOMBIE_VALUE)


class StrongZombie(Enemy):

	def __init__(self, x, y):
		super().__init__(images.zombie_strong, constants.STRONG_ZOMBIE_SPEED, constants.STRONG_ZOMBIE_DAMAGE, constants.STRONG_ZOMBIE_HEALTH,
		x, y, constants.STRONG_ZOMBIE_VALUE)


class SpeedZombie(Enemy):

	def __init__(self, x, y):
		super().__init__(images.zombie_speed, constants.SPEED_ZOMBIE_SPEED, constants.SPEED_ZOMBIE_DAMAGE, constants.SPEED_ZOMBIE_HEALTH, 
		x, y, constants.SPEED_ZOMBIE_VALUE)
