# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

import json
from . import constants as consts
from . import models
import os


class Database:
    def __init__(self):
        # print("Database initialization.")
        self.user_store_db = read_json(os.path.join(f'{consts.ROOT_PATH}', 'db', 'user_store.json'))
        self.player = models.Player(self.user_store_db)

        self.const_db = read_json(os.path.join(f'{consts.ROOT_PATH}', 'db', 'const_db.json'))

        self.all_moves = [models.FightMove(move) for move in self.const_db['ALL_MOVES']]

        self.settings_db = read_json(os.path.join(f'{consts.ROOT_PATH}', 'settings.json'))

    def get_all_moves(self):
        return self.all_moves

    def get_move_from_name(self, name):
        for move in self.all_moves:
            if move.name == name:
                return move
        else:
            return None

    def get_player_moves(self):
        moves = [self.get_move_from_name(i) for i in self.player.selected_moves]
        return moves

    def get_player_details(self):
        return self.player

    def set_player_details(self, player):
        d = player.to_dict()
        self.user_store_db = d
        self.player = player
        store_json(os.path.join(f'{consts.ROOT_PATH}', 'db', 'user_store.json'), self.user_store_db)

    def get_settings(self):
        return self.settings_db

    def set_settings(self, new_settings):
        self.settings_db = new_settings
        store_json(os.path.join(consts.ROOT_PATH, 'settings.json'), self.settings_db)


def read_json(fp):
    with open(fp, "r") as f:
        json_f = json.load(f)
    return json_f


def store_json(fp, json_dict):
    with open(fp, "w") as f:
        json.dump(json_dict, f)


def validate_databases_and_settings():
    # TODO: add validation system
    pass
