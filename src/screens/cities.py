# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Ayush Gupta

if __name__ == "__main__":
    import sys

    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

import pygame

from .. import utils
from ..main_logic import Game
from . import chase
from . import end_screen
from ..utils.widgets import TextButton
from ..utils import constants as consts
import os
from . import home_screen
from .. import music_controller


def play():
    city_coords = [[(545, 425), (64, 30)], [(155, 245), (64, 30)], [(350, 365), (77, 30)], [(150, 445), (125, 30)],
                   [(550, 278), (63, 30)]]

    cities_list = utils.models.City.get_all_cities()

    bg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'cities.png'))

    coin_limit = 25000

    show_city = False

    def city_name(name, x, y):
        font = utils.constants.FONT_MONO_MEDIUM
        text = font.render(name, True, (0, 0, 0))
        utils.constants.MAIN_DISPLAY.blit(text, (x, y))

    stats_showing = False
    tada = True

    game_obj = Game()

    running = True
    true_city_t = 'a'
    while running:

        pygame.display.update()
        utils.constants.MAIN_DISPLAY.blit(bg, (0, 0))
        mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    music_controller.play_click_normal()
                    return home_screen.play()


        # Draw coins stolen
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect(0, 550, 800, 50))
        font = utils.constants.FONT_MONO_SMALL
        current_coins = game_obj.total_coins_stolen
        coins_stolen_text = font.render(f'Coins stolen ({current_coins}/{coin_limit})', True, (255, 255, 255))
        # losing condition
        if current_coins >= coin_limit:
            return end_screen.end_screen_func(1)
        w = coins_stolen_text.get_rect().width
        utils.constants.MAIN_DISPLAY.blit(coins_stolen_text, (100 + (600 - w) / 2, 555))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (200, 200, 200), pygame.Rect(120, 575, 560, 10))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (255, 215, 0),
                         pygame.Rect(120, 575, (current_coins / coin_limit) * 560, 10))

        # Draw robber statistics
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect(0, 0, 800, 140))  # rectangle up top
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (255, 255, 255), pygame.Rect(2, 2, 796, 136), 1)
        font = utils.constants.FONT_MONO_MEDIUM
        text = font.render('Robber Stats', True, (200, 200, 200))
        font = utils.constants.FONT_MONO_SMALL
        w = text.get_rect().width
        utils.constants.MAIN_DISPLAY.blit(text, ((800 - w) / 2, 5))
        # the following takes the str from Game and pretty formats it to blit
        random_string = str(game_obj)
        temp = 0
        # the following takes the str from Game and pretty formats it to blit

        for i in random_string.split('\n'):
            text = font.render(i, True, (200, 200, 200))
            w = text.get_rect().width
            utils.constants.MAIN_DISPLAY.blit(text, ((800 - w) / 2 - 10, 40 + temp * 20))
            temp += 1

        text = consts.FONT_MONO_SMALL.render('Choose which city the robber is going to go to:', True, (200, 200, 200))
        utils.constants.MAIN_DISPLAY.blit(text, (20, 120))

        for i, a, b in zip([pygame.Rect(a, b) for [a, b] in city_coords], cities_list, city_coords):

            if pygame.mouse.get_pressed()[0]:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (i.collidepoint(x, y)):
                    music_controller.play_click_normal()
                    show_city = True

                if pygame.mouse.get_pressed()[0] and i.collidepoint(x, y):
                    true_city = i
                    true_city_t = a
                    true_b = b

            pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), i, 2)
            city_name(a.name, b[0][0] + 2, b[0][1] + 2)

            if show_city:
                pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), true_city, 2)
                pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 255, 0), true_city)
                city_name(true_city_t.name, true_b[0][0] + 2, true_b[0][1] + 2)
                choose_city = TextButton(surface=consts.MAIN_DISPLAY, pos=(600,
                                                                           500),
                                         width=150, height=20, fg_color=(0, 0, 0), bg_color=(0, 255, 0),
                                         font=utils.constants.FONT_MONO_SMALL,
                                         text='Check if the robber is in this city')

            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if i.collidepoint(x, y) and not stats_showing and a != true_city_t:
                stats_showing = a

                mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

                text_a = utils.constants.FONT_MONO_SMALL.render(str(stats_showing).split('\n')[0], True,
                                                                (255, 255, 255))
                text_b = utils.constants.FONT_MONO_SMALL.render(str(stats_showing).split('\n')[1], True,
                                                                (255, 255, 255))
                text_c = utils.constants.FONT_MONO_SMALL.render(str(stats_showing).split('\n')[2], True,
                                                                (255, 255, 255))
                text_d = utils.constants.FONT_MONO_SMALL.render(str(stats_showing).split('\n')[3], True,
                                                                (255, 255, 255))
                text_e = utils.constants.FONT_MONO_SMALL.render(str(stats_showing).split('\n')[4], True,
                                                                (255, 255, 255))
                text_f = utils.constants.FONT_MONO_SMALL.render(str(stats_showing).split('\n')[5], True,
                                                                (255, 255, 255))

                s = pygame.Surface((300,
                                    5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                    text_c.get_rect().height + 5 + text_d.get_rect().height + 5 +
                                    text_e.get_rect().height + 5 + text_f.get_height() + 5))

                s.blit(text_a, (5, 0))
                s.blit(text_b, (5, 5 + text_a.get_rect().height + 5))
                s.blit(text_c, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5))
                s.blit(text_d, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                text_c.get_rect().height + 5))
                s.blit(text_e, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                text_c.get_rect().height + 5 + text_d.get_rect().height + 5))
                s.blit(text_f, (5, 5 + text_a.get_rect().height + 5 + text_b.get_rect().height + 5 +
                                text_c.get_rect().height + 5 + text_d.get_rect().height + 5 +
                                text_e.get_rect().height + 5))

                if mx + 300 <= 800:
                    utils.constants.MAIN_DISPLAY.blit(s, (mx, my))

                else:
                    utils.constants.MAIN_DISPLAY.blit(s, (mx - 300, my))

            if not i.collidepoint(x, y) and stats_showing:
                stats_showing = False

        if show_city:
            if choose_city.hovered:
                choose_city.toggle_bg((0, 100, 0))
                if mouse_down:
                    music_controller.play_click_woop()
                    do_chase, skill_level = game_obj.play_turn(true_city_t)
                    if do_chase:
                        s = pygame.Surface((800, 600))  # the size of your rect
                        s.set_alpha(240)  # alpha level
                        s.fill((0, 0, 0))  # this fills the entire surface
                        utils.constants.MAIN_DISPLAY.blit(s, (0, 0))  # (0,0) are the top-left coordinates
                        font = utils.constants.FONT_MONO_VERY_LARGE
                        text = font.render('You found the robber!', True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (170, 200))
                        font = utils.constants.FONT_MONO_MEDIUM
                        text = font.render('The robber is trying to run away.', True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (170, 300))
                        text = font.render('Chase him till his fuel runs out!', True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (170, 350))
                        text = font.render("Use 'W', 'S' or arrow keys to navigate ", True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (140, 400))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        return chase.play(skill_level, true_city_t.name)

                    else:
                        s = pygame.Surface((800, 600))  # the size of your rect
                        s.set_alpha(240)  # alpha level
                        s.fill((0, 0, 0))  # this fills the entire surface
                        utils.constants.MAIN_DISPLAY.blit(s, (0, 0))  # (0,0) are the top-left coordinates
                        font = utils.constants.FONT_MONO_VERY_LARGE
                        text = font.render('You guessed wrong!!', True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (200, 200))
                        text = font.render('Try again', True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (300, 300))
                        pygame.display.update()
                        pygame.time.wait(1000)

        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
