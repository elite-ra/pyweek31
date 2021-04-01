# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import pygame

from . import chase
from . import cities
from ..utils import constants as consts
from ..utils.widgets import TextButton
from ..utils import colors
from .. import utils
from . import home_screen
from ..utils import database

# TODO: show message on hover on button.


# settings screen
def play():

    plyr = consts.DB.get_player_details()
    allmoe = consts.DB.get_all_moves()
    allmove = [move for move in allmoe if not move.is_intial]

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    no_coins = False
    is_game_over = False
    back = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 400,
                                                        (consts.SCREEN_HEIGHT / 2) - 300),
                      width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                      font=pygame.font.Font('freesansbold.ttf', 30), text='<-')

    while not is_game_over:
        if not no_coins:
            utils.constants.MAIN_DISPLAY.fill((255, 255, 255))

            informant = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                     (consts.SCREEN_HEIGHT / 2) + 100),
                                   width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                   font=pygame.font.Font('freesansbold.ttf', 30), text='INFORMANT')

            if consts.DB.get_player_details().has_reached_fight:
                bm1 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 250,
                                                                   (consts.SCREEN_HEIGHT / 2) - 100),
                                 width=500, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=pygame.font.Font('freesansbold.ttf', 30), text=f'Buy New Move: {allmove[0].name}')
                bm2 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 250,
                                                                   (consts.SCREEN_HEIGHT / 2) + 0),
                                 width=500, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BLACK_COLOR,
                                 font=pygame.font.Font('freesansbold.ttf', 30), text=f'Buy New Move: {allmove[1].name}')
            else:
                bm1 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 250,
                                                                   (consts.SCREEN_HEIGHT / 2) - 100),
                                 width=500, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.GREY_COLOR,
                                 font=pygame.font.Font('freesansbold.ttf', 30), text=f'???')
                bm2 = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 250,
                                                                   (consts.SCREEN_HEIGHT / 2) + 0),
                                 width=500, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.GREY_COLOR,
                                 font=pygame.font.Font('freesansbold.ttf', 30), text=f'???')

        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if informant.hovered and not no_coins:
            informant.toggle_bg(colors.BROWN_COLOR)
            if mouse_down:
                informant.toggle_bg(colors.BROWN_COLOR)
                # check coins
                if plyr.coins < 150:
                    s = pygame.Surface((800, 600))  # the size of your rect
                    s.set_alpha(240)  # alpha level
                    s.fill((0, 0, 0))  # this fills the entire surface
                    consts.MAIN_DISPLAY.blit(s, (0, 0))
                    t = consts.FONT_MONO_MEDIUM.render("You don't have enough coins!", True, (255, 255, 255))
                    utils.constants.MAIN_DISPLAY.blit(t, (10, 10))
                    no_coins = True
                else:
                    plyr = consts.DB.get_player_details()
                    if plyr.has_informant:
                        s = pygame.Surface((800, 600))  # the size of your rect
                        s.set_alpha(240)  # alpha level
                        s.fill((0, 0, 0))  # this fills the entire surface
                        consts.MAIN_DISPLAY.blit(s, (0, 0))
                        t = consts.FONT_MONO_MEDIUM.render("You already have this upgrade", True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(t, (10, 10))
                        no_coins = True
                    else:
                        s = pygame.Surface((800, 600))  # the size of your rect
                        s.fill((0, 0, 0))  # this fills the entire surface
                        consts.MAIN_DISPLAY.blit(s, (0, 0))
                        t = consts.FONT_MONO_MEDIUM.render("Bought!", True, (100, 100, 100))
                        consts.MAIN_DISPLAY.blit(t, (50, 100))
                        plyr.has_informant = True
                        plyr.coins -= 150
                        consts.DB.set_player_details(plyr)
                        no_coins = True
        else:
            informant.toggle_bg(colors.BLACK_COLOR)

        if consts.DB.get_player_details().has_reached_fight:
            if bm1.hovered and not no_coins:
                bm1.toggle_bg(colors.BROWN_COLOR)
                if mouse_down:
                    bm1.toggle_bg(colors.BROWN_COLOR)
                    # check coins
                    if plyr.coins < allmove[0].price:
                        s = pygame.Surface((800, 600))  # the size of your rect
                        s.set_alpha(240)  # alpha level
                        s.fill((0, 0, 0))  # this fills the entire surface
                        consts.MAIN_DISPLAY.blit(s, (0, 0))
                        t = consts.FONT_MONO_MEDIUM.render("You don't have enough coins!", True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(t, (10, 10))
                        no_coins = True
                    else:
                        if allmove[0].name in plyr.bought_moves:
                            s = pygame.Surface((800, 600))  # the size of your rect
                            s.set_alpha(240)  # alpha level
                            s.fill((0, 0, 0))  # this fills the entire surface
                            consts.MAIN_DISPLAY.blit(s, (0, 0))
                            t = consts.FONT_MONO_MEDIUM.render("You already have this upgrade", True, (255, 255, 255))
                            utils.constants.MAIN_DISPLAY.blit(t, (10, 10))
                            no_coins = True
                        else:
                            s = pygame.Surface((800, 600))  # the size of your rect
                            s.fill((0, 0, 0))  # this fills the entire surface
                            consts.MAIN_DISPLAY.blit(s, (0, 0))
                            t = consts.FONT_MONO_MEDIUM.render("Bought!", True, (100, 100, 100))
                            consts.MAIN_DISPLAY.blit(t, (50, 100))
                            plyr = consts.DB.get_player_details()
                            plyr.bought_moves.append(allmove[0].name)
                            plyr.coins -= allmove[0].price
                            consts.DB.set_player_details(plyr)
                            no_coins = True
            else:
                bm1.toggle_bg(colors.BLACK_COLOR)

        if consts.DB.get_player_details().has_reached_fight:
            if bm2.hovered and not no_coins:
                bm2.toggle_bg(colors.BROWN_COLOR)
                if mouse_down:
                    bm2.toggle_bg(colors.BROWN_COLOR)
                    # check coins
                    if plyr.coins < allmove[1].price:
                        s = pygame.Surface((800, 600))  # the size of your rect
                        s.set_alpha(240)  # alpha level
                        s.fill((0, 0, 0))  # this fills the entire surface
                        consts.MAIN_DISPLAY.blit(s, (0, 0))
                        t = consts.FONT_MONO_MEDIUM.render("You don't have enough coins!", True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(t, (10, 10))
                        no_coins = True
                    else:
                        if allmove[1].name in plyr.bought_moves:
                            s = pygame.Surface((800, 600))  # the size of your rect
                            s.set_alpha(240)  # alpha level
                            s.fill((0, 0, 0))  # this fills the entire surface
                            consts.MAIN_DISPLAY.blit(s, (0, 0))
                            t = consts.FONT_MONO_MEDIUM.render("You already have this upgrade", True, (255, 255, 255))
                            utils.constants.MAIN_DISPLAY.blit(t, (10, 10))
                            no_coins = True
                        else:
                            s = pygame.Surface((800, 600))  # the size of your rect
                            s.fill((0, 0, 0))  # this fills the entire surface
                            consts.MAIN_DISPLAY.blit(s, (0, 0))
                            t = consts.FONT_MONO_MEDIUM.render("Bought!", True, (100, 100, 100))
                            consts.MAIN_DISPLAY.blit(t, (50, 100))
                            plyr = consts.DB.get_player_details()
                            plyr.bought_moves.append(allmove[1].name)
                            plyr.coins -= allmove[1].price
                            consts.DB.set_player_details(plyr)
                            no_coins = True
            else:
                bm2.toggle_bg(colors.BLACK_COLOR)

        if no_coins:
            # show X
            txx = consts.FONT_MONO_LARGE.render('X', True, (255, 0, 0))
            consts.MAIN_DISPLAY.blit(txx, (100, 100))
            tx = 100
            ty = 100

            if mouse_down:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if (tx <= x <= tx + txx.get_width()) and (ty <= y <= ty + txx.get_height()):
                    no_coins = False
                else:
                    no_coins = True

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
