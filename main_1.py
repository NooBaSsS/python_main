import os
from random import randint, choice

first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый")


def make_hero(
        name=None,
        hp_now=None,
        hp_max=None,
        lvl=1,
        xp_now=0,
        attack=1,
        defence=1,
        luck=1,
        money=None,
        inventory=None,
) -> dict:

    if not name:
        name = choice(first_names) + " " + choice(last_names)

    if not hp_now:
        hp_now = randint(50, 100)
    
    if not hp_max:
        hp_max = hp_now

    xp_next = lvl * 100

    if money is None:
        money = randint(0, 100)

    if not inventory:
        inventory = []
    
    return {
        "имя": name,
        "жизни": hp_now,
        "жизни_макс": hp_max,
        "уровень": lvl,
        "опыт": xp_now,
        "опыт до уровня": xp_next,
        "атака": attack,
        "защита": defence,
        "удача": luck,
        "деньги": money,
        "инвентарь": inventory
    }
"""
    Персонаж - это список
    [0] name - имя
    [1] hp_now - здоровье текущее
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до следующего уровня
    [6] attack - сила атаки, применяется в бою
    [7] defence - защита, применяется в бою
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предметов
"""
def show_hero(hero: dict) -> None:
    for k, v in hero.items():
        print(f"{k}: {v}")


def levelup(hero: list) -> None:
    """
    TODO: что растет с уровнем?
    """
    while hero['опыт'] >= hero["опыт до уровня"]:
        hero["жизни_макс"] += 1
        hero["опыт до уровня"] = hero['уровень'] * 100
        print(f"{hero['имя']} получил {hero['уровень']} уровень\n")


def buy_item(hero: list, price: int, item: str) -> None:
    os.system("cls")
    if hero["деньги"] >= price:
        hero["деньги"] -= price
        hero['инвентарь'].append(item)
        print(f"{hero['имя']} купил {item} за {price} монет!")
    else:
        print(f"У {hero['имя']} нет столько монет! Не хватило {price - hero['деньги']}")
    input("нажмите ENTER чтобы продолжить")

"""
    Персонаж - это список
    [0] name - имя
    [1] hp_now - здоровье текущее
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до следующего уровня
    [6] attack - сила атаки, применяется в бою
    [7] defence - защита, применяется в бою
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предметов
"""
def consume_item(hero: dict) -> None:
    os.system("cls")
    show_options(hero, hero['инвентарь'])
    idx = choose_options(hero, hero['инвентарь'])
    os.system("cls")
    if idx is not None:
        if idx <= len(hero['инвентарь']) - 1 and idx > -1:
            print(f"{hero['имя']} употребил {hero['инвентарь'][idx]}", end=", ")
            if hero['инвентарь'][idx] == "зелье здоровья":
                hero['жизни'] += 25
                if hero['жизни'] > hero['жизни_макс']:
                    hero['жизни'] = hero['жизни_макс']
                    print(f"{hero['имя']} вылечился")
            elif hero['инвентарь'][idx] == "зелье силы":
                hero['атака'] += 2
                print(f"{hero['имя']} стал сильнее")
            else:
                print("Никакого эффекта")
            hero['инвентарь'].pop(idx)
    else:
        print("Нет такого индекса!")
    print("")



def play_dice(hero: dict, bet: int) -> None:
    """
    Ставка от 1 монеты до количества монет героя
    Игрок и казино бросаю кости, кто больше, то забирает ставку
    TODO: Как удача влияет на кости?
    """
    try:
        bet = int(bet)
    except ValueError:
        print("введите целое неотрицательное число")
    else:
        if bet > 0:
            if hero['деньги'] >= bet:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"{hero['имя']} выбросил {hero_score}")
                print(f"Трактирщик выбросил {casino_score}")
                if hero_score > casino_score:
                    hero['деньги'] += bet
                    print(f"{hero['имя']} выиграл {bet} монет")
                    input("\nНажмите ENTER чтобы продолжить")я
                elif hero_score < casino_score:
                    hero['деньги'] -= bet
                    print(f"{hero['имя']} проиграл {bet} монет")
                    input("\nНажмите ENTER чтобы продолжить")
                else:
                    print("Ничья!")
                    input("\nНажмите ENTER чтобы продолжить")
            else:
                print(f"У {hero['имя']} нет денег на такую ставку!")
                input("\nНажмите ENTER чтобы продолжить")
        else:
            print("Ставки начинаются от 1 монеты!")
            input("\nНажмите ENTER чтобы продолжить")
        print("")

