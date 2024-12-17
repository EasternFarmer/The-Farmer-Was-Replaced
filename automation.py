from better_min import better_min
from sunflower import sunflower
from universal_plant import universal_plant
from harvest_all import harvest_all
from moveTo import moveTo
from Maze_follow_left_wall import maze
from Bubble_sort_cactus import cactus
from Brute_Force_Snake import dino
from pumpkin_v3 import pumpkin_harvest

the_items = [Items.Hay,
			Items.Wood,
			Items.Carrot,
			Items.Pumpkin,
			Items.Bone,
			#Items.Gold,
			#Items.Cactus
			]
uni_plant = {
	Items.Hay : Entities.Grass,
	Items.Carrot : Entities.Carrot,
	Items.Wood : Entities.Tree
}
str = {
	Items.Hay : 'Hay',
	Items.Wood : 'Wood',
	Items.Carrot : 'Carrot',
	Items.Pumpkin : 'Pumpkin',
	Items.Bone : 'Bones'
}
moveTo()
last_item = None
while True:
	VeryImportantItemIndex = better_min(the_items)
	theVeryImportantItem = the_items[VeryImportantItemIndex]
	a = num_items(theVeryImportantItem)
	if num_items(Items.Power) < 10000:
		sunflower()
	if theVeryImportantItem in uni_plant:
		universal_plant(uni_plant[theVeryImportantItem])
	elif theVeryImportantItem == Items.Pumpkin:
		harvest_all()
		pumpkin_harvest()
	elif theVeryImportantItem == Items.Gold:
		maze()
	elif theVeryImportantItem == Items.Cactus:
		harvest_all()
		cactus()
	elif theVeryImportantItem == Items.Bone:
		dino()
	last_item = str[theVeryImportantItem]
	quick_print('D: Itteration done succesfully')
	quick_print('D: Last item farmed: "', last_item, '"')
	quick_print('D: Amount of the item farmed "', num_items(theVeryImportantItem)-a, '"')