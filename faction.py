class Faction:
    def __init__(self, number_of_units: int, attack_points: float, health_points: float, unit_regeneration_number: float, name: str = 'Default',) -> None:
        self.name = name
        self.is_alive = True
        self.first_enemy: Faction = None
        self.second_enemy: Faction = None
        self.number_of_units = number_of_units
        self.attack_points = attack_points
        self.health_points = health_points
        self.unit_regeneration_number = unit_regeneration_number
        self.total_heath = number_of_units * health_points

    def assign_enemy(self, enemy: 'Faction'):
        if self.first_enemy is None:
            self.first_enemy = enemy
        elif self.second_enemy is None:
            self.second_enemy = enemy
        else:
            print('Already assigned two enemies')

    def perform_attack():
        pass

    def receive_attack(attack_from: str, attack_points: float):
        pass

    def purchase_weapons(self, purchase_amount: int) -> int:
        pass

    def purchase_armors(self, purchase_amount: int) -> int:
        pass

    def print(self):
        pass
