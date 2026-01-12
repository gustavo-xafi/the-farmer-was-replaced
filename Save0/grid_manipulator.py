import square
import helpers
import rules
import Variables

world_size = get_world_size() - 1


def move_and_update(way):
    if way == None:
        return None
    move(way)

    # Variables.came_from = [Variables.oposite[way]]
    # quick_print(Variables.came_from)


def stuck(way):
    if can_move(way) == True:
        move_and_update(way)
        return False
    return True


def find_next_pos(pos, way):
    x, y = pos
    next_pos = ()
    X = [North, South]
    Y = [East, West]
    if way in X:
        return (x + rules.path_finding_x[way], y)
    if way in Y:
        return (x, y + rules.path_finding_y[way])
    quick_print("I SHOULD NOT EXIST, I AM A BUG, TELL ME WHYYYY")
    return None


def where_can_i_go():
    Variables.walkable = set()
    for way in Variables.directions:
        if can_move(way):
            Variables.walkable.add(way)
    quick_print(Variables.walkable)


def best_way(pos):
    quick_print(measure())
    measured = Variables.apple_pos
    if measured == None:
        return None
    tx, ty = measured
    x, y = pos

    # Calcula a distância relativa
    dx = tx - x
    dy = ty - y

    # Valor absoluto manual para comparação
    abs_x = dx
    if dx >= 0:
        abs_x = dx
    else:
        abs_x = -dx
    abs_y = dy

    if dy >= 0:
        abs_y = dy
    else:
        abs_y = -dy

    # Se a distância horizontal for maior ou igual à vertical
    if abs_x >= abs_y:
        if dx > 0:
            return East
        elif dx < 0:
            return West
        # Se dx for 0, mas abs_x >= abs_y, significa que ambos são 0 ou só resta Y
        if dy > 0:
            return North
        else:
            return South

    # Se a distância vertical for maior que a horizontal
    else:
        if dy > 0:
            return North
        elif dy < 0:
            return South

        if dx > 0:
            return East
        else:
            return West


def dinossaur_hunter(came_from=Variables.came_from):
    if Variables.is_dinossaur_hat_on == False:
        change_hat(Hats.Dinosaur_Hat)
        Variables.is_dinossaur_hat_on = True

    if Variables.apple_pos == None:
        Variables.apple_pos = measure()

    pos = (get_pos_x(), get_pos_y())
    update_walked_in(pos)
    where_i_go = Variables.walkable
    move_and_update(best_way(pos))
    helpers.dinossaur_harvest_and_till()


def maze_lazy_walker():
    maze_walker()


def update_walked_in(pos):
    Variables.walked_in.add(pos)


def walk_random():
    next_pos = Variables.directions[random() * len(Variables.directions) // 1]
    move(next_pos)


def world_walker():

    if get_pos_y() == world_size:
        move_and_update(East)
        move_and_update(North)

    elif get_pos_y() != world_size:
        move_and_update(North)

    if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
        rules.safe_counter += 1
        rules.found_dead_pumpkin = False


def populate_matrix(matrix):
    square.map_tile_info_into_matrix(matrix)
    return matrix


def generate_tuple_matrix_by_square_number(square_number):
    number_of_fields = square_number**square_number
    matrix_array = []
    for x in range(square_number):
        for y in range(square_number):
            matrix_array.append((x, y))
    return matrix_array


def update_matrix(matrix, square_number, crop):
    if helper.is_world_mapped():

        matrix_tuple = generate_tuple_matrix_by_square_number(square_number)
        for tuple in matrix_tuple:
            for i in matrix:
                if tuple == i:
                    matrix[i] = square.create_tile_with_crop(crop)
