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
        self.inventory = ['']


class Player(Hero):
    def __init__(self):
        super().__init__()
        self.name = input('q ')


class Ene(Hero):
    def __init__(self):
        super().__init__()
        self.name = 'aaa'


class Weapon:
    def __init__(self):
        self.dmg = 2


class Item:
    def __init__(self):
        self.name = None
        self.effects = None


class Heal_item(Item):
    def __init__(self):
        super().__init__()
        self.heal = 10


def combat_turn(attacker, defender):
    if attacker.hp_now > 0:
        damage = attacker.attack
        defender.hp_now -= damage
        print(f"{attacker.name} ударил {defender.name} на {damage} жизней!")


def fight(attacker, defender):
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


hero_1 = Player()
enem = Ene()

fight(hero_1, enem)

print('aaaaaaaaaaaaa')
