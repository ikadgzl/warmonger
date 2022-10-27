from faction import Faction


class Elves(Faction):
    def __init__(self, number_of_units: int, attack_points: float, health_points: float, unit_regeneration_number: float, name: str = 'Default') -> None:
        super().__init__(number_of_units, attack_points,
                         health_points, unit_regeneration_number, name)

    def perform_attack(self):
        pass

    def receive_attack(self, attack_from: str, attack_points: float):
        pass

    def purchase_weapons(self, purchase_amount: int) -> int:
        pass

    def purchase_armors(self, purchase_amount: int) -> int:
        pass

    def print(self):
        print('--- You cannot reach our elegance. ---')
