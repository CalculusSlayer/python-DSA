# car.py
class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def drive(self) -> None:
        print(f"Driving the car {self.brand} {self.model}")