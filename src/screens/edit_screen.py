# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import pygame

from . import chase
from . import cities
from . import settings
from . import fight
from . import shop
from . import home_screen
from ..utils import constants as consts
from ..utils.widgets import TextButton
from ..utils import colors
import os


# temporary home screen
def play():
    back = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                        (consts.SCREEN_HEIGHT / 2) - 300),
                      width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                      font=pygame.font.Font('freesansbold.ttf', 30), text='<-')

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        consts.MAIN_DISPLAY.fill((255, 255, 255))

        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if back.hovered:
            back.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                back.toggle_bg(colors.BROWN_COLOR)
                # update volume bar
                return home_screen.play()
        else:
            back.toggle_bg(colors.BLACK_COLOR)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
