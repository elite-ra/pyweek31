import pygame
import random
import os
from .. import utils
import time
from . import end_screen
from . import fight
from .. utils import constants as consts

city_bg_map = {
    "Giza": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'giza_chase_blur.png'),
    "New York": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'ny_chase_blur.png'),
    "Paris": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'paris_chase_blur.png'),
    "Agra": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'agra_chase_blur.png'),
    "Rome": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'rome_chase_blur.png')
}


def play(skill_level, city_name):
    chase_cont = pygame.image.load(os.path.join(consts.ROOT_PATH, 'assets', 'images', 'bg', 'chase_cont.png')).convert()

    plyr = utils.constants.DB.get_player_details()
    plyr.has_reached_chase = True
    utils.constants.DB.set_player_details(plyr)
    heli = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'helicopter.png'))
    heli_x = 100
    heli_y = 200
    heli_change = 0

    robber = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'robber_jetpack.png'))
    robber_small = pygame.transform.scale(robber, (125, 60))
    robber_x = 650
    robber_y = 200



    n = 6
    bird = []
    bird_x = []
    bird_y = []
    bird_change = []
    for i in range(n):
        bird.append(
            pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'seagull.png')))
        bird_x.append(random.randint(800, 1540))
        bird_y.append(random.randint(0, 350))
        bird_change.append(2 + 0.1 * skill_level)

    m = 3
    coin = []
    coin_x = []
    coin_y = []
    for i in range(m):
        coin.append(pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'textures', 'coin.png')))
        coin_x.append(random.randint(800, 1540))
        coin_y.append(random.randint(0, 350))
    coin_change = 2 + 0.1 * skill_level

    coin_triple = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'textures', 'coin_triple.png'))
    coin_triple_x = 500
    coin_triple_y = 500
    coins = 0

    coins_font = utils.constants.FONT_MONO_MEDIUM

    def heli_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(heli, (x, y))

    def robber_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(robber_small, (x, y))

    def bird_game(x, y, i):
        utils.constants.MAIN_DISPLAY.blit(bird[i], (x, y))

    def coin_game(x,y, i):
        utils.constants.MAIN_DISPLAY.blit(coin[i], (x, y))

    def coin_triple_display(x, y):
        utils.constants.MAIN_DISPLAY.blit(coin_triple, (x, y))

    def is_collision(heli_x, heli_y, bird_x, bird_y):
        if heli_x - 40 <= bird_x <= heli_x + 104 and heli_y - 30 <= bird_y <= heli_y + 94:
            return True
        else:
            return False

    def is_collect_coin(heli_x, heli_y, coin_x, coin_y, i):
        if heli_x - 40 <= coin_x <= heli_x + 104 and heli_y - 30 <= coin_y <= heli_y + 94:
            return True
        else:
            return False

    def coins_display(x, y):
        coins_text = coins_font.render(str(coins), True, (255, 255, 0))
        utils.constants.MAIN_DISPLAY.blit(coins_text, (x , y))

    def display_time(timern):
        time_display = utils.constants.FONT_MONO_SMALL.render(timern, True, (0,0,0))
        utils.constants.MAIN_DISPLAY.blit(time_display, (750, 10))

    time1 = time.time()
    bg_X = 0
    status = True
    while status:

        rel_x = bg_X % chase_cont.get_width()
        utils.constants.MAIN_DISPLAY.blit(chase_cont, (rel_x - chase_cont.get_width(), 0))
        if rel_x < consts.SCREEN_WIDTH:
            utils.constants.MAIN_DISPLAY.blit(chase_cont, (rel_x, 0))
        bg_X -= 2 + 0.1 * skill_level



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    heli_change = -3
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    heli_change = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    heli_change = 0

        heli_y += heli_change
        if heli_y >= 350:
            heli_y = 350
        if heli_y <= -27:
            heli_y = -27
        
        for i in range(m):
            coin_x[i] -= coin_change
            if coin_x[i] <= -60:
                coin_x[i] = random.randint(800, 1540)
                coin_y[i] = random.randint(0,350)

            coin_game(coin_x[i], coin_y[i], i)

            collect_coin = is_collect_coin(heli_x, heli_y, coin_x[i], coin_y[i], i)
            if collect_coin:
                plyr = consts.DB.get_player_details()
                # increase:
                plyr.coins += 30
                coins += 30
                # set
                consts.DB.set_player_details(plyr)
                coin_x[i] = random.randint(800, 1540)
                coin_y[i] = random.randint(0,350)
        
        for i in range(n):
            if bird_x[i] <= -60:
                bird_x[i] = random.randint(800, 1540)
                bird_y[i] = random.randint(0, 350)

            bird_game(bird_x[i], bird_y[i], i)
            bird_x[i] -= bird_change[i]
            collision = is_collision(heli_x, heli_y, bird_x[i], bird_y[i])
            if collision:
                return end_screen.end_screen_func(2)

            for j in range(m):
                if bird_x[i] - 40 <= coin_x[j] <= bird_x[i] + 104 and bird_y[i] - 30 <= coin_y[j] <= bird_y[i] + 94:
                    coin_x[j] = random.randint(800, 1540)
                    coin_y[j] = random.randint(0, 350)

        

        heli_game(heli_x, heli_y)
        robber_game(robber_x, robber_y)
        coin_triple_display(coin_triple_x, coin_triple_y)
        coins_display(575, 510)


        time_taken = round(time.time() - time1, 1)
        display_time(str(time_taken))

        # show fight scene
        if time_taken >= 30:
            s = pygame.Surface((800, 600))  # the size of your rect
            s.set_alpha(240)  # alpha level
            s.fill((0, 0, 0))  # this fills the entire surface
            utils.constants.MAIN_DISPLAY.blit(s, (0, 0))  # (0,0) are the top-left coordinates
            font = utils.constants.FONT_MONO_VERY_LARGE
            text = font.render('You caught the robber!', True, (255, 255, 255))
            utils.constants.MAIN_DISPLAY.blit(text, (170, 200))
            font = utils.constants.FONT_MONO_MEDIUM
            text = font.render('The robber is hostile! Fight him!', True, (255, 255, 255))
            utils.constants.MAIN_DISPLAY.blit(text, (175, 300))
            pygame.display.update()
            pygame.time.wait(4000)
            return fight.main(skill_level)

        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), (0, 50, 75, 500))
        font = utils.constants.FONT_MONO_VERY_SMALL
        text = font.render('Robber Fuel', True, (255, 255, 255))
        utils.constants.MAIN_DISPLAY.blit(text, (0, 60))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (50, 50, 50), (5, 100, 65, 400))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (95, 106, 0),
                         pygame.Rect(5, (100 + int((time_taken / 30)*400)), 65, int(((30 - time_taken) / 30) * 400)))
        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
