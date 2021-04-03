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

        explanation = '''You are on the robber's tail! But... where is he now?

Guess which city the robber the robber is now - he moves cities after every theft.

Tips: If his health is low, he needs a hospital, 
      and if he needs to sell his stolen goods, 
      he will try to sell it on a black market.
      
Remember, The robber may suprise you!

Hire an informant from the police department to get more information about the robber.
'''

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
        consts.MAIN_DISPLAY.blit(text, ((800-w)/2 + 20, 10))
        temp = 1
        font = consts.FONT_MONO_SMALL
        for i in explanation.split('\n')[1:]:
            text = font.render(i, True, (200, 200, 200))
            consts.MAIN_DISPLAY.blit(text, (20, 10 + temp * 20))
            temp += 1
        if city_button.hovered:
            city_button.toggle_bg((139, 0, 0))
            if mouse_down:
                city_button.toggle_bg((255, 0, 0))
                music_controller.play_click_normal()
                return cities.play()

        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
