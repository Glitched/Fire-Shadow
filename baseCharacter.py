import pygame
import images
import projectile
import constants


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
            if self.getFacing() != constants.LEFT:
                self.setFacing(constants.LEFT)
                self.sprite = images.wizard_left
        if key == 'd':
            if self.getFacing() != constants.RIGHT:
                self.setFacing(constants.RIGHT)
                self.sprite = images.wizard
        if key == 'w':        
            if self.getFacing() != constants.UP:
                self.setFacing(constants.UP)
        if key == 's':
            if self.getFacing() != constants.DOWN:
                self.setFacing(constants.DOWN)

    def attack_flip(self, prevDir):

        if self.getFacing() == constants.LEFT:
            self.sprite = images.wizard_left
        elif self.getFacing() == constants.RIGHT:
            self.sprite = images.wizard
        elif self.getFacing() == constants.UP:
            if prevDir == constants.LEFT:
                self.sprite = images.wizard_left
            elif prevDir == constants.RIGHT:
                self.sprite = images.wizard
        elif self.getFacing() == constants.DOWN:
            if prevDir == constants.LEFT:
                self.sprite = images.wizard_left
            elif prevDir == constants.RIGHT:
                self.sprite = images.wizard


    

    # TODO: Implement getters and setters for the rest of these functions

class PlayerCharacter(Character):

    def __init__(self,x,y,maxHealth,speed,atk,defence,rng,gold,purchases):
        super().__init__(x,y,maxHealth,speed,atk,defence,rng)
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

    def __init__(self, x, y, maxHealth, speed, atk, defence, rng, gold, purchases):
        super().__init__(x, y, maxHealth, speed, atk, defence, rng, gold, purchases) 
        self.sprite = images.wizard

    def attack(self):
        x = self.getX()
        y = self.getY()
        dirn = self.getFacing()
        new_proj = projectile.WizardShot(x, y, dirn)

        if dirn == constants.LEFT:
            self.sprite = images.wizard_attack_left
        elif dirn == constants.RIGHT:
            self.sprite = images.wizard_attack_right
        elif dirn == constants.UP:
            self.sprite = images.wizard_attack_up
        elif dirn == constants.DOWN:
            self.sprite = images.wizard_attack_down

        return new_proj





