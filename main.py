from map import galaxy_map, map_print
from spaceship import SpaceShip
from player import Player
from earth import Earth
from kalsi import Kalsi
from mars import Mars
from venus import Venus
from os import system,name
from constants import FUEL_LOST_PER_DISTANCE1,FUEL_GAIN_PER_FUEL_CELL,FUEL_CELL_PRICE,HEALTH_CELL_PRICE,HEALTH_GAIN_PER_HEALTH_CELL,IMMUNITY_HAZARD_PRICE,MARKET_PREDICTOR_PRICE,TELEPORT_PRICE,MINNING_ASTEROID_DEVICE_PRICE,EFFICIENCY_BOOSTER_PRICE
from time import sleep
from random_number import random_number_generator






def wait() -> None:
    sleep(1.5)


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






def check_what_market_buy(player: Player, ship: SpaceShip, earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:

    IF_FALSE_SKIP: bool = True

    if earth.get_y_position() == ship.get_y_position() and earth.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = earth.buy_something_from_market(ship,player)

    elif kalsi.get_y_position() == ship.get_y_position() and kalsi.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = kalsi.buy_something_from_market(ship,player)

    
    elif mars.get_y_position() == ship.get_y_position() and mars.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = mars.buy_something_from_market(ship,player)

    
    elif venus.get_y_position() == ship.get_y_position() and venus.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = venus.buy_something_from_market(ship,player)


    
    if IF_FALSE_SKIP == False:
        wait()
    

    return




def check_what_market_sell(player: Player, ship: SpaceShip, earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:
    IF_FALSE_SKIP: bool = True

    if earth.get_y_position() == ship.get_y_position() and earth.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = earth.sell_something_from_ship(ship,player)

    elif kalsi.get_y_position() == ship.get_y_position() and kalsi.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = kalsi.sell_something_from_ship(ship,player)

    
    elif mars.get_y_position() == ship.get_y_position() and mars.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = mars.sell_something_from_ship(ship,player)

    
    elif venus.get_y_position() == ship.get_y_position() and venus.get_x_position() == ship.get_x_position():
        IF_FALSE_SKIP = venus.sell_something_from_ship(ship,player)


    
    if IF_FALSE_SKIP == False:
        wait()
    

    return


def check_what_market_multiplier_sell(ship: SpaceShip,earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:

    name_planet: str = ""
    multiplier_planet_sell: float = None
    
    if earth.get_y_position() == ship.get_y_position() and earth.get_x_position() == ship.get_x_position():
        name_planet = earth.get_name()
        multiplier_planet_sell = earth.get_sell_cost_multiplier()

    elif kalsi.get_y_position() == ship.get_y_position() and kalsi.get_x_position() == ship.get_x_position():
        name_planet = kalsi.get_name()
        multiplier_planet_sell = kalsi.get_sell_cost_multiplier()

    
    elif mars.get_y_position() == ship.get_y_position() and mars.get_x_position() == ship.get_x_position():
        name_planet = mars.get_name()
        multiplier_planet_sell = mars.get_sell_cost_multiplier()

    
    elif venus.get_y_position() == ship.get_y_position() and venus.get_x_position() == ship.get_x_position():
        name_planet = venus.get_name()
        multiplier_planet_sell = venus.get_sell_cost_multiplier()
    

    if multiplier_planet_sell != None:
        print(f"{name_planet} sell multiplier is: {multiplier_planet_sell}")

    else:
        print("no planet found")

    return



def check_what_market_multiplier_buy(ship: SpaceShip,earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:

    name_planet: str = ""
    multiplier_planet_buy: float = None
    
    if earth.get_y_position() == ship.get_y_position() and earth.get_x_position() == ship.get_x_position():
        name_planet = earth.get_name()
        multiplier_planet_buy = earth.get_buy_cost_multiplier()

    elif kalsi.get_y_position() == ship.get_y_position() and kalsi.get_x_position() == ship.get_x_position():
        name_planet = kalsi.get_name()
        multiplier_planet_buy = kalsi.get_buy_cost_multiplier()

    
    elif mars.get_y_position() == ship.get_y_position() and mars.get_x_position() == ship.get_x_position():
        name_planet = mars.get_name()
        multiplier_planet_buy = mars.get_buy_cost_multiplier()

    
    elif venus.get_y_position() == ship.get_y_position() and venus.get_x_position() == ship.get_x_position():
        name_planet = venus.get_name()
        multiplier_planet_buy = venus.get_buy_cost_multiplier()
    

    if multiplier_planet_buy != None:
        print(f"{name_planet} buy multiplier is: {multiplier_planet_buy}")
    
    else:
        print("no planet found")

    return



def market_go_up_or_down(earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:
    counter: int = 0

    list_planet = [earth,kalsi,mars,venus]

    while counter <= 3:
        minus_plus_sell: int = random_number_generator(0,5)
        minus_plus_buy: int = random_number_generator(0,5)
        multiplier_sell: float = random_number_generator(0.10,0.20)
        multiplier_buy: float = random_number_generator(0.15,0.25)

        list_planet[counter].market_substract_plus(minus_plus_sell,minus_plus_buy,multiplier_sell,multiplier_buy)

        counter += 1

    return





def game_loop(player: Player, ship: SpaceShip, earth: Earth, kalsi: Kalsi, mars: Mars, venus: Venus) -> None:
    clear_screen()
    map_print(ship,earth,kalsi,mars,venus)
    
    print("type 1 to check the instructions for the consumables")
    print("type 2 to move your ship")
    print("type 3 to buy items if on a planet")
    print("type 4 to sell your items if on a planet")
    print("type 5 to check your money")
    print("type 6 to check your fuel")
    print("type 7 to check your cargo")
    print("type 8 to use a fuel cell")
    print("type 9 to get the buy cost multiplier of a planet if on a planet")
    print("type 10 to get the sell cost multiplier of a planet if on a planet")

    number_str: str = input("type your choice: ")
    number: int = int(number_str)

    if number == 1:
        while print_instructions_consumables() == False:
            clear_screen()

    
    elif number == 2:
        while ship.move() == False:
            sleep(1.5)
            clear_screen()
            
            map_print(ship,earth,kalsi,mars,venus)
            if ship.check_fuel() == False:
                print("no fuel left")
                sleep(1.5)
                return
    


    elif number == 3:
        check_what_market_buy(player, ship, earth, kalsi, mars, venus)
    

    elif number == 4:
       check_what_market_sell(player, ship, earth, kalsi, mars, venus)
        

    
    elif number == 5:
        print(f"how much money: {player.get_money()}")
        wait()


    elif number == 6:
        print(f"how much fuel: {ship.get_fuel()}")
        wait()

    
    elif number == 7:
        ship.print_items_and_weight_cargo()
        wait()

    
    elif number == 8:
        ship.use_fuel_cell()
        wait()
    
    elif number == 9:
        check_what_market_multiplier_sell(ship,earth,kalsi,mars,venus)
        wait()

    elif number == 10:
        check_what_market_multiplier_buy(ship,earth,kalsi,mars,venus)
        wait()
    
    else:
        print("unkown number")
        wait()

    return


def main() -> None:
    player = Player()
    ship = SpaceShip()
    earth = Earth()
    kalsi = Kalsi()
    mars = Mars()
    venus = Venus()
    
    while print_welcome(ship) != True:
        clear_screen()

    
    while ship.check_fuel() == True and player.check_if_alive() == True:
        game_loop(player,ship,earth,kalsi,mars,venus)
        market_go_up_or_down(earth,kalsi,mars,venus)
    

    if ship.check_fuel() == False or player.check_if_alive() == False:
        clear_screen()
        print("game over")
    
    return


main()