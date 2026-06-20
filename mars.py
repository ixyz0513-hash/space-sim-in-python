from planet import Planet
from constants import MARS_MARKET,MARS_ITEM_WEIGHTS,MARS_ITEM_PRICE_DEFAULT


class Mars(Planet):

    def __init__(
    self, name: str = "Mars",
    x_position: int = 6,
    y_position: int = 6,
    sell_cost_multiplier: float = 1.25,
    buy_cost_multiplier: float = 1.05,
    market: dict[str,float] = MARS_MARKET,
    item_weights: list[int] = MARS_ITEM_WEIGHTS,
    item_prices_default: list[float] = MARS_ITEM_PRICE_DEFAULT
    ) -> None:
        super().__init__(name,x_position,y_position,sell_cost_multiplier,buy_cost_multiplier,market,item_weights,item_prices_default)
    

        return