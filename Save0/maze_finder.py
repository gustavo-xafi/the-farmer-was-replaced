import Variables
import helpers


def random_walk(directions=None):
	if random_walk() == True:
		return True
	if get_entity_type() == Entities.Treasure:
		return helpers.create_maze()
	next_pos = directions
	if directions == None:
		next_pos = Variables.directions[random() * len(Variables.directions) // 1]
	walked = move(next_pos)
	if walked == False:
		return True
	random_walk(next_pos)
	return False