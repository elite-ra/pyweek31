import random
from utils.models import City

Giza = City('Giza', 3, False, 40000, 20, 83, True, ['sarcophagus', 'gold slipper'])
Agra = City('Agra', 10, False, 530000, 18, 37, False, ['mughal artefact'])
Paris = City('Paris', 22, True, 9310000, 15, 65, True, ['painting from le louvre'])
New_York = City('New York', 24, True, 12245180, 1, 32, False, None)
Rome = City('Rome', 20, False, 56213, 17, 72, True, ['precious gladiator sword'])

cities_list = [Giza, Agra, Paris, Rome, New_York]


class Game:

    def __init__(self):
        self.chances_done = 0
        self.robber_health = 100
        self.last_seen = None
        self.total_coins = 0
        self.skill_level = (self.chances_done ** 1.4 / 21 ** 1.4) * 10 + 1
        self.robber_location = None
        self.stolen_item = None
        self.coins = 0

    def play_turn(self, city_chosen):
        self.robber_next_move()
        if city_chosen == self.robber_location:
            # go to chase
            pass
        else:
            self.chances_done += 1
            self.skill_level = (self.chances_done ** 1.4 / 21 ** 1.4) * 10 + 1
            if self.skill_level > 10:
                self.skill_level = 10
            # increasing robber skill
            # Error message

    def robber_next_move(self):
        # calculating robbers new attributes based on skill level and make move
        self.robber_health -= random.randint(int((10 - self.skill_level) * 3), int((11 - self.skill_level) * 3))
        self.coins = random.randint(int(self.skill_level * 1000), int(self.skill_level * 2500))
        self.total_coins += self.coins
        # selling previously stolen item
        if self.stolen_item:
            self.total_coins += random.randint(5000, 10000)
        chance = random.choice([0, 0, 1])
        if chance and self.last_seen.has_artefacts:
            self.stolen_item = random.choice(self.last_seen.artefacts)
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
#
