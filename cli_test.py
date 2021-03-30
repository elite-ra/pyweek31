from src import main_logic
from src.utils import models

ng = main_logic.Game()


while True:
    print(ng.robber_type, repr(ng.current_robber_location), ng.skill_level, repr(ng.last_seen_city), ng.stolen_item, ng.is_item_stolen, ng.coins_stolen, ng.number_of_invalid_guesses, ng.robber_health, ng.total_coins_stolen)
    t = input("turn:")
    v = ng.play_turn(models.City.get_city_from_name(t))
    print(v)
