import pygame
import math
import random
import os
from ..utils import constants


def chase():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Cops!")

    heli = pygame.image.load(os.path.join(constants.ROOT_PATH, 'assets', 'images', 'sprites', 'helicopter.png'))
    heli_X = 100
    heli_Y = 200
    heli_change = 0

    robber = pygame.image.load(os.path.join(constants.ROOT_PATH, 'assets', 'images', 'sprites', 'robber.png'))
    robber_X = 700
    robber_Y = 200

    bird = pygame.image.load(os.path.join(constants.ROOT_PATH, 'assets', 'images', 'sprites', 'seagull.png'))
    bird_X = 600
    bird_Y = random.randint(0, 350)
    bird_change = 1

    def heli_game(x, y):
        screen.blit(heli, (x, y))

    def robber_game(x, y):
        screen.blit(robber, (x, y))

    def bird_game(x, y):
        screen.blit(bird, (x, y))

    def is_collision(heli_X, heli_Y, bird_X, bird_Y):
        d = math.sqrt(math.pow(heli_X - bird_X, 2) + math.pow(heli_Y - bird_Y, 2))
        if d <= 100:
            return True
        else:
            return False

    game_over_font = pygame.font.Font('freesansbold.ttf', 50)

    def game_over_text():
        game_over = game_over_font.render("GAME OVER LOSER", True, (0, 0, 0))
        screen.blit(game_over, (90, 250))

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

        screen.fill((0, 0, 100))

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
