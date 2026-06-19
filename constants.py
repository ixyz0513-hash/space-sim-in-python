FUEL_LOST_PER_DISTANCE1 = 5
TURN_COUNT = 0

# items earth
TOY_PRICE: float = 15.0
FUEL_CELL: float = 25.0
FURNITURE: float = 75.0
PAINT_BUCKET: float = 30.0

TOY_WEIGHT: int = 2
FUEL_CELL_WEIGHT: int = 3
FURNITURE_WEIGHT: int = 10
PAINT_BUCKET_WEIGHT: int = 5

EARTH_MARKET: dict[str,float] = {
            "Toy": TOY_PRICE, 
            "Fuel cell": FUEL_CELL, 
            "Furniture": FURNITURE, 
            "Paintbucket": PAINT_BUCKET
            }

EARTH_ITEM_WEIGHTS: list[int] = [TOY_WEIGHT,FUEL_CELL_WEIGHT,FURNITURE_WEIGHT,PAINT_BUCKET_WEIGHT]
EARTH_ITEM_PRICES_DEFAULT: list[float] = [TOY_PRICE,FUEL_CELL,FURNITURE,PAINT_BUCKET]