# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import pygame
from pathlib import Path
import os
import platform

# CWD
SRC_PATH = str(Path(__file__).parents[1])
ROOT_PATH = str(Path(__file__).parents[2])

# game
SCREEN_TITLE = ""
TICK_RATE = 60
CLOCK = pygame.time.Clock()

# TODO: add display here, with FIXED screen resolution!
