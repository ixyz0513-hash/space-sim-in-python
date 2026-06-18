import math
from constants import FUEL_LOST_PER_DISTANCE1

class SpaceShip:

    def __init__(self, load_weight: int = 15, fuel: float = 50, x_position: int = 4, y_position: int = 3) -> None:
        self.__load_weight = load_weight
        self.__fuel = fuel
        self.__x_position = x_position
        self.__y_position = y_position
        self.__engine_name = "engine.0.1"
        self.__engine = {self.__engine_name: 0.5} # engine name and fuel efficiency
        self.__cargo: dict[str,float] = {}
        pass

    def get_load_weight(self) -> int:
        return self.__load_weight


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


    
    

