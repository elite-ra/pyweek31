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
from .. import utils
from . import home_screen
from .. import music_controller
import os


# settings screen
def play():
    plyr = consts.DB.get_player_details()
    allmoe = consts.DB.get_all_moves()
    allmove = [move for move in allmoe if not move.is_intial]

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    no_coins = False
    is_game_over = False

    modal_showing = False
    x_btn = None

    def show_modal(title, text):

        nonlocal modal_showing
        modal_showing = True
        maj_sur = pygame.Surface((800, 600))
        maj_sur.set_alpha(180)
        maj_sur.fill(colors.BLACK_COLOR)
        consts.MAIN_DISPLAY.blit(maj_sur, (0, 0))
        text_aaa = consts.FONT_MONO_MEDIUM.render(title, True, (255, 255, 255))
        text_bbb = consts.FONT_MONO_SMALL.render(text, True, (255, 255, 255))

        surf = pygame.Surface((500,
                               20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20))

        surf.blit(text_aaa, (20, 20))
        surf.blit(text_bbb, (20, 20 + text_aaa.get_rect().height + 5))
        nonlocal x_btn
        x_btn = TextButton(surface=surf, pos=(470, 0), width=30, height=30, fg_color=colors.WHITE_COLOR,
                           bg_color=colors.RED_COLOR, font=utils.constants.FONT_MONO_LARGE,
                           text=f'X')

        consts.MAIN_DISPLAY.blit(surf, (consts.SCREEN_WIDTH / 2 - 250, consts.SCREEN_HEIGHT / 2 -
                                        (20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20)))
        btn_x = consts.SCREEN_WIDTH / 2 - 250 + 470
        btn_y = consts.SCREEN_HEIGHT / 2 - (20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20) + 0
        return btn_x, btn_y

    REL_COORDS = None

    back = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                        (consts.SCREEN_HEIGHT / 2) - 300),
                      width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                      font=utils.constants.FONT_MONO_LARGE, text='<-')

    while not is_game_over:

        if not modal_showing:
            img = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'bg', 'bg_screen.png'))
            consts.MAIN_DISPLAY.blit(img, (0, 0))

            t = consts.FONT_TITLE.render('Police Department', True, (255, 255, 255))
            w = t.get_rect().width
            consts.MAIN_DISPLAY.blit(t, ((800 - w) / 2, 60))

            informant = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 250,
                                                                     (consts.SCREEN_HEIGHT / 2) + 100),
                                   width=500, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                   font=utils.constants.FONT_MONO_LARGE, text='Informant | 400')

            if consts.DB.get_player_details().has_reached_fight:
                bm1 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 350,
                                                                   (consts.SCREEN_HEIGHT / 2) - 100),
                                 width=700, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=utils.constants.FONT_MONO_LARGE, text=f'Buy New Move: {allmove[0].name} '
                                                                            f'| {allmove[0].price}')
                bm2 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 350,
                                                                   (consts.SCREEN_HEIGHT / 2) + 0),
                                 width=700, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=utils.constants.FONT_MONO_LARGE, text=f'Buy New Move: {allmove[1].name} '
                                                                            f'| {allmove[1].price}')
            else:
                bm1 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 350,
                                                                   (consts.SCREEN_HEIGHT / 2) - 100),
                                 width=700, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.GREY_COLOR,
                                 font=utils.constants.FONT_MONO_LARGE, text=f'???')
                bm2 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 350,
                                                                   (consts.SCREEN_HEIGHT / 2) + 0),
                                 width=700, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.GREY_COLOR,
                                 font=utils.constants.FONT_MONO_LARGE, text=f'???')

            t = consts.FONT_MONO_MEDIUM.render(f'{plyr.coins}', True, (255, 215, 0))
            consts.MAIN_DISPLAY.blit(t, (711, 10))
            consts.MAIN_DISPLAY.blit(consts.COIN_TRIPLE_IMG, (650, 10))

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
                back.toggle_bg((128, 128, 128))
                # update volume bar
                return home_screen.play()
        elif not modal_showing:
            back.toggle_bg(colors.BLACK_COLOR)

        if informant.hovered and not modal_showing:
            informant.toggle_bg((128, 128, 128))
            if not mouse_down:
                mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

                text_a = consts.FONT_MONO_MEDIUM.render('Informant!', True, (255, 255, 255))
                text_b = consts.FONT_MONO_SMALL.render('Hire an informant. The informant', True, (255, 255, 255))
                text_c = consts.FONT_MONO_SMALL.render('reveals more details about the robber.', True, (255, 255, 255))
                text_d = consts.FONT_MONO_SMALL.render('Cost: 400 coins', True, (255, 255, 255))

                s = pygame.Surface((400,
                                    5 + text_a.get_height() + 5 + text_b.get_height() + 5 + text_c.get_height() + 5 + text_d.get_height() + 5))

                s.blit(text_a, (5, 0))
                s.blit(text_b, (5, 5 + text_a.get_rect().height + 5))
                s.blit(text_c, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5))
                s.blit(text_d, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                text_c.get_rect().height + 5))
                consts.MAIN_DISPLAY.blit(s, (mx, my))

            else:
                informant.toggle_bg((128, 128, 128))
                # check coins
                if plyr.coins < 400 and not plyr.has_informant:
                    REL_COORDS = show_modal(title='Error!', text=f"You not have enough coin!")
                else:
                    plyr = consts.DB.get_player_details()
                    if plyr.has_informant:
                        REL_COORDS = show_modal(title="Error!", text="You already have this upgrade!")
                    else:
                        plyr = consts.DB.get_player_details()
                        plyr.games_played = 0
                        consts.DB.set_player_details(plyr)

                        REL_COORDS = show_modal(title="Done!", text="You hired an informant!")
                        plyr = consts.DB.get_player_details()
                        plyr.has_informant = True
                        plyr.coins -= 400
                        consts.DB.set_player_details(plyr)
        elif not modal_showing:
            informant.toggle_bg(colors.BLACK_COLOR)

        if consts.DB.get_player_details().has_reached_fight:
            if bm1.hovered and not modal_showing:

                bm1.toggle_bg((128, 128, 128))

                if not mouse_down:
                    mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

                    text_a = consts.FONT_MONO_MEDIUM.render(f'{allmove[0].name}', True, (255, 255, 255))
                    text_b = consts.FONT_MONO_SMALL.render(f'Buy the "{allmove[0].name}" move', True, (255, 255, 255))
                    text_c = consts.FONT_MONO_SMALL.render(f'{allmove[0].description}', True, (255, 255, 255))
                    text_d = consts.FONT_MONO_SMALL.render(f'Cost: {allmove[0].price} coins', True, (255, 255, 255))

                    s = pygame.Surface((400,
                                        5 + text_a.get_height() + 5 + text_b.get_height() + 5 + text_c.get_height() + 5 + text_d.get_height() + 5))

                    s.blit(text_a, (5, 0))
                    s.blit(text_b, (5, 5 + text_a.get_rect().height + 5))
                    s.blit(text_c, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5))
                    s.blit(text_d, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                    text_c.get_rect().height + 5))
                    consts.MAIN_DISPLAY.blit(s, (mx, my))

                    pygame.display.update()
                else:
                    bm1.toggle_bg((128, 128, 128))
                    # check coins
                    if plyr.coins < allmove[0].price:
                        REL_COORDS = show_modal(title='Error!', text=f"You not have enough coin!")
                    else:
                        if allmove[0].name in plyr.bought_moves + plyr.selected_moves:
                            REL_COORDS = show_modal(title="Error!", text="You already have this upgrade!")
                        else:
                            REL_COORDS = show_modal(title="Done!", text="You got the move!")
                            plyr = consts.DB.get_player_details()
                            plyr.bought_moves.append(allmove[0].name)
                            plyr.coins -= allmove[0].price
                            consts.DB.set_player_details(plyr)
            elif not modal_showing:
                bm1.toggle_bg(colors.BLACK_COLOR)
        else:
            if bm1.hovered:
                t = consts.FONT_MONO_SMALL.render('Play the game to find out what this is!', True, (0, 0, 0))
                consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH / 2 - t.get_width() / 2, 550))

        if consts.DB.get_player_details().has_reached_fight:
            if bm2.hovered and not modal_showing:

                if not mouse_down:
                    mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    bm2.toggle_bg((128, 128, 128))
                    text_a = consts.FONT_MONO_MEDIUM.render(f'{allmove[1].name}', True, (255, 255, 255))
                    text_b = consts.FONT_MONO_SMALL.render(f'Buy the "{allmove[1].name}" move', True, (255, 255, 255))
                    text_c = consts.FONT_MONO_SMALL.render(f'{allmove[1].description}', True, (255, 255, 255))
                    text_d = consts.FONT_MONO_SMALL.render(f'Cost: {allmove[1].price} coins', True, (255, 255, 255))

                    s = pygame.Surface((400,
                                        5 + text_a.get_height() + 5 + text_b.get_height() + 5 + text_c.get_height() + 5 + text_d.get_height() + 5))

                    s.blit(text_a, (5, 0))
                    s.blit(text_b, (5, 5 + text_a.get_rect().height + 5))
                    s.blit(text_c, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5))
                    s.blit(text_d, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                    text_c.get_rect().height + 5))
                    consts.MAIN_DISPLAY.blit(s, (mx, my))

                    pygame.display.update()
                else:

                    bm2.toggle_bg((128, 128, 128))
                    # check coins
                    if plyr.coins < allmove[1].price:
                        REL_COORDS = show_modal(title='Error!', text=f"You not have enough coin!")
                    else:
                        if allmove[1].name in plyr.bought_moves + plyr.selected_moves:
                            REL_COORDS = show_modal(title="Error!", text="You already have this upgrade!")
                        else:
                            REL_COORDS = show_modal(title="Done!", text="You got the move!")
                            plyr = consts.DB.get_player_details()
                            plyr.bought_moves.append(allmove[1].name)
                            plyr.coins -= allmove[1].price
                            consts.DB.set_player_details(plyr)
            elif not modal_showing:
                bm2.toggle_bg(colors.BLACK_COLOR)
        else:
            if bm2.hovered:
                t = consts.FONT_MONO_SMALL.render('Play the game to find out what this is!', True, (0, 0, 0))
                consts.MAIN_DISPLAY.blit(t, (consts.SCREEN_WIDTH / 2 - t.get_width() / 2, 550))

        if modal_showing:

            # NOTE: cant use .hovered here as .hovered is relative to the passed position with correspond to the
            #  main screen, not surface
            row, col = pygame.mouse.get_pos()

            if REL_COORDS[0] <= row <= REL_COORDS[0] + 30 and REL_COORDS[1] <= col <= REL_COORDS[1] + 30:
                if mouse_down:
                    modal_showing = False

        if (consts.DB.get_player_details().has_reached_fight and bm1.hovered and not modal_showing) or \
                (consts.DB.get_player_details().has_reached_fight and bm2.hovered and not modal_showing):
            pass
        else:
            pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
