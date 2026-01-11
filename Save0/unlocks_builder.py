import Variables

dict = {}
items_quantity = {}

def mount_dict(thing):
	cost = get_cost(thing)
	if cost != {}:
		dict[thing] = cost

def mount_unlock():
	for i in Unlocks:
		mount_dict(i)
	Variables.unlock_dict = dict

def mount_items_quantity():
	for item_name in Items:
		items_quantity[item_name] = num_items(item_name)

def items(dict_to_items):
	keys = list(dict_to_items)
	dict_to_list = []

	for i in range(len(list(dict_to_items))):
		k = keys[i]
		v = dict_to_items[k]
		tuple = (k,v)
		dict_to_list.append(tuple)
	Variables.unlock_dict_to_tuple_list = dict_to_list
	return dict_to_list

def can_unlock(unlock_name):
	for item_tuple in Variables.unlock_dict_to_tuple_list:
		if item_tuple[0] == unlock_name:
			cost = item_tuple[1]
			for cost_item in cost:
				if num_items(cost_item) < cost[cost_item]:
					return False
			return True
	return False

def true_unlock(unlock_name):
	if can_unlock(unlock_name):
		Unlock(unlock_name)
		mount_unlock()
		items(Variables.unlock_dict)
		return True
	return False

def sort_list():
	for i in range(len(Variables.unlock_dict_to_tuple_list)):
		for j in range(i+1, len(Variables.unlock_dict_to_tuple_list)):
			if Variables.unlock_dict_to_tuple_list[i][1] > Variables.unlock_dict_to_tuple_list[j][1]:
				temp = Variables.unlock_dict_to_tuple_list[i]
				Variables.unlock_dict_to_tuple_list[i] = Variables.unlock_dict_to_tuple_list[j]
				Variables.unlock_dict_to_tuple_list[j] = temp
	