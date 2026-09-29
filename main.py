"""Run a small demonstration of the parking-ticket simulator."""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    """Create collaborating objects and display the result of an inspection."""
    car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 95)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("Jordan Lee", "A-1042")
    ticket = officer.inspect_car(car, meter)
    if ticket is None:
        print("No parking violation.")
    else:
        print(ticket)


if __name__ == "__main__":
    main()

