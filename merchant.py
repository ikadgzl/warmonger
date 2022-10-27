from faction import Faction


class Merchant:
    def __init__(self, weapon_points: int = 20, armor_points: int = 20) -> None:
        self.first_faction: Faction = None
        self.second_faction: Faction = None
        self.third_faction: Faction = None
        self.base_weapon_points = weapon_points
        self.base_armor_points = armor_points
        self.weapon_points = weapon_points
        self.armor_points = armor_points
        self.revenue = 0

    def assign_factions(self, faction: Faction):
        if self.first_faction is None:
            self.first_faction = faction
        elif self.second_faction is None:
            self.second_faction = faction
        elif self.third_faction is None:
            self.third_faction = faction
        else:
            print('\nMerchant already have 3 factions\n')

    def sell_weapons(self, to: Faction, amount: int) -> int:
        pass

    def sell_armors(self, to: Faction, amount: int) -> int:
        pass

    def print(self):
        pass

    def end_turn(self):
        self.weapon_points = self.base_weapon_points
        self.armor_points = self.base_armor_points
