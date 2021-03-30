# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import pygame
from pathlib import Path
import os
import platform
from . import database

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

# TODO: load fonts
