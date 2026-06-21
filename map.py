from spaceship import SpaceShip
from earth import Earth
from kalsi import Kalsi
from mars import Mars
from venus import Venus

# 0 means empty space / random events maybe, 1 means hazard zone

galaxy_map: list[str] = [
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"]
]


def map_print(ship: SpaceShip, earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:
    found: bool = False
    
    for i in range(0, len(galaxy_map)):
        for j in range(0, len(galaxy_map[i])):
            
            
            if ship.get_y_position() == i and ship.get_x_position() == j:
                galaxy_map[ship.get_y_position()][ship.get_x_position()] = "P"

            elif earth.get_y_position() == i and earth.get_x_position() == j:
                galaxy_map[earth.get_y_position()][earth.get_x_position()] = "E"

            elif kalsi.get_y_position() == i and kalsi.get_x_position() == j:
                galaxy_map[kalsi.get_y_position()][kalsi.get_x_position()] = "K"

            elif mars.get_y_position() == i and mars.get_x_position() == j:
                galaxy_map[mars.get_y_position()][mars.get_x_position()] = "M"

            elif venus.get_y_position() == i and venus.get_x_position() == j:
                galaxy_map[venus.get_y_position()][venus.get_x_position()] = "V"
            
            if found == False:
                print(galaxy_map[i][j],end=" ")
    
        print()
    
    return


def check_if_on_something(ship: SpaceShip) -> bool:
    
    if galaxy_map[ship.get_y_position()][ship.get_x_position()] == 1:
        return True
    
    return False

