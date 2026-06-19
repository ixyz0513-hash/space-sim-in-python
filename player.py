class Player:

    def __init__(self,name: str = "John", health: int = 100, money: float = 50.0) -> None:
        self._name: str = name
        self._health: int = health
        self._money: float = money
        return

    def get_name(self) -> str:
        return self._name

    
    def get_health(self) -> int:
        return self._health

    
    def get_money(self) -> float:
        return self._money

    def substract_money(self, item: float) -> None:
        self._money -= item
        return

    def add_money(self, item: float) -> None:
        self._money += item
        return
