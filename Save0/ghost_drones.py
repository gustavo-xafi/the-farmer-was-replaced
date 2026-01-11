import helpers
import grid_manipulator
import rules
import square
import Variables

def dance():
	last_y = get_world_size()-1
	for _ in range(last_y*2):
		
		position = helpers.get_pos_tuple()
		quadrant = square.which_quadrant(position)
		helpers.clean_harvest_and_till(can_harvest(), helpers.get_random(), Variables.matrix)
		grid_manipulator.world_walker()

