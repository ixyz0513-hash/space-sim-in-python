from planet import Planet



class Venus(Planet):

    def __init__(
    self, name: str,
    x_position: int,
    y_position: int,
    sell_cost_multiplier: float,
    buy_cost_multiplier: float,
    market: dict[str,float],
    item_weights: list[int],
    item_prices_default: list[float]
    ) -> None:
        super().__init__(name,x_position,y_position,sell_cost_multiplier,buy_cost_multiplier,market,item_weights,item_prices_default)
    

        return