import pygame
import os
import random
import math
from .. import utils
from . import end_screen
from ..utils.widgets import TextButton
from ..utils import constants as consts
from . import win_screen


def main():
    BG = (153, 102, 255)

    myfont = utils.constants.FONT_MONO_VERY_SMALL

    # Images and Sprites
    background_image = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'i01_BG.png'))
    copimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Cop.png'))
    vilimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Villain.png'))

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

        punch = TextButton(surface=consts.MAIN_DISPLAY, pos=(7, 482),
                           width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                           font=consts.FONT_MONO_VERY_SMALL, text='PUNCH')

        kick = TextButton(surface=consts.MAIN_DISPLAY, pos=(96, 482),
                          width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                          font=consts.FONT_MONO_VERY_SMALL, text='KICK')

        shoot = TextButton(surface=consts.MAIN_DISPLAY, pos=(7, 536),
                           width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                           font=consts.FONT_MONO_VERY_SMALL, text='SHOOT')

        wild_swing = TextButton(surface=consts.MAIN_DISPLAY, pos=(96, 536),
                                width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                                font=consts.FONT_MONO_VERY_SMALL, text='WILD SWING')

    done = False
    hpcop = 100
    hpvil = 100
    condition = True
    damage = 0

    while not done:

        mouse_down = False
        temp = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

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

        punch = TextButton(surface=consts.MAIN_DISPLAY, pos=(7, 482),
                           width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                           font=consts.FONT_MONO_VERY_SMALL, text='PUNCH')

        kick = TextButton(surface=consts.MAIN_DISPLAY, pos=(96, 482),
                          width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                          font=consts.FONT_MONO_VERY_SMALL, text='KICK')

        shoot = TextButton(surface=consts.MAIN_DISPLAY, pos=(7, 536),
                           width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                           font=consts.FONT_MONO_VERY_SMALL, text='SHOOT')

        wild_swing = TextButton(surface=consts.MAIN_DISPLAY, pos=(96, 536),
                                width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                                font=consts.FONT_MONO_VERY_SMALL, text='WILD SWING')

        if punch.hovered:
            punch.toggle_bg((100, 100, 100))
            if mouse_down:
                punch.toggle_bg((50, 50, 50))
                damage = Attacks(1, hpvil)
                hpvil = hpvil - damage
                hpcop = hpcop - random.randint(10, 20)

        if kick.hovered:
            kick.toggle_bg((100, 100, 100))
            if mouse_down:
                kick.toggle_bg((50, 50, 50))
                damage = Attacks(2, hpvil)
                hpvil = hpvil - damage
                hpcop = hpcop - random.randint(10, 20)

        if shoot.hovered:
            shoot.toggle_bg((100, 100, 100))
            if mouse_down:
                shoot.toggle_bg((50, 50, 50))
                damage = Attacks(3, hpvil)
                hpvil = hpvil - damage
                hpcop = hpcop - random.randint(10, 20)

        if wild_swing.hovered:
            wild_swing.toggle_bg((100, 100, 100))
            if mouse_down:
                wild_swing.toggle_bg((50, 50, 50))
                damage = Attacks(4, hpvil)
                if damage == 0:
                    hpcop = hpcop * 0.5
                hpvil = hpvil - damage
                hpcop = hpcop - 0.1

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)

    # end(screen) end screen
    if condition:
        return win_screen.play()
    else:
        return end_screen.end_screen_func(3)
