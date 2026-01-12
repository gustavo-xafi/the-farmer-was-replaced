import main
import Variables

set_world_size(8)
# spawn_drone(main.drone_orders())
spawn_drone(main.drone_orders)
main.helpers.start_maze_hunt()
