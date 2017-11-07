import pygame

class Character(object):

    def __init__(self, x, y, maxHealth, speed, atk, defence, rng):
        self.x = x
        self.y = y
        self.health = maxHealth

    def getX():
        return self.x

    def setX(arg):
        self.x = arg

    def getY():
        return self.y

    def setY(arg):
        self.y = arg

    def setHealth(arg):
        self.health = arg

    def getHealth():
        return self.health

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
        wiz_img = pygame.image.load('images/wizard.png')
        self.sprite = wiz_img

    #def update(self):




