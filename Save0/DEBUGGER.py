import square

test = Items
keys = list(Items)
values = keys[0]
values_list = []
for i in range(len(keys)):
	k = keys[i]
	v = test[k]
	tuple = (k,v)
	values_list.append(tuple)
	
quick_print(test)
	
quick_print(values_list)
	