# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Sohan Varier

if __name__ == "__main__":
    import sys

    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

import pygame
import random
import os
from .. import utils
from . import end_screen
from . import fight
from ..utils import constants as consts
from . import home_screen
from .. import music_controller


def play(skill_level, city_name):
    # SOUNDS
    music_controller.play_heli_looped()
    music_controller.play_jetpack_looped()
    music_controller.play_chase_bg()

    chase_cont = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'bg', 'chase_cont.png'))

    plyr = utils.constants.DB.get_player_details()
    plyr.has_reached_chase = True
    utils.constants.DB.set_player_details(plyr)
    heli = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'helicopter.png'))
    heli_x = 100
    heli_y = 200
    heli_change_x = 0
    heli_change_y = 0

    robber = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'robber_jetpack.png'))
    robber_small = pygame.transform.scale(robber, (150, 40))
    robber_x = 650
    robber_y = 220

    n = 6
    missile = []
    missile_x = []
    missile_y = []
    missile_change = []
    for i in range(n):
        missile.append(
            pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'missile.png')))
        missile_x.append(random.randint(800, 1540))
        missile_y.append(random.randint(-19, 600 - 45))
        missile_change.append(3 + 0.5 * skill_level)

    m = 3
    coin = []
    coin_x = []
    coin_y = []
    for i in range(m):
        coin.append(
            pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'textures', 'coin.png')))
        coin_x.append(random.randint(800, 2340))
        coin_y.append(random.randint(0, 350))
    coin_change = 1.5

    coin_triple = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'textures', 'coin_triple.png'))
    coin_triple_x = 500
    coin_triple_y = 500
    coins = 0

    coins_font = utils.constants.FONT_MONO_MEDIUM

    def heli_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(heli, (x, y))

    def robber_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(robber_small, (x, y))

    def missile_game(x, y, i):
        utils.constants.MAIN_DISPLAY.blit(missile[i], (x, y))

    def coin_game(x, y, i):
        utils.constants.MAIN_DISPLAY.blit(coin[i], (x, y))

    def coin_triple_display(x, y):
        utils.constants.MAIN_DISPLAY.blit(coin_triple, (x, y))

    def is_collision(heli_x, heli_y, missile_x, missile_y):
        if heli_x - 40 <= missile_x <= heli_x + 104 and heli_y - 15 <= missile_y <= heli_y + 79:
            return True
        else:
            return False

    def is_collect_coin(heli_x, heli_y, coin_x, coin_y, i):
        if heli_x - 8 <= coin_x <= heli_x + 104 and heli_y - 2 <= coin_y <= heli_y + 98:
            return True
        else:
            return False

    def coins_display(x, y):
        coins_text = coins_font.render(str(coins), True, (255, 255, 0))
        utils.constants.MAIN_DISPLAY.blit(coins_text, (x, y))

    def display_time(timern):
        time_display = utils.constants.FONT_MONO_SMALL.render(timern, True, (0, 0, 0))
        utils.constants.MAIN_DISPLAY.blit(time_display, (750, 10))

    bg_X = 0
    status = True
    no_of_frames = 0
    while status:

        rel_x = bg_X % chase_cont.get_width()
        utils.constants.MAIN_DISPLAY.blit(chase_cont, (rel_x - chase_cont.get_width(), 0))
        if rel_x < consts.SCREEN_WIDTH:
            utils.constants.MAIN_DISPLAY.blit(chase_cont, (rel_x, 0))
        bg_X -= 1.5
        no_of_frames += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    heli_change_y = -3
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    heli_change_y = 3
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    heli_change_x = -3
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    heli_change_x = +3
                if event.key == pygame.K_ESCAPE:
                    music_controller.play_click_normal()

                    return home_screen.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    heli_change_y = 0
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    heli_change_x = 0

        heli_y += heli_change_y
        if heli_y >= 600 - 98:
            heli_y = 600 - 98
        if heli_y <= -30:
            heli_y = -30

        if heli_x > 300 and heli_change_x > 0:
            heli_change_x = ((10000 / heli_x) - 20) * 9 / 40

        heli_x += heli_change_x
        if heli_x <= 100:
            heli_x = 100

        for i in range(m):
            coin_x[i] -= coin_change
            if coin_x[i] <= -60:
                coin_x[i] = random.randint(800, 2340)
                coin_y[i] = random.randint(0, 350)

            coin_game(coin_x[i], coin_y[i], i)

            collect_coin = is_collect_coin(heli_x, heli_y, coin_x[i], coin_y[i], i)
            if collect_coin:
                plyr = consts.DB.get_player_details()
                # increase:
                # plyr.coins += 30
                coins += 15
                # set
                music_controller.play_coin_collect()
                coin_x[i] = random.randint(800, 1600 - 32)
                coin_y[i] = random.randint(0, 600 - 32)

        for i in range(n):
            if missile_x[i] <= -60:
                missile_x[i] = random.randint(800, 1540)
                missile_y[i] = random.randint(-19, 600 - 45)

            missile_game(missile_x[i], missile_y[i], i)

            missile_x[i] -= missile_change[i]

            collision = is_collision(heli_x, heli_y, missile_x[i], missile_y[i])
            if collision:
                # SOUNDS
                music_controller.stop_bg()
                music_controller.stop_fx1()
                music_controller.play_explosion()
                music_controller.stop_fx2()

                return end_screen.end_screen_func(2)

        heli_game(heli_x, heli_y)
        robber_game(robber_x, robber_y)
        coin_triple_display(coin_triple_x, coin_triple_y)
        coins_display(575, 510)

        time_taken = round(no_of_frames / 60, 1)  # round(time.time() - time1, 1)
        display_time(str(time_taken))

        # show fight scene
        if time_taken >= 30:
            # SOUNDS
            robber_x -= 1.5
            robber_y += 0.5
        if robber_x - 90 <= heli_x:
            music_controller.stop_fx2()
            music_controller.stop_fx1()
            s = pygame.Surface((800, 600))  # the size of your rect
            s.fill((0, 0, 0))  # this fills the entire surface
            utils.constants.MAIN_DISPLAY.blit(s, (0, 0))  # (0,0) are the top-left coordinates
            music_controller.play_coin_bag()
            font = utils.constants.FONT_MONO_MEDIUM
            text = font.render(f'You caught the robber, and got {coins} coins!', True, (255, 255, 255))
            utils.constants.MAIN_DISPLAY.blit(text, (400 - text.get_rect().width / 2, 200))
            font = utils.constants.FONT_MONO_MEDIUM
            text = font.render('The robber is angry! Fight him!', True, (255, 255, 255))
            utils.constants.MAIN_DISPLAY.blit(text, (400 - text.get_rect().width / 2, 300))
            pygame.display.update()
            pygame.time.wait(4000)
            plyr.coins += coins
            consts.DB.set_player_details(plyr)
            music_controller.stop_bg()
            return fight.play(skill_level)

        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), (0, 50, 75, 500))
        font = utils.constants.FONT_MONO_VERY_SMALL
        text = font.render('Jetpack Fuel', True, (255, 255, 255))
        utils.constants.MAIN_DISPLAY.blit(text, (0, 60))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (50, 50, 50), (5, 100, 65, 400))
        if time_taken <= 30:
            pygame.draw.rect(utils.constants.MAIN_DISPLAY, (95, 106, 0),
                             pygame.Rect(5, (100 + int((time_taken / 30) * 400)), 65,
                             400 - int((time_taken / 30) * 400)))
        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
