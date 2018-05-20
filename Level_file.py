# from  Platforms import Platform
# import pygame
# from Player import Player
# from Policeman import Policeman


level = [
        "                                                                                                                                         ",
        "                                                                                                                p                        ",
        "                                                                                                                -------------------------",
        "                       p                        -----                                                     p     ll                      -",
        "                ---    ----              ---   x           p                                           ------------------  --------------",
        "                                  p          ---         ----                                          -                                -",
        "                               ---------                        ----                            -----  -  p                            p-",
        "         ---                                                        x                                  ---------xxx-----------xx-    ----",
        "     -               p                   xxx  xxx                   x   ----            -----          x                                -",
        "     -        ----------              ------------                                                     x     -                          -",
        "   ---        x        x              x    x                                                           x     ----------------------------",
        "              x        x    --        x                                         ----x                  x                              s -",
        "-             x    p   x         -    x k        -                              -                  k   -                                -",
        "--------------------------------------------------    ---- -------  ----------- -------------------------------------xxx-----xxx---------",]

level_hight = len(level)*50
SIZE = (640, 480)




# ###############################################make level
# def new_game():
#         screen = pygame.Surface(SIZE)
#         #make hero
#         hero = Player(55, 55)
#         left = right = up = False
#         policeman_1 = Policeman(400, 600)
#         policeman_2 = Policeman(440, 600)
#         policeman_3 = Policeman(480, 600)
#         sprite_group = pygame.sprite.Group()
#         sprite_group.add(hero)
#
#
#
#         sprite_group.add(policeman_1, policeman_2, policeman_3)
#         free_mobs = [policeman_1, policeman_2, policeman_3]
#
#
#         #####массивы платформ
#         platforms = []
#         killers = []
#         platforn_number_one = []
#         platforn_number_two = []
#         policeman = []
#         keys = []
#         #####массивы платформ
#         x = 0
#         y = 0
#
#
#         ##############названия платформ
#
#         classical_platform = 0
#         killer_platform = 1
#         teleport_platform = 2
#         policeman_platform = 3
#         keys_platform = 4
#
#         ##############названия платформ
#         #- обычные
#         #x убиваторские
#         #числа - телепорты
#         #p - policeman
#         ##############цикл по созданию платформ
#         for row in level:
#             for col in row:
#                 if col == '-':
#                     pl = Platform(x, y, classical_platform)
#                     sprite_group.add(pl)
#                     platforms.append(pl)
#
#                 if col == 'k':
#                     pl = Platform(x, y, keys_platform)
#                     sprite_group.add(pl)
#                     keys.append(pl)
#
#                 if col == 'x':
#                     pl = Platform(x, y, killer_platform)
#                     sprite_group.add(pl)
#                     killers.append(pl)
#
#                 if col == 'p':
#                     pl = Platform(x, y, policeman_platform)
#                     sprite_group.add(pl)
#                     policeman.append(pl)
#
#
#                 x += 50
#             y += 50
#             x = 0
#         ##############цикл по созданию платформ
#
#
#         pl = pygame.Surface((40, 40))
#         pl.fill((210, 120, 60))
#         ###############################################make level