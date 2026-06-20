from planet import Planet
from constants import VENUS_MARKET,VENUS_ITEM_WEIGHTS,VENUS_ITEM_PRICE_DEFAULT



class Venus(Planet):

    def __init__(
    self, name: str = "Venus",
    x_position: int = 8,
    y_position: int = 2,
    sell_cost_multiplier: float = 1.10,
    buy_cost_multiplier: float = 0.95,
    market: dict[str,float] = VENUS_MARKET,
    item_weights: list[int] = VENUS_ITEM_WEIGHTS,
    item_prices_default: list[float] = VENUS_ITEM_PRICE_DEFAULT
    ) -> None:
        super().__init__(name,x_position,y_position,sell_cost_multiplier,buy_cost_multiplier,market,item_weights,item_prices_default)
    

        return