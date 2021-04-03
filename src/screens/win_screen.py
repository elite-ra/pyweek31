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


def play():

    # GIVE COINS
    plyr = consts.DB.get_player_details()
    plyr.coins += 150
    consts.DB.set_player_details(plyr)

    running = True

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
        # they get em coins.

        text = font.render('You caught the robber! You get 150 coins!', True, (255, 255, 255))
        w, h = text.get_rect().width, text.get_rect().height
        consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        city_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                   (consts.SCREEN_HEIGHT / 2) + 100),
                                 width=200, height=40, fg_color=(0, 0, 0), bg_color=(255, 0, 0),
                                 font=consts.FONT_MONO_LARGE, text='Home')

        if city_button.hovered:
            city_button.toggle_bg((139, 0, 0))
            if mouse_down:
                city_button.toggle_bg((255, 0, 0))
                return home_screen.play()

        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
