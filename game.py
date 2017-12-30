import constants


class Game(object):

    def __init__(self):
        self.projectiles = []
        self.enemies = []
        self.towers = []
        self.lights = [(constants.DISPLAY_WIDTH / 2, constants.DISPLAY_HEIGHT / 2)]
        self.score = 0
