from moveTo import moveTo
def universal_plant(entity):
	ws = get_world_size()
	moveTo()
	if not entity in [Entities.Tree, Entities.Pumpkin]:
		for i in range(ws):
			for j in range(ws):
				if get_ground_type() == Grounds.Grassland:
					till()
				if can_harvest():
					harvest()
				plant(entity)
				move(North)
			move(East)
		while not can_harvest():
			pass
	elif entity == Entities.Tree:
		for i in range(ws):
			for j in range(ws):
				if get_ground_type() == Grounds.Grassland:
					till()
				if can_harvest():
					harvest()
				if (j+i) % 2 == 0:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
				move(North)
			move(East)
		while not can_harvest():
			pass