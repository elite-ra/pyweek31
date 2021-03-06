# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

if __name__ == "__main__":
    import sys

    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

import pygame

from ..utils import constants as consts
from ..utils.widgets import TextButton
from ..utils import colors
from . import home_screen
from .. import music_controller
from .. import utils
import os


def play():
    img = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'bg', 'bg_screen.png'))

    back = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                        (consts.SCREEN_HEIGHT / 2) - 300),
                      width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                      font=utils.constants.FONT_MONO_LARGE, text='<-')

    all_moves = consts.DB.get_all_moves()

    mv1_btn = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                           (consts.SCREEN_HEIGHT / 2) - 250 + 50),
                         width=308, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                         font=utils.constants.FONT_MONO_LARGE, text=f'{all_moves[0].name}')
    mv2_btn = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                           (consts.SCREEN_HEIGHT / 2) - 200 + 50),
                         width=308, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                         font=utils.constants.FONT_MONO_LARGE, text=f'{all_moves[1].name}')
    mv3_btn = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                           (consts.SCREEN_HEIGHT / 2) - 150 + 50),
                         width=308, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                         font=utils.constants.FONT_MONO_LARGE, text=f'{all_moves[2].name}')
    mv4_btn = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                           (consts.SCREEN_HEIGHT / 2) - 100 + 50),
                         width=308, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                         font=utils.constants.FONT_MONO_LARGE, text=f'{all_moves[3].name}')
    mv5_btn = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                           (consts.SCREEN_HEIGHT / 2) - 50 + 50),
                         width=308, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                         font=utils.constants.FONT_MONO_LARGE, text=f'{all_moves[4].name}')
    mv6_btn = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                           (consts.SCREEN_HEIGHT / 2) - 0 + 50),
                         width=308, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                         font=utils.constants.FONT_MONO_LARGE, text=f'{all_moves[5].name}')

    lock_moves = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 154,
                                                              consts.SCREEN_HEIGHT / 2 + 100 + 50), width=308,
                            height=40,
                            fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                            font=consts.FONT_MONO_SMALL_MEDIUM, text=f'Save move selection')

    mv_btns = [(all_moves[0].name, mv1_btn),
               (all_moves[1].name, mv2_btn),
               (all_moves[2].name, mv3_btn),
               (all_moves[3].name, mv4_btn),
               (all_moves[4].name, mv5_btn),
               (all_moves[5].name, mv6_btn)]

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    selected = []
    selc_moves = [mv.name for mv in consts.DB.get_player_moves()]

    for mv, mv_btn in mv_btns:
        if mv in selc_moves:
            selected.append(mv_btn)

    modal_showing = False
    x_btn = None

    def show_modal(title, text, color):
        nonlocal modal_showing
        modal_showing = True
        maj_sur = pygame.Surface((800, 600))
        maj_sur.set_alpha(180)
        maj_sur.fill(colors.BLACK_COLOR)
        consts.MAIN_DISPLAY.blit(maj_sur, (0, 0))
        text_a = consts.FONT_MONO_MEDIUM.render(title, True, color)
        text_b = consts.FONT_MONO_SMALL.render(text, True, (255, 255, 255))

        s = pygame.Surface((700,
                            20 + text_a.get_height() + 5 + text_b.get_height() + 20))

        s.blit(text_a, (20, 20))
        s.blit(text_b, (20, 20 + text_a.get_rect().height + 5))
        nonlocal x_btn
        x_btn = TextButton(surface=s, pos=(670, 0), width=30, height=30, fg_color=colors.WHITE_COLOR,
                           bg_color=colors.RED_COLOR, font=utils.constants.FONT_MONO_LARGE,
                           text=f'X')

        consts.MAIN_DISPLAY.blit(s, (consts.SCREEN_WIDTH / 2 - 350, consts.SCREEN_HEIGHT / 2 -
                                     (20 + text_a.get_height() + 5 + text_b.get_height() + 20)))
        btn_x = consts.SCREEN_WIDTH / 2 - 350 + 670
        btn_y = consts.SCREEN_HEIGHT / 2 - (20 + text_a.get_height() + 5 + text_b.get_height() + 20) + 0
        return btn_x, btn_y

    REL_COORDS = None
    while not is_game_over:
        if not modal_showing:
            consts.MAIN_DISPLAY.blit(img, (0, 0))
            t = consts.FONT_TITLE.render('Choose your moves for fighting', True, (255, 255, 255))
            w = t.get_rect().width
            consts.MAIN_DISPLAY.blit(t, ((800 - w) / 2, 60))

        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    music_controller.play_click_normal()
                    return home_screen.play()

        if back.hovered and not modal_showing:
            back.toggle_bg((128, 128, 128))
            if mouse_down:
                music_controller.play_click_normal()
                back.toggle_bg((128, 128, 128))
                # update volume bar
                return home_screen.play()
        elif not modal_showing:
            back.toggle_bg(colors.BLACK_COLOR)

        c = 0
        for mv, btn in mv_btns:
            if btn.hovered and not modal_showing:
                t_test1 = consts.FONT_MONO_SMALL.render(all_moves[c].description, True, (0, 0, 0))
                consts.MAIN_DISPLAY.blit(t_test1, (20, 525))

                btn.toggle_bg((128, 128, 128))
                if mouse_down:
                    music_controller.play_click_normal()
                    btn.toggle_bg(colors.GREEN_COLOR)
                    if btn in selected:
                        selected.remove(btn)
                    else:
                        selected.append(btn)
            elif not modal_showing:
                btn.toggle_bg(colors.BLACK_COLOR)
            c += 1
        for i in selected:
            if not modal_showing:
                i.toggle_bg(colors.GREEN_COLOR)

        if lock_moves.hovered and not modal_showing:
            lock_moves.toggle_bg((128, 128, 128))
            if mouse_down:
                music_controller.play_click_normal()
                lock_moves.toggle_bg((128, 128, 128))
                # save selction
                # check if too large
                if len(selected) > 4:
                    REL_COORDS = show_modal(title='Error!', text="Too many moves selcted! Maximum: 4", color=(100, 0, 0))

                elif len(selected) < 4:
                    REL_COORDS = show_modal(title='Error!', text="Too less moves selcted! Minimum: 4", color=(100, 0, 0))
                else:
                    # lock and save
                    plyr = consts.DB.get_player_details()

                    for i in selected:
                        # NOTE: HACK: sneaky, using TextButton.text as a parameter: DO NOT CHANGE Button text!
                        if i.text not in plyr.bought_moves + plyr.selected_moves:
                            REL_COORDS = show_modal(title='Error!', text=f"You haven't bought move '{i.text}', "
                                                                         f"Please go to the police dept!", color=(100, 0, 0))
                            break
                    else:
                        new_selection = [i.text for i in selected]

                        not_selected = [i.name for i in all_moves if i.name not in new_selection]

                        plyr.selected_moves = new_selection
                        plyr.bought_moves = not_selected

                        consts.DB.set_player_details(plyr)

                        REL_COORDS = show_modal(title='Saved!', text=f"Saved your moves!", color=(0, 100, 0))

        elif not modal_showing:
            lock_moves.toggle_bg(colors.BLACK_COLOR)

        if modal_showing:
            # NOTE: cant use .hovered here as .hovered is relative to the passed position with correspond to the
            #  main screen, not surface
            row, col = pygame.mouse.get_pos()

            if REL_COORDS[0] <= row <= REL_COORDS[0] + 30 and REL_COORDS[1] <= col <= REL_COORDS[1] + 30:

                if mouse_down:
                    modal_showing = False

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
