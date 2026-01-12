import square
import helpers
import rules
import Variables

world_size = get_world_size() - 1


def move_and_update(way):
    move(way)
    Variables.came_from = [Variables.oposite[way]]
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
    Variables.walkable = []
    for way in Variables.directions:
        if can_move(way):
            Variables.walkable.append(way)
    quick_print(Variables.walkable)


def best_way(pos):
    tx, ty = measure()
    x, y = pos
    dx = tx - x
    dy = ty - y

    # Cálculo manual do valor absoluto
    abs_x = dx
    if dx < 0:
        abs_x = -dx

    abs_y = dy
    if dy < 0:
        abs_y = -dy

    # Decisão de direção baseada na maior distância
    if abs_x >= abs_y:
        if dx > 0:
            return East
        if dx < 0:
            return West
        # Se x está alinhado, tenta y
        if dy > 0:
            return North
        return South
    else:
        if dy > 0:
            return North
        if dy < 0:
            return South
        # Se y está alinhado, tenta x
        if dx > 0:
            return East
        return West


def maze_walker():
    pos = (get_pos_x(), get_pos_y())
    update_walked_in(pos)
    where_can_i_go()
    where_i_go = Variables.walkable

    # Se só tem um caminho disponível, ele é o caminho de volta ou a única saída
    if len(where_i_go) == 1:
        move_and_update(where_i_go[0])
        return

    # Pegamos a direção matematicamente melhor
    target = best_way(pos)

    # 1. Tentar a melhor direção, desde que não seja de onde viemos
    # (A menos que seja a única opção)
    if target in where_i_go:
        if target != Variables.came_from[0]:
            move_and_update(target)
            return

    # 2. Se a melhor direção não serve ou é de onde viemos,
    # tentamos qualquer outra que não seja a de volta
    for way in where_i_go:
        if way != Variables.came_from[0]:
            move_and_update(way)
            return

    # 3. Se chegamos aqui, é um beco sem saída absoluto.
    # A única opção no where_i_go é o came_from[0]
    move_and_update(Variables.came_from[0])


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
