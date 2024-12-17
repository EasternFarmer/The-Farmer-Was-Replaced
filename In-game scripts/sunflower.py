from moveTo import moveTo, get_location
size = get_world_size()
for _ in range(size):
	for _ in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
		move(North)
	move(East)

def sunflower():
	maxPetals = 15
	sunflowerList = [[],[],[],[],[],[],[],[],[]]
	moveTo()
	for _ in range(size):
		for _ in range(size):
			plant(Entities.Sunflower)
			if get_water() < 0.5:
				use_item(Items.Water)
			sunflowerList[maxPetals - measure()].append(get_location())
			move(North)
		move(East)
	for elem in sunflowerList:
		for elem2 in elem:
			#quick_print(elem2)
			moveTo(elem2)
			if get_entity_type() == Entities.Sunflower:
				while not can_harvest():
					use_item(Items.Fertilizer)
			harvest()
	moveTo()
while num_items(Items.Power) < 100000:
	sunflower()