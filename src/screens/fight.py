# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Kartikey Pandey


if __name__ == "__main__":
    import sys

    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()

import pygame
import os
import random
import math
from .. import utils
from . import end_screen
from ..utils.widgets import TextButton
from ..utils import constants as consts
from . import win_screen
from . import home_screen
from .. import music_controller

ROB_DMG_MIN, ROB_DMG_MAX = 0, 0


def main(skill_level):
    plyr = utils.constants.DB.get_player_details()
    plyr.has_reached_fight = True
    utils.constants.DB.set_player_details(plyr)

    global ROB_DMG_MAX, ROB_DMG_MIN

    ROB_DMG_MIN = (10 * int(skill_level) / 10 * 2) - (0 if 10 * int(skill_level) / 10 * 5 < 21 else 20)
    ROB_DMG_MAX = 10 * int(skill_level) / 10 * 5
    rob_max_helth = 100 * (skill_level / 10 - 0.1 + 1)

    # Images and Sprites
    background_image = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'fight_bg_blur.png'))
    copimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Cop_n.png'))
    copimg = pygame.transform.scale(copimg, (108, 200))
    vilimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Robber.png'))
    vilimg = pygame.transform.scale(vilimg, (108, 220))
    img = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'bg_platform_down.png'))

    screen = utils.constants.MAIN_DISPLAY

    def health_cop(value, dscreen):
        if value > 50:
            colour = (0, 255, 0)
        elif 50 >= value > 10:
            colour = (255, 200, 0)
        else:
            colour = (255, 0, 0)
        pygame.draw.rect(dscreen, (255, 255, 255), (40, 10, 200, 20))
        pygame.draw.rect(dscreen, colour, (41, 11, math.ceil(2 * value - 1), 18))

    def health_vil(value, dscreen):

        percentval = (value / rob_max_helth) * 100
        if percentval > 50:
            colour = (0, 255, 0)
        elif 50 >= percentval > 10:
            colour = (255, 200, 0)
        else:
            colour = (255, 0, 0)
        pygame.draw.rect(dscreen, (255, 255, 255), (560, 10, 200, 20))
        pygame.draw.rect(dscreen, colour, (561, 11, math.ceil(2 * percentval - 1), 18))

    done = False
    hpcop = 100
    hpvil = rob_max_helth
    condition = True

    player_selected_moves = consts.DB.get_player_moves()
    screen.blit(background_image, [0, 0])

    # draw background at top to show what moves did
    s = pygame.Surface((800, 100))
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    while not done:
        mouse_down = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    music_controller.play_click_normal()
                    return home_screen.play()

        screen.blit(copimg, [230, 100 + 200])
        screen.blit(vilimg, [490, 60 + 220])

        screen.blit(img, [0, 500])

        move_1 = TextButton(surface=consts.MAIN_DISPLAY, pos=(25, 525),
                            width=160, height=25, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[0].name}')

        move_2 = TextButton(surface=consts.MAIN_DISPLAY, pos=(185 + 5, 525),
                            width=160, height=25, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[1].name}')

        move_3 = TextButton(surface=consts.MAIN_DISPLAY, pos=(25, 555),
                            width=160, height=25, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[2].name}')

        move_4 = TextButton(surface=consts.MAIN_DISPLAY, pos=(185 + 5, 555),
                            width=160, height=25, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[3].name}')

        moves = [move_1, move_2, move_3, move_4]

        if hpvil <= 0:
            break
        elif hpcop <= 0:
            condition = False
            break

        # update cop, villain health
        health_cop(hpcop, screen)
        health_vil(hpvil, screen)

        c = 0
        for move in moves:
            if move.hovered:

                t_test1 = consts.FONT_MONO_SMALL.render(player_selected_moves[c].description, True, (0, 0, 0))

                if t_test1.get_width() > 600 - 525:
                    t_test1 = consts.FONT_MONO_SMALL. \
                        render(" ".join(player_selected_moves[c].description.split(" ")[:7]), True, (0, 0, 0))
                    t_test2 = consts.FONT_MONO_SMALL. \
                        render(" ".join(player_selected_moves[c].description.split(" ")[7:]), True, (0, 0, 0))
                    consts.MAIN_DISPLAY.blit(t_test1, (185 + 5 + 160 + 30, 525))
                    consts.MAIN_DISPLAY.blit(t_test2, (185 + 5 + 160 + 30, 555))

                else:
                    consts.MAIN_DISPLAY.blit(t_test1, (185 + 5 + 160 + 30, 525))

                move.toggle_bg((100, 100, 100))
                if mouse_down:
                    move.toggle_bg((50, 50, 50))
                    ncphp, nrbhp, cpdm, rbdm, is_bckfre = play_turn(player_selected_moves[c], hpcop, hpvil)
                    music_controller.play_fight_sound()
                    music_controller.play_fight_sound()
                    if rbdm is None:
                        # missed
                        t_mis1 = consts.FONT_MONO_SMALL.render(f'You missed! The robber dealt {cpdm} damage to you!',
                                                               True, (255, 255, 255))

                        s = pygame.Surface((770, t_mis1.get_height() + 10))
                        s.fill((0, 0, 0))
                        screen.blit(s, (15, 45))

                        consts.MAIN_DISPLAY.blit(t_mis1, (20, 50))
                        hpcop = ncphp
                    else:
                        # not missed

                        hpcop = ncphp
                        hpvil = nrbhp
                        cpdm, rbdm = round(cpdm, 1), round(rbdm, 1)

                        if is_bckfre:
                            # backfired
                            t_mis1 = consts.FONT_MONO_SMALL.render(f'You tried to hit the robber, '
                                                                   f'but it backfired! You suffer {cpdm} damage!',
                                                                   True, (255, 255, 255))

                            s = pygame.Surface((770, t_mis1.get_height() + 10))
                            s.fill((0, 0, 0))
                            screen.blit(s, (15, 45))

                            consts.MAIN_DISPLAY.blit(t_mis1, (20, 50))
                        else:
                            # normal, not missed, not backfire
                            t_mis1 = consts.FONT_MONO_SMALL.render(f'You did {rbdm} damage to the robber, '
                                                                   f'and the robber '
                                                                   f'dealt {cpdm} damage to you!', True,
                                                                   (255, 255, 255))

                            s = pygame.Surface((770, t_mis1.get_height() + 10))
                            s.fill((0, 0, 0))
                            screen.blit(s, (15, 45))

                            consts.MAIN_DISPLAY.blit(t_mis1, (20, 50))

            c += 1

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)
    else:
        pygame.quit()

    # end(screen) end screen
    if condition:
        return win_screen.play()
    else:
        return end_screen.end_screen_func(3)


