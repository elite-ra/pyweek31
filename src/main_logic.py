import random

main_dict = {'Giza': {'Big Banks': 2, 'Hospitals': 0, 'Rich Population': 3, 'Old Artefacts': 9, 'Crime Rate': 8,
                      'Black Market': 1},
             'Agra': {'Big Banks': 5, 'Hospitals': 0, 'Rich Population': 6, 'Old Artefacts': 8, 'Crime Rate': 3,
                      'Black Market': 0},
             'Paris': {'Big Banks': 9, 'Hospitals': 1, 'Rich Population': 7, 'Old Artefacts': 7, 'Crime Rate': 6,
                       'Black Market': 1},
             'New York': {'Big Banks': 10, 'Hospitals': 5, 'Rich Population': 8, 'Old Artefacts': 1, 'Crime Rate': 3,
                          'Black Market': 0},
             'Rome': {'Big Banks': 9, 'Hospitals': 3, 'Rich Population': 3, 'Old Artefacts': 8, 'Crime Rate': 7,
                      'Black Market': 1}}

artefacts = {'Giza': ['sarcophagus', 'gold slipper'], 'Agra': ['mughal artefact'], 'Paris': ['painting from le louvre'],
             'Rome': ['precious gladiator sword']}


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
        if chance:
            if artefacts.get(self.last_seen):
                self.stolen_item = random.choice(artefacts.get(self.last_seen))
        else:
            self.stolen_item = None

        # hospital case
        choices = list(main_dict.keys())
        if self.robber_health < 60:
            temp = choices[:]
            for i in temp:
                if not main_dict[i]['Hospital']:
                    choices.remove(i)
        if self.stolen_item:
            temp = choices[:]
            for i in temp:
                if not main_dict[i]['Black Market']:
                    choices.remove(i)

        choices.sort(key = lambda x: main_dict[x]['Big Banks'])



def get_prev_steal():
    global prev_steal
    return prev_steal


def get_last_seen():
    global last_seen
    return last_seen


def get_coins():
    global coins
    return coins


def get_skill_level():
    global skill_level
    return skill_level

# changing robber values based on difficulty ((number of chances**1.4/20**1.4) * 10)
#
