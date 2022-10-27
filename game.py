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

    def handle_turn(self):
        self.orcs.perform_attack() if self.orcs.is_alive else None
        self.dwarves.perform_attack() if self.dwarves.is_alive else None
        self.elves.perform_attack() if self.elves.is_alive else None

        self.merchant.end_turn()
        self.orcs.end_turn()
        self.dwarves.end_turn()
        self.elves.end_turn()

        self.day += 1
        print('Turn ended!')
        print('It is day {} in Warmonger!.\n'.format(self.day))

    def handle_inputs(self) -> str:
        print('1. See merchant')
        print('2. See faction details')
        print('3. Sell merchs')
        print('4. End turn')
        print('5. Quit game\n')

        command = input('What do you want to do?')

        return command

    def start(self):
        print(
            '\n*** Welcome to the game of Warmonger, the sun rises as it is your 1st day here and sale starts. ***\n')

        while True:
            command = self.handle_inputs()
            print()

            if command == '1':
                self.merchant.print()
            elif command == '2':
                self.see_faction_details()
            elif command == '3':
                self.handle_sales()
            elif command == '4':
                self.handle_turn()
            elif command == '5':
                break
            else:
                print('Give me a correct command, boy!')
