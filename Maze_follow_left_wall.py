amount = get_world_size()*num_unlocked(Unlocks.Mazes)
def moveMaze(LM):
	# LM is short for lastmovement, i changed it for better readability
	rotCCW = {North:West, East:North, South:East, West:South}
	rotCW = {North:East, East:South, South:West, West:North}
	if move(rotCCW[LM[0]]):
		LM.insert(0, rotCCW[LM[0]])
		return LM
	elif move(LM[0]):
		LM.insert(0, LM[0])
		return LM
	elif move(rotCCW[LM[0]]):
		LM.insert(0, rotCCW[LM[0]])
		return LM
	elif move(rotCW[LM[0]]):
		LM.insert(0, rotCW[LM[0]])
		return LM
	elif move(rotCW[rotCW[LM[0]]]):
		LM.insert(0, rotCW[rotCW[LM[0]]])
		return LM
def maze():
	lastmovement = []
	plant(Entities.Bush)
	while get_entity_type() == Entities.Bush:
		use_item(Items.Weird_Substance, amount)
	lastmovement.insert(0, North)
	while not measure():
		lastmovement = moveMaze(lastmovement)
	harvest()
while num_items(Items.Gold) < 300000:
	maze()