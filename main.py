from map import galaxy_map, map_print
from spaceship import SpaceShip
from player import Player
from planet import Planet


def main() -> None:
    player1 = Player()
    ship = SpaceShip()
    planet1 = Planet()

    planet1.buy_something_from_market(ship,player1)
    print(ship.count_weight_cargo())
    print(player1.get_money())

    planet1.sell_something_from_ship(ship,player1)
    print(ship.count_weight_cargo())
    print(player1.get_money())

    pass

main()