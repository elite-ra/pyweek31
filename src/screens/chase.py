import pygame
import random
import os
from .. import utils
import time
from . import end_screen
from . import fight

city_bg_map = {
    "Giza": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'giza_chase_blur.png'),
    "New York": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'ny_chase_blur.png'),
    "Paris": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'paris_chase_blur.png'),
    "Agra": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'agra_chase_blur.png'),
    "Rome": os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'rome_chase_blur.png')
}


def play(skill_level, city_name):

    heli = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'helicopter.png'))
    heli_x = 100
    heli_y = 200
    heli_change = 0

    robber = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'robber_jetpack.png'))
    robber_small = pygame.transform.scale(robber, (125,60))
    robber_x = 650
    robber_y = 200

    bgimg = pygame.image.load(city_bg_map[city_name])

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

    def heli_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(heli, (x, y))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect(x + 24, y + 30, 80, 68), 2)

    def robber_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(robber_small, (x, y))

    def bird_game(x, y, i):
        utils.constants.MAIN_DISPLAY.blit(bird[i], (x, y))
        pygame.draw.rect(utils.constants.MAIN_DISPLAY, (0, 0, 0), pygame.Rect(x, y + 4, 64, 56), 2)

    def is_collision(heli_x, heli_y, bird_x, bird_y):
        if heli_x - 40 <= bird_x <= heli_x + 104 and heli_y - 30 <= bird_y <= heli_y + 94:
            return True
        else:
            return False

    def display_time(timern):
        time_display = utils.constants.FONT_MONO_SMALL.render(timern, True, (0, 0, 0))
        utils.constants.MAIN_DISPLAY.blit(time_display, (750, 10))

    time1 = time.time()

    status = True
    while status:
        utils.constants.MAIN_DISPLAY.blit(bgimg, (0,0))
        # TODO: blur instead!
        s = pygame.Surface((800, 600))  # the size of your rect
        s.set_alpha(120)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        utils.constants.MAIN_DISPLAY.blit(s, (0, 0))  # (0,0) are the top-left coordinates

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    heli_change = -3
                if event.key == pygame.K_s:
                    heli_change = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or pygame.K_s:
                    heli_change = 0

        heli_y += heli_change
        if heli_y >= 350:
            heli_y = 350
        if heli_y <= -27:
            heli_y = -27

        for i in range(n):
            if bird_x[i] <= -60:
                bird_x[i] = random.randint(800, 1540)
                bird_y[i] = random.randint(0, 350)

            bird_game(bird_x[i], bird_y[i], i)
            bird_x[i] -= bird_change[i]
            collision = is_collision(heli_x, heli_y, bird_x[i], bird_y[i])
            if collision:
                return end_screen.end_screen_func(2)

        heli_game(heli_x, heli_y)
        robber_game(robber_x, robber_y)

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
            return fight.main()

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
