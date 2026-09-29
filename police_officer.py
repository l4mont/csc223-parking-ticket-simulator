"""Define the PoliceOfficer class for the parking-ticket simulator."""

from parking_ticket import ParkingTicket
from parked_car import ParkedCar
from parking_meter import ParkingMeter


class PoliceOfficer:
    """Represent a police officer who inspects parked cars."""

    def __init__(self, name, badge_number):
        """Initialize an officer with validated identifying information."""
        self.name = name
        self.badge_number = badge_number

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty")
        return value

    @property
    def name(self):
        """Return the officer's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the officer's name, rejecting empty or non-string values."""
        self._name = self._validate_text(value, "name")

    @property
    def badge_number(self):
        """Return the officer's badge number."""
        return self._badge_number

    @badge_number.setter
    def badge_number(self, value):
        """Set the badge number, rejecting empty or non-string values."""
        self._badge_number = self._validate_text(value, "badge_number")

    def inspect_car(self, car, meter):
        """Inspect a car against a supplied meter and return a ticket or None.

        Args:
            car: ParkedCar object supplied through dependency injection.
            meter: ParkingMeter object supplied through dependency injection.
        Returns:
            ParkingTicket when parked time exceeds purchased time; otherwise None.
        Raises:
            TypeError: If car or meter has the wrong type.
        """
        if not isinstance(car, ParkedCar):
            raise TypeError("car must be a ParkedCar")
        if not isinstance(meter, ParkingMeter):
            raise TypeError("meter must be a ParkingMeter")
        illegal_minutes = car.minutes_parked - meter.minutes_purchased
        if illegal_minutes <= 0:
            return None
        return ParkingTicket(car, self, illegal_minutes)

