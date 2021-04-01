# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import pygame

from . import chase
from . import cities
from . import settings
from ..utils import constants as consts
from ..utils.widgets import TextButton
from ..utils import colors

pygame.init()


# temporary home screen
def play():
    city_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                               (consts.SCREEN_HEIGHT / 2) + 100),
                             width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                             font=pygame.font.Font('freesansbold.ttf', 30), text='Cities')
    chase_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 160,
                                                                (consts.SCREEN_HEIGHT / 2) + 160),
                              width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                              font=pygame.font.Font('freesansbold.ttf', 30), text='Chase')

    play_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                               (consts.SCREEN_HEIGHT / 2) + 0),
                             width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                             font=pygame.font.Font('freesansbold.ttf', 30), text='Actually Play')

    shop_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                               (consts.SCREEN_HEIGHT / 2) - 300),
                             width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                             font=pygame.font.Font('freesansbold.ttf', 30), text='Shop')

    settings_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) + 100,
                                                                   (consts.SCREEN_HEIGHT / 2) - 300),
                                 width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=pygame.font.Font('freesansbold.ttf', 30), text='Settings')

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        mouse_down = False
        consts.MAIN_DISPLAY.fill((0, 0, 0))
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        # button interaction
        if city_button.hovered:
            city_button.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                city_button.toggle_bg(colors.BROWN_COLOR)
                return cities.play()
        else:
            city_button.toggle_bg(colors.BLACK_COLOR)

        if chase_button.hovered:
            chase_button.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                chase_button.toggle_bg(colors.BROWN_COLOR)
                return chase.play(1)
        else:
            chase_button.toggle_bg(colors.BLACK_COLOR)

        if play_button.hovered:
            play_button.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                play_button.toggle_bg(colors.BROWN_COLOR)
                return cities.play()
        else:
            play_button.toggle_bg(colors.BLACK_COLOR)

        if shop_button.hovered:
            shop_button.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                shop_button.toggle_bg(colors.BROWN_COLOR)
                pass  # return shop.play()
        else:
            shop_button.toggle_bg(colors.BLACK_COLOR)

        if settings_button.hovered:
            settings_button.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                settings_button.toggle_bg(colors.BROWN_COLOR)
                return settings.play()
        else:
            settings_button.toggle_bg(colors.BLACK_COLOR)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
