import Variables
import helpers
import main


def random_direction(directions):
	if (len(directions) == 0):
		return None
	random_dir = directions[random() * len(directions) // 1]
	return random_dir


def move_random():
	next_pos = random_direction(Variables.directions)
	move_and_update(next_pos)


def follow_path(direction):
	while can_move(direction):
		move(direction)
	return direction


def walk_back(came_from):
	return move(Variables.oposite[came_from])


def is_corner(direction):
	came_from = Variables.directions
	can_move_directions = []
	for dir in came_from:
		if dir == direction:
			continue
		if can_move(dir):
			can_move_directions.append(dir)
		if len(can_move_directions) == 0:
			return False
	return True


def can_go():
	dir_options = []
	for direction in Variables.directions:
		if direction == Variables.last_path:
			continue
		if can_move(direction):
			dir_options.append(direction)
	return dir_options


def move_and_update(way):
	helpers.treasure_catch_and_restart()
	if way == None:
		move_random()
		return False
	if can_move(way) == True:
		Variables.last_path = way
		return move(way)
	elif can_move(Variables.oposite[way]) == True:
		Variables.last_path = Variables.oposite[way]
		return move(Variables.oposite[way])
	else:
		move_random()


def move_smart():
	directions = can_go()
	way = random_direction(directions)
	while can_move(way):
		new_directions = can_go()
		if (random() * 2 // 1) == 1:
			move_and_update(random_direction(new_directions))
		move_and_update(way)


def random_walk():
	move_smart()
