from faction import Faction


class Elves(Faction):
    def __init__(self, number_of_units: int, attack_points: float, health_points: float, unit_regeneration_number: float, name: str = 'Default') -> None:
        super().__init__(number_of_units, attack_points,
                         health_points, unit_regeneration_number, name)

    def perform_attack(self):
        orcs = self.first_enemy if self.first_enemy.name == 'Orcs' else self.second_enemy
        dwarves = self.first_enemy if self.first_enemy.name == 'Dwarves' else self.second_enemy

        if orcs.is_alive and dwarves.is_alive:
            orcs.receive_attack(
                self.name, self.attack_points * 0.6 * self.number_of_units)
            dwarves.receive_attack(
                self.name, self.attack_points * 0.4 * self.number_of_units * 1.5)
            return

        if orcs.is_alive:
            print('yeah?')
            print(self.__dict__)
            orcs.receive_attack(
                self.name, self.attack_points * self.number_of_units)

        if dwarves.is_alive:
            print(self.__dict__)
            print('yeah?')
            dwarves.receive_attack(
                self.name, self.attack_points * self.number_of_units * 1.5)

    def receive_attack(self, attack_from: str, attack_points: float):
        calculated_attack_points = attack_points

        if attack_from == 'Orcs':
            calculated_attack_points *= 1.25

        if attack_from == 'Dwarves':
            calculated_attack_points *= 0.75

        self.number_of_units -= int(calculated_attack_points /
                                    self.health_points)

    def purchase_weapons(self, purchase_amount: int) -> int:
        self.attack_points += purchase_amount * 2

        return 15 * purchase_amount

    def purchase_armors(self, purchase_amount: int) -> int:
        self.health_points += purchase_amount * 4

        return 5 * purchase_amount

    def print(self):
        print('--- You cannot reach our elegance. ---')
        super().print()