"""
    Персонаж - это список
    [0] name - имя
    [1] hp_now - здоровье текущее
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до следующего уровня
    [6] attack - сила атаки, применяется в бою
    [7] defence - защита, применяется в бою
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предметов
"""
def combat_turn(attacker, defender):
    if attacker['жизни'] > 0:
        damage = attacker['атака']
        defender['жизни'] -= damage
        print(f"{attacker['имя']} ударил {defender['имя']} на {damage} жизней!")


def start_fight(hero: dict) -> None:
    enemy = make_hero(hp_now=30, xp_now=12, money=10, inventory=["меч"])
    options = [
            "атаковать противника",
            "использовать предмет из инвентаря"
    ]
    show_hero(hero)
    show_hero(enemy)

    while hero['жизни'] > 0 and enemy[1] > 0:
        show_options(hero, options)
        option = choose_options(hero, options)
        os.system("cls")
        if option == 0:
            combat_turn(hero, enemy)
            combat_turn(enemy, hero)
            show_hero(hero)
            show_hero(enemy)
        elif option == 1:
            consume_item(hero)
            combat_turn(enemy, hero)
            show_hero(hero)
            show_hero(enemy)
    combat_result(hero, enemy)
    input("\nНажмите ENTER чтобы продолжить")
    os.system("cls")


def combat_result(hero, enemy) -> None:
    os.system("cls")
    if hero['жизни'] > 0 and enemy[1] <= 0:
        print(f"{hero['имя']} победил!")
        print(enemy[4], "опыта")
        hero[4] += enemy[4]
        print(enemy[9], "монет")
        hero['деньги'] += enemy[9]
        print("забрал")
        for item in enemy[10]:
            print(item, end=",")
        hero['инвентарь'] += enemy[10]
        levelup(hero)
    elif hero['жизни'] <= 0 and enemy[1] > 0:
        print(f"{enemy[0]} победил!")
        return main_menu(hero)
    else:
        print(f"{hero['имя']} и {enemy[0]} пали в бою:(")


def show_options(hero: dict, options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def choose_options(hero: dict, options: list) -> int:
    option = input("\nвведите номер варианта: ")
    try:
        option = int(option)
    except ValueError:
        print("введите целое неотрицательное число")
    else:
        if option < len(options) and option > -1:
            return option
        else:
            print("такой выбор невозможен")


def visit_hub(hero: dict) -> None:
    os.system("cls")
    text = "w"
    options = [
        "зайти в лавку алхимика",
        "использовать предмет из инвентаря",
        "пойти на арену",
        "зайти в казино",
        "магазин",
        "выйти в главное меню"
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_options(hero, options)
    os.system("cls")
    show_hero(hero)
    if option == 0:
        return visit_shop(hero)


def visit_shop(hero: dict) -> None:
    """
    текст магазина 
    опции с разными товарами и ценами
    покупка товаров + добавить их эффекты в функцию consume_item

    """
    text = f"{hero['имя']} зашел в лавку алхимика"
    options = [
        "купить зелье здоровья за 10 монет",
        "купить зелье силы за 15 монет",
        "выйти в Хаб",
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_options(hero, options)
    os.system("cls")
    if option == 0:
        buy_item(hero, 10, "зелье здоровья")
        return visit_shop(hero)
    elif option == 1:
        buy_item(hero, 15, "зелье силы")
        return visit_shop(hero)
    elif option == 2:
        return visit_hub(hero)
    else:
        print("такого варианта нет")
        return visit_shop(hero)


player = make_hero()
while True:
    visit_hub(player)