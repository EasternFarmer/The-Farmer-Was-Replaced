from moveTo import moveTo
def bubble_sort(direction):
	for i in range(get_world_size()):
		for j in range(get_world_size()-i):
			if measure() > measure(direction):
				swap(direction)
			move(direction)
#clear()
def cactus():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)
			move(North)
		bubble_sort(North)
		move(East)
	moveTo(0,0)
	for i in range(get_world_size()):
		bubble_sort(East)
		move(North)
	harvest()

moveTo()
cactus()