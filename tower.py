import images
import projectile
import math


def process_towers(instance):
	fx = []
	for item in instance.towers:
		if item.cooldown <= 0:
			fx = process_tower(fx, instance, item)
		else:
			item.cooldown -= 1
	return fx


def process_tower(fx, instance, item):
	if isinstance(item, Trap):
		item.sprite = images.trap
		for badguy in instance.enemies:
			if abs(badguy.x - item.x) < 20 and abs(badguy.y - item.y) < 20:
				instance.enemies.remove(badguy)
				item.sprite = images.trap_disabled
				item.cooldown = item.max_cooldown
				break
	elif isinstance(item, Freeze):
		item.cooldown = item.max_cooldown
		for badguy in instance.enemies:
			if abs(badguy.x - item.x) < 64 and abs(badguy.y - item.y) < 64 and badguy.speed != 0:
				fx.append((item.x - 48, item.y - 48))
				badguy.speed = 1
	elif isinstance(item, Turret):
		item.cooldown = item.max_cooldown
		for badguy in instance.enemies:
			if abs(badguy.x - item.x) < 92 and abs(badguy.y - item.y) < 92:
				proj = projectile.TurretShot(
					item.x, item.y,
					math.atan((badguy.y - item.y) / (0.0001 + badguy.x - item.x)),
					(item.y < badguy.y), (item.x < badguy.x)
				)
				instance.projectiles.append(proj)
				break
	return fx

class Tower(object):

	def __init__(self, sprite, x, y, price, max_cooldown):

		self.sprite = sprite
		self.cooldown = 0
		self.max_cooldown = max_cooldown

		self.x = x
		self.y = y
		self.price = price


class Trap(Tower):
	def __init__(self, x, y, cooldown):
		super().__init__(images.trap, x, y, 40, cooldown)


class Trap1(Trap):
	def __init__(self, x, y):
		super().__init__(x, y, 48)


class Trap2(Trap):
	def __init__(self, x, y):
		super().__init__(x, y, 24)


class Freeze(Tower):
	def __init__(self, x, y):
		super().__init__(images.freeze, x, y, 200, 24)


class Turret(Tower):
	def __init__(self, x, y):
		super().__init__(images.turret, x, y, 250, 4)