def damage_calc(move: utils.models.FightMove, cophp, robhp):
    if random.random() < move.accuracy / 100:
        not_miss = True
    else:
        not_miss = False

    if not not_miss:
        return None, None

    if move.is_percentage_based:
        # move is precentage based
        # check backfire
        if move.can_backfire:
            backfire_chance = random.choice([0, 0, 1])  # fixed for all moves.
            if backfire_chance:
                # move hits cop itself
                dmg = (move.percentage_damage / 100) * cophp
                return dmg, True
            else:
                # move hits robber
                dmg = (move.percentage_damage / 100) * robhp
                return dmg, False
        else:
            # cant backfire
            dmg = (move.percentage_damage / 100) * robhp
            return dmg, False
    else:
        # move is normal damage
        dmg = move.damage
        if move.can_backfire:
            backfire_chance = random.choice([0, 0, 1])
            if backfire_chance:
                return dmg, True
            else:
                return dmg, False
        else:
            # move cant backfire
            return dmg, False


def play_turn(mv: utils.models.FightMove, cophp, vilhp):
    damagee, is_backfire = damage_calc(mv, cophp, vilhp)
    copdmg, robdmg = 0, 0
    if damagee is None:
        # missed
        robdmg = None
    else:
        # didnt miss
        if is_backfire is True:
            # backfired
            cophp -= damagee
            copdmg += damagee
        else:

            # didnt backfire, normal hit
            vilhp -= damagee
            robdmg += damagee

    # robber hit, always hits.
    ndm = random.randint(ROB_DMG_MIN, ROB_DMG_MAX)
    copdmg += ndm
    cophp -= ndm

    return cophp, vilhp, copdmg, robdmg, is_backfire
