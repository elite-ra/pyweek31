import pygame
import os
import random
import math
from .. import utils
from . import end_screen
from ..utils.widgets import TextButton
from ..utils import constants as consts
from . import win_screen

ROB_DMG_MIN, ROB_DMG_MAX = 0, 0


def main(skill_level):
    global ROB_DMG_MAX, ROB_DMG_MIN
    print(skill_level)
    ROB_DMG_MIN = (10 * int(skill_level)/10 * 2) - (0 if 10 * int(skill_level)/10 * 5 < 21 else 20)
    ROB_DMG_MAX = 10 * int(skill_level)/10 * 5
    rob_max_helth = 100 * (skill_level/10 - 0.1 + 1)
    BG = (153, 102, 255)
    print(rob_max_helth)

    myfont = utils.constants.FONT_MONO_VERY_SMALL

    # Images and Sprites
    background_image = pygame.image.load(
        os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'bg', 'i01_BG.png'))
    copimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Cop.png'))
    vilimg = pygame.image.load(os.path.join(utils.constants.ROOT_PATH, 'assets', 'images', 'sprites', 'Villain.png'))

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

        percentval = (value/rob_max_helth) * 100
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

    while not done:

        mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        screen.blit(background_image, [0, 0])
        screen.blit(copimg, [230, 300])
        screen.blit(vilimg, [490, 300])

        if hpvil <= 0:
            break
        elif hpcop <= 0:
            condition = False
            break

        # update cop, villain health
        health_cop(hpcop, screen)
        health_vil(hpvil, screen)

        move_1 = TextButton(surface=consts.MAIN_DISPLAY, pos=(7, 482),
                            width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[0].name}')

        move_2 = TextButton(surface=consts.MAIN_DISPLAY, pos=(96, 482),
                            width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[1].name}')

        move_3 = TextButton(surface=consts.MAIN_DISPLAY, pos=(7, 536),
                            width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[2].name}')

        move_4 = TextButton(surface=consts.MAIN_DISPLAY, pos=(96, 536),
                            width=87, height=52, fg_color=(255, 255, 255), bg_color=(50, 50, 50),
                            font=consts.FONT_MONO_VERY_SMALL, text=f'{player_selected_moves[3].name}')

        if move_1.hovered:
            move_1.toggle_bg((100, 100, 100))
            if mouse_down:
                move_1.toggle_bg((50, 50, 50))
                ncphp, nrbhp, cpdm, rbdm, is_bckfre = play_turn(player_selected_moves[0], hpcop, hpvil)
                if rbdm is None:
                    # missed
                    # TODO: show eror
                    pass
                else:
                    # not missed
                    print(ncphp)
                    hpcop = ncphp
                    hpvil = nrbhp
                    print(hpvil, hpcop)
                    # TODO: show damage
                    if is_bckfre:
                        # TODO: show msg
                        pass

        if move_2.hovered:
            move_2.toggle_bg((100, 100, 100))
            if mouse_down:
                move_2.toggle_bg((50, 50, 50))
                ncphp, nrbhp, cpdm, rbdm, is_bckfre = play_turn(player_selected_moves[1], hpcop, hpvil)
                if rbdm is None:
                    # missed
                    # TODO: show eror
                    pass
                else:
                    # not missed
                    hpcop = ncphp
                    hpvil = nrbhp
                    # TODO: show damage
                    if is_bckfre:
                        # TODO: show msg
                        pass

        if move_3.hovered:
            move_3.toggle_bg((100, 100, 100))
            if mouse_down:
                move_3.toggle_bg((50, 50, 50))
                ncphp, nrbhp, cpdm, rbdm, is_bckfre = play_turn(player_selected_moves[2], hpcop, hpvil)
                if rbdm is None:
                    # missed
                    # TODO: show eror
                    pass
                else:
                    # not missed
                    hpcop = ncphp
                    hpvil = nrbhp
                    # TODO: show damage
                    if is_bckfre:
                        # TODO: show msg
                        pass

        if move_4.hovered:
            move_4.toggle_bg((100, 100, 100))
            if mouse_down:
                move_4.toggle_bg((50, 50, 50))
                ncphp, nrbhp, cpdm, rbdm, is_bckfre = play_turn(player_selected_moves[3], hpcop, hpvil)
                if rbdm is None:
                    # missed
                    # TODO: show eror
                    pass
                else:
                    # not missed
                    hpcop = ncphp
                    hpvil = nrbhp
                    # TODO: show damage
                    if is_bckfre:
                        # TODO: show msg
                        pass

        pygame.display.update()
        utils.constants.CLOCK.tick(utils.constants.TICK_RATE)

    # end(screen) end screen
    if condition:
        return win_screen.play()
    else:
        return end_screen.end_screen_func(3)


def damage_calc(move: utils.models.FightMove, cophp, robhp):
    if random.random() < move.accuracy/100:
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
                dmg = (move.percentage_damage/100) * cophp
                return dmg, True
            else:
                # move hits robber
                dmg = (move.percentage_damage/100) * robhp
                return dmg, False
        else:
            # cant backfire
            dmg = (move.percentage_damage/100) * robhp
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
            print("HIT", damagee)
            # didnt backfire, normal hit
            vilhp -= damagee
            robdmg += damagee

    # robber hit, always hits.
    ndm = random.randint(ROB_DMG_MIN, ROB_DMG_MAX)
    copdmg += ndm
    cophp -= ndm
    print(ndm)
    return cophp, vilhp, copdmg, robdmg, is_backfire
