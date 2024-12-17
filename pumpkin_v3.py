from moveTo import moveTo, get_location

def breakPumpkins(listOfEmpty):
	for tuple in listOfEmpty:
		moveTo(tuple)
		if not can_harvest():
			plant(Entities.Pumpkin)
		if get_location() == tuple:
			if get_entity_type() == Entities.Pumpkin:
				if can_harvest():
					listOfEmpty.remove(tuple)
	return listOfEmpty
	
def pumpkin_harvest():
	listOfEmpty = [(0,0)]
	while len(listOfEmpty) > 0:
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				CoordsTuple = get_location()
				if get_entity_type() != Entities.Pumpkin:
					listOfEmpty.append(CoordsTuple)
					plant(Entities.Pumpkin)
				elif CoordsTuple in listOfEmpty:
					if can_harvest():
						listOfEmpty.remove(CoordsTuple)
				move(North)
			move(East)
		while len(listOfEmpty) > 0:
			listOfEmpty = breakPumpkins(listOfEmpty)
	harvest()