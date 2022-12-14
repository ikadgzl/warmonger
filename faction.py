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
        info = ''

        for k, v in self.__dict__.items():
            if k == 'first_enemy' or k == 'second_enemy':
                continue

            formatted_key = k.replace(
                '_', ' ').capitalize() if k != 'is_alive' else 'Status'
            formatted_value = v if k != 'is_alive' else 'Alive' if v else 'Defeated'

            info += f'{formatted_key}: \t {formatted_value}\n'

        print(info.expandtabs(30))

    def end_turn(self):
        if not self.is_alive:
            self.number_of_units = 0
            return

        if self.number_of_units <= 0:
            self.number_of_units = 0
            self.is_alive = False
            print('*' * 30)
            print(f'** {self.name.upper()} has been defeated! **')
            print('*' * 30, '\n')
