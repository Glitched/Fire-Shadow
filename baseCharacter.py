import pygame
import images

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

class Character(object):

    def __init__(self, x, y, maxHealth, speed, atk, defence, rng):
        self.x = x
        self.y = y
        self.health = maxHealth
        self.facing = RIGHT

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

    def flipScript(self):
        if self.getFacing()!= LEFT:
                self.setFacing(LEFT)
                self.sprite= images.wizard_left
        if self.getFacing()!= RIGHT:
                self.setFacing(RIGHT)
                self.sprite= images.wizard
        if self.getFacing()!= UP:
                self.setFacing(UP)
        if self.getFacing()!= DOWN:
                self.setFacing(DOWN)

    # TODO: Implement getters and setters for the rest of these functions

class PlayerCharacter(Character):

    def __init__(self,x,y,maxHealth,speed,atk,defence,rng,gold,purchases):
        super().__init__(x,y,maxHealth,speed,atk,defence,rng)
        self.gold = gold
        self.purchases = purchases

    #TODO: Implement getters and setters for gold(int) and purchases (list)

class Wizard(PlayerCharacter):

    def __init__(self, x, y, maxHealth, speed, atk, defence, rng, gold, purchases):
        super().__init__(x, y, maxHealth, speed, atk, defence, rng, gold, purchases) 
        self.sprite = images.wizard

    #def update(self):




