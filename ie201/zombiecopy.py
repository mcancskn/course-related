from pickle import NONE
import pygame
from pygame import image
from pygame.locals import *
import random


class Zombies:   #Zombie class generalizes the three types of zombies. It contains a method which sends zombies randomly.
    def __init__(self, ):
        # Var
        self._hp = None
        # Sprite
        self._activesprite = None
        self._eatingsprites = []
        self._walkingsprites = []
        self._currentsprite = None
        self._lastsprite = None
        self._lastmove = None
        self._gif = self._sprites[self._currentsprite]
        self._zrect = self._gif.get_rect()
        self._zrect.top, self._zrect.left = None, None
        self._lane = None
        self._key = None
        self._eat = False
        self._Damage = None
        self._lasteat = None
        self._temp = None
        # Slow
        self._slowed = None
        self._lastslow = None
        self._slowrate = None

    def start(self):
        self._lane = random.randint(0,4)
        if self._lane == 0:
            self._zrect.top = 80
        elif self._lane == 1:
            self._zrect.top = 179
        elif self._lane == 2:
            self._zrect.top = 279
        elif self._lane == 3:
            self._zrect.top = 376
        elif self._lane == 4:
            self._zrect.top = 475
        
    def sprite_initialization(self):
        pass

    def update_sprite(self, current):
        if self._currentsprite <= 10:
            if self._key == "Quick_Zombie":
                if self._eat: 
                    self._temp = 21 
                    self._activesprite = self._eatingsprites
                else: 
                    self._temp = 22
                    self._activesprite = self._walkingsprites

            if self._key == "Weak_Zombie":
                if self._eat: 
                    self._temp = 11
                    self._activesprite = self._eatingsprites
                else:
                    self._temp = 21
                    self._activesprite = self._walkingsprites
            
            if self._key == "Strong_Zombie":
                if self._eat:
                    self._temp = 11
                    self._activesprite = self._eatingsprites
                else:
                    self._temp = 15
                    self._activesprite = self._walkingsprites

        if current - self._lastsprite >= (1000/60)*6:
            self._currentsprite += 1
            self._lastsprite = current
            if self._currentsprite % self._temp == 0:
                self._currentsprite = 0
            self._gif = self._activesprite[self._currentsprite]


    def return_zrect(self):
        return self._zrect

    def update_hp(self, n):
        self._hp -= n

    def return_hp(self):
        return self._hp
    
    def return_zlane(self):
        return self._lane

    def return_damage(self):
        return self._Damage

    def return_lastslow(self):
        return self._lastslow

    def is_slowed(self):
        return self._slowed

    def check_slow(self, current):
        if self._slowed:
            if current - self._lastslow > (1000/60) * 100:
                self._slowed = False
                self.fast(self._slowrate)

            
    def setslowrate(self, bslowrate):
        self._slowrate = bslowrate

    
    def eat(self, current):
        if current - self._lasteat >= (1000/60) * 50:
            self._lasteat = current
            return True
        else:
            return False

    def set_eating(self, bool):
        self._eat = bool

    def slow(self, slowrate, current):
        self._lastslow = current
        self._slowed = True
        self._slowrate /= slowrate

    def fast(self, slowrate):
        self._slowed = True
        self._slowrate *= slowrate
    
    # Render
    def render_zombie(self, screen, image, rect):
        screen.blit(image, rect)

    def return_zombieinstance(self):
        return self._gif, self._zrect


class Quick_Zombie(Zombies):  #Quick_zombie moves faster than the others
    def __init__(self):
        self._key = "Quick_Zombie"
        self._hp = 100
        self._Damage = 10
        self._left = 1101
        # Var
        self._lastsprite = 0
        self._lastmove = 0
        self._eat = False
        self._lasteat = 0
        self._slowed = False
        self._lastslow = 0
        self._slowrate = 1
        # Sprite
        self._temp = 22
        self._walkingsprites = []
        self._eatingsprites = []
        self.sprite_initialization()
        self._activesprite = self._walkingsprites
        self._gif = self._activesprite[self._currentsprite]
        # Rect
        self._zrect = self._gif.get_rect()
        self._zrect.left = self._left
        self.start()

    def sprite_initialization(self):
        self._currentsprite = 0
        for i in range(22):
            zomimage = pygame.image.load("./assets/Images/Zombie/ZombieWalk/Zombie_" + str(i) + ".png")
            zomimage = pygame.transform.scale(zomimage, (int(zomimage.get_width())*7/10,int(zomimage.get_height())*7/10))
            self._walkingsprites.append(zomimage)
        for i in range(21):
            zomimage2 = pygame.image.load("./assets/Images/Zombie/ZombieAttack/ZombieAttack_" + str(i) + ".png")
            zomimage2 = pygame.transform.scale(zomimage2, (int(zomimage2.get_width())*7/10,int(zomimage2.get_height())*7/10))
            self._eatingsprites.append(zomimage2)

    
    # Actions
    def move(self, current):
        if current - self._lastmove >= (1000/60)*3:
            self._lastmove = current
            self._zrect.left -= 1 * self._slowrate


