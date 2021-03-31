# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun main.py instead!\n\n")
    sys.exit()


from .screens import home_screen
from .utils import constants
from .utils import database
import os


def play_game():
    database.validate_databases_and_settings()
    home_screen.play()
