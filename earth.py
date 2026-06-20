from planet import Planet
from constants import EARTH_MARKET,EARTH_ITEM_WEIGHTS,EARTH_ITEM_PRICES_DEFAULT


class Earth(Planet):

    def __init__(
    self, name: str = "Earth", 
    x_position: int = 1, 
    y_position: int = 5, 
    sell_cost_multiplier: float = 0.90,
    buy_cost_multiplier: float = 1.0,
    market: dict[str,float] = EARTH_MARKET,
    item_weights: list[int] = EARTH_ITEM_WEIGHTS,
    item_prices_default: list[float] = EARTH_ITEM_PRICES_DEFAULT
    ) -> None:
        super().__init__(name,x_position,y_position,sell_cost_multiplier,buy_cost_multiplier,market,item_weights,item_prices_default)
        
        return