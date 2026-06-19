from spaceship import SpaceShip

# 0 means empty space / random events maybe, 1 means an planet, 2 means hazard zone

galaxy_map = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


def map_print(ship: SpaceShip) -> None:

    for i in range(0, len(galaxy_map)):
        for j in range(0, len(galaxy_map[i])):
            
            if ship.get_y_position() == i and ship.get_x_position() == j:
                print("P",end=" ")
            
            else:
                print(galaxy_map[i][j],end=" ")
    
        print("")
    
    return


def check_if_on_something(ship: SpaceShip) -> bool:
    
    if galaxy_map[ship.get_y_position()][ship.get_x_position()] == 1:
        return True
    
    return False

