# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Ayush Gupta, Pranjal Rastogi

import random
from .utils.models import City
from .utils import constants as consts

Giza = City('Giza', 3, False, 40000, 20, 37, True, ['sarcophagus', 'gold slipper'])
Agra = City('Agra', 10, False, 530000, 18, 83, False, ['mughal artefact'])
Paris = City('Paris', 22, True, 9310000, 15, 65, True, ['painting from le louvre'])
New_York = City('New York', 24, True, 12245180, 1, 32, False, None)
Rome = City('Rome', 20, False, 56213, 17, 72, True, ['precious gladiator sword'])

cities_list = City.get_all_cities()


class Game:
    robber_types = ['MUSEUM', 'BANK', 'NORM', 'GROUP_PERSON']

    def __init__(self):

        # number of invalid guesses: used to calculate skill_level
        self.number_of_invalid_guesses = 0
        self.__calculate_skill_level()

        # robber attributes
        self.robber_health = 100
        self.last_seen_city = None
        self.total_coins_stolen = 0
        self.current_robber_location = None
        self.stolen_item = None
        self.is_item_stolen = False
        self.coins_stolen = 0

        # robber type
        self.robber_type = random.choice(Game.robber_types)

    def __calculate_skill_level(self):
        # skill level - based on number of invalid guesses. The more invalid guesses, the higher the skill of the
        # robber gets.
        self.skill_level = (self.number_of_invalid_guesses ** 1.4 / 21 ** 1.4) * 10 + 1  # normalized exp func.
        if self.skill_level > 10:
            self.skill_level = 10

    def play_turn(self, city_chosen_by_player):
        # TODO: return something

        # do the robbers turn, which changes the robber's location.
        self.do_robber_turn()

        if city_chosen_by_player == self.current_robber_location:
            # It is a correct guess - the robber moved to what you chose!
            return True, self.skill_level

        else:
            # It is a wrong guess

            # increase robber skill
            self.number_of_invalid_guesses += 1
            self.__calculate_skill_level()

            return False, self.skill_level

    def do_robber_turn(self):
        # calculating robbers new attributes based on skill level
        change_robber_health = random.randint(int((10 - self.skill_level) * 3), int((11 - self.skill_level) * 3))
        coins_change = random.randint(int(self.skill_level * 1000), int(self.skill_level * 2500))



        # make move based on attributes
        choices = cities_list[:]  # all the available choices

        # health case - HIGHEST PRIORITY
        if self.robber_health < 60:  # if health < 60, then **must** go to the hospital city
            choices_for_hosp = set([i for i in choices if i.is_hospital_present is True])
            if self.current_robber_location in choices_for_hosp:
                choices_for_hosp.remove(self.current_robber_location)
        else:
            choices_for_hosp = set()

        # if item stolen, then go to blackmarket
        print(self.is_item_stolen)
        if self.is_item_stolen:
            choices_for_blckmrkt = set([i for i in choices if i.is_blackmarket_present is True])
            print([i.name for i in choices_for_blckmrkt])
            if self.current_robber_location in choices_for_blckmrkt:
                choices_for_blckmrkt.remove(self.current_robber_location)
        else:
            choices_for_blckmrkt = set()

        intersect_of_above = choices_for_blckmrkt.intersection(choices_for_hosp)
        if self.current_robber_location in intersect_of_above:
            intersect_of_above.remove(self.current_robber_location)
        if intersect_of_above == set():
            # no choice based on black market and hospital, prioritize hospital
            if choices_for_hosp != set():
                next_move = sorted(list(choices_for_hosp), key=lambda x: x.per_capita_income_norm)[-1]
                self.robber_health = random.randint(90, 100) + change_robber_health
            else:
                # no hosp, prioritize blackmarket
                if choices_for_blckmrkt != set():
                    next_move = sorted(list(choices_for_blckmrkt), key=lambda x: x.per_capita_income_norm)[-1]
                else:
                    # no hosp, no blackmarket required, just go based on high Museum if Robber is MUSEUM, or PCI if
                    # robber is normal, or BANK if robber is bank.
                    if self.robber_type == "MUSEUM":  # likes high museum count
                        sort_on_museum = sorted(choices, key=lambda x: x.museum_norm)
                        if self.current_robber_location in sort_on_museum:
                            sort_on_museum.remove(self.current_robber_location)
                        next_move = sort_on_museum[-1]
                    elif self.robber_type == "BANK":  # likes high bank count
                        sort_on_bank = sorted(choices, key=lambda x: x.bank_norm)
                        if self.current_robber_location in sort_on_bank:
                            sort_on_bank.remove(self.current_robber_location)
                        next_move = sort_on_bank[-1]
                    elif self.robber_type == "GROUP_PERSON":  # likes high crime rate
                        sort_on_crime_rate = sorted(choices, key=lambda x: x.crime_rate_norm)
                        if self.current_robber_location in sort_on_crime_rate:
                            sort_on_crime_rate.remove(self.current_robber_location)
                        next_move = sort_on_crime_rate[-1]
                    elif self.robber_type == "NORM":  # likes high PCI/ doesnt care
                        sort_on_pci = sorted(choices, key=lambda x: x.per_capita_income_norm)
                        if self.current_robber_location in sort_on_pci:
                            sort_on_pci.remove(self.current_robber_location)
                        chance = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                        if not chance:
                            # pci chance
                            next_move = sort_on_pci[-1]
                        else:
                            # doesnt care
                            next_move = random.choice(choices)
                    else:
                        # this connect happen, unreachable code.
                        return False
        else:
            # blackmrkt and hospital can be chosen together
            next_move = sorted(list(intersect_of_above), key=lambda x: x.per_capita_income_norm)[-1]
            self.robber_health = random.randint(90, 100) + change_robber_health
        # CHANGE VARIABLES BASED ON MOVE
        self.last_seen_city = self.current_robber_location
        self.current_robber_location = next_move
        self.robber_health -= change_robber_health
        self.coins_stolen = coins_change
        self.total_coins_stolen += self.coins_stolen
        # selling previously stolen item
        if self.is_item_stolen and self.current_robber_location.is_blackmarket_present:
            self.is_item_stolen = False  # reset: it is now sold.
            self.stolen_item = None
            # selling price 5000-10000
            coins_change += random.randint(5000, 10000)

        # stealing item chance = 25%
        if self.current_robber_location is not None:
            chance_steal = random.choice([0, 1])
            if chance_steal and self.current_robber_location.has_artefacts():  # can steal
                # steal a random item
                self.stolen_item = random.choice(self.current_robber_location.artefacts)
                self.is_item_stolen = True
            else:
                # can't steal
                self.stolen_item = None
                self.is_item_stolen = False
        else:
            # can't steal
            self.stolen_item = None
            self.is_item_stolen = False
        return True

    def __str__(self):
        lastseenstr = str(self.current_robber_location.name) if self.current_robber_location is not None else "N/A"
        stolenitemstr = str(self.stolen_item.capitalize()) if self.stolen_item is not None else "N/A"
        s = f"- Robber Health:{(30 - len(str(self.robber_health))) * ' '}{self.robber_health}\n" \
            f"- Last Seen City:{(28 - len(lastseenstr)) * ' '}{lastseenstr}\n" \
            f"- Stolen Item:{(24 - len(stolenitemstr)) * ' '}{stolenitemstr}\n"
        return s
