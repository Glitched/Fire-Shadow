import pygame
import images
import projectile
import constants
import sounds


class Character(object):

    def __init__(self, x, y, max_health, speed, atk, defence, rng):
        self.x = x
        self.y = y
        self.health = max_health
        self.max_health = max_health
        self.prevDir = constants.RIGHT
        self.facing = constants.RIGHT
        self.atk = atk
        self.speed = speed
        self.speed_upgrades = 0
        self.dx = 0
        self.dy = 0


    def getX(self):
        return self.x

    def setX(self, arg):
        self.x = arg

    def getY(self):
        return self.y

    def setY(self, arg):
        self.y = arg

    def setHealth(self, arg):
        self.health = arg

    def getHealth(self):
        return self.health

    def getFacing(self):
        return self.facing

    def setFacing(self, arg):
        self.facing = arg

    def attack_flip(self):
        if self.getFacing() == constants.LEFT:
            self.sprite = images.wizard_left
        elif self.getFacing() == constants.RIGHT:
            self.sprite = images.wizard
        elif self.getFacing() == constants.UP:
            if self.prevDir == constants.LEFT:
                self.sprite = images.wizard_left
            elif self.prevDir == constants.RIGHT:
                self.sprite = images.wizard
        elif self.getFacing() == constants.DOWN:
            if self.prevDir == constants.LEFT:
                self.sprite = images.wizard_left
            elif self.prevDir == constants.RIGHT:
                self.sprite = images.wizard

    def set_momentum(self, key):
        if key == pygame.K_a:
            self.dx = -self.speed
            self.prevDir = constants.LEFT
        elif key == pygame.K_d:
            self.dx = self.speed
            self.prevDir = constants.RIGHT
        if key == pygame.K_w:
            self.dy = -self.speed
        elif key == pygame.K_s:
            self.dy = self.speed
        self.flip_facing_direction(key)

    def flip_facing_direction(self, key):
        if key == pygame.K_a:
            if self.getFacing() != constants.LEFT:
                self.setFacing(constants.LEFT)
                self.sprite = images.wizard_left
        if key == pygame.K_d:
            if self.getFacing() != constants.RIGHT:
                self.setFacing(constants.RIGHT)
                self.sprite = images.wizard
        if key == pygame.K_w:
            if self.getFacing() != constants.UP:
                self.setFacing(constants.UP)
        if key == pygame.K_s:
            if self.getFacing() != constants.DOWN:
                self.setFacing(constants.DOWN)

    def move(self):
        self.x = max(0, min(self.x + self.dx, constants.DISPLAY_WIDTH - constants.TILE_SIZE))
        self.y = max(0, min(self.y + self.dy, constants.DISPLAY_HEIGHT - constants.TILE_SIZE))


        # TODO: Implement getters and setters for the rest of these functions


class PlayerCharacter(Character):

    def __init__(self, x, y, max_health, speed, atk, defence, rng, gold, purchases):
        super().__init__(x, y, max_health, speed, atk, defence, rng)
        self.gold = gold
        self.purchases = purchases

    def getGold(self):
        return self.gold

    def setGold(self, arg):
        self.gold = arg

    def getPurchases(self):
        return self.purchases

    def addToPurchases(self, arg):
        self.purchases.append(arg)


class Wizard(PlayerCharacter):

    def __init__(self, x, y, max_health, speed, atk, defence, rng, gold, purchases):
        super().__init__(x, y, max_health, speed, atk, defence, rng, gold, purchases)
        self.sprite = images.wizard

    def attack(self):
        sounds.attack.play()
        x = self.getX()
        y = self.getY()
        dirn = self.getFacing()
        new_proj = projectile.WizardShot(x, y, dirn, self.atk)

        if dirn == constants.LEFT:
            self.sprite = images.wizard_attack_left
        elif dirn == constants.RIGHT:
            self.sprite = images.wizard_attack_right
        elif dirn == constants.UP:
            self.sprite = images.wizard_attack_up
        elif dirn == constants.DOWN:
            self.sprite = images.wizard_attack_down

        return new_proj





