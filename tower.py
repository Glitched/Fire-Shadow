import images


class Tower(object):

	def __init__(self, sprite, x, y):

		self.sprite = sprite
		self.cooldown = 0

		self.x = x
		self.y = y


class Trap(Tower):

	def __init__(self, x, y):
		super().__init__(images.trap, x, y)


class Freeze(Tower):

	def __init__(self, x, y):
		super().__init__(images.freeze, x, y)


class Turret(Tower):

	def __init__(self, x, y):
		super().__init__(images.turret, x, y)