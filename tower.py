import images
import projectile
import math


def process_towers(instance):
	fx = []
	for item in instance.towers:
		if item.cooldown <= 0:
			location = item.update(instance)
			if location is not None:
				fx.append(location)
		else:
			item.cooldown -= 1
	return fx


class Tower(object):

	def __init__(self, sprite, x, y, max_cooldown):

		self.sprite = sprite
		self.cooldown = 0
		self.max_cooldown = max_cooldown

		self.x = x
		self.y = y


class Trap(Tower):
	def __init__(self, x, y, cooldown):
		super().__init__(images.trap, x, y, cooldown)

	def update(self, instance):
		self.sprite = images.trap
		for badguy in instance.enemies:
			if abs(badguy.x - self.x) < 20 and abs(badguy.y - self.y) < 20:
				instance.enemies.remove(badguy)
				self.sprite = images.trap_disabled
				self.cooldown = self.max_cooldown
				break


class Trap1(Trap):
	def __init__(self, x, y):
		super().__init__(x, y, 48)
		self.name = "Trap (Level 1)"


class Trap2(Trap):
	def __init__(self, x, y):
		super().__init__(x, y, 24)
		self.name = "Trap (Level 2)"


class Freeze(Tower):
	def __init__(self, x, y, range):
		super().__init__(images.freeze, x, y, 24)
		self.range = range

	def update(self, instance):
		self.cooldown = self.max_cooldown
		fx = None
		for badguy in instance.enemies:
			if abs(badguy.x - self.x) < self.range and abs(badguy.y - self.y) < self.range and badguy.speed != 0:
				fx = (self.x - 48, self.y - 48)
				badguy.speed = 1
		return fx


class Freeze1(Freeze):
	def __init__(self, x, y):
		super().__init__(x, y, 64)
		self.name = "Freeze (Level 1)"


class Freeze2(Freeze):
	def __init__(self, x, y):
		super().__init__(x, y, 80)
		self.name = "Freeze (Level 2)"


class Freeze3(Freeze):
	def __init__(self, x, y):
		super().__init__(x, y, 92)
		self.name = "Freeze (Level 3)"


class Turret(Tower):
	def __init__(self, x, y, range, cooldown):
		self.range = range
		super().__init__(images.turret, x, y, cooldown)

	def update(self, instance):
		self.cooldown = self.max_cooldown
		for badguy in instance.enemies:
			if abs(badguy.x - self.x) < self.range and abs(badguy.y - self.y) < self.range:
				proj = projectile.TurretShot(
					self.x, self.y,
					math.atan((badguy.y - self.y) / (0.0001 + badguy.x - self.x)),
					(self.y < badguy.y), (self.x < badguy.x)
				)
				instance.projectiles.append(proj)
				break


class Turret1(Turret):
	def __init__(self, x, y):
		super().__init__(x, y, 92, 6)
		self.name = "Turret (Level 1)"


class Turret2(Turret):
	def __init__(self, x, y):
		super().__init__(x, y, 98, 4)
		self.name = "Turret (Level 2)"


class Turret3(Turret):
	def __init__(self, x, y):
		super().__init__(x, y, 108, 3)
		self.name = "Turret (Level 3)"
