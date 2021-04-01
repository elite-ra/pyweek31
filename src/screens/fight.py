import pygame
import os
import random
import math
from .. import utils
from . import end_screen


def main():
    BG = (153, 102, 255)

    myfont = utils.constants.FONT_MONO_VERY_SMALL

    # Images and Sprites
    background_image = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'i01_BG.png'))
    copimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Cop.png'))
    vilimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Villain.png'))

    pygame.init()
    screen = utils.constants.MAIN_DISPLAY

    def HealthCop(value, screen):
        if value > 50:
            colour = (0, 255, 0)
        elif value <= 50 and value > 10:
            colour = (255, 200, 0)
        else:
            colour = (255, 0, 0)
        pygame.draw.rect(screen, (255, 255, 255), (40, 10, 200, 20))
        pygame.draw.rect(screen, colour, (41, 11, math.ceil(2 * value - 1), 18))

    def HealthVil(value, screen):
        if value > 50:
            colour = (0, 255, 0)
        elif value <= 50 and value > 10:
            colour = (255, 200, 0)
        else:
            colour = (255, 0, 0)
        pygame.draw.rect(screen, (255, 255, 255), (560, 10, 200, 20))
        pygame.draw.rect(screen, colour, (561, 11, math.ceil(2 * value - 1), 18))

    def Attacks(choice, hpvil):
        if choice == 1:
            return 10
        elif choice == 2:
            return 12
        elif choice == 3:
            a = random.randint(0, 1)
            return 20 * a
        elif choice == 4:
            a = random.randint(0, 1)
            return (0.5 * hpcop * a)

    def attackchoice(screen):
        pygame.draw.rect(screen, (130, 130, 130), (5, 480, 180, 110))

        pygame.draw.rect(screen, (50, 50, 50), (7, 482, 87, 52))
        punch = myfont.render('PUNCH', False, (255, 255, 255))

        pygame.draw.rect(screen, (50, 50, 50), (96, 482, 87, 52))
        kick = myfont.render('KICK', False, (255, 255, 255))

        pygame.draw.rect(screen, (50, 50, 50), (7, 536, 87, 52))
        shoot = myfont.render('SHOOT', False, (255, 255, 255))

        pygame.draw.rect(screen, (50, 50, 50), (96, 536, 87, 52))
        WildSwing = myfont.render('''WILD SWING''', False, (255, 255, 255))

        # printing the text
        screen.blit(punch, (27, 495))
        screen.blit(kick, (116, 495))
        screen.blit(shoot, (26, 556))
        screen.blit(WildSwing, (97, 556))

    done = False
    hpcop = 100
    hpvil = 100
    condition = True
    damage = 0

    while not done:

        temp = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if pygame.Rect((7, 482, 87, 52)).collidepoint(x, y):
                    damage = Attacks(1, hpvil)
                    hpvil = hpvil - damage

                elif pygame.Rect((7, 536, 87, 52)).collidepoint(x, y):
                    damage = Attacks(3, hpvil)
                    hpvil = hpvil - damage

                elif pygame.Rect((96, 482, 87, 52)).collidepoint(x, y):
                    damage = Attacks(2, hpvil)
                    hpvil = hpvil - damage

                elif pygame.Rect((96, 536, 87, 52)).collidepoint(x, y):
                    damage = Attacks(4, hpvil)
                    if damage == 0:
                        hpcop = hpcop * 0.5
                        temp = True
                    hpvil = hpvil - damage
                
                if not temp:
                    hpcop = hpcop - random.randint(7, 10)

        screen.blit(background_image, [0, 0])
        screen.blit(copimg, [230, 300])
        screen.blit(vilimg, [490, 300])

        if hpvil <= 0:
            break
        elif hpcop <= 0:
            condition = False
            break
        HealthCop(hpcop, screen)
        HealthVil(hpvil, screen)
        attackchoice(screen)
        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)

    # end(screen) end screen
    if condition:
        pass  # win screen
    else:
        return end_screen.end_screen_func(3)
