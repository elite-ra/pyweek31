# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar

import pygame

from . import chase
from . import cities
from ..utils import constants as consts
from ..utils.widgets import TextButton
from ..utils import colors

pygame.init()


# temporary home screen
def home_screen():
    city_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                               (consts.SCREEN_HEIGHT / 2) + 100),
                             width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                             font=pygame.font.Font('freesansbold.ttf', 30), text='Cities')
    chase_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 160,
                                                                (consts.SCREEN_HEIGHT / 2) + 160),
                              width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                              font=pygame.font.Font('freesansbold.ttf', 30), text='Chase')

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        mouse_down = False
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
                return chase.play()
        else:
            chase_button.toggle_bg(colors.BLACK_COLOR)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
