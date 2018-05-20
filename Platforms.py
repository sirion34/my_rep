from pygame.sprite import Sprite
from pygame import image

class Platform(Sprite):

    def __init__(self, x, y, number):
        Sprite.__init__(self)
        self.array_of_images = ['data/images/durov.png',
                                'data/images/killers.png',
                                'data/images/platform.png',
                                'data/images/policemanl1.png',
                                'data/images/key.png',
                                'data/images/lock.png',
                                'data/images/putin.png']


        self.image = image.load(self.array_of_images[number])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


