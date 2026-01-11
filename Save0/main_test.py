def should_crop_pumpkin(matrix, safe_counter):
	for item in first_square:
		check = first_square[item][2]
		if check == Entities.Dead_Pumpkin:
			return False
	safe_counter += 1
