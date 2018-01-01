import constants


class Game(object):

    def __init__(self):
        self.projectiles = []
        self.enemies = []
        self.towers = []
        self.lights = [(constants.DISPLAY_WIDTH / 2, constants.DISPLAY_HEIGHT / 2)]
        self.light_map = None

        self.frame = 0
        self.seconds = 0

        self.score = 0

        self.debug_mode = False
        self.build_mode = False

        self.current_tower = None

        self.current_wave = None

    def tick(self):
        self.frame += 1
        if self.frame >= 24:
            self.seconds += 1
            self.frame = 0
