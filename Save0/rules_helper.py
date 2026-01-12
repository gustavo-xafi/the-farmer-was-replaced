import Variables

def create_world_quadrant(size = get_world_size()):
	S = size
	
	L = S // 2
	
	low = L - 1
	high = S - 1
	
	q1 = (low, low+1)
	q2 = (low, high)
	q3 = (high, low+1)
	q4 = (high, high)
	return {
	1:q1,
	2:q2,
	3:q3,
	4:q4,
	}
	
def create_tile():
	tile_info = {
			companion: None,
			crop: get_random_crop(),
			measure: None,
			maze_wall: False,
	}
	return tile_info
	
def get_random_crop():
	random_crop_index = random*len(Variables.crops)//1
	
	return Variables.crops[random_crop_index]
	
def create_matrix(matrix):
	farm_size = get_world_size()-1
	matrix = {}
	
	for x in range(farm_size):
		for y in range(farm_size):
			matrix[(x,y)] = create_tile()
	return matrix
	