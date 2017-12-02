import images


class Tower(object):

	def __init__(self, sprite, x, y):

		self.sprite = sprite
		self.x = x
		self.y = y


class Trap(Tower):

	def __init__(self, x, y):
		self.cooldown = 0
		super().__init__(images.trap, x, y)


class Freeze(Tower):

	def __init__(self, x, y):
		self.cooldown = 0
		super().__init__(images.freeze, x, y)