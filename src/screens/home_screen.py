# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi


if __name__ == "__main__":
    import sys

    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

import pygame

from . import settings
from . import explain_city
from . import shop
from .. import utils
from ..utils import constants as consts
from ..utils.widgets import TextButton, ImageButton
from ..utils import colors
from . import edit_screen
from .. import music_controller
import os

icon = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'icon.png'))
pygame.init()
pygame.display.set_caption('Aquilam')
pygame.display.set_icon(icon)


# temporary home screen
def play():
    logo = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'logo.png'))
    # INITIALIZE the sounds
    music_controller.update_volume()
    music_controller.stop_fx1()
    music_controller.stop_fx2()
    music_controller.stop_fx3()
    music_controller.stop_fx4()
    music_controller.stop_bg()

    img = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'bg', 'bg_screen.png'))

    play_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                               (consts.SCREEN_HEIGHT / 2) + 100),
                             width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                             font=utils.constants.FONT_MONO_LARGE, text='Play')

    plyr = consts.DB.get_player_details()
    if plyr.has_reached_fight:
        edit_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 150,
                                                                   (consts.SCREEN_HEIGHT / 2) + 200),
                                 width=300, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=utils.constants.FONT_MONO_LARGE, text='Edit Fight Moves')
    else:
        edit_button = None
        edit_d_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 150,
                                                                     (consts.SCREEN_HEIGHT / 2) + 200),
                                   width=300, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.GREY_COLOR,
                                   font=utils.constants.FONT_MONO_LARGE, text='???')

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:

        mouse_down = False
        consts.MAIN_DISPLAY.blit(img, (0, 0))

        shop_button = ImageButton(surface=consts.MAIN_DISPLAY, pos=(5,
                                                                    5),
                                  width=70, height=70,
                                  image_path=os.path.join(consts.ROOT_PATH, 'assets', 'images', 'textures', 'shop.png'))

        settings_button = ImageButton(surface=consts.MAIN_DISPLAY, pos=(730,
                                                                        5),
                                      width=70, height=70,
                                      image_path=os.path.join(consts.ROOT_PATH, 'assets', 'images', 'textures',
                                                              'settings.png'))

        consts.MAIN_DISPLAY.blit(logo, [(800 - 512) / 2, -100])
        title = consts.FONT_MAIN_SCREEN.render('AQUILAM', True, (200, 255, 255))
        consts.MAIN_DISPLAY.blit(title, (consts.SCREEN_WIDTH / 2 - title.get_width() / 2, 230))
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if play_button.hovered:
            play_button.toggle_bg((0, 100, 0))
            if mouse_down:
                music_controller.play_click_normal()
                play_button.toggle_bg(colors.BROWN_COLOR)
                return explain_city.play()
        else:
            play_button.toggle_bg(colors.BLACK_COLOR)

        if shop_button.hovered:

            if mouse_down:
                music_controller.play_click_normal()
                return shop.play()

        if settings_button.hovered:
            if mouse_down:
                music_controller.play_click_normal()
                return settings.play()

        if edit_button is None:
            edit_d_button.toggle_bg(colors.GREY_COLOR)
        else:
            if edit_button.hovered:
                edit_button.toggle_bg((0, 100, 0))
                if mouse_down:
                    music_controller.play_click_normal()
                    edit_button.toggle_bg(colors.RED_COLOR)
                    return edit_screen.play()
            else:
                edit_button.toggle_bg(colors.BLACK_COLOR)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
