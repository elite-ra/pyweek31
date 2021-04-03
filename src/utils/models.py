# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

# weighted conversion scale
# 1 : bank_count  < 02 | per_capita_income        <    10000 | crime_rate 10-20% | musuem_count,
# 2 : bank_count 03-05 | per_capita_income    10001-   50000 | crime_rate 21-30% | similar to bank_count.
# 3 : bank_count 06-07 | per_capita_income    50001-  100000 | crime_rate 31-40% |
# 4 : bank_count 08-09 | per_capita_income   100001-  200000 | crime_rate 41-50% |
# 5 : bank_count 10-12 | per_capita_income   200001-  500000 | crime_rate 51-60% |
# 6 : bank_count 13-14 | per_capita_income   500001-  750000 | crime_rate 61-70% |
# 7 : bank_count 15-17 | per_capita_income   750001- 1000000 | crime_rate 71-80% |
# 8 : bank_count 18-20 | per_capita_income  1000001- 5000000 | crime_rate 81-90% |
# 9 : bank_count 21-25 | per_capita_income  5000001-10000000 | crime_rate 90-95% |
# 10: bank_count 26+   | per_capita_income 10000001-25000000 | crime_rate 96-99% |

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()


import typing
from . import constants as consts


class City:
    __all_cities = []

    @classmethod
    def get_all_cities(cls):
        return cls.__all_cities

    @classmethod
    def get_city_from_name(cls, name):
        for city in cls.__all_cities:
            if city.name == name:
                return city
        else:
            return None

    def __init__(self, name: str, bank_count: int, is_hospital_present: bool,
                 per_capita_income: int, museum_count: int, crime_rate: float,
                 is_blackmarket_present: bool, artefacts: typing.Union[list, None]):
        """ Pass none to is_blackmarket if the user is not having informant."""

        self.name = name

        self.bank_count = bank_count
        self.__convert_bank_count()

        self.per_capita_income = per_capita_income
        self.__convert_per_capita_income()

        self.museum_count = museum_count
        self.__convert_museum_count()

        self.crime_rate = crime_rate
        self.__convert_crime_rate()

        self.is_hospital_present = is_hospital_present
        self.is_blackmarket_present = is_blackmarket_present

        self.artefacts = artefacts

        City.__all_cities.append(self)

    def __convert_bank_count(self):
        if self.bank_count <= 2:
            self.bank_norm = 1
        elif 3 <= self.bank_count <= 5:
            self.bank_norm = 2
        elif 6 <= self.bank_count <= 7:
            self.bank_norm = 3
        elif 8 <= self.bank_count <= 9:
            self.bank_norm = 4
        elif 10 <= self.bank_count <= 12:
            self.bank_norm = 5
        elif 13 <= self.bank_count <= 14:
            self.bank_norm = 6
        elif 15 <= self.bank_count <= 17:
            self.bank_norm = 7
        elif 18 <= self.bank_count <= 20:
            self.bank_norm = 8
        elif 21 <= self.bank_count <= 25:
            self.bank_norm = 9
        else:
            self.bank_norm = 10

    def __convert_museum_count(self):
        if self.museum_count <= 2:
            self.museum_norm = 1
        elif 3 <= self.museum_count <= 5:
            self.museum_norm = 2
        elif 6 <= self.museum_count <= 7:
            self.museum_norm = 3
        elif 8 <= self.museum_count <= 9:
            self.museum_norm = 4
        elif 10 <= self.museum_count <= 12:
            self.museum_norm = 5
        elif 13 <= self.museum_count <= 14:
            self.museum_norm = 6
        elif 15 <= self.museum_count <= 17:
            self.museum_norm = 7
        elif 18 <= self.museum_count <= 20:
            self.museum_norm = 8
        elif 21 <= self.museum_count <= 25:
            self.museum_norm = 9
        else:
            self.museum_norm = 10

    def __convert_crime_rate(self):
        self.crime_rate_norm = self.crime_rate // 10

    def __convert_per_capita_income(self):
        if self.per_capita_income <= 10000:
            self.per_capita_income_norm = 1
        elif 10001 <= self.per_capita_income <= 50000:
            self.per_capita_income_norm = 2
        elif 50001 <= self.per_capita_income <= 100000:
            self.per_capita_income_norm = 3
        elif 100001 <= self.per_capita_income <= 200000:
            self.per_capita_income_norm = 4
        elif 200001 <= self.per_capita_income <= 500000:
            self.per_capita_income_norm = 5
        elif 500001 <= self.per_capita_income <= 750000:
            self.per_capita_income_norm = 6
        elif 750001 <= self.per_capita_income <= 1000000:
            self.per_capita_income_norm = 7
        elif 1000001 <= self.per_capita_income <= 5000000:
            self.per_capita_income_norm = 8
        elif 5000001 <= self.per_capita_income <= 10000000:
            self.per_capita_income_norm = 9
        else:
            self.per_capita_income_norm = 10

    def __str__(self):

        pci_str = "{:,}".format(self.per_capita_income)
        hosp_str = "Not " * (not self.is_hospital_present) + "Present"

        if consts.DB.player.has_informant:
            blckmrkt_str = "Not " * (not self.is_blackmarket_present) + "Present"
        else:
            blckmrkt_str = "???"

        s = f"No. of banks:{(15 - len(str(self.bank_count))) * ' '}{self.bank_count}\n" \
            f"No. of museums:{(13 - len(str(self.museum_count))) * ' '}{self.museum_count}\n" \
            f"Crime rate:{(16 - len(str(self.crime_rate))) * ' '}{self.crime_rate}%\n" \
            f"Per Capita Income:{(9 - len(pci_str)) * ' '}${pci_str}\n" \
            f"Hospital:{(19 - len(hosp_str)) * ' '}{hosp_str}\n" \
            f"Black market:{(15 - len(blckmrkt_str)) * ' '}{blckmrkt_str}\n"

        return s

    def __repr__(self):

        return f'<utils.models.City({self.name}, {self.bank_count, self.is_hospital_present, self.per_capita_income, self.museum_count, self.crime_rate, self.is_blackmarket_present, self.artefacts})>'

    def has_artefacts(self):
        if self.artefacts is None:
            return False
        else:
            return True


