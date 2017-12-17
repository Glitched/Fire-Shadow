import images


class Tower(object):

	def __init__(self, sprite, x, y, price, max_cooldown):

		self.sprite = sprite
		self.cooldown = 0
		self.max_cooldown = max_cooldown

		self.x = x
		self.y = y
		self.price = price


class Trap(Tower):

	def __init__(self, x, y):
		super().__init__(images.trap, x, y, 40, 48)


class Trap2(Tower):

	def __init__(self, x, y):
		super().__init__(images.trap, x, y, 40, 24)


class Freeze(Tower):

	def __init__(self, x, y):
		super().__init__(images.freeze, x, y, 200, 24)


class Turret(Tower):

	def __init__(self, x, y):
		super().__init__(images.turret, x, y, 250, 4)
