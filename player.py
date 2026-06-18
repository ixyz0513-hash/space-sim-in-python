class Player:

    def __init__(self,name: str = "John", health: int = 100, money: float = 50.0) -> None:
        self.__name = name
        self.__health = health
        self.__money = money
        pass

    def get_name(self) -> str:
        return self.__name

    
    def get_health(self) -> int:
        return self.__health

    
    def get_money(self) -> float:
        return self.__money