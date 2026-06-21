from map import galaxy_map, map_print
from spaceship import SpaceShip
from player import Player
from earth import Earth
from kalsi import Kalsi
from mars import Mars
from venus import Venus
from os import system,name
from constants import FUEL_LOST_PER_DISTANCE1,FUEL_GAIN_PER_FUEL_CELL,FUEL_CELL_PRICE,HEALTH_CELL_PRICE,HEALTH_GAIN_PER_HEALTH_CELL,IMMUNITY_HAZARD_PRICE,MARKET_PREDICTOR_PRICE,TELEPORT_PRICE,MINNING_ASTEROID_DEVICE_PRICE,EFFICIENCY_BOOSTER_PRICE


def clear_screen() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    return


def check_if_leave() -> bool:
    number_str: str = input("Type 1 to leave: ")
    number: int = int(number_str)

    if number <= 0 or number > 1:
        return False


    return True


def print_welcome(ship: SpaceShip) -> bool:
    clear_screen()

    print("Hello this is the space simulator game its all about navigating and selling your cargo to planets for now there are four planets and probably there will be only four forever")
    print(f"fuel is the most important thing in this game otherwise you wouldnt be able to move so game lost ggs your starting fuel is unless you changed it in the code {ship.get_fuel()}")
    print(f"a way to gain fuel is by buying fuel cells and using them when you use a fuel cell you get {FUEL_GAIN_PER_FUEL_CELL} its normally 35 and you lose {FUEL_LOST_PER_DISTANCE1} per distance the formula for this is fuel lost per distance divided by your engine efficiency and then multiplied by the distance")
    print("there is a alot of stuff like consumables only fuel cells work for now but i plan to make all of these other consumables work asap there is a instruction guide you can check what everything does and the other consumables that dont work too")
    print("i plan to add alot of things like random events and maybe turn based attacking and secret items gained from quests but that will come sometime because i need to get the main things working first")
    print("still going i plan to add things like reputation systems for planets too but thats all for now go play the game")
    
    

    if check_if_leave() == False:
        return False
    
    return True


def print_instructions_consumables() -> bool:
    clear_screen()
    
    print(f"fuel cell: fuel cell costs default {FUEL_CELL_PRICE} the price can be not the same because the multiplier for the market is not 1.0 it gives you {FUEL_GAIN_PER_FUEL_CELL}")
    print(f"health cell: health cell costs default {HEALTH_CELL_PRICE} it can be random like always it gives you {HEALTH_GAIN_PER_HEALTH_CELL} not implemented yet but you can sell it")
    print(f"immunity hazard armor: immunity hazard armor costs default {IMMUNITY_HAZARD_PRICE} it gives you 3 turns of immunity to hazards not implemented yet but you can sell it")
    print(f"market predictor: market predictor costs default {MARKET_PREDICTOR_PRICE} it gives you info what will change in every planets market multipliers like buy and sell not implemented yet but you can sell it")
    print(f"teleport device: teleport device costs default {TELEPORT_PRICE} it gives you the ability to teleport maximum 4 distance not implemented yet but you can sell it")
    print(f"minning asteroid device: minning asteroid device costs default {MINNING_ASTEROID_DEVICE_PRICE} it gives you the ability to mine asteroids for special items not implemented yet but you can sell it")
    print(f"efficiency booster: efficiency booster costs default {EFFICIENCY_BOOSTER_PRICE} it gives you 0.5 efficiency for 3 turns not implemented yet but you can sell it")


    if check_if_leave() == False:
        return False
    
    return True



def game_loop(player: Player, ship: SpaceShip, earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> bool:
    clear_screen()
    
    if print_instructions_consumables() == False:
        return False

    return True


def main() -> None:
    player = Player()
    ship = SpaceShip()
    earth = Earth()
    kalsi = Kalsi()
    mars = Mars()
    venus = Venus()
    
    while print_welcome(ship) != True:
        print()

    
    while game_loop(player,ship,earth,kalsi,mars,venus) != True:
        print()
    
    return

main()