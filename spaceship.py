import math
from constants import FUEL_LOST_PER_DISTANCE1

class SpaceShip:

    def __init__(self, load_weight: int = 5, fuel: float = 50.0, x_position: int = 4, y_position: int = 3) -> None:
        self.__load_weight: int = load_weight
        self.__fuel: float = fuel
        self.__x_position: int = x_position
        self.__y_position: int = y_position
        self.__engine_name: str = "engine.0.1"
        self.__engine: dict[str,float] = {self.__engine_name: 0.5} # engine name and fuel efficiency
        self.__cargo: dict[str,float] = {}
        self.__weight_cargo: list[int] = []
        pass

    def get_load_weight(self) -> int:
        return self.__load_weight
    

    def get_weight_cargo(self) -> int:
        return self.__weight_cargo

    
    def add_weight_cargo(self, item: int) -> None:
        self.__weight_cargo.append(item)
        pass

    def substract_weight_cargo(self, index: int) -> None:
        self.__weight_cargo.pop(index)
        pass

    def throw_last_weight_cargo(self) -> None:
        self.__weight_cargo.pop()
        pass

    def count_weight_cargo(self) -> int:
        weight: int = 0

        for i in range(0,len(self.__weight_cargo)):
            weight += self.__weight_cargo[i]

        return weight

    def print_items_and_weight_cargo(self) -> None:
        
        counter: int = 0
        
        for obj in self.__cargo:
            
            print(f"Name {obj}:  Buy price {self.__cargo[obj]}:  Weight {self.__weight_cargo[counter]}")

            counter += 1
        
        pass

    
    def add_weight_cargo(self, item: int) -> None:
        self.__cargo.append(item) # dict todo fix it
        pass


    def get_length_cargo(self) -> None:
        return len(self.__cargo)
        pass

    
    def get_item_price_cargo(self, index: int) -> float:
        
        counter: int = 0

        for obj in self.__cargo:

            if counter == index:
                return self.__cargo[obj]

        pass


    def get_item_weight_cargo(self, index: int) -> int:
        return self.__weight_cargo[index]
        


    def get_x_position(self) -> int:
        return self.__x_position
    

    def get_y_position(self) -> int:
        return self.__y_position
    

    def get_fuel(self) -> float:
        return self.__fuel
    
    
    def get_engine_efficiency(self) -> dict[str,float]:
        return self.__engine
    

    def move(self) -> bool:

        x_position_str: str = input("Enter x position: ")
        y_position_str: str = input("Enter y position: ")

        x_position = int(x_position_str)
        y_position = int(y_position_str)

        if self.__x_position == x_position and self.__y_position == y_position:
            print("same position")
            return False
        
        elif x_position > 9 or y_position > 7:
            print("out of bounds")
            return False

        final_position = (self.__x_position - x_position)**2 + (self.__y_position - y_position)**2
        distance = math.sqrt(final_position)
        distance_final = round(distance)
        fuel_lost = (FUEL_LOST_PER_DISTANCE1 / self.__engine[self.__engine_name]) * distance_final

        if fuel_lost > self.__fuel:
            print("not enough fuel")
            return False
        
        self.__fuel -= fuel_lost
        self.__x_position = x_position
        self.__y_position = y_position

        return True


    
    

