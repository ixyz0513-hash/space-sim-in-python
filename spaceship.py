from math import sqrt
from constants import FUEL_LOST_PER_DISTANCE1,FUEL_GAIN_PER_FUEL_CELL

class SpaceShip:

    def __init__(self, load_weight: int = 5, fuel: float = 50.0, x_position: int = 4, y_position: int = 3) -> None:
        self._load_weight: int = load_weight
        self._fuel: float = fuel
        self._x_position: int = x_position
        self._y_position: int = y_position
        self._engine_name: str = "engine.0.1"
        self._engine: dict[str,float] = {self._engine_name: 0.75} # engine name and fuel efficiency
        self._cargo: dict[str,float] = {}
        self._weight_cargo: list[int] = []
        self._quantity_cargo: list[int] = []
        return

    def get_load_weight(self) -> int:
        return self._load_weight
    

    def get_weight_cargo(self) -> int:
        return self._weight_cargo

    
    def add_weight_cargo(self, item: int, name: str) -> None:
        found: bool = False


        for obj in self._cargo:

            if obj == name:
                found = True
                break
        
        if found == False:
            self._weight_cargo.append(item)

        return

    def substract_weight_cargo(self, index: int) -> None:
        if self._quantity_cargo[index] > 1:
            self._quantity_cargo[index] -= 1
            
        else:
            self._weight_cargo.pop(index)

        return

    def throw_last_weight_cargo(self) -> None:
        self._weight_cargo.pop()
        return

    def count_weight_cargo(self) -> int:
        weight: int = 0

        for i in range(0,len(self._weight_cargo)):
            weight += self._weight_cargo[i] * self._quantity_cargo[i]

        return weight

    def print_items_and_weight_cargo(self) -> None:
        
        if self.get_length_cargo() == None:
            print("no items to check")
            return

        counter: int = 0
        
        for obj in self._cargo:
            
            print(f"Name {obj}:  Sell price {self._cargo[obj]}:  Weight {self._weight_cargo[counter]}: Quantity {self._quantity_cargo[counter]}")

            counter += 1
        
        return

    
    def add_item_cargo(self, name: str,item_price: float) -> None:
        found: bool = False
        counter: int = 0


        for obj in self._cargo:

            if obj == name:
                self._quantity_cargo[counter] += 1
                found = True
                break
                        
                counter += 1
        
        if found == False:
            self._cargo[name] = item_price
            self._quantity_cargo.append(1)

        return

    def sub_item_cargo(self,name: str) -> None:
        found: bool = False
        counter: int = 0

        for obj in self._cargo:

            if obj == name and self._quantity_cargo[counter] > 1:
                found = True
                break

            
            counter += 1

        if found == False:
            self._cargo.pop(name,None)

        return

    
    def recaculate_item_price(self, multiplier: float, index: int) -> None:

        counter: int = 0

        for obj in self._cargo:

            if index == counter:
                self._cargo[obj] *= multiplier
                break
            
            counter += 1
        
        return
    
    def set_item_price_default(self,name: str, price: float) -> None:
        self._cargo[name] = price
        return


    def get_length_cargo(self) -> int:
        return len(self._cargo)
    
    def get_item_price_cargo(self, index: int) -> float:
        
        counter: int = 0

        for obj in self._cargo:

            if counter == index:
                return self._cargo[obj]

        pass
    
    def get_item_name_cargo(self, index: int) -> str:
        counter: int = 0

        for obj in self._cargo:

            if counter == index:
                return obj

        pass


    def get_item_weight_cargo(self, index: int) -> int:
        return self._weight_cargo[index]
        


    def get_x_position(self) -> int:
        return self._x_position
    

    def get_y_position(self) -> int:
        return self._y_position
    

    def get_fuel(self) -> float:
        return self._fuel
    
    
    def check_fuel(self) -> bool:
        return self._fuel > 0
    
    
    def get_engine_efficiency(self) -> dict[str,float]:
        return self._engine
    

    def move(self) -> bool:

        x_position_str: str = input("Enter x position: ")
        y_position_str: str = input("Enter y position: ")

        x_position = int(x_position_str)
        y_position = int(y_position_str)

        if self._x_position == x_position and self._y_position == y_position:
            print("same position")
            return False
        
        elif x_position > 9 or y_position > 7:
            print("out of bounds")
            return False

        final_position = (self._x_position - x_position)**2 + (self._y_position - y_position)**2
        distance = math.sqrt(final_position)
        distance_final = round(distance)
        fuel_lost = (FUEL_LOST_PER_DISTANCE1 / self._engine[self._engine_name]) * distance_final

        if fuel_lost > self._fuel:
            print("not enough fuel")
            return False
        
        self._fuel -= fuel_lost
        self._x_position = x_position
        self._y_position = y_position

        return True

    

    def use_fuel_cell(self) -> bool:

        counter: int = 0
       
        for obj in self._cargo:

            if "Fuel cell" == obj:
                self._fuel += FUEL_GAIN_PER_FUEL_CELL
                self.sub_item_cargo("Fuel cell")
                self.substract_weight_cargo(counter)
                print("fuel replenished")
                return True

            counter += 1
        
        print("no fuel cells")
        return False


    
    

