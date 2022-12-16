from main import*
player = make_hero(name="1",hp_now=2, inventory=["зелье здоровья", "меч"])
game = True
while game:
	visit_hub(player)