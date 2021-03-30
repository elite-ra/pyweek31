import pygame
import math
import random
import os
from .. import utils


def play():

    heli = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'helicopter.png'))
    heli_X = 100
    heli_Y = 200
    heli_change = 0

    robber = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'robber.png'))
    robber_X = 700
    robber_Y = 200

    bird = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'seagull.png'))
    bird_X = 600
    bird_Y = random.randint(0, 350)
    bird_change = 1

    def heli_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(heli, (x, y))

    def robber_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(robber, (x, y))

    def bird_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(bird, (x, y))

    def is_collision(heli_x, heli_y, bird_x, bird_y):
        d = math.sqrt(math.pow(heli_x - bird_x, 2) + math.pow(heli_y - bird_y, 2))
        if d <= 100:
            return True
        else:
            return False

    game_over_font = pygame.font.Font('freesansbold.ttf', 50)

    def game_over_text():
        game_over = game_over_font.render("GAME OVER LOSER", True, (0, 0, 0))
        utils.constants.MAIN_DISPLAY.blit(game_over, (90, 250))

    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    heli_change = -1.5
                if event.key == pygame.K_s:
                    heli_change = 1.5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or pygame.K_s:
                    heli_change = 0

        utils.constants.MAIN_DISPLAY.fill((0, 0, 100))

        heli_Y += heli_change
        if heli_Y >= 350:
            heli_Y = 350
        if heli_Y <= 0:
            heli_Y = 0

        bird_X -= bird_change

        collision = is_collision(heli_X, heli_Y, bird_X, bird_Y)
        if collision:
            game_over_text()

        heli_game(heli_X, heli_Y)
        robber_game(robber_X, robber_Y)
        bird_game(bird_X, bird_Y)

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)

