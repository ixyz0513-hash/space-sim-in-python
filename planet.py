from constants import EARTH_MARKET,EARTH_ITEM_WEIGHTS,EARTH_ITEM_PRICES_DEFAULT
from spaceship import SpaceShip
from player import Player


class Planet:

    def __init__(
    self, name = "Earth", 
    x_position: int = 2, 
    y_position: int = 4, 
    sell_cost_multiplier: float = 0.90,
    buy_cost_multiplier: float = 1.0,
    market: dict[str,float] = EARTH_MARKET,
    item_weights: list[int] = EARTH_ITEM_WEIGHTS,
    item_prices_default: list[float] = EARTH_ITEM_PRICES_DEFAULT
    ) -> None:

        self._name: str = name
        self._x_position: int = x_position
        self._y_position: int = y_position
        self._sell_cost_multiplier: float = sell_cost_multiplier
        self._buy_cost_multiplier: float = buy_cost_multiplier
        
        self._market: dict[str,float] = market

        self._items_weight: list[int] = item_weights
        self._items_prices_default: list[float] = item_prices_default
        return


    def get_x_position(self) -> int:
        return self._x_position
    

    def get_y_position(self) -> int:
        return self._y_position
    
    
    def get_name(self) -> str:
        return self._name
    

    def get_sell_cost_multiplier(self) -> float:
        return self._sell_cost_multiplier
    
    def get_buy_cost_multiplier(self) -> float:
        return self._sell_buy_multiplier
    
    
    def get_market(self) -> dict[str,float]:
        return self._market
    

    def get_items_weight(self) -> list[int]:
        return self._items_weight

    
    def print_items_and_weight(self) -> None:
        
        counter: int = 0
        
        for obj in self._market:
            
            print(f"Name {obj}:  Buy price {self._market[obj]}:  Weight {self._items_weight[counter]}")

            counter += 1
        
        return
    

    def get_item_price(self, index: int) -> float:
        
        counter: int = 0

        for obj in self._market:

            if counter == index:
                return self._market[obj] 

            counter += 1

        return

    def get_item_name(self, index: int) -> str:
        
        counter: int = 0

        for obj in self._market:

            if counter == index:
                return obj

            counter += 1

        return

    def get_item_weight(self,index: int) -> int:
        return self._items_weight[index]


    def recalculate_market(self, multiplier: float) -> None:

        counter: int = 0

        for obj in self._market:
            self._market[obj] = self._items_prices_default[counter]
            self._market[obj] *= multiplier

            counter += 1

        return
    

    def buy_something_from_market(self, ship: SpaceShip, player: Player) -> bool:
        self.recalculate_market(self._buy_cost_multiplier)
        self.print_items_and_weight()
        
        what_item_str: str = input("from 1 to 4 choose what you want to buy: ")
        what_item: int = int(what_item_str)
        what_item -= 1

        if what_item < 0 or what_item > 3:
            print("out of bounds")
            return False
        
        elif player.get_money() < self.get_item_price(what_item):
            print("not enough money")
            return False
        
        
        elif ship.get_load_weight() < self.get_item_weight(what_item):
             print("item is too heavy")
             return False

        ship.add_weight_cargo(self.get_item_weight(what_item), self.get_item_name(what_item))
        self.recalculate_market(self._sell_cost_multiplier)
        ship.add_item_cargo(self.get_item_name(what_item),self.get_item_price(what_item))


        if ship.count_weight_cargo() > ship.get_load_weight():
             print("item is too heavy")
             ship.throw_last_weight_cargo()
             return False
        
        self.recalculate_market(self._buy_cost_multiplier)
        player.substract_money(self.get_item_price(what_item))

        return True
    



    def sell_something_from_ship(self,ship: SpaceShip, player: Player) -> bool:
        
        if ship.get_length_cargo() <= 0:
            print("no items to sell")
            return False

        ship.print_items_and_weight_cargo()

        what_item_str: str = input("you know the drill pick any of them to sell them: ")
        what_item: int = int(what_item_str)

        what_item -= 1

        if what_item < 0 or what_item >= ship.get_length_cargo():
            print("out of bounds")
            return False
        
        player.add_money(ship.get_item_price_cargo(what_item))
        ship.substract_weight_cargo(what_item,self.get_item_weight(what_item))
        ship.sub_item_cargo(what_item)

        return True
    