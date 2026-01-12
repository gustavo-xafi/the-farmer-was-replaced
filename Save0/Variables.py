matrix = {}
unlock_dict = {}
unlock_dict_to_tuple_list = []

is_dinossaur_hunt = True
is_dinossaur_hat_on = False
should_not_fertilize=True
should_not_watering=False
is_maze_hunt = False

apple_pos = None
collected = False

crop_list = [
Entities.Cactus,
Entities.Sunflower, 
Entities.Grass,
Entities.Tree,
Entities.Cactus,
Entities.Carrot,
Entities.Pumpkin
]

crop_list_without_tree = [
Entities.Sunflower, 
Entities.Grass,
Entities.Cactus,
Entities.Carrot,
#Entities.Pumpkin
]

hat_list = [
Hats.Brown_Hat,
Hats.Cactus_Hat,
Hats.Carrot_Hat,
Hats.Gray_Hat,
Hats.Pumpkin_Hat,
Hats.Purple_Hat,
Hats.Sunflower_Hat,
Hats.Wizard_Hat]

wrong_path = 0

came_from = [None]

crops = [
Entities.Cactus,
Entities.Carrot,
Entities.Tree,
Entities.Pumpkin
]

walked_in = set()

repeated_walk = 3

walkable = set()

directions = [North,East,South,West]

oposite = {
North:South,
South:North,
East:West,
West:East
}


