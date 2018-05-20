import pygame, sys
from Player import Player
from Platforms import Platform
from pygame import image
from pygame import Surface
from Policeman import Policeman
from Level_file import *

SIZE = (640, 480)
window = pygame.display.set_mode(SIZE)


################################################### меню
class Menu():
    def __init__(self, punkts = [120, 140, 'Punkt', (250, 250, 30), (250, 30, 250)]):
        #пункты меню
        self.punkts = punkts
        #загружает фоновое изображение
        self.image_menu = image.load('data/images/menu.jpg')


    def render(self, poverhnost, font, num_punkt):

        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True

        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            #отрисовывает фоновое изображение на экране, цифры это координаты начала отрисовки
            screen.blit(self.image_menu, (0, 0))


            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 200 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]

            self.render(screen, font_menu, punkt)


            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                if i.type == pygame.K_DOWN:
                    if i.key == pygame.K_ESCAPE:
                        sys.exit()
                    if i.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if i.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            window.blit(screen, (0, 0))
            pygame.display.flip()

pygame.font.init()
speed_font = pygame.font.Font(None, 32)
################################################### меню


screen = pygame.Surface(SIZE)
#make hero
hero = Player(55, 55)
left = right = up = False
policeman_1 = Policeman(400, 600)
# policeman_2 = Policeman(440, 600)
# policeman_3 = Policeman(480, 600)

policeman_4 = Policeman(2000, 600)
# policeman_5 = Policeman(2040, 600)
# policeman_6 = Policeman(2080, 600)

policeman_7 = Policeman(4910, 600)
# policeman_8 = Policeman(4950, 600)
# policeman_9 = Policeman(4990, 600)

policeman_10 = Policeman(5900, 450)
# policeman_11 = Policeman(5940, 450)
# policeman_12 = Policeman(5980, 450)

###############################################make level




sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
# sprite_group.add(policeman_1, policeman_2, policeman_3, policeman_4, policeman_5, policeman_6, policeman_7, policeman_8, policeman_9, policeman_10, policeman_11, policeman_12)
# free_mobs = [policeman_1, policeman_2, policeman_3, policeman_4, policeman_5, policeman_6, policeman_7, policeman_8, policeman_9, policeman_10, policeman_11, policeman_12]
sprite_group.add(policeman_1, policeman_4, policeman_7, policeman_10)
free_mobs = [policeman_1, policeman_4, policeman_7, policeman_10]


#####массивы платформ
platforms = []
killers = []
platforn_number_one = []
platforn_number_two = []
policeman = []
keys = []
locks = []
putin = []
#####массивы платформ
x = 0
y = 0


##############названия платформ

classical_platform = 0
killer_platform = 1
teleport_platform = 2
policeman_platform = 3
keys_platform = 4
locks_platform = 5
putin_platform = 6

##############названия платформ
#- обычные
#x убиваторские
#числа - телепорты
#p - policeman
##############цикл по созданию платформ
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x, y, classical_platform)
            sprite_group.add(pl)
            platforms.append(pl)

        if col == 'k':
            pl = Platform(x, y, keys_platform)
            sprite_group.add(pl)
            keys.append(pl)

        if col == 'x':
            pl = Platform(x, y, killer_platform)
            sprite_group.add(pl)
            killers.append(pl)

        if col == 'p':
            pl = Platform(x, y, policeman_platform)
            sprite_group.add(pl)
            policeman.append(pl)

        if col == 'l':
            pl = Platform(x, y, locks_platform)
            sprite_group.add(pl)
            locks.append(pl)

        if col == 's':
            pl = Platform(x, y, putin_platform)
            sprite_group.add(pl)
            putin.append(pl)


        x += 50
    y += 50
    x = 0
##############цикл по созданию платформ


pl = pygame.Surface((40, 40))
pl.fill((210, 120, 60))
###############################################make level

###############################################camera
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.y + SIZE[1]/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - SIZE[0]), l)
    t = max(-(camera.height - SIZE[1]), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)
###############################################camera


###############################################отвечает за размер карты
total_level_width = len(level[0]) * 50
total_level_height = len(level) * 50
###############################################отвечает за размер карты
level_hight = len(level)

###############################################camera
camera = Camera(camera_func, total_level_width, total_level_height)
###############################################camera


###############################################пункты меню
punkts = [(160, 260, 'Сопротивляться', (0, 0, 0), (100, 100, 100), 0),
          (100, 340, 'Заняться чем-то полезным', (0, 0, 0), (100, 100, 100), 1)]
###############################################пункты меню

###############################################создание меню
game = Menu(punkts)
game.menu()
###############################################создание меню

###############################################основной цикл
done = True
timer = pygame.time.Clock()
pygame.mixer.init()
music = pygame.mixer.music.load('data/fon.mp3')
pygame.mixer.music.play(-1, 0.0)
main_image = image.load('data/images/fonimage.png')

while done:

    #блок управления событиями
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                left = True
            if i.key == pygame.K_RIGHT:
                right = True
            if i.key == pygame.K_UP:
                up = True
            if i.key == pygame.K_ESCAPE:
                game.menu()
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                left = False
            if i.key == pygame.K_RIGHT:
                right = False
            if i.key == pygame.K_UP:
                up = False
    #закрашиваем рабочую поверхность

    # screen.fill((200, 200, 0))

    screen.blit(main_image, (0, 0))

    #отображение героя
    for man in free_mobs:
        man.update(platforms)
    hero.update(left, right, up, platforms, killers, policeman, free_mobs, keys, sprite_group, locks, putin, music)
    camera.update(hero)
    for i in sprite_group:
        screen.blit(i.image, camera.apply(i))
    # sprite_group.draw(screen)

    #отображаем рабочую поверхность в окне
    window.blit(screen, (0, 0))

    #обновляем окно
    pygame.display.flip()
    timer.tick(30)
