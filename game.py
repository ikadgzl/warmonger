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

    def handle_sales(self):
        print('1. Weapons')
        print('2. Armor\n')

        sale_type = input('What do you want to sell? ')

        print('\n1. Orcs')
        print('2. Dwarves')
        print('3. Elves\n')

        to = input('To which faction? ')
        amount = int(input('\nHow many armors do you want to sell? '))

        if sale_type == '1':
            if to == '1':
                self.merchant.sell_weapons(self.orcs, amount)
            elif to == '2':
                self.merchant.sell_weapons(self.dwarves, amount)
            elif to == '3':
                self.merchant.sell_weapons(self.elves, amount)
            else:
                print('Wrong faction name!')

        if sale_type == '2':
            if to == '1':
                self.merchant.sell_armors(self.orcs, amount)
            elif to == '2':
                self.merchant.sell_armors(self.dwarves, amount)
            elif to == '3':
                self.merchant.sell_armors(self.elves, amount)
            else:
                print('Wrong faction name!')
