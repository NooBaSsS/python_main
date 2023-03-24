from random import randint

class hero:
    def __init__(self):
        self.name = 'aa'
        self.hp_now = randint(50, 100)
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

class weapon:
    def __init__(self):
        self.dmg = 2



def combat_turn(attacker, defender):
    if attacker.hp_now > 0:
        damage = attacker.attack
        defender.hp_now -= damage
        print(f"{attacker.name} ударил {defender.name} на {damage} жизней!")


hero_1 = hero()
hero_2 = hero()
hero_1.name = 'aaa'

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


fight(hero_1, hero_2)



print('aaaaaaaaaaaaa')