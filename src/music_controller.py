# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()


from pygame import mixer
import os
from .utils import constants as consts


# let channel 0 be for Backgrounds
# let channel 1 be for effects
# let channel 2 be for more effects
# let channel 3 be for even more effects

channel_bg = mixer.Channel(0)
channel_fx1 = mixer.Channel(1)
channel_fx2 = mixer.Channel(2)
channel_fx3 = mixer.Channel(3)
channel_fx4 = mixer.Channel(4)


FX_explosion = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'explosion.ogg'))
FX_fight = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'fight_sound.ogg'))
FX_heli = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'helicopter_final.ogg'))
FX_jetpack = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'jetpack_final.ogg'))
FX_select_norm = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'select_norm.ogg'))
FX_select_woop = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'select_woop.ogg'))

BG_chase = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'bg', 'chase_bg.ogg'))

FX_coin_collect = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'money_collect.ogg'))
FX_coin_bag = mixer.Sound(os.path.join(consts.ROOT_PATH, 'assets', 'audio', 'effects', 'money_bag.ogg'))


def update_volume():
    vol_set = consts.DB.get_settings()['volume']
    channel_bg.set_volume(vol_set['music']/100)
    channel_fx1.set_volume(vol_set['fx']/100)
    channel_fx2.set_volume(vol_set['fx']/100)
    channel_fx3.set_volume(vol_set['fx']/100)


def play_menu_bg():
    pass


def play_chase_bg():
    channel_bg.stop()
    channel_bg.play(BG_chase, loops=-1)


def play_fight_bg():
    pass


def play_click_normal():
    channel_fx1.stop()
    channel_fx1.play(FX_select_norm)


def play_click_woop():
    channel_fx1.stop()
    channel_fx1.play(FX_select_woop)


def play_heli_looped():
    channel_fx1.stop()
    channel_fx1.play(FX_heli, loops=-1)


def play_jetpack_looped():
    channel_fx2.stop()
    channel_fx2.play(FX_jetpack, loops=-1)


def play_fight_sound():
    channel_fx1.stop()
    channel_fx1.play(FX_fight)


def play_explosion():
    channel_fx3.stop()
    channel_fx3.play(FX_explosion)

def play_coin_collect():
    channel_fx4.stop()
    channel_fx4.play(FX_coin_collect)

def play_coin_bag():
    channel_fx4.stop()
    channel_fx4.play(FX_coin_bag)

def stop_fx1():
    channel_fx1.stop()


def stop_fx2():
    channel_fx2.stop()


def stop_fx3():
    channel_fx3.stop()


def stop_bg():
    channel_bg.stop()
