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


def default_farm():
	grid_manipulator.populate_matrix(matrix)
	grid_manipulator.world_walker()
	position = helpers.get_pos_tuple()
	quadrant = square.which_quadrant(position)
	if helpers.can_spawn_drone():
		helpers.spawn_drones(quadrant, matrix)

	if quadrant in rules.crop_configuration:
		helpers.clean_harvest_and_till(
			can_harvest(), rules.crop_configuration[quadrant], matrix
		)
	else:
		helpers.clean_harvest_and_till(can_harvest(), helpers.get_random(), matrix)


def start_variables():
	unlocks_builder.mount_unlock()
	unlocks_builder.mount_items_quantity()
	unlocks_builder.items_quantity(Variables.unlock_dict)


def treasure_finder():
	if num_drones() < max_drones():
		spawn_drone(drone_orders)
		grid_manipulator.maze_lazy_walker()
		helpers.treasure_catch_and_reset()


def drone_orders():
	quick_print("I am Born", matrix, Variables.unlock_dict)
	while rules.not_popped:
		if Variables.is_maze_hunt:
			treasure_finder()
		if Variables.is_dinossaur_hunt:
			grid_manipulator.dinossaur_hunter()
		if Variables.is_dinossaur_hunt == False and Variables.is_maze_hunt == False:
			default_farm()
