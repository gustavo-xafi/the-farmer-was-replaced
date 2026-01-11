import helpers
import grid_manipulator
import square
import rules
import Variables
import ghost_drones
import unlocks_builder

target = Entities.Carrot
safe_counter = 0
matrix = Variables.matrix
harvest_pupkin = False

def start_variables():
	unlocks_builder.mount_unlock()
	unlocks_builder.mount_items_quantity()
	unlocks_builder.items_quantity
def new_drone_orders():
	while True:
		if num_drones() < max_drones():
			spawn_drone(f0.solve_with_bfs)
		
		f0.solve_with_bfs()

def drone_orders():
	quick_print("I am Born", matrix, Variables.unlock_dict)
	while rules.not_popped:
		if Variables.maze_mode == True:
			if num_drones() < max_drones():
				spawn_drone(drone_orders)
			grid_manipulator.maze_lazy_walker()
			helpers.treasure_hunt()
		else:
			grid_manipulator.populate_matrix(matrix)
			if (Variables.dinossaur):
				grid_manipulator.walk_random()
			else:
				grid_manipulator.world_walker()
			position = helpers.get_pos_tuple()
			quadrant = square.which_quadrant(position)
			quick_print(num_drones())
			if num_drones() != max_drones():
				spawn_drone(ghost_drones.dance)
				move(East)
				if quadrant in rules.crop_configuration:
					helpers.clean_harvest_and_till(can_harvest(), rules.crop_configuration[quadrant], matrix)
				else:
					helpers.clean_harvest(helpers.get_random())
						

			if quadrant in rules.crop_configuration:
				helpers.clean_harvest_and_till(can_harvest(), rules.crop_configuration[quadrant], matrix)
			else:
				helpers.clean_harvest_and_till(can_harvest(), helpers.get_random(), matrix)
		