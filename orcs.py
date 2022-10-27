from faction import Faction


class Orcs(Faction):
    def __init__(self, number_of_units: int, attack_points: float, health_points: float, unit_regeneration_number: float, name: str = 'Default') -> None:
        super().__init__(number_of_units, attack_points,
                         health_points, unit_regeneration_number, name)

    def perform_attack(self):
        if self.first_enemy.is_alive and self.second_enemy.is_alive:
            elves = self.first_enemy if self.first_enemy.name == 'Elves' else self.second_enemy
            dwarves = self.first_enemy if self.first_enemy.name == 'Dwarves' else self.second_enemy

            elves.receive_attack(
                self.name, self.attack_points * 0.7 * self.number_of_units)
            dwarves.receive_attack(
                self.name, self.attack_points * 0.3 * self.number_of_units)
            return

        last_enemy = self.first_enemy if self.first_enemy.is_alive else self.second_enemy
        last_enemy.receive_attack(
            self.name, self.attack_points * self.number_of_units)

    def receive_attack(self, attack_from: str, attack_points: float):
        calculated_attack_points = attack_points

        if attack_from == 'Elves':
            calculated_attack_points *= 0.75

        if attack_from == 'Dwarves':
            calculated_attack_points *= 0.8

        self.number_of_units -= int(calculated_attack_points /
                                    self.health_points)

    def purchase_weapons(self, purchase_amount: int) -> int:
        self.attack_points += purchase_amount * 2

        return 20 * purchase_amount

    def purchase_armors(self, purchase_amount: int) -> int:
        self.health_points += purchase_amount * 3

        return 1 * purchase_amount

    def print(self):
        print('--- Stop running, you\'ll only die tired! ---')
        super().print()
