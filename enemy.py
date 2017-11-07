import images


class Enemy(object):

	def __init__(self, sprite, speed, damage, x, y):

		self.sprite = sprite
		self.speed = speed
		self.damage = damage
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
		super().__init__(images.zombie, 1, 2, x, y)
