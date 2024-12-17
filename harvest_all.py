from moveTo import moveTo
def harvest_all():
	moveTo(0,0)
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			move(North)
		move(East)