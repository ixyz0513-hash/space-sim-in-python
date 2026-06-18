from spaceship import SpaceShip

galaxy_map = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
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
    
    pass
