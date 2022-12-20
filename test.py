from main_1 import*
player = make_hero(
    name="1",
    hp_now=100,
    money=1000,
    inventory=[
        {
            "тип": "оружие",
            "название": "необычный меч",
            "модификатор": 4,
            "цена": 105,
        }
    ]
    )
game = True
while game:
	visit_hub(player)