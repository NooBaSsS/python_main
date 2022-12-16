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
) -> list:
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
    
    return [
        name,
        hp_now,
        hp_max,
        lvl,
        xp_now,
        xp_next,
        attack,
        defence,
        luck,
        money,
        inventory
    ]


def show_hero(hero:list) -> None:
    print("имя:", hero[0])
    print("здоровье:", hero[1], "/", hero[2])
    print("уровень:", hero[3])
    print("опыт:", hero[4], "/", hero[5])
    print("атака:", hero[6])
    print("защита:", hero[7])
    print("удача:", hero[8])
    print("деньги:", hero[9])
    print("инвентарь:", hero[10])  # TODO: показать предметы и их количество
    print("")


def levelup(hero: list) -> None:
    """
    TODO: что растет с уровнем?
    """
    while hero[4] >= hero[5]:
        hero[3] += 1
        hero[5] = hero[3] * 100
        print(f"{hero[0]} получил {hero[3]} уровень\n")


def buy_item(hero: list, price: int, item: str) -> None:
    """
    Покупает предмет item за price монет и кладет его в инвентарь героя
    """
    os.system("cls")
    if hero[9] >= price:
        hero[9] -= price
        hero[10].append(item)
        print(f"{hero[0]} купил {item} за {price} монет!")
    else:
        print(f"У {hero[0]} нет столько монет! Не хватило {price - hero[9]}")
    input("нажмите ENTER чтобы продолжить")

def consume_item(hero: list) -> None:
    """
    TODO: кидает в меню вместо хаба
    """
    os.system("cls")
    show_options(hero, hero[10])
    idx = choose_options(hero, hero[10])
    os.system("cls")
    if idx is not None:
        if idx <= len(hero[10]) - 1 and idx > -1:
            print(f"{hero[0]} употребил {hero[10][idx]}", end=", ")
            if hero[10][idx] == "зелье здоровья":
                hero[1] += 25
                if hero[1] > hero[2]:
                    hero[1] = hero[2]
                    print(f"{hero[0]} вылечился")
            elif hero[10][idx] == "зелье силы":
                hero[6] += 2
                print(f"{hero[0]} стал сильнее")
            else:
                print("Никакого эффекта")
            hero[10].pop(idx)
    else:
        print("Нет такого индекса!")
    print("")



def play_dice(hero: list, bet: int) -> None:
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
            if hero[9] >= bet:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"{hero[0]} выбросил {hero_score}")
                print(f"Трактирщик выбросил {casino_score}")
                if hero_score > casino_score:
                    hero[9] += bet
                    print(f"{hero[0]} выиграл {bet} монет")
                    input("\nНажмите ENTER чтобы продолжить")
                elif hero_score < casino_score:
                    hero[9] -= bet
                    print(f"{hero[0]} проиграл {bet} монет")
                    input("\nНажмите ENTER чтобы продолжить")
                else:
                    print("Ничья!")
                    input("\nНажмите ENTER чтобы продолжить")
            else:
                print(f"У {hero[0]} нет денег на такую ставку!")
                input("\nНажмите ENTER чтобы продолжить")
        else:
            print("Ставки начинаются от 1 монеты!")
            input("\nНажмите ENTER чтобы продолжить")
        print("")


def combat_turn(attacker, defender):
    if attacker[1] > 0:
        damage = attacker[6]
        defender[1] -= damage
        print(f"{attacker[0]} ударил {defender[0]} на {damage} жизней!")


def start_fight(hero: list) -> None:
    enemy = make_hero(hp_now=30, xp_now=12, money=10, inventory=["меч"])
    options = [
            "атаковать противника",
            "использовать предмет из инвентаря"
    ]
    show_hero(hero)
    show_hero(enemy)

    while hero[1] > 0 and enemy[1] > 0:
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
    if hero[1] > 0 and enemy[1] <= 0:
        print(f"{hero[0]} победил!")
        print(enemy[4], "опыта")
        hero[4] += enemy[4]
        print(enemy[9], "монет")
        hero[9] += enemy[9]
        print("забрал")
        for item in enemy[10]:
            print(item, end=",")
        hero[10] += enemy[10]
        levelup(hero)
    elif hero[1] <= 0 and enemy[1] > 0:
        print(f"{enemy[0]} победил!")
        return main_menu(hero)
    else:
        print(f"{hero[0]} и {enemy[0]} пали в бою:(")


def fishing(hero):
    pass


def show_options(hero: list, options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")

def choose_options(hero: list, options: list) -> int:
    """
    описание ситуации, где происходит выбор
    принимает список возможных вариантов
    спросить пользователя вариант
    проверяет, есть ли такой вариант
    если есть, возвращает
    """
    
    
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


def visit_hub(hero: list) -> None:
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
    elif option == 1:
        idx = choose_options(hero, hero[10])
        if idx is not None:
            consume_item(hero, idx)
    elif option == 2:
        return visit_arena(hero)
    elif option == 3:
        return visit_casino(hero)
    elif option == 4:
        return visit_fishing_s(hero)
    elif option == 5:
        return main_menu(hero)
    else:
        print("такого варианта нет")
    input("\n э")


def visit_shop(hero: list) -> None:
    """
    текст магазина 
    опции с разными товарами и ценами
    покупка товаров + добавить их эффекты в функцию consume_item

    """
    text = f"{hero[0]} зашел в лавку алхимика"
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



def visit_casino(hero: list) -> None:
    text = f"{hero[0]} зашел в казино"
    options = [
        "выбрать ставку и сыграть в кости",
        "выйти в Хаб",
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_options(hero, options)
    os.system("cls")
    if option == 0:
        bet = input("сколько поставить? ")
        play_dice(hero, bet)
        return visit_casino(hero)
    elif option == 1:
        return visit_hub(hero)
    else:
        print("такого варианта нет")
        return visit_casino(hero)
        input("\nНажмите ENTER чтобы продолжить")
    input("\n э")


def visit_arena(hero: list) -> None:
    text = f"{hero[0]} зашел на арену"
    options = [
        "начать бой",
        "выйти в Хаб",
    ]
    show_options(hero, options)
    option = choose_options(hero, options)
    os.system("cls")
    if option == 0:
        start_fight(hero)
        return visit_arena(hero)
    elif option == 1:
        return visit_hub(hero)
    else:
        print("такого варианта нет")
        input("\nНажмите ENTER чтобы продолжить")
        return visit_arena(hero)


def visit_fishing_s(hero: list) -> None:
    text = f"{hero[0]} зашел "
    options = [
    "1"
    ]
    show_options(hero, options)
    option = choose_options(hero, options)
    os.system("cls")
    if option == 0:
        pass
    elif option == 1:
        return visit_hub(hero)
    else:
        print("такого варианта нет")
        input("\nНажмите ENTER чтобы продолжить")
        return visit_fishing_s(hero)


def main_menu(hero):
    os.system("cls")
    text = "Вы в главном меню"
    options = [
        "начать новую игру",
    ]
    show_options(hero, options)
    option = choose_options(hero, options)
    os.system("cls")
    if option == 0:
        return visit_hub(hero)
    else:
        print("такого варианта нет")
        return main_menu(hero)