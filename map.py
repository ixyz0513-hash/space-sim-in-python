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
    
    
    for i in range(0, len(galaxy_map)):
        for j in range(0, len(galaxy_map[i])):
            
            if ship.get_y_position() == i and ship.get_x_position() == j:
                print("P",end=" ")

            elif earth.get_y_position() == i and earth.get_x_position() == j:
                print("E",end=" ")

            elif kalsi.get_y_position() == i and kalsi.get_x_position() == j:
                print("K",end=" ")

            elif mars.get_y_position() == i and mars.get_x_position() == j:
                print("M",end=" ")

            elif venus.get_y_position() == i and venus.get_x_position() == j:
                print("V",end=" ")
            
            else:
                print(galaxy_map[i][j],end=" ")
    
        print()
    
    return


    

