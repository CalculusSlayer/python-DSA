# main.py
from typing import Union
from bike import Bike
from car import Car

def use_vehicle(vehicle: Union[Bike, Car]) -> None:
    if isinstance(vehicle, Bike):
        vehicle.ride()
    elif isinstance(vehicle, Car):
        vehicle.drive()

# Example usage:
def main():
    my_bike = Bike(brand="Trek", model="FX 3")
    my_car = Car(brand="Toyota", model="Corolla")

    use_vehicle(my_bike)  # Output: Riding the bike Trek FX 3
    use_vehicle(my_car)   # Output: Driving the car Toyota Corolla

if __name__ == '__main__':
    main()
