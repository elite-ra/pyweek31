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


def play():

    logo = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'logo.png'))

    # INITIALIZE the sounds
    music_controller.update_volume()
    music_controller.stop_fx2()
    music_controller.stop_fx3()
    music_controller.stop_fx4()
    music_controller.stop_bg()
    music_controller.play_menu_bg()

    img = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'bg', 'bg_screen.png'))
    consts.MAIN_DISPLAY.blit(img, (0, 0))

    consts.MAIN_DISPLAY.blit(logo, [(800 - 512) / 2, -100])
    title = consts.FONT_MAIN_SCREEN.render('AQUILAM', True, (200, 255, 255))
    consts.MAIN_DISPLAY.blit(title, (consts.SCREEN_WIDTH / 2 - title.get_width() / 2, 230))

    play_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                               (consts.SCREEN_HEIGHT / 2) + 100),
                             width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                             font=utils.constants.FONT_MONO_LARGE, text='Play')

    plyr = consts.DB.get_player_details()

    x_btn = None
    modal_showing = False
    REL_COORDS = None

    def show_modal(titlee, text1, text2):

        nonlocal modal_showing
        modal_showing = True
        maj_sur = pygame.Surface((800, 600))
        maj_sur.set_alpha(180)
        maj_sur.fill(colors.BLACK_COLOR)
        consts.MAIN_DISPLAY.blit(maj_sur, (0, 0))
        text_aaa = consts.FONT_MONO_MEDIUM.render(titlee, True, (100, 0, 0))
        text_bbb = consts.FONT_MONO_SMALL.render(text1, True, (255, 255, 255))
        text_ccc = consts.FONT_MONO_SMALL.render(text2, True, (255, 255, 255))

        surf = pygame.Surface((400,
                               20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20 + text_ccc.get_height() + 5))

        surf.blit(text_aaa, (20, 20))
        surf.blit(text_bbb, (20, 20 + text_aaa.get_rect().height + 5))
        surf.blit(text_ccc, (20, 20 + text_aaa.get_rect().height + 5 + text_bbb.get_rect().height + 5))
        nonlocal x_btn
        x_btn = TextButton(surface=surf, pos=(370, 0), width=30, height=30, fg_color=colors.WHITE_COLOR,
                           bg_color=colors.RED_COLOR, font=utils.constants.FONT_MONO_LARGE,
                           text=f'X')

        consts.MAIN_DISPLAY.blit(surf, (consts.SCREEN_WIDTH / 2 - 200, consts.SCREEN_HEIGHT / 2 -
                                        (20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 5 + text_ccc.get_height() + 20)))
        btn_x = consts.SCREEN_WIDTH / 2 - 200 + 370
        btn_y = consts.SCREEN_HEIGHT / 2 - (20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 5 + text_ccc.get_height() + 20) + 0
        return btn_x, btn_y

    if plyr.has_reached_fight:
        edit_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 150,
                                                                   (consts.SCREEN_HEIGHT / 2) + 200),
                                 width=300, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=utils.constants.FONT_MONO_LARGE, text='Edit Fight Deck')
    else:
        edit_button = None
        edit_d_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 150,
                                                                     (consts.SCREEN_HEIGHT / 2) + 200),
                                   width=300, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.GREY_COLOR,
                                   font=utils.constants.FONT_MONO_LARGE, text='???')

    shop_button = ImageButton(surface=consts.MAIN_DISPLAY, pos=(5,
                                                                5),
                              width=70, height=70,
                              image_path=os.path.join(consts.ROOT_PATH, 'assets', 'images', 'textures', 'shop.png'))

    settings_button = ImageButton(surface=consts.MAIN_DISPLAY, pos=(730,
                                                                    5),
                                  width=70, height=70,
                                  image_path=os.path.join(consts.ROOT_PATH, 'assets', 'images', 'textures',
                                                          'settings.png'))
    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)

    is_game_over = False
    while not is_game_over:
        if plyr.has_informant:
            if plyr.games_played >= 4:
                # show modal
                plyr.games_played = None
                plyr.has_informant = False
                REL_COORDS = show_modal('Oh no!', 'Your informant has resigned!', 'You\'ll have to hire another one!')
                consts.DB.set_player_details(plyr)
        else:
            plyr.games_played = None
            consts.DB.set_player_details(plyr)

        mouse_down = False
        if not modal_showing:
            consts.MAIN_DISPLAY.blit(img, (0, 0))

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

        if play_button.hovered and not modal_showing:
            play_button.toggle_bg((0, 100, 0))
            if mouse_down:
                music_controller.play_click_normal()
                play_button.toggle_bg(colors.BROWN_COLOR)
                return explain_city.play()
        elif not modal_showing:
            play_button.toggle_bg(colors.BLACK_COLOR)

        if shop_button.hovered and not modal_showing:
            shop_button.reblit()
            if mouse_down:
                music_controller.play_click_normal()
                return shop.play()
        elif not modal_showing:
            shop_button.reblit()

        if settings_button.hovered and not modal_showing:
            settings_button.reblit()
            if mouse_down:
                music_controller.play_click_normal()
                return settings.play()
        elif not modal_showing:
            settings_button.reblit()

        if edit_button is None:
            edit_d_button.toggle_bg(colors.GREY_COLOR)
            if edit_d_button.hovered and not modal_showing:
                t = consts.FONT_MONO_SMALL.render('Play the game to find out what this is!', True, (0, 0, 0))
                consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH/2 -t.get_width()/2, 550))

        else:
            if edit_button.hovered and not modal_showing:
                edit_button.toggle_bg((0, 100, 0))
                if mouse_down:
                    music_controller.play_click_normal()
                    edit_button.toggle_bg(colors.RED_COLOR)
                    return edit_screen.play()
            elif not modal_showing:
                edit_button.toggle_bg(colors.BLACK_COLOR)

        if modal_showing:

            # NOTE: cant use .hovered here as .hovered is relative to the passed position with correspond to the
            #  main screen, not surface
            row, col = pygame.mouse.get_pos()

            if REL_COORDS[0] <= row <= REL_COORDS[0] + 30 and REL_COORDS[1] <= col <= REL_COORDS[1] + 30:
                x_btn.toggle_bg(colors.DARK_RED)
                if mouse_down:
                    modal_showing = False
            else:
                x_btn.toggle_ng(colors.RED_COLOR)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
