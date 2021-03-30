import random
from utils.models import City

Giza = City('Giza', 3, False, 40000, 20, 83, True, ['sarcophagus', 'gold slipper'])
Agra = City('Agra', 10, False, 530000, 18, 37, False, ['mughal artefact'])
Paris = City('Paris', 22, True, 9310000, 15, 65, True, ['painting from le louvre'])
New_York = City('New York', 24, True, 12245180, 1, 32, False, None)
Rome = City('Rome', 20, False, 56213, 17, 72, True, ['precious gladiator sword'])

cities_list = City.get_all_cities()
#print(cities_list)


class Game:

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
            # It is a correct guess

            pass
        else:
            # It is a wrong guess

            # increasing robber skill
            self.number_of_invalid_guesses += 1
            self.__calculate_skill_level()

    def do_robber_turn(self):
        # calculating robbers new attributes based on skill level and make move
        self.robber_health -= random.randint(int((10 - self.skill_level) * 3), int((11 - self.skill_level) * 3))
        self.coins_stolen = random.randint(int(self.skill_level * 1000), int(self.skill_level * 2500))
        self.total_coins_stolen += self.coins_stolen
        # selling previously stolen item
        if self.stolen_item:
            self.total_coins_stolen += random.randint(5000, 10000)
        chance = random.choice([0, 0, 1])
        if chance and self.last_seen_city.has_artefacts:
            self.stolen_item = random.choice(self.last_seen_city.artefacts)
        else:
            self.stolen_item = None

        # hospital case
        choices = cities_list[:]
        if self.robber_health < 60:
            temp = choices[:]
            for i in temp:
                if not i.is_hospital_present:
                    choices.remove(i)
        if self.stolen_item:
            temp = choices[:]
            for i in temp:
                if not i.is_blackmarket_present:
                    choices.remove(i)

        choices.sort(key=lambda x: x.bank_count)


# changing robber values based on difficulty ((number of chances**1.4/20**1.4) * 10)

