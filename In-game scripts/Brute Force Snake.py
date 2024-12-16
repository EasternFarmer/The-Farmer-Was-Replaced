def dino():
	path = [
		North,North,North,North,North,North,North,North,North,
		East,
		South,South,South,South,South,South,South,South,
		East,
		North,North,North,North,North,North,North,North,
		East,
		South,South,South,South,South,South,South,South,
		East,
		North,North,North,North,North,North,North,North,
		East,
		South,South,South,South,South,South,South,South,
		East,
		North,North,North,North,North,North,North,North,
		East,
		South,South,South,South,South,South,South,South,
		East,
		North,North,North,North,North,North,North,North,
		East,
		South,South,South,South,South,South,South,South,South,
		West,West,West,West,West,West,West,West,West
	]
	
	change_hat(Hats.Dinosaur_Hat)
	true = True
	while true:
		for dir in path:
			if not move(dir):
				change_hat(Hats.Straw_Hat)
				true = False
				break