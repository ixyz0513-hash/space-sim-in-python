import math
from constants import FUEL_LOST_PER_DISTANCE1,FUEL_GAIN_PER_FUEL_CELL

class SpaceShip:

    def __init__(self, load_weight: int = 5, fuel: float = 50.0, x_position: int = 4, y_position: int = 3) -> None:
        self._load_weight: int = load_weight
        self._fuel: float = fuel
        self._x_position: int = x_position
        self._y_position: int = y_position
        self._engine_name: str = "engine.0.1"
        self._engine: dict[str,float] = {self._engine_name: 0.5} # engine name and fuel efficiency
        self._cargo: dict[str,float] = {}
        self._weight_cargo: list[int] = []
        return

    def get_load_weight(self) -> int:
        return self._load_weight
    

    def get_weight_cargo(self) -> int:
        return self._weight_cargo

    
    def add_weight_cargo(self, item: int) -> None:
        self._weight_cargo.append(item)
        return

    def substract_weight_cargo(self, index: int) -> None:
        self._weight_cargo.pop(index)
        return

    def throw_last_weight_cargo(self) -> None:
        self._weight_cargo.pop()
        return

    def count_weight_cargo(self) -> int:
        weight: int = 0

        for i in range(0,len(self._weight_cargo)):
            weight += self._weight_cargo[i]

        return weight

    def print_items_and_weight_cargo(self) -> None:

        counter: int = 0
        
        for obj in self._cargo:
            
            print(f"Name {obj}:  Buy price {self._cargo[obj]}:  Weight {self._weight_cargo[counter]}")

            counter += 1
        
        return

    
    def add_item_cargo(self, name: str,item_price: float) -> None:
        
        if name in self._cargo:
            self._cargo[name] += item_price
            return
        
        self._cargo[name] = item_price

        return

    def sub_item_cargo(self,name: str) -> None:
        self._cargo.pop(name,None)
        return


    def get_length_cargo(self) -> int:
        return len(self._cargo)
    
    def get_item_price_cargo(self, index: int) -> float:
        
        counter: int = 0

        for obj in self.__cargo:

            if counter == index:
                return self._cargo[obj]

        pass


    def get_item_weight_cargo(self, index: int) -> int:
        return self._weight_cargo[index]
        


    def get_x_position(self) -> int:
        return self._x_position
    

    def get_y_position(self) -> int:
        return self._y_position
    

    def get_fuel(self) -> float:
        return self._fuel
    
    
    def get_engine_efficiency(self) -> dict[str,float]:
        return self._engine
    

    def move(self) -> bool:

        x_position_str: str = input("Enter x position: ")
        y_position_str: str = input("Enter y position: ")

        x_position = int(x_position_str)
        y_position = int(y_position_str)

        if self._x_position == x_position and self._y_position == y_position:
            print("same position")
            return False
        
        elif x_position > 9 or y_position > 7:
            print("out of bounds")
            return False

        final_position = (self._x_position - x_position)**2 + (self._y_position - y_position)**2
        distance = math.sqrt(final_position)
        distance_final = round(distance)
        fuel_lost = (FUEL_LOST_PER_DISTANCE1 / self._engine[self._engine_name]) * distance_final

        if fuel_lost > self._fuel:
            print("not enough fuel")
            return False
        
        self._fuel -= fuel_lost
        self._x_position = x_position
        self._y_position = y_position

        return True

    

    def use_fuel_cell(self) -> bool:

        counter: int = 0
       
        for obj in self._cargo:

            if "Fuel cell" == obj:
                self._fuel += FUEL_GAIN_PER_FUEL_CELL
                self.sub_item_cargo("Fuel cell")
                self.substract_weight_cargo(counter)
                print("fuel replenished")
                return True

            counter += 1
        
        print("no fuel cells")
        return False


    
    

