from map import galaxy_map, map_print
from spaceship import SpaceShip
from player import Player
from planet import Planet
from kalsi import Kalsi
from venus import Venus


def main() -> None:
    player1 = Player()
    ship = SpaceShip()
    earth = Planet()
    kalsi = Kalsi()



    earth.buy_something_from_market(ship,player1)
    print(ship.count_weight_cargo())
    print(ship.print_items_and_weight_cargo())
    earth.buy_something_from_market(ship,player1)
    print(ship.count_weight_cargo())
    print(ship.print_items_and_weight_cargo())
    print(player1.get_money())
    
    earth.sell_something_from_ship(ship,player1)
    print(player1.get_money())
    print(ship.get_fuel())
    print(ship.count_weight_cargo())
    print(ship.print_items_and_weight_cargo())

    pass

main()