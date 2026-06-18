from map import galaxy_map, map_print
from spaceship import SpaceShip
from player import Player


def main() -> None:
    ship = SpaceShip()
    print(ship.get_fuel())
    map_print(ship)
    ship.move()
    map_print(ship)
    print(ship.get_fuel())
    pass

main()