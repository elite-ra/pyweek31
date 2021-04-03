# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

import pygame

from . import chase
from . import cities
from ..utils import constants as consts
from ..utils.widgets import TextButton
from ..utils import colors
from .. import utils
from ..utils import database
from . import home_screen


# settings screen
def play():

    # print(utils.constants.DB.get_settings())
    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    inc_main_vol = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) + 100,
                                                                (consts.SCREEN_HEIGHT / 2) + 100),
                              width=25, height=25, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                              font=pygame.font.Font('freesansbold.ttf', 18), text='+')
    dec_main_vol = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                (consts.SCREEN_HEIGHT / 2) + 100),
                              width=25, height=25, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                              font=pygame.font.Font('freesansbold.ttf', 18), text='-')

    inc_fx_vol = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) + 100,
                                                              (consts.SCREEN_HEIGHT / 2) + 50),
                            width=25, height=25, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                            font=pygame.font.Font('freesansbold.ttf', 18), text='+')
    dec_fx_vol = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                              (consts.SCREEN_HEIGHT / 2) + 50),
                            width=25, height=25, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                            font=pygame.font.Font('freesansbold.ttf', 18), text='-')

    back = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                        (consts.SCREEN_HEIGHT / 2) - 300),
                      width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                      font=pygame.font.Font('freesansbold.ttf', 30), text='<-')

    reset_btn = TextButton(surface=consts.MAIN_DISPLAY, pos = (500, 100), width=100, height=40,
                           fg_color=colors.WHITE_COLOR, bg_color=colors.RED_COLOR,
                           font=pygame.font.Font('freesansbold.ttf', 10), text='Reset Game Progress')

    is_game_over = False
    while not is_game_over:
        utils.constants.MAIN_DISPLAY.fill((255, 255, 255))
        curr_setting = consts.DB.get_settings()

        t = consts.FONT_MONO_SMALL.render(f'Music: ', True, (0, 0, 0))
        consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH/2 - 150, consts.SCREEN_HEIGHT/2 + 100))
        t = consts.FONT_MONO_MEDIUM.render(f'{curr_setting["volume"]["music"]}', True, (0, 0, 0))
        consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH/2 + 0, consts.SCREEN_HEIGHT/2 + 100))

        t = consts.FONT_MONO_MEDIUM.render(f'{curr_setting["volume"]["fx"]}', True, (0, 0, 0))
        consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH / 2 + 0, consts.SCREEN_HEIGHT / 2 + 50))
        t = consts.FONT_MONO_SMALL.render(f'Fx: ', True, (0, 0, 0))
        consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH/2 - 150, consts.SCREEN_HEIGHT/2 + 50))

        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if curr_setting['volume']['music'] == 100:
            inc_main_vol.toggle_bg(colors.GREY_COLOR)
        else:
            # button interaction
            if inc_main_vol.hovered and curr_setting['volume']['music'] < 100:
                inc_main_vol.toggle_bg(colors.BROWN_COLOR)
                if mouse_down:
                    inc_main_vol.toggle_bg(colors.BROWN_COLOR)
                    # update volume bar

                    ns = dict(curr_setting)
                    ns['volume']['music'] += 10

                    consts.DB.set_settings(ns)
            else:
                inc_main_vol.toggle_bg(colors.BLACK_COLOR)

        if curr_setting['volume']['music'] == 0:
            dec_main_vol.toggle_bg(colors.GREY_COLOR)
        else:
            if dec_main_vol.hovered and curr_setting['volume']['music'] > 0:
                dec_main_vol.toggle_bg(colors.BROWN_COLOR)
                if mouse_down:
                    dec_main_vol.toggle_bg(colors.BROWN_COLOR)
                    # update volume bar
                    ns = dict(curr_setting)
                    ns['volume']['music'] -= 10
                    consts.DB.set_settings(ns)
            else:
                dec_main_vol.toggle_bg(colors.BLACK_COLOR)

        if curr_setting['volume']['fx'] == 100:
            inc_fx_vol.toggle_bg(colors.GREY_COLOR)
        else:
            if inc_fx_vol.hovered and curr_setting['volume']['fx'] < 100:
                inc_fx_vol.toggle_bg(colors.BROWN_COLOR)
                if mouse_down:
                    inc_fx_vol.toggle_bg(colors.BROWN_COLOR)
                    # update volume bar
                    ns = dict(curr_setting)
                    ns['volume']['fx'] += 10
                    consts.DB.set_settings(ns)
            else:
                inc_fx_vol.toggle_bg(colors.BLACK_COLOR)

        if curr_setting['volume']['fx'] == 0:
            dec_fx_vol.toggle_bg(colors.GREY_COLOR)
        else:
            if dec_fx_vol.hovered and curr_setting['volume']['fx'] > 0:
                dec_fx_vol.toggle_bg(colors.BROWN_COLOR)
                if mouse_down:
                    dec_fx_vol.toggle_bg(colors.BROWN_COLOR)
                    # update volume bar
                    ns = dict(curr_setting)
                    ns['volume']['fx'] -= 10
                    consts.DB.set_settings(ns)
            else:
                dec_fx_vol.toggle_bg(colors.BLACK_COLOR)

        if back.hovered:
            back.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                back.toggle_bg(colors.BROWN_COLOR)
                # update volume bar
                return home_screen.play()
        else:
            back.toggle_bg(colors.BLACK_COLOR)

        if reset_btn.hovered:
            reset_btn.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                consts.DB.reset_player_settings()

                return home_screen.play()
        else:
            reset_btn.toggle_bg(colors.RED_COLOR)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
