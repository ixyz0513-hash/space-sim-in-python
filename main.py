from map import galaxy_map, map_print
from spaceship import SpaceShip
from player import Player
from earth import Earth
from kalsi import Kalsi
from mars import Mars
from venus import Venus
from os import system,name


def clear_screen() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    return


def game_loop(player: Player, ship: SpaceShip, earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> bool:
    
    return True


def main() -> None:
    player1 = Player()
    ship = SpaceShip()
    earth = Earth()
    kalsi = Kalsi()
    mars = Mars()
    venus = Venus()

    map_print(ship,earth,kalsi,mars,venus)
    clear_screen()

    return

main()