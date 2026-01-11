import helpers
import rules

	
def map_tile_info_into_matrix(matrix):
	matrix[helpers.get_pos_tuple()] = create_tile()
	
def manipulate_tile(tile, ground_type, entity_type):
	tile[0] = ground_type
	tile[2] = entity_type
	
	return tile
	
def create_tile():
	tile = [
	get_ground_type(),
	get_companion(),
	get_entity_type()
	]
	return tile

def create_tile_with_crop(crop):
	tile = [
	rules.crop_configuration[crop],
	get_companion(),
	crop
	]
	return tile

def create_tile_tuple(pos):
	return (pos, create_tile())
	
def which_quadrant(pos):
	x,y = pos
	for i in rules.quadrant_if:
		X, Y = rules.quadrant_if[i]
		if x <= X and y <= Y:
			return i
	
	