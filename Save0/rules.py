import rules_helper

crop_configuration = {
3: Entities.Sunflower
}
not_popped = True

crop_to_fertilize = [
Entities.Bush, 
Entities.Carrot,
Entities.Tree,
]

counter = 0
found_dead_pumpkin = False

quadrant_crop = {
0: Entities.Grass,
1: Entities.Carrot,
2: Entities.Sunflower,
3: Entities.Tree,
}

mode = {
1:"linear",
2:"flip",
}


mode_on = 1

quadrant_if  = rules_helper.create_world_quadrant()
quick_print(quadrant_if)
safe_counter = 0

path_finding_x = {
North:1,
South:-1,
}
path_finding_y = {
East:1,
West:-1,
}
