# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Ayush Gupta

import pygame

from .. import utils
from ..main_logic import Game
from . import chase
from . import home_screen

import os


def play():
    city_coords = [[(545, 425), (64, 30)], [(155, 245), (64, 30)], [(350, 365), (77, 30)], [(150, 445), (125, 30)],
                   [(550, 278), (63, 30)]]

    cities_list = utils.models.City.get_all_cities()

    bg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'cities.png'))

    coin_limit = 50000

    mouse_pressed = False

    def city_name(name, x, y):
        font = utils.constants.FONT_MONO_MEDIUM
        text = font.render(name, True, (0, 0, 0))
        utils.constants.MAIN_DISPLAY.blit(text, (x, y))

    stats_showing = False

    game_obj = Game()

    running = True
    while running:

        utils.constants.MAIN_DISPLAY.fill((0, 255, 255))
        utils.constants.MAIN_DISPLAY.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Coins stolen
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect(0, 550, 800, 50))
        font = utils.constants.FONT_MONO_SMALL
        current_coins = game_obj.total_coins_stolen
        text = font.render(f'Coins stolen({current_coins}/{coin_limit})', True, (255, 255, 255))
        # losing condition
        if current_coins >= 50000:
            pass
        w = text.get_rect().width
        utils.constants.MAIN_DISPLAY.blit(text, (100 + (600 - w) / 2, 555))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (200, 200, 200), pygame.Rect(120, 575, 560, 10))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (255, 215, 0),
                         pygame.Rect(120, 575, (current_coins / coin_limit) * 560, 10))

        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect(0, 0, 800, 90))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (255, 255, 255), pygame.Rect(2, 2, 796, 86), 1)
        font = utils.constants.FONT_MONO_MEDIUM
        text = font.render('Robber Stats', True, (200, 200, 200))
        font = utils.constants.FONT_MONO_SMALL
        w = text.get_rect().width
        utils.constants.MAIN_DISPLAY.blit(text, ((800 - w) / 2, 5))
        random_string = str(game_obj)
        temp = 0
        for i in random_string.split('\n'):
            text = font.render(i, True, (200, 200, 200))
            utils.constants.MAIN_DISPLAY.blit(text, (30, 30 + temp * 20))
            temp += 1

        for i, a, b in zip([pygame.Rect(a, b) for [a, b] in city_coords], cities_list, city_coords):
            pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), i, 2)
            city_name(a.name, b[0][0] + 2, b[0][1] + 2)
            if pygame.mouse.get_pressed()[0]:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if i.collidepoint(x, y) and not stats_showing:
                    stats_showing = a
                if pygame.Rect((620, 200), (30, 30)).collidepoint(x, y) and stats_showing:
                    stats_showing = False
            if pygame.mouse.get_pressed()[2] and not stats_showing:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if i.collidepoint(x, y) and not mouse_pressed:
                    # 'a' is the city name and this condition means that there was a right click on the city name
                    # Change scene to chase
                    do_chase, skill_level = game_obj.play_turn(a)
                    #print(do_chase, skill_level, game_obj.current_robber_location.name)
                    mouse_pressed = True
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
                        font = utils.constants.FONT_MONO_MEDIUM
                        text = font.render('Chase him till his fuel runs out!', True, (255, 255, 255))
                        utils.constants.MAIN_DISPLAY.blit(text, (170, 350))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        return chase.play(skill_level)

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


            else:
                mouse_pressed = False

        if stats_showing:
            s = pygame.Surface((800, 600))  # the size of your rect
            s.set_alpha(128)  # alpha level
            s.fill((0, 0, 0))  # this fills the entire surface
            utils.constants.MAIN_DISPLAY.blit(s, (0, 0))  # (0,0) are the top-left coordinates
            pygame.draw.rect(utils.constants.MAIN_DISPLAY, (255, 255, 255), pygame.Rect((150, 200), (500, 200)))
            pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect((150, 200), (500, 200)), 2)
            font = utils.constants.FONT_MONO_LARGE
            text = font.render(stats_showing.name, True, (0, 0, 0))
            w = text.get_rect().width
            utils.constants.MAIN_DISPLAY.blit(text, (150 + (500 - w) / 2, 205))

            font = utils.constants.FONT_MONO_SMALL
            temp = 0
            for condition in str(stats_showing).split('\n'):
                text = font.render(condition, True, (0, 0, 0))
                utils.constants.MAIN_DISPLAY.blit(text, (190, 250 + temp * 20))
                temp += 1

            # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((446, 480), (54, 20)))
            pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect((620, 200), (30, 30)), 1)
            font = utils.constants.FONT_MONO_MEDIUM
            text = font.render('X', True, (255, 0, 0))
            utils.constants.MAIN_DISPLAY.blit(text, (627, 202))

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
