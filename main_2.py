import random


class Hero:
    def __init__(self):
        self.hp_now = random.randint(50, 100)
        self.hp_max = self.hp_now
        self.lvl = 1
        self.xp_now = 0
        self.weapon = None
        self.shield = None
        self.attack = 1
        self.defence = 1
        self.luck = 1
        self.money = 0
        self.inventory = []


class Player(Hero):
    def __init__(self):
        super().__init__()
        self.name = input('q ')


class Ene(Hero):
    def __init__(self):
        super().__init__()
        self.name = 'aaa'


class Item:
    def __init__(self, price):
        self.name = None
        self.effects = None
        self.price = price


class Weapon(Item):
    def __init__(self, name='меч'):
        super().__init__(self)
        self.dmg = 2
        self.name = name

    def __str__(self):
        return 'aaaaaaaaa'


class Heal_item(Item):
    def __init__(self):
        super().__init__()
        self.heal = 10


def combat_turn(attacker, defender):
    if attacker.hp_now > 0:
        damage = attacker.attack
        defender.hp_now -= damage
        print(f"{attacker.name} ударил {defender.name} на {damage} жизней!")


def show_inventory(self):
    for i in range(len(self.inventory)):
        print(self.inventory[i])


'''def fight(attacker, defender):
    while attacker.hp_now > 0 and defender.hp_now > 0:
        combat_turn(attacker, defender)
        print(attacker.hp_now, defender.hp_now)
        combat_turn(defender, attacker)
        print(defender.hp_now, attacker.hp_now)
    if attacker.hp_now > 0 and defender.hp_now <= 0:
        print(f'{attacker.name} победил')
        attacker.inventory += defender.inventory
    elif attacker.hp_now <= 0 and defender.hp_now > 0:
        print(f'{defender.name} победил')
        defender.inventory += attacker.inventory
'''


def fight(attacker, defender):
    while attacker.hp_now > 0 and defender.hp_now > 0:
        show_inventory(attacker)
        a = int(input())
        if a == 1:
            pass


hero_1 = Player()
enem = Ene()
sword = Weapon(name='меч')
sword.name = 'Меч'
hero_1.inventory.append(sword)

fight(hero_1, enem)

print('aaaaaaaaaaaaa')
