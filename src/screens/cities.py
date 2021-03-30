# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Ayush Gupta

import pygame
from utils.models import City

pygame.init()
screen = pygame.display.set_mode((800, 600))

city_coords = [[(0, 0), (52, 20)], [(50, 50), (52, 20)], [(130, 60), (52, 20)], [(150, 300), (52, 20)],
               [(400, 200), (52, 20)], [(600, 500), (52, 20)]]


import main_logic  # so that main_logic is run and the cities are defined (we can remove once we actually make the
# whole thing run together)
cities_list = City.get_all_cities()
print(cities_list)

coin_limit = 50000


def city_name(name, x, y, size):
    font = pygame.font.SysFont("monospace", size)
    text = font.render(name, True, (0, 0, 0))
    screen.blit(text, (x, y))


stats_showing = False

running = True
while running:

    screen.fill((0, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 550, 600, 50))
    font = pygame.font.SysFont("monospace", 15)
    current_coins = 25000
    text = font.render(f'Coins stolen({current_coins}/{coin_limit})', True, (255, 255, 255))
    w = text.get_rect().width
    screen.blit(text, (100 + (600 - w) / 2, 555))

    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(120, 575, 560, 10))
    pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(120, 575, (current_coins / coin_limit) * 560, 10))

    for i, a, b in zip([pygame.Rect(a, b) for [a, b] in city_coords], cities_list, city_coords):
        pygame.draw.rect(screen, (0, 0, 0), i, 2)
        city_name(a.name, b[0][0] + 2, b[0][1] + 2, 18)
        if pygame.mouse.get_pressed()[0]:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if i.collidepoint(x, y) and not stats_showing:
                stats_showing = a
            if pygame.Rect((620, 200), (30, 30)).collidepoint(x, y) and stats_showing:
                stats_showing = False
        if pygame.mouse.get_pressed()[2]:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if i.collidepoint(x, y):
                # 'a' is the city name and this condition means that there was a right click on the city name
                # Change scene to chase
                pass

    if stats_showing:
        s = pygame.Surface((1000, 750))  # the size of your rect
        s.set_alpha(128)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((150, 200), (500, 200)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((150, 200), (500, 200)), 2)
        font = pygame.font.SysFont("monospace", 30)
        text = font.render(stats_showing.name, True, (0, 0, 0))
        w = text.get_rect().width
        screen.blit(text, (150 + (500 - w) / 2, 205))

        font = pygame.font.SysFont("monospace", 15)
        temp = 0
        for condition in str(stats_showing).split('\n'):
            text = font.render(condition, True, (0, 0, 0))
            screen.blit(text, (190, 250 + temp * 20))
            temp += 1

        # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((446, 480), (54, 20)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((620, 200), (30, 30)), 1)
        font = pygame.font.SysFont("monospace", 25)
        text = font.render('X', True, (255, 0, 0))
        screen.blit(text, (627, 202))

    pygame.display.update()
