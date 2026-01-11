import rules
import Variables

def get_random():
	return Variables.crop_list[random()*len(Variables.crop_list)//1]

def some(crop_list, crop):
	I = len(crop_list)
	for I in range(len(crop_list)):
		if crop_list[I] == crop:
			return True
	
	return False

def flip_hat():
	do_a_flip()
	remove_trash()
	
def remove_trash_linear():
	if get_entity_type() == Entities.Dead_Pumpkin:
		till()
		till()
		plant(Entities.Pumpkin)
		if rules.found_dead_pumpkin == False:
			rules.safe_counter -= 1
			rules.found_dead_pumpkin = True 

def remove_trash_flip():
	if get_entity_type() == Entities.Dead_Pumpkin:
		till()
		till()
		plant(Entities.Pumpkin)
		use_item(Items.Water, 2)
		flip_hat()
			

def smart_till():
	if get_ground_type() != Grounds.Soil:
		till()
		
def should_crop_pumpkin(matrix):
	if (rules.safe_counter == 1):
		if len(matrix) == get_world_size()*get_world_size():
			for item in matrix:
				check = matrix[item][2]
				if check == Entities.Dead_Pumpkin:
					return False
			rules.safe_counter = 0
			return True
	return False

def tree_rule():
	even_tile = abs(get_pos_x() - get_pos_y())
	if even_tile % 2 == 0:
		return True
	return False

def watering_the_world():
	if Variables.should_not_watering:
		return False
	
	if get_water() < 0.5:
		use_item(Items.Water)

def clean_fertilizer(crop):
	rules.counter += 1
	if Variables.should_not_fertilize:
		return False
	if crop in rules.crop_to_fertilize:
		#if (rules.counter % 4):
		use_item(Items.Fertilizer)
	
def clean_harvest_and_till(harvestable, crop, matrix):
	clean_fertilizer(crop)
	watering_the_world()
	#rules.not_popped = False
	lucky_number = ((random() * (get_world_size()*15))//1)
	if crop == Entities.Tree and tree_rule() == True:
		if harvestable:
			harvest()
			smart_till()
	elif crop == Entities.Tree and not tree_rule() == True:
		crop = Variables.crop_list_without_tree[random()*len(Variables.crop_list_without_tree)//1]
			
	if (rules.mode_on == 1):
		remove_trash_linear()
	else:
		remove_trash()
	if harvestable and get_entity_type() != Entities.Pumpkin:
		harvest()
		smart_till()
		if lucky_number < 0:
			plant(Entities.Sunflower)
			return None
		plant(crop)
	if harvestable and crop != Entities.Pumpkin:
		harvest()
		smart_till()
		plant(crop)
	if crop == Entities.Pumpkin:
		harvest()
		smart_till()
		plant(crop)
	elif get_entity_type() == None:
		plant(crop)
	return None

def clean_harvest(crop, harvestable = can_harvest()):
	if harvestable:
		harvest()
		plant(crop)
	return None

def create_maze():
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)

def treasure_hunt():
	if get_entity_type() == Entities.Treasure:
		harvest()
	if get_entity_type() == Entities.Bush:
		create_maze()
	else:
		plant(Entities.Bush)
		create_maze()

def harvest_without_plant(harvestable):
	if harvestable:
		harvest()
	return None

def is_alternate_position():
	return (get_pos_x() + get_pos_y()) % 2

def is_last_tile():
	return get_pos_y() == (get_world_size()-1)
	
def get_pos_tuple():
	return (get_pos_x(), get_pos_y())
	
def is_world_mapped():
	return get_world_size()*get_world_size() == len(matrix)

	