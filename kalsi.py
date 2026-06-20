from planet import Planet
from constants import KALSI_MARKET,KALSI_ITEM_WEIGHTS,KALSI_ITEM_PRICES_DEFAULT


class Kalsi(Planet):

    def __init__(
    self, name: str = "Kalsi",
    x_position: int = 5,
    y_position: int = 1,
    sell_cost_multiplier: float = 1.05,
    buy_cost_multiplier: float = 1.0,
    market: dict[str,float] = KALSI_MARKET,
    item_weights: list[int] = KALSI_ITEM_WEIGHTS,
    item_prices_default: list[float] = KALSI_ITEM_PRICES_DEFAULT
    ) -> None:
        super().__init__(name,x_position,y_position,sell_cost_multiplier,buy_cost_multiplier,market,item_weights,item_prices_default)
    

        return