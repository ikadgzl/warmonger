from faction import Faction


class Dwarves(Faction):
    def __init__(self, number_of_units: int, attack_points: float, health_points: float, unit_regeneration_number: float, name: str = 'Default') -> None:
        super().__init__(number_of_units, attack_points,
                         health_points, unit_regeneration_number, name)

    def perform_attack(self):
        if self.first_enemy.is_alive and self.second_enemy.is_alive:
            self.first_enemy.receive_attack(self.name,
                                            self.attack_points * 0.5 * self.number_of_units)
            self.second_enemy.receive_attack(self.name,
                                             self.attack_points * 0.5 * self.number_of_units)
            return

        last_enemy = self.first_enemy if self.first_enemy.is_alive else self.second_enemy
        last_enemy.receive_attack(
            self.name, self.attack_points * self.number_of_units)

    def receive_attack(self, attack_from: str, attack_points: float):
        self.number_of_units -= int(attack_points / self.health_points)

    def purchase_weapons(self, purchase_amount: int) -> int:
        self.attack_points += purchase_amount

        return 10 * purchase_amount

    def purchase_armors(self, purchase_amount: int) -> int:
        self.health_points += purchase_amount * 2

        return 3 * purchase_amount

    def print(self):
        print('--- Taste the power of our axes! ---')
        super().print()
