from main import*
player = make_hero(name="1", inventory=["зелье здоровья", "меч"])
game = True
while game:
	main_menu(player)