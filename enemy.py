import images
import constants
import wave


def spawn_enemies(instance):
	if len(instance.current_wave.getEnemies()) > 0:
		if instance.frame % 12 == 0:
			instance.enemies.append(instance.current_wave.getEnemies().pop())

	elif len(instance.current_wave.getEnemies()) <= 0 and len(instance.enemies) == 0:
		instance.current_wave.setGap(instance.current_wave.getGap() - (1 / 60))

		if instance.current_wave.getGap() <= 0:
			instance.current_wave = wave.init_new_wave(instance.current_wave)


def process_enemies(instance, player):
	for badguy in instance.enemies:
		badguy.update(player.x, player.y)
		if abs(badguy.x - player.x) < 20 and abs(badguy.y - player.y) < 20 and not instance.debug_mode:
			player.setHealth(player.getHealth() - badguy.damage)



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
