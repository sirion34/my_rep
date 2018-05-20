# import pygame
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from Platforms import Platform
from pygame import time
from pygame import image
from pygame import display
import pyganim

timer = time.Clock()
MOVE_POLICEMAN_SPEED = 5
GRAVITY = 0.80
JUMP_POWER = -15
COLOR = 10, 120, 10


ANIMATION_POLICEMAN_DELAY = 75
ANIMATION_POLICEMAN_STAY = [('data/policeman/hero1.png', ANIMATION_POLICEMAN_DELAY)]
# ANIMATION_POLICEMAN_RIGHT = ['data/policeman/heror1.png',
#                     'data/policeman/heror2.png',
#                     'data/policeman/heror1.png',
#                     'data/policeman/heror3.png']
ANIMATION_POLICEMAN_LEFT = ['data/policeman/policemanl1.png',
                    'data/policeman/policemanl2.png',
                    'data/policeman/policemanl1.png',
                    'data/policeman/policemanl3.png']

class Policeman(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((31, 50))
        # self.image = image.load('data/hero/hero1.png')
        self.rect = self.image.get_rect()
        self.yvel = 0
        self.xvel = 0
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
        self.image.set_colorkey(COLOR)

        # def make_boltAnimR(anim_list, delay):
        #     boltAnim = []
        #     for anim in ANIMATION_POLICEMAN_RIGHT:
        #         boltAnim.append((anim, delay))
        #     Anim = pyganim.PygAnimation(boltAnim)
        #     return Anim

        def make_boltAnimL(anim_list, delay):
            boltAnim = []
            for anim in ANIMATION_POLICEMAN_LEFT:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.image.set_colorkey(COLOR)

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_POLICEMAN_STAY)
        self.boltAnimStay.play()


        # self.boltAnimRight = make_boltAnimR(ANIMATION_POLICEMAN_RIGHT, ANIMATION_POLICEMAN_DELAY)
        # self.boltAnimRight.play()
        self.boltAnimLeft = make_boltAnimL(ANIMATION_POLICEMAN_LEFT, ANIMATION_POLICEMAN_DELAY)
        self.boltAnimLeft.play()



    def update(self, platforms):
        # if left:
        #     self.xvel = -MOVE_SPEED
        #     self.image.fill(COLOR)
        #     self.boltAnimLeft.blit(self.image, (0, 0))
        # if right:
        #     self.xvel = MOVE_SPEED
        #     self.image.fill(COLOR)
        #     self.boltAnimRight.blit(self.image, (0, 0))
        # if not(left or right):
        #     self.xvel = 0
        #     if not up:
        #         self.image.fill(COLOR)
        #         self.boltAnimStay.blit(self.image, (0, 0))
        # if up:
        #     if self.onGround:
        #         self.yvel = JUMP_POWER
        if not self.onGround:
           self.yvel += GRAVITY
        if self.xvel == 0:
            self.xvel = MOVE_POLICEMAN_SPEED





        self.image.fill(COLOR)
        self.boltAnimLeft.blit(self.image, (0, 0))


        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        # if self.collide_on(self.xvel, platforms) == 0:
        #     self.xvel = MOVE_POLICEMAN_SPEED
        # else:
        #     self.xvel = -MOVE_POLICEMAN_SPEED


    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.xvel = -MOVE_POLICEMAN_SPEED
                    self.yvel = 0
                    # self.rect.right = pl.rect.left
                    # xvel = -MOVE_POLICEMAN_SPEED
                if xvel < 0:
                    self.xvel = MOVE_POLICEMAN_SPEED
                    self.yvel = 0
                    # self.rect.left = pl.rect.right
                    # xvel = MOVE_POLICEMAN_SPEED
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0

    # def collide_on(self, xvel, platforms):
    #     for pl in platforms:
    #         if collide_rect(self, pl):
    #             return 1
    #         else:
    #             return 0