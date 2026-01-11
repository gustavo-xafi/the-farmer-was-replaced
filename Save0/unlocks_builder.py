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
	