class FightMove:

    def __init__(self, d):
        # print(d)

        self.name = d['name']
        self.description = d['description']

        self.damage = d['damage']
        if self.damage is None:
            self.is_percentage_based = True
            self.percentage_damage = d['percent_damage']

        self.percentage_damage = d['percent_damage']
        if self.percentage_damage is None:
            self.is_percentage_based = False
            self.damage = d['damage']

        self.can_backfire = d['can_backfire']
        self.accuracy = d['accuracy']
        self.price = d['price']
        if self.price == 0:
            self.is_intial = True
        else:
            self.is_intial = False


class Player:
    def __init__(self, user_store_db):

        self.has_reached_fight = user_store_db['HAS_REACHED_FIGHT_ONCE']
        self.has_reached_chase = user_store_db['HAS_REACHED_CHASE_ONCE']
        self.has_informant = user_store_db['HAS_INFORMANT']
        # selected, bought is only move name.
        self.selected_moves = user_store_db['STORE']['SELECTED']
        self.bought_moves = user_store_db['STORE']['BOUGHT_BUT_UNUSED']
        self.coins = user_store_db['COINS']

    def to_dict(self):
        d = {
            'HAS_REACHED_FIGHT_ONCE': self.has_reached_fight,
            'HAS_REACHED_CHASE_ONCE': self.has_reached_chase,
            'HAS_INFORMANT': self.has_informant,
            'COINS': self.coins,
            'STORE': {
                "SELECTED": self.selected_moves,
                "BOUGHT_BUT_UNUSED": self.bought_moves
            }
        }

        return d

    @classmethod
    def new(cls):
        d = {
            'HAS_REACHED_FIGHT_ONCE': False,
            'HAS_REACHED_CHASE_ONCE': False,
            'HAS_INFORMANT': False,
            'COINS': 0,
            'STORE': {
                "SELECTED": ['Punch', 'Kick', 'Super Mega Smash', 'Gunshot'],
                "BOUGHT_BUT_UNUSED": []
            }
        }
        return Player(d)
