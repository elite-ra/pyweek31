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

    n = 5
    bird = []
    bird_X = []
    bird_Y = []
    bird_change = []
    for i in range(n):
        bird.append(pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'seagull.png')))
        bird_X.append(random.randint(500,600))
        bird_Y.append(random.randint(0, 350))
        bird_change.append(2)

    def heli_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(heli, (x, y))

    def robber_game(x, y):
        utils.constants.MAIN_DISPLAY.blit(robber, (x, y))

    def bird_game(x, y,i):
        utils.constants.MAIN_DISPLAY.blit(bird[i], (x, y))

    def is_collision(heli_x, heli_y, bird_x, bird_y):
        if bird_x in range(heli_x - 10, heli_x + 100) and bird_y in range(heli_y, heli_y + 90): 
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
                    heli_change = -3
                if event.key == pygame.K_s:
                    heli_change = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or pygame.K_s:
                    heli_change = 0

        utils.constants.MAIN_DISPLAY.fill((0, 0, 100))

        heli_Y += heli_change
        if heli_Y >= 350:
            heli_Y = 350
        if heli_Y <= -27:
            heli_Y = -27
        
        for i in range(n):
            if bird_X[i] <= 0:
                bird_X[i] = random.randint(500,600)
                bird_Y[i] = random.randint(0,350)
            bird_X[i] -= bird_change[i]

            collision = is_collision(heli_X, heli_Y, bird_X[i], bird_Y[i])
            if collision:
                game_over_text()

            bird_game(bird_X[i],bird_Y[i],i)

        heli_game(heli_X, heli_Y)
        robber_game(robber_X, robber_Y)

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
