from constants import TOY_PRICE,FUEL_CELL,FURNITURE,PAINT_BUCKET


class Planet:

    def __init__(self, name = "Earth", x_position: int = 3, y_position: int = 2, sell_cost_multiplier: float = 0.90,buy_cost_multiplier: float = 1.0) -> None:
        self.__name = name
        self.__x_position = x_position
        self.__y_position = y_position
        self.__sell_cost_multiplier = sell_cost_multiplier
        self.__buy_cost_multiplier = buy_cost_multiplier
        self.__market: dict[str,float] = {
            "Toy": TOY_PRICE * self.__buy_cost_multiplier, 
            "Fuel cell": FUEL_CELL * self.__buy_cost_multiplier, 
            "Furniture": FURNITURE * self.__buy_cost_multiplier, 
            "Paintbucket": PAINT_BUCKET * self.__buy_cost_multiplier
            }
        pass

    def get_x_position(self) -> int:
        return self.__x_position
    

    def get_y_position(self) -> int:
        return self.__y_position
    
    
    def get_name(self) -> str:
        return self.__name
    

    def get_sell_cost_multiplier(self) -> float:
        return self.__sell_cost_multiplier
    
    def get_buy_cost_multiplier(self) -> float:
        return self.__sell_buy_multiplier
    
    
    def get_market(self) -> dict[str,float]:
        return self.__market
    
    def recalculate_market(self) -> None:
        self.__market: dict[str,float] = {
            "Toy": TOY_PRICE * self.__buy_cost_multiplier, 
            "Fuel cell": FUEL_CELL * self.__buy_cost_multiplier, 
            "Furniture": FURNITURE * self.__buy_cost_multiplier, 
            "Paintbucket": PAINT_BUCKET * self.__buy_cost_multiplier
            }
        
        pass
    