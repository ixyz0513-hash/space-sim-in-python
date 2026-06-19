class Player:

    def __init__(self,name: str = "John", health: int = 100, money: float = 50.0) -> None:
        self.__name: str = name
        self.__health: int = health
        self.__money: float = money
        return

    def get_name(self) -> str:
        return self.__name

    
    def get_health(self) -> int:
        return self.__health

    
    def get_money(self) -> float:
        return self.__money

    def substract_money(self, item: float) -> None:
        self.__money -= item
        return

    def add_money(self, item: float) -> None:
        self.__money += item
        return
