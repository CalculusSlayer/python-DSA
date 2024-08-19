# bike.py
class Bike:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def ride(self) -> None:
        print(f"Riding the bike {self.brand} {self.model}")