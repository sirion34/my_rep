# import pygame
from pygame.sprite import Sprite, collide_rect
from pygame import Surface, mixer
from Platforms import Platform
from pygame import time
from pygame import image
from pygame import display
from Level_file import level_hight
import pyganim
from sys import exit

timer = time.Clock()
MOVE_SPEED = 15
GRAVITY = 0.80
JUMP_POWER = -15
COLOR = 10, 120, 10
is_this_window_of_die = display.set_mode((640, 480))
end_window = display.set_mode((640, 480))

ANIMATION_DELAY = 75
ANIMATION_STAY = [('data/hero/hero1.png', ANIMATION_DELAY)]
ANIMATION_RIGHT = ['data/hero/heror1.png',
                    'data/hero/heror2.png',
                    'data/hero/heror1.png',
                    'data/hero/heror3.png']
ANIMATION_LEFT = ['data/hero/herol1.png',
                    'data/hero/herol2.png',
                    'data/hero/herol1.png',
                    'data/hero/herol3.png']

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((31, 50))
        self.yvel = 0
        self.xvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
        self.image.set_colorkey(COLOR)

        def make_boltAnimR(anim_list, delay):
            boltAnim = []
            for anim in ANIMATION_RIGHT:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        def make_boltAnimL(anim_list, delay):
            boltAnim = []
            for anim in ANIMATION_LEFT:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.image.set_colorkey(COLOR)

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()


        self.boltAnimRight = make_boltAnimR(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()
        self.boltAnimLeft = make_boltAnimL(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()



    def update(self, left, right, up, platforms, killers, policeman, mobs1, keys, sprite_group, locks, putin, music):
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(COLOR)
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(COLOR)
            self.boltAnimRight.blit(self.image, (0, 0))
        if not(left or right):
            self.xvel = 0
            if not up:
                self.image.fill(COLOR)
                self.boltAnimStay.blit(self.image, (0, 0))
        if up:
            if self.onGround:
                self.yvel = JUMP_POWER
        if not self.onGround:
           self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, killers, policeman, keys, sprite_group, locks, putin, music)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, killers, policeman, keys, sprite_group, locks, putin, music)
        self.collide_mobs(self.yvel, mobs1, keys, locks)
        if self.rect.y > level_hight + 50:
            self.screen_of_die(keys,locks)



    def coords_x(self):
        return self.rect.x

    def coords_y(self):
        return self.rect.y

    def collide(self, xvel, yvel, platforms, killers, policeman, keys, sprite_group, locks, putin, music):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0
            for pl in locks:
                if collide_rect(self, pl):
                    if xvel > 0:
                        self.rect.right = pl.rect.left
                    if xvel < 0:
                        self.rect.left = pl.rect.right
                    if yvel > 0:
                        self.rect.bottom = pl.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = pl.rect.bottom
                        self.yvel = 0

        for pl in keys:
            if collide_rect(self, pl):
                if pl == keys[0]:
                    keys[0].rect.x = -100
                    locks[0].rect.x = -100
                if pl == keys[1]:
                    keys[1].rect.x = -100
                    locks[1].rect.x = -100


                ################киляторы
        for pl in killers:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                    self.screen_of_die(keys,locks)
                if xvel < 0:
                    self.rect.left = pl.rect.right
                    self.screen_of_die(keys,locks)
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                    self.screen_of_die(keys,locks)
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0
                    self.screen_of_die(keys,locks)

                ################киляторы


                ################телепортаторы
        # for pl in platforn_number_one:
        #     if collide_rect(self, pl):
        #         if xvel > 0:
        #             self.rect.right = pl.rect.left
        #             self.rect.x = 1500
        #             self.rect.y = 55
        #         if xvel < 0:
        #             self.rect.left = pl.rect.right
        #             self.rect.x = 1500
        #             self.rect.y = 55
        #         if yvel > 0:
        #             self.rect.bottom = pl.rect.top
        #             self.onGround = True
        #             self.yvel = 0
        #             self.rect.x = 1500
        #             self.rect.y = 55
        #         if yvel < 0:
        #             self.rect.top = pl.rect.bottom
        #             self.yvel = 0
        #             self.rect.x = 1500
        #             self.rect.y = 55
        #     ################телепортаторы
        #     ################телепортаторы
        # for pl in platforn_number_two:
        #     if collide_rect(self, pl):
        #         if xvel > 0:
        #             self.rect.right = pl.rect.left
        #             self.rect.x = 55
        #             self.rect.y = 55
        #         if xvel < 0:
        #             self.rect.left = pl.rect.right
        #             self.rect.x = 55
        #             self.rect.y = 55
        #         if yvel > 0:
        #             self.rect.bottom = pl.rect.top
        #             self.onGround = True
        #             self.yvel = 0
        #             self.rect.x = 55
        #             self.rect.y = 55
        #         if yvel < 0:
        #             self.rect.top = pl.rect.bottom
        #             self.yvel = 0
        #             self.rect.x = 55
        #             self.rect.y = 55
        #     ################телепортаторы
        for pl in policeman:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                    self.screen_of_die(keys,locks)
                if xvel < 0:
                    self.rect.left = pl.rect.right
                    self.screen_of_die(keys,locks)
                if yvel > 0:
                    self.rect.top = pl.rect.top
                    self.screen_of_die(keys,locks)
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0
                    self.screen_of_die(keys,locks)

        for pl in putin:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                music = mixer.music.load('data/end.mp3')
                mixer.music.play(-1, 0.0)
                self.end()

    def screen_of_die(self, keys, locks):
        self.screen = is_this_window_of_die
        self.image_of_dead = image.load('data/images/dead.png')
        self.screen.blit(self.image_of_dead, (0, 0))
        display.flip()
        timer.tick(60)

        time.wait(3000)
        self.rect.x = 55
        self.rect.y = 55
        keys[0].rect.x = 2000
        keys[1].rect.x = 4950
        locks[0].rect.x = 5600
        locks[1].rect.x = 5650

    def end(self):
        self.screen = end_window
        self.end1 = image.load('data/images/end1.png')
        self.screen.blit(self.end1, (0, 0))
        display.flip()
        timer.tick(60)
        time.wait(5000)
        self.screen = end_window
        self.end2 = image.load('data/images/end2.png')
        self.screen.blit(self.end2, (0, 0))
        display.flip()
        timer.tick(60)
        time.wait(5000)
        exit()

    def collide_mobs(self, yvel, mobs1, keys, locks):
        for pl in mobs1:
            if collide_rect(self, pl):
                if yvel > 0:
                    self.screen_of_die(keys, locks)
