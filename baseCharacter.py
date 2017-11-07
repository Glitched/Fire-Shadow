import pygame
import images
import projectiles



class Character(object):

    def __init__(self, x, y, maxHealth, speed, atk, defence, rng):
        self.x = x
        self.y = y
        self.health = maxHealth
        self.facing = constants.RIGHT

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

    def flipScript(self, key):
        if key == 'a':
            if self.getFacing()!= constants.LEFT:
                self.setFacing(constants.LEFT)
                self.sprite= images.wizard_left
        if key == 'd':
            if self.getFacing()!= constants.RIGHT:
                self.setFacing(constants.RIGHT)
                self.sprite= images.wizard
        if key == 'w':        
            if self.getFacing()!= constants.UP:
                self.setFacing(constants.UP)
        if key == 's':
            if self.getFacing()!= constants.DOWN:
                self.setFacing(constants.DOWN)

    def attack(self):
        x = player.getX()
        y = player.getY()
        dirn = player.getFacing()


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




