# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Ayush Gupta


from . import home_screen
import pygame
from ..utils.widgets import TextButton
from ..utils import constants as consts


def end_screen_func(a):
    running = True

    while running:

        mouse_down = False
        consts.MAIN_DISPLAY.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        font = consts.FONT_MONO_LARGE
        # coins limit reached
        if a == 1:
            text = font.render('Too much was stolen! The robber won.', True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        # bird strike
        elif a == 2:
            text = font.render('Your crashed and the robber got away. The robber won.', True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        # losing in fight
        elif a == 3:
            text = font.render('You lost all your health! The robber won.', True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        city_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                   (consts.SCREEN_HEIGHT / 2) + 100),
                                 width=200, height=40, fg_color=(0, 0, 0), bg_color=(255, 0, 0),
                                 font=consts.FONT_MONO_LARGE, text='Try Again')

        if city_button.hovered:
            city_button.toggle_bg((139, 0, 0))
            if mouse_down:
                city_button.toggle_bg((255, 0, 0))
                return home_screen.play()

        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