class Weak_Zombie(Zombies):  #Weak_zombie requires less shouts to be killed.
    def __init__(self):
        self._key = "Weak_Zombie"
        self._hp = 100
        self._Damage = 10
        self._left = 1101
        # Var
        self._lastsprite = 0
        self._lastmove = 0
        self._eat = False
        self._lasteat = 0
        self._slowed = False
        self._lastslow = 0
        self._slowrate = 1
        # Sprite
        self._temp = 21
        self._walkingsprites = []
        self._eatingsprites = []
        self.sprite_initialization()
        self._activesprite = self._walkingsprites
        self._gif = self._activesprite[self._currentsprite]
        # Rect
        self._zrect = self._gif.get_rect()
        self._zrect.left = self._left
        self.start()

    def sprite_initialization(self):
        self._currentsprite = 0
        for i in range(21):
            zomimage = pygame.image.load("./assets/Images/ConeheadZombie/ConeheadZombie/ConeheadZombie_" + str(i) + ".png")
            zomimage = pygame.transform.scale(zomimage, (int(zomimage.get_width())*7/10,int(zomimage.get_height())*7/10))
            self._walkingsprites.append(zomimage)
        for i in range(11):
            zomimage2 = pygame.image.load("./assets/Images/ConeheadZombie/ConeheadZombieAttack/ConeheadZombieAttack_" + str(i) + ".png")
            zomimage2 = pygame.transform.scale(zomimage2, (int(zomimage2.get_width())*7/10,int(zomimage2.get_height())*7/10))
            self._eatingsprites.append(zomimage2)
    
    # Actions
    def move(self, current):
        if current - self._lastmove >= (1000/60)*6:
            self._lastmove = current
            self._zrect.left -= 1 * self._slowrate


class Strong_Zombie(Zombies):   #Strong_zombie requires more shouts to be killed.
    def __init__(self):
        self._key = "Strong_Zombie"
        self._hp = 150
        self._WaitingTime = 5
        self._Damage = 20
        self._left = 1101
        # Var
        self._lastsprite = 0
        self._lastmove = 0
        self._eat = False
        self._lasteat = 0
        self._slowed = False
        self._lastslow = 0
        self._slowrate = 1
        # Sprite
        self._temp = 15
        self._walkingsprites = []
        self._eatingsprites = []
        self.sprite_initialization()
        self._activesprite = self._walkingsprites
        self._gif = self._activesprite[self._currentsprite]
        # Rect
        self._zrect = self._gif.get_rect()
        self._zrect.left = self._left
        self.start()

    def sprite_initialization(self):
        self._currentsprite = 0
        for i in range(15):
            zomimage = pygame.image.load("./assets/Images/BucketheadZombie_Image/BucketheadZombie/BucketheadZombie_" + str(i) + ".png")
            zomimage = pygame.transform.scale(zomimage, (int(zomimage.get_width())*7/10,int(zomimage.get_height())*7/10))
            self._walkingsprites.append(zomimage)
        for i in range(11):
            zomimage2 = pygame.image.load("./assets/Images/BucketheadZombie_Image/BucketheadZombieAttack/BucketheadZombieAttack_" + str(i) + ".png")
            zomimage2 = pygame.transform.scale(zomimage2, (int(zomimage2.get_width())*7/10,int(zomimage2.get_height())*7/10))
            self._eatingsprites.append(zomimage2)
    
    # Actions
    def move(self, current):
        if current - self._lastmove >= (1000/60)*3:
            self._lastmove = current
            self._zrect.left -= 1 * self._slowrate
