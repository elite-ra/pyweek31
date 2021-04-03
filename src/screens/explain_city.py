# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

from . import home_screen
import pygame
from ..utils.widgets import TextButton
from ..utils import constants as consts
from . import cities
from .. import music_controller


def play():
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

        # You are faces with details about a robber, and a few cities which the robber goes to.
        # The game's objective is to guess the city the robber is going to go to on the next turn.
        #
        # All of the robbers follow certain rules.
        #
        # 1) They must change cities after every move.
        # 2) They lose a certain amount of health during every turn.
        # 3) If their health drops below a fixed threshold, they have to go to a city with a hospital.
        # 4) If they have stolen an artefact they will prefer a city with a black market but will prioritize going to
        # a hospital if no city is available with both and health is below the threshold.
        #
        # Robbers don't follow the same pattern each time, they may prefer banks or, museums, or something else!
        #
        # The information regarding black market is hidden initially and can be unlocked by buying an informant from
        # the shop by using the coins gotten from the later stages of the game.

        explanation = '''City Choosing Explanation:

You are faced with details about a robber, and a few cities which the robber goes to.
The game's objective is to guess the city the robber is going to go to on the next turn.

All of the robbers follow certain rules.

1) They must change cities after every move.
2) They lose a certain amount of health during every turn.
3) If their health drops below a fixed threshold, they have to go to a city with a 
   hospital.
4) If they have stolen an artefact they will prefer a city with a black market but will 
   prioritize going to a hospital if no city is available with both and health is below 
   the threshold.

Robbers don't follow the same pattern each time, they may prefer banks or, museums, or 
something else!

The information regarding black market is hidden initially and can be unlocked by buying 
an informant from the shop by using the coins gotten from the later stages of the game.'''

        font = consts.FONT_MONO_SMALL
        text = font.render('', True, (255, 255, 255))
        w, h = text.get_rect().width, text.get_rect().height
        consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        city_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                   (consts.SCREEN_HEIGHT / 2) + 200),
                                 width=200, height=40, fg_color=(0, 0, 0), bg_color=(255, 0, 0),
                                 font=consts.FONT_MONO_LARGE, text='Continue')

        font = consts.FONT_MONO_MEDIUM
        text = font.render(explanation.split('\n')[0], True, (200, 200, 200))
        w = text.get_rect().width
        consts.MAIN_DISPLAY.blit(text, ((800-w)/2, 10))
        temp = 1
        font = consts.FONT_MONO_SMALL
        for i in explanation.split('\n')[1:]:
            text = font.render(i, True, (200, 200, 200))
            consts.MAIN_DISPLAY.blit(text, (5, 10 + temp * 20))
            temp += 1
        if city_button.hovered:
            city_button.toggle_bg((139, 0, 0))
            if mouse_down:
                city_button.toggle_bg((255, 0, 0))
                music_controller.play_click_normal()
                return cities.play()


        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)