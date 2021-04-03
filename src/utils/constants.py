# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import pygame
from pathlib import Path
import os
from . import database

pygame.init()

# CWD
SRC_PATH = str(Path(__file__).parents[1])
ROOT_PATH = str(Path(__file__).parents[2])

# game
SCREEN_TITLE = ""
TICK_RATE = 60
CLOCK = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
MAIN_DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DB = database.Database()

FONT_MONO_VERY_SMALL = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'PTMono-Regular.ttf'), 12)
FONT_MONO_SMALL = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'PTMono-Regular.ttf'), 15)
FONT_MONO_SMALL_MEDIUM = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'PTMono-Regular.ttf'), 18)
FONT_MONO_MEDIUM = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'PTMono-Regular.ttf'), 25)
FONT_MONO_LARGE = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'PTMono-Regular.ttf'), 30)
FONT_MONO_VERY_LARGE = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'PTMono-Regular.ttf'), 40)
FONT_MAIN_SCREEN = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'BloggerSans-MediumItalic.otf'), 140)
FONT_TITLE = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'BloggerSans-MediumItalic.otf'), 32)

# TODO: load all images here instead

COIN_TRIPLE_IMG = pygame.image.load(os.path.join(ROOT_PATH, 'assets', 'images', 'textures', 'coin_triple.png'))
