from dwarves import Dwarves
from elves import Elves
from merchant import Merchant
from orcs import Orcs


class Game:
    def __init__(self) -> None:
        self.day = 1

        self.merchant = Merchant(20, 20)
        self.orcs = Orcs(50, 9, 100, 0.2, 'Orcs')
        self.dwarves = Dwarves(50, 8, 100, 0.3, 'Dwarves')
        self.elves = Elves(50, 11, 100, 0.5, 'Elves')

        self.merchant.assign_factions(self.orcs)
        self.merchant.assign_factions(self.dwarves)
        self.merchant.assign_factions(self.elves)

        self.orcs.assign_enemy(self.dwarves)
        self.orcs.assign_enemy(self.elves)

        self.dwarves.assign_enemy(self.orcs)
        self.dwarves.assign_enemy(self.elves)

        self.elves.assign_enemy(self.orcs)
        self.elves.assign_enemy(self.dwarves)

    def see_faction_details(self):
        self.orcs.print()
        self.dwarves.print()
        self.elves.print()
