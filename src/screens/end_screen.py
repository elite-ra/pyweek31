# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Ayush Gupta

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

from . import home_screen
import pygame
from ..utils.widgets import TextButton
from ..utils import constants as consts
from .. import music_controller


def end_screen_func(a):
    running = True
    plyr = consts.DB.get_player_details()
    if plyr.has_informant:
        plyr.games_played += 1
    consts.DB.set_player_details(plyr)

    while running:

        mouse_down = False
        consts.MAIN_DISPLAY.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    music_controller.play_click_normal()
                    return home_screen.play()

        font = consts.FONT_MONO_LARGE
        # coins limit reached
        if a == 1:
            text = font.render('The robber stole too much!', True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2) - 100))
            text = font.render('Better luck next time!', True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        # bird strike
        elif a == 2:
            text = font.render("You were hit by the robber's missile!", True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)-40))
            text = font.render('The robber got away!', True, (255, 255, 255))
            w, h = text.get_rect().width, text.get_rect().height
            consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        # losing in fight
        elif a == 3:
            text = font.render('The robber defeated you!', True, (255, 255, 255))
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
                music_controller.play_click_normal()
                return home_screen.play()

        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